# Before you enter this client I'd like you to know that Volleyball and Harmony Hustle are the two most stupidest things
# to work around because 1, they don't have a timer, 2, they don't behave like any other sport and THREE THEY DON'T HAVE
# A TIMER. Anyways, have fun going through this.
import asyncio
import logging
import random
import traceback
from collections import deque
from random import randint, uniform
from typing import Dict, Set, Optional, Any
import Utils
import time

tracker_loaded = False
try:
    from worlds.tracker.TrackerClient import TrackerGameContext as SuperContext, \
                                             TrackerCommandProcessor as SuperCommandProcessor
    tracker_loaded = True
except ModuleNotFoundError:
    from CommonClient import CommonContext as SuperContext, ClientCommandProcessor as SuperCommandProcessor

from .. import MSMUtils
from MultiServer import mark_raw
from NetUtils import ClientStatus, JSONMessagePart
from .MSMInterface import MSMInterface, ConnectionState
from ..items import item_table
from ..locations import LOCATION_NAME_TO_ID
from .MSMFunctions import *
from . import dolphin_connection as dc
from .memory_addresses_pal import *
from .common_address_library import AddressLib

logger = logging.getLogger("Client")


id_to_name = {data.id: name for name, data in item_table.items()}
CLIENT_VERSION = "3.0.0"
COMPATIBLE_VERSIONS = []

not_match_prefix = ["s39", "s34", "s21", "s31", "s32", "s33"]

# Messages that get displayed when the user does /status
status_messages = {
    ConnectionState.IN_MATCH: "In Match",
    ConnectionState.IN_BOSS: "In Boss",
    ConnectionState.IN_MENU: "In Main Menu",
    ConnectionState.IN_TOURNAMENT_MAP: "In Tournament Map",
    ConnectionState.FEED_PETEY: "In Feed Petey",
    ConnectionState.HARMONY_HUSTLE: "In Harmony Hustle",
    ConnectionState.BOB_OMB_DODGE: "In Bob-omb Dodge",
    ConnectionState.SMASH_SKATE: "In Smash Skate",
    ConnectionState.DISCONNECTED: "Unable to connect to the Dolphin instance, attempting to reconnect...",
    ConnectionState.CONNECTED: "Connected to Dolphin!",
}

player_score_addresses = [
    PlayerAddresses.Score.score_period_1,
    PlayerAddresses.Score.score_period_2,
    PlayerAddresses.Score.score_period_3,
    PlayerAddresses.Score.score_period_4,
    PlayerAddresses.Score.score_period_5,
]

opponent_score_addresses = [
    OpponentAddresses.Score.score_period_1,
    OpponentAddresses.Score.score_period_2,
    OpponentAddresses.Score.score_period_3,
    OpponentAddresses.Score.score_period_4,
    OpponentAddresses.Score.score_period_5,
]

character_names = [
    "mario", "luigi", "peach", "daisy", "yoshi", "wario", "waluigi",
    "donkey_kong", "diddy_kong", "toad", "bowser", "bowser_jr",
    "moogle", "white_mage", "black_mage", "ninja", "cactuar", "slime"
]

# Court IDs in the order they appear in the cups
tournament_round_stages = {
    "Basketball": {
        "Mushroom": ["s01", "s02", "s05"],
        "Flower": ["s06", "s17", "s07"],
        "Star": ["s10", "s11", "s16"],
    },
    "Dodgeball": {
        "Mushroom": ["s01", "s02", "s03"],
        "Flower": ["s05", "s04", "s07"],
        "Star": ["s09", "s11", "s16"],
    },
    "Volleyball": {
        "Mushroom": ["s01", "s02", "s03"],
        "Flower": ["s05", "s06", "s17"],
        "Star": ["s10", "s11", "s16"],
    },
    "Hockey": {
        "Mushroom": ["s01", "s04", "s03"],
        "Flower": ["s17", "s09", "s07"],
        "Star": ["s10", "s12", "s16"],
    },
}

tournament_map_cups = {
    "s31": "Mushroom Cup",
    "s32": "Flower Cup",
    "s33": "Star Cup",
}

id_to_char = {
    255: "None",
    0: "Mario", 1: "Luigi", 2: "Peach", 3: "Daisy", 4: "Yoshi",
    5: "Wario", 6: "Waluigi", 7: "Donkey Kong", 8: "Diddy Kong", 9: "Toad",
    10: "Bowser", 11: "Bowser Jr", 12: "Moogle", 13: "Cactuar",
    14: "Ninja", 15: "White Mage", 16: "Slime", 17: "Black Mage",
    19: "Mii (Male)", 20: "Mii (Female)",
}

# Costumes linked to their ID with the character
costume_database = {
    "Yoshi": {1: "Pink Yoshi", 2: "Light Blue Yoshi", 3: "Yellow Yoshi"},
    "Toad": {1: "Blue Toad", 2: "Green Toad", 3: "Yellow Toad"},
    "Slime": {1: "She-Slime", 2: "Metal Slime"},
    "Peach": {1: "Tennis-wear Peach"},
    "Daisy": {1: "Tennis-wear Daisy"},
    "Ninja": {1: "Shadow White Ninja"},
    "White Mage": {1: "Pure White - White Mage"},
    "Black Mage": {1: "Magic Red Black Mage"},
}


# AP server storage is room-wide, so filler/trap save keys need seed + slot in the name.
CONSUMABLE_STORAGE_CATEGORY = "msm_consumables"
LOCATION_STORAGE_CATEGORY = "msm_locations"
CUSTOM_STORAGE_CATEGORY = "msm_customization"
# Build the reverse lookup once so persisted AP location IDs can be shown as local names.
LOCATION_ID_TO_NAME = {location_id: name for name, location_id in LOCATION_NAME_TO_ID.items()}


class MSMCommandProcessor(SuperCommandProcessor):
    ctx: "MSMContext"

    def __init__(self, ctx: "MSMContext"):
        super().__init__(ctx)

    @mark_raw
    def _cmd_check(self, location_name: str):
        """Check a location - Used for dev purposes, or if you're lazy ig"""
        asyncio.create_task(self.ctx.check_location(location_name))

    def _cmd_debug_mode(self):
        """Toggle client debugging on and off (Default off)"""
        if not self.ctx.DEBUGGING:
            self.ctx.DEBUGGING = True
            logger.info("Debugging on")
            self.ctx.debug_log(
                f"\n=========================================\n"
                f"Welcome to debug mode! This is what a debug message will look like!\n"
                f"Debug mode will tell you about things such as: Is the game ready_to_handle?\n"
                f"Has my item been stopped from swapping? What's the current forced_item_id?\n"
                f"You can use /change_debug_amount to change the amount of debug messages stored "
                f"at once so the client doesn't spam messages!"
                f"\n=========================================\n"
            )
        else:
            self.ctx.DEBUGGING = False
            logger.info("Debugging off")


    def _cmd_change_debug_amount(self, amount: str):
        """Change the amount of debug messages that are stored so they don't repeat

        :param amount: The amount of debug messages to store
        """
        try:
            new_amount = int(amount)
            from collections import deque
            self.ctx.last_debug_messages = deque(self.ctx.last_debug_messages, maxlen=new_amount)
            logger.info(f"Changed debug amount to {new_amount}")
        except ValueError:
            logger.info(f"Error: '{amount}' is not a valid number! Please enter an integer.")

    def _cmd_read_address(self, address: str, addr_type: str, *pointers: str):
        """Read the value of any address - Used for diagnostic purposes.
        :param address: Should look like 0x80000000 (8 digits after 0x),
        :param addr_type: Any from Byte, Halfword, Word, Float or String.
        :param pointers: Optional and should look like 0x1F4, 0x8,"""

        # ADDED , 16 HERE: This tells Python to parse the string as hexadecimal
        try:
            numeric_address = int(address, 16)
        except ValueError:
            return f"Error: '{address}' is not a valid hexadecimal address."

        # Use the newly converted numeric_address instead of the raw string
        if pointers:
            new_pointers = []
            for p in pointers:
                # Strip out any brackets or commas
                clean_p = p.replace("[", "").replace("]", "").replace(",", "")

                # Skip any empty strings caused by extra spaces
                if not clean_p:
                    continue

                try:
                    new_pointers.append(int(clean_p, 16))
                except ValueError:
                    return f"Error: Pointer '{p}' is not valid hex."
            final_address = self.ctx.game_interface.dolphin_client.follow_pointers(get_address(numeric_address),
                                                                                   new_pointers)
        else:
            final_address = get_address(numeric_address)

        client = self.ctx.game_interface.dolphin_client
        result = ""

        match addr_type.lower():
            case "byte":
                result = client.read_byte(final_address)
            case "halfword":
                result = client.read_bytes(final_address, 2)
            case "word":
                result = client.read_word(final_address)
            case "float":
                result = client.read_float(final_address)
            case "string":
                result = client.read_string(final_address)
            case _:
                error_msg = f"Error: Unsupported address type '{addr_type}'"
                logger.error(error_msg)
                return error_msg

        # Format final_address with hex() makes it easier to read back.
        if dc.GAME_VERSION == "PAL":
            log_message = f"[Memory Read - PAL] {addr_type.title()} at {hex(final_address)}. Result: {result}"
        elif dc.GAME_VERSION == "NTSC-U" and is_save_addr(address):
            log_message = f"[Memory Read - NTSC-U] {addr_type.title()} at {hex(final_address)} (In Exceptions). Result: {result}"
        elif dc.GAME_VERSION == "NTSC-U":
            log_message = f"[Memory Read - NTSC-U] {addr_type.title()} at {hex(final_address)} (Original Address: {address}). Result: {result}"
        else:
            log_message = "Invalid Region"

        logger.info(log_message)
        return log_message

    def _cmd_status(self):
        """Display the current dolphin connection status."""
        logger.info(f"Connection Status: {status_messages[self.ctx.connection_state]}")

    def _cmd_reapply_unlocks(self):
        """Reapply unlocks if you don't have them!"""
        asyncio.create_task(self.ctx.handle_received_items())
        logger.info("Reapplied unlocks!")

    def _cmd_unlock_tabs(self):
        """This command unlocks the tabs if they are already not unlocked"""
        unlock_tabs(self.ctx.hard_tournament_difficulty)
        logger.info("Tabs unlocked!")

    def _cmd_print_cached(self):
        """Print out the cached values"""
        for prop in AddressLib.address_properties:
            if prop in self.ctx.addresslib.__dict__:
                value = self.ctx.addresslib.__dict__[prop]

                # Format it nicely based on what type of data it is
                if isinstance(value, int):
                    logger.info(f"{prop}: {hex(value)}")
                elif isinstance(value, (bytes, bytearray)):
                    logger.info(f"{prop}: 0x{value.hex().upper()}")
                else:
                    logger.info(f"{prop}: {value}")

            else:
                # If it's not in the dictionary, it's empty!
                logger.info(f"{prop}: None (Currently Empty/Cleared)")

    def _cmd_reset_cached(self):
        """Manually reset the cached values if address errors are coming up when switching regions"""
        self.ctx.addresslib.reset_all_addresses(logger)

    def _cmd_debug_memory(self):
        """Forces the client to read Dolphin memory and print the live values."""

        logger.info("Fetching live memory from Dolphin...")

        for prop in AddressLib.address_properties:
            # We intentionally use getattr here!
            # If it's not cached, this forces it to read from Dolphin right now.
            value = getattr(self.ctx.addresslib, prop)

            if value is None:
                logger.info(f"{prop}: Read Failed (None)")

            elif isinstance(value, int):
                logger.info(f"{prop}: {hex(value)}")

            elif isinstance(value, (bytes, bytearray)):
                logger.info(f"{prop}: 0x{value.hex().upper()}")

            else:
                logger.info(f"{prop}: {value}")

    def _cmd_deathlink(self):
        """Toggle deathlink from client. Overrides default setting."""
        self.ctx.deathlink_enabled = not self.ctx.deathlink_enabled
        asyncio.create_task(self.ctx.update_death_link(self.ctx.deathlink_enabled))
        logger.info(f"Deathlink {'Enabled' if self.ctx.deathlink_enabled else 'Disabled'}!")

    @mark_raw
    def _cmd_unlocked(self, type: str):
        """See what type of item you have unlocked.
        :param type: Any from Modes, Ex/Exhibition, Courts, Cups, Characters/Chars/Char, Costumes/Costs/Cost, Abilities, Panel, Crystals, Alt Paths"""

        type_to_cmd = {
            "modes": self.unlocked_modes,
            "courts": self.unlocked_courts,
            "cups": self.unlocked_cups,
            "alt paths": self.unlocked_alt_paths,
            "exhibition": self.unlocked_ex,
            "ex": self.unlocked_ex,
            "characters": self.unlocked_characters,
            "chars": self.unlocked_characters,
            "char": self.unlocked_characters,
            "costumes": self.unlocked_costumes,
            "costs": self.unlocked_costumes,
            "cost": self.unlocked_costumes,
            "abilities": self.unlocked_abilities,
            "panel": self.unlocked_panel,
            "crystals": self.unlocked_crystals
        }

        type = type.strip().lower()

        if type in type_to_cmd:
            function = type_to_cmd[type]
            function()
        else:
            logger.error(f"Invalid type: {type}. Check the command description for valid types.")

    def unlocked_modes(self):
        """Display what main_sports you have unlocked."""
        unlocked_modes = self.ctx.unlocked_modes
        final_items = []
        if unlocked_modes:
            for mode in unlocked_modes:
                final_items.append(mode)
            logger.info(f"Unlocked Modes: {final_items}")
        else:
            logger.info("No unlocked modes")

    def unlocked_ex(self):
        """Display what exhibition diffs you have unlocked."""
        unlocked_diffs = self.ctx.unlocked_ex_diffs
        final_items = []
        if unlocked_diffs:
            for mode in unlocked_diffs:
                final_items.append(mode.replace("Exhibition ", ""))
            logger.info(f"Unlocked Difficulties: {final_items}")
        else:
            logger.info("No unlocked difficulties")

    def unlocked_characters(self):
        """Display what characters you have unlocked."""
        unlocked_characters = self.ctx.unlocked_characters
        final_items = []
        if unlocked_characters:
            for char in unlocked_characters:
                final_items.append(char)
            logger.info(f"Unlocked Characters: {final_items}")
        else:
            logger.info("No unlocked characters")

    def unlocked_costumes(self):
        """Display what costumes you have unlocked"""
        unlocked_costumes = self.ctx.unlocked_costumes
        final_items = []
        if unlocked_costumes:
            for costume in unlocked_costumes:
                final_items.append(costume)
            logger.info(f"Unlocked Costumes: {final_items}")
        else:
            logger.info("No unlocked costumes")

    def unlocked_cups(self):
        """Display what cups you have unlocked."""
        unlocked_cups = self.ctx.unlocked_cups
        final_items = []
        if unlocked_cups:
            for cup in unlocked_cups:
                final_items.append(cup)
            logger.info(f"Unlocked Cups: {final_items}")
        else:
            logger.info("No unlocked cups")

    def unlocked_courts(self):
        """Display what courts you have unlocked."""
        unlocked_courts = self.ctx.unlocked_courts
        final_items = []
        if unlocked_courts:
            for item in unlocked_courts:
                final_items.append(item)
            logger.info(f"Unlocked Courts: {final_items}")
        else:
            logger.info("No unlocked courts")
    
    def unlocked_alt_paths(self):
        """Display what alt paths you have unlocked."""
        unlocked_alt_paths = self.ctx.unlocked_alt_paths
        final_items = []
        if unlocked_alt_paths:
            for item in unlocked_alt_paths:
                final_items.append(item)
            logger.info(f"Unlocked Alt Paths: {final_items}")
        else:
            logger.info("No unlocked alt paths")

    def unlocked_abilities(self):
        """Display what abilities you have unlocked."""
        unlocked_abilities = self.ctx.unlocked_abilities
        final_items = []
        if unlocked_abilities:
            for ability in unlocked_abilities:
                final_items.append(ability)
            logger.info(f"Unlocked Abilities: {final_items}")
        else:
            logger.info("No unlocked abilities")

    def unlocked_panel(self):
        """Display what ?-Panel items you have unlocked."""
        unlocked_panel = self.ctx.unlocked_panel_items
        final_items = []
        if unlocked_panel:
            for item in unlocked_panel:
                final_items.append(item.replace("?-Panel: ", ""))
            logger.info(f"Unlocked Panel Items: {final_items}")
        else:
            logger.info("No unlocked ?-Panel items")

    def unlocked_crystals(self):
        """Display what Sports Crystals you have unlocked."""
        unlocked_crystals = self.ctx.unlocked_sports_crystals
        final_items = []
        if unlocked_crystals:
            for item in unlocked_crystals:
                final_items.append(item.replace("Sports Crystal:", ""))
            logger.info(f"Unlocked Sports Crystals: {final_items}")
        else:
            logger.info("No unlocked Sports Crystals")

    def _cmd_item(self):
        """Show what item you currently have"""
        current_item = self.ctx.current_item_func()
        item_map = {
            -1: "No Current Item",
            0: "Green Shell",
            1: "Red Shell",
            2: "Mini Mushroom",
            3: "Bob-omb",
            4: "Super Star",
            5: "Banana",
        }
        if self.ctx.DEBUGGING:
            logger.info(f"Current Item: {item_map[current_item]} - ID is {current_item}")
        else:
            logger.info(f"Current Item: {item_map[current_item]}")

    def _cmd_filler(self):
        """Display the filler queue"""
        filler_queue = self.ctx.filler_to_give
        final_items = []

        if filler_queue:
            for entry in filler_queue:
                # Check if the entry is a tuple (index, name) or just a string
                if isinstance(entry, tuple):
                    # The item name is the second part of the tuple
                    item_name = entry[1]
                else:
                    item_name = entry

                # Now that we have the string, perform the replacement
                final_items.append(item_name.replace("1 ", ""))

            logger.info(f"Filler Queue: {final_items}")
        else:
            logger.info("No filler in queue")

    def _cmd_trap(self):
        """Display the trap queue"""
        trap_queue = self.ctx.traps_to_give
        final_items = []

        if trap_queue:
            for entry in trap_queue:
                # Check if the entry is a tuple (index, name) or just a string
                if isinstance(entry, tuple):
                    # The item name is the second part of the tuple
                    item_name = entry[1]
                else:
                    item_name = entry

                final_items.append(item_name)

            logger.info(f"Trap Queue: {final_items}")
        else:
            logger.info("No traps in queue")

    # def _cmd_filler_reduce(self):
    #     """Reduces the size of the filler queue by 20 if issues occur (Only if filler queue is more than 30)"""
    #
    #     if len(self.ctx.filler_to_give) > 30:
    #         for _ in range(20):
    #             self.ctx.filler_to_give.popleft()
    #
    #         logger.info(f"Cleared 20 items from filler queue!\n"
    #                     f"Updated Queue: {self.ctx.filler_to_give}")
    #     else:
    #         logger.info("Filler queue is less than 30, if an issue is still occurring, ping electrostarz")


# noinspection PyDeprecation
class MSMContext(SuperContext):
    tags = {"AP"}
    game = "Mario Sports Mix"
    game_interface: MSMInterface
    connection_state = ConnectionState.DISCONNECTED
    command_processor = MSMCommandProcessor
    items_handling = 0b111
    want_slot_data = True
    items_handled = set()
    last_error_message: Optional[str] = None

    slot_data: Dict[str, Utils.Any] = {}

    # Here as placeholders, most will be replaced upon connection by slot data



    def __init__(self, server_address: str, password: str):
        super().__init__(server_address, password)
        self.game_interface = MSMInterface(logger)
        self.items_received = []
        self.items_handled = set()
        self.seed: Optional[str] = None


        self.goal_condition: int = 0
        self.behemoth_hp: float = 0.0
        self.behemoth_king_hp: float = 0.0
        self.win_cups_amount: int = 0

        self.enabled_sports: tuple = ()
        self.restrict_sports_mix: bool = False
        self.start_with_mushroom: int = 0
        self.exhibition_difficulties: tuple = ()
        self.hard_tournament_difficulty: bool = False
        self.sports_mix_unlock: int = 0
        self.court_unlock_type: int = 0
        self.cup_unlock_type: int = 0
        self.exhibition_type: int = 0

        self.include_alt_paths: bool = False
        self.alt_path_type: int = 0
        self.always_spawn_alt_paths: bool = False

        self.is_behemoth: bool = False
        self.is_behemoth_king: bool = False

        # Deathlink Stuff
        self.deathlink_enabled: bool = False
        self.deathlink_action: int = 0
        self.deathlink_consequence: int = 0
        self.deathlink_o_get_points: int = 0
        self.deathlink_o_scores_points: int = 0
        self.deathlink_boss_recovered: float = 0.0
        self.deathlink_dodge_health_lost: int = 0

        # Custom Tournament Settings
        self.custom_basket_time: int = 0
        self.enable_b_points: bool = False
        self.b_points_win: int = 0
        self.b_period: int = 0

        self.custom_dodge_time: int = 0
        self.d_period: int = 0
        self.d_max_health: int = 0

        self.v_points_win: int = 0
        self.v_period: int = 0

        self.custom_hockey_time: int = 0
        self.enable_h_points: bool = False
        self.h_points_win: int = 0
        self.h_period: int = 0

        self.party_modes: tuple = ()
        self.party_mode_opponent: int = 0

        # Sanity stuff
        self.character_sanity: int = 0
        self.send_both_character_sanity: bool = False
        self.special_sanity: int = 0
        self.court_sanity: int = 0
        self.score_sanity: int = 0
        self.score_sanity_max: int = 0
        self.score_sanity_points_req: int = 0

        # Cosmetic Options
        self.oops_all_character: int = 0
        self.replace_extra: bool = False
        self.shuffle_music: int = 0
        self.random_tint: int = 0
        self.tint_volleyball: bool = False


        # AP gives every received item a position/index in the received item list.
        # Use that index, not the item name, so duplicate filler items are handled separately.
        # AP gives every received item a stable index in the received-item list.
        # I use that index (not the item name) so duplicate filler items are tracked separately.
        self.queued_consumable_indices: Set[int] = set()
        self.handled_consumable_indices: Set[int] = set()
        # Set when a Get/SetReply for handled consumables has been applied this session.
        self._consumables_load_event = asyncio.Event()
        # Set when a Get/SetReply for handled customization data has been applied this session.
        self._custom_data_load_event = asyncio.Event()
        self.start_process = True
        self.handled_gecko_codes = False
        self.game_session_active = False
        self.active_game_version = None
        self.unlocked_sports_mix = False
        self.locking_period = False
        self.trap_running = False

        self.one_time_running = False
        self.item_processed = False
        self.awaiting_use = False
        self.forced_item_id = None
        self.last_match_score_total: Optional[int] = None
        self.previous_held_item: Optional[int] = -1
        self.pending_panel_replacement = False
        self.suppress_panel_until = 0.0

        self.boss_hp_handled: bool = False
        self.boss_defeat_handled: bool = False
        self.goal_handled: bool = False

        self.in_tournament_match: bool = False
        self.last_tournament_location_name: Optional[str] = None
        self.last_alt_path_location_name: Optional[str] = None
        self.cups_won: set[str] = set()
        self.exhibitions_won: set[str] = set()
        self.party_won: set[str] = set()

        self.minus_one = 0xFFFFFFFF

        # Deathlink Stuff
        self.has_sent_death: bool = True
        self.received_death: bool = True
        self.previous_opponent_score: int | None = None

        # Custom Tournament Settings Stuff
        self.handled_custom_timer: bool = False

        # Lists for items
        self.unlocked_modes: set[str] = set()
        self.unlocked_cups: set[str] = set()
        self.unlocked_alt_paths: set[str] = set()
        self.progressive_alt_paths: int = 0
        self.unlocked_ex_diffs: set[str] = set()
        self.progressive_courts: int = 0
        self.progressive_cups: int = 0
        self.unlocked_sports_crystals: set[str] = set()
        self.unlocked_courts: set[str] = set()
        self.unlocked_characters: set[str] = set()
        self.unlocked_costumes: set[str] = set()
        self.unlocked_panel_items: set[str] = set()
        self.unlocked_abilities: set[str] = set()
        self.filler_to_give = deque()
        self.traps_to_give = deque()

        self.custom_data: Dict[str, Dict[str, Any]] = {"music": {}, "tints": {}}
        self.music_randomization_applied = False

        # QOL Helpers
        self.previous_node: int = 0
        self.current_sm_alt_sport: str = ""
        self.spawn_side_choice: int = 0

        # Address Library
        self.addresslib = AddressLib()

        # Debug Stuff
        self.DEBUGGING: bool = False
        self.last_debug_messages = deque(maxlen=5)  # Stores up to 5 messages at a time at default
        self._toggle_log_states = {}
        self._log_once_states = {}
        self._rate_log_states = {}

    # --- Log types ---

    def debug_log(self, message: str) -> None:
        """Sends messages to the client if debugging is on"""

        if self.DEBUGGING:
            if message not in self.last_debug_messages:
                self.last_debug_messages.append(message)
                logger.info(f"[MSM Debug] {message}")

    def toggle_log(self, key: str, message_true: str, message_false: str, condition: bool, debug_mode: bool):
        """2 messages, one for true, one for false. Checks the key and if the condition has changed, sends the message"""

        if not hasattr(self, "_toggle_log_states"):
            self._toggle_log_states = {}

        previous = self._toggle_log_states.get(key)

        if previous is None or previous != condition:
            if debug_mode:
                self.debug_log(message_true if condition else message_false)
            else:
                logger.info(message_true if condition else message_false)
            self._toggle_log_states[key] = condition

    def log_once(self, key: str, message: str, debug_mode: bool):
        """Logs a message only if it differs from the last one logged for this key."""
        if not hasattr(self, "_log_once_states"):
            self._log_once_states = {}

        if self._log_once_states.get(key) != message:
            if debug_mode:
                self.debug_log(message)
            else:
                logger.info(message)
            self._log_once_states[key] = message

    def rate_log(self, key: str, message: str, interval: float, debug_mode: bool):
        """Logs a message at most once per interval (in seconds) for a given key."""
        if not hasattr(self, "_rate_log_states"):
            self._rate_log_states = {}

        now = asyncio.get_event_loop().time()
        last_logged = self._rate_log_states.get(key, 0.0)

        if now - last_logged >= interval:
            if debug_mode:
                self.debug_log(message)
            else:
                logger.info(message)
            self._rate_log_states[key] = now

    async def delay_log(self, message: str, delay: int, debug: bool = False):
        """Waits the delay time before logging the message"""

        if debug:
            self.debug_log(message)
        else:
            logger.info(message)

        await asyncio.sleep(delay)

    def log_colour(self, text: str, colour: str):
        """Logs the message in full colour"""

        if self.ui is not None:
            message: JSONMessagePart = {"type": "color", "text": text, "color": colour}
            self.ui.print_json([message])

    # --- Consumable persistence (filler + traps) ---
    # These are one-shot items tracked by AP received-item index and saved to server storage
    # so reconnects don't hand them out again. Key is scoped per slot.

    @property
    def consumable_storage_key(self) -> Optional[str]:
        """Returns a key which is linked to the game and the slot name"""

        if self.seed is None or self.slot is None:
            return None
        return f"{CONSUMABLE_STORAGE_CATEGORY}_{self.slot}"

    @property
    def custom_storage_key(self) -> Optional[str]:
        """Returns a key which is linked to the game and the slot name"""

        if self.seed is None or self.slot is None:
            return None
        return f"{CUSTOM_STORAGE_CATEGORY}_{self.slot}"

    def _on_consumables_storage_update(self, value: Any) -> None:
        """Apply server storage for handled filler/trap indices and drop any stale queue entries."""
        if value is None:
            self.handled_consumable_indices = set()
        elif isinstance(value, list):
            self.handled_consumable_indices = {int(index) for index in value}
        else:
            logger.warning(f"Unexpected handled consumables value type: {type(value)}")
            return

        handled = self.handled_consumable_indices
        self.filler_to_give = deque(
            entry for entry in self.filler_to_give
            if not (isinstance(entry, tuple) and entry[0] in handled)
        )
        self.traps_to_give = deque(
            entry for entry in self.traps_to_give
            if not (isinstance(entry, tuple) and entry[0] in handled)
        )
        self.queued_consumable_indices -= handled
        self._consumables_load_event.set()
        self.debug_log(f"Loaded {len(self.handled_consumable_indices)} handled consumables")

    def _on_custom_storage_update(self, value: Any) -> None:
        """Apply server storage for handled customization data."""
        if value is None:
            self.custom_data = {"music": {}, "tints": {}}
        elif isinstance(value, dict):
            if "music" in value or "tints" in value:
                custom_music_data = value.get("music", {})
                custom_tint_data = value.get("tints", {})

                if isinstance(custom_music_data, dict):
                    music_data = {str(song): str(new_song) for song, new_song in custom_music_data.items()}
                else:
                    music_data = {}
                    
                if isinstance(custom_tint_data, dict):
                    tint_data = {str(stage): [int(tint[0]), int(tint[1]), int(tint[2])] for stage, tint in custom_tint_data.items()}
                else:
                    tint_data = {}

                self.custom_data = {"music": music_data, "tints": tint_data}
        else:
            logger.warning(f"Unexpected customization data value type: {type(value)}")
            return

        self._custom_data_load_event.set()
        self.log_once("load",f"Loaded {len(self.custom_data)} customization data entries",False)

    async def load_handled_consumables(self, initialise: bool = False) -> None:
        """Load handled filler/trap indices from AP storage before queuing ReceivedItems."""
        key = self.consumable_storage_key
        if key is None or self._consumables_load_event.is_set():
            return

        self._consumables_load_event.clear()
        if initialise:
            # First connect for this seed/slot: create the key if missing, then subscribe to updates.
            await self.send_msgs([{
                "cmd": "Set",
                "key": key,
                "default": [],
                "want_reply": False,
                "operations": [{"operation": "default", "value": 0}],
            }])
            self.set_notify(key)
        else:
            await self.send_msgs([{"cmd": "Get", "keys": [key]}])

        try:
            await asyncio.wait_for(self._consumables_load_event.wait(), timeout=10.0)
        except asyncio.TimeoutError:
            logger.warning("Timed out loading handled consumables from server storage")
            self._consumables_load_event.set()

    async def load_custom_data(self, initialise: bool = False) -> None:
        """Load handled customization data from AP storage"""
        key = self.custom_storage_key
        if key is None:
            return

        self._custom_data_load_event.clear()

        if initialise:
            await self.send_msgs([{
                "cmd": "Set",
                "key": key,
                "default": {},
                "want_reply": False,
                "operations": [{"operation": "default", "value": {}}],
            }])
            self.set_notify(key)
        else:
            await self.send_msgs([{"cmd": "Get", "keys": [key]}])

        try:
            await asyncio.wait_for(self._custom_data_load_event.wait(), timeout=10.0)
        except asyncio.TimeoutError:
            logger.warning("Timed out loading customization data from server storage")
            self._custom_data_load_event.set()

    async def _handle_received_items_consumables(self, args: dict) -> None:
        """Gets called when the client receives a ReceivedItems package, handles both consumables and
        regular items"""

        # Wait for storage before queuing — otherwise reconnects re-fire already-handled items.
        await self.load_handled_consumables()

        start_index = args["index"]
        if start_index == 0:
            # CommonContext replaced items_received with a full inventory snapshot.
            # Keep that list and rebuild only unlock state from it.
            self.reset_local_item_state(clear_received=False)

        self.debug_log(
            f"ReceivedItems packet start={start_index}, count={len(args['items'])}, "
            f"handled_consumables={len(self.handled_consumable_indices)}"
        )

        for offset, item in enumerate(args["items"]):
            item_index = start_index + offset

            if item_index in self.handled_consumable_indices or item_index in self.queued_consumable_indices:
                self.debug_log(f"Skipping already queued/handled consumable index {item_index}")
                continue

            item_id = item.item if hasattr(item, "item") else item[0]
            item_name = id_to_name.get(item_id)

            if not item_name:
                self.debug_log(f"Skipping unknown item id {item_id} at index {item_index}")
                continue

            if item_name.startswith("1") or "Charge" in item_name:
                self.filler_to_give.append((item_index, item_name))
                self.queued_consumable_indices.add(item_index)
                logger.info(f"Queued filler: {item_name}")
                self.debug_log(f"Filler queue size is now {len(self.filler_to_give)}")

            elif "Trap" in item_name:
                self.traps_to_give.append((item_index, item_name))
                self.queued_consumable_indices.add(item_index)
                logger.info(f"Queued trap: {item_name}")
                self.debug_log(f"Trap queue size is now {len(self.traps_to_give)}")


        await self.handle_received_items()

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(MSMContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        """Handles the different packets sent by the Archipelago server"""

        super().on_package(cmd, args)

        if cmd == "Connected":
            new_team = args["team"]
            new_slot = args["slot"]
            ap_locations_checked = args["checked_locations"]
            self.locations_checked.update(ap_locations_checked)
            if self.team is not None and self.slot is not None and (self.team, self.slot) != (new_team, new_slot):
                # Clear before CommonContext handles Connected so it cannot send stale local checks for the new slot.
                self.reset_local_item_state(clear_received=True, clear_consumed=True)
                self.reset_location_state()


            self.slot_data = args.get("slot_data", {})

            # Goal Data
            self.goal_condition = self.slot_data.get("goal_condition", 1) # Only default to 1 or 2
            self.behemoth_hp = self.slot_data.get("behemoth_hp", 2400) # 2400 = Default
            self.behemoth_king_hp = self.slot_data.get("behemoth_king_hp", 3000) # 3000 = Default
            self.win_cups_amount = self.slot_data.get("win_cups_amount", 15) # Default in options.py

            # Enabled/Unlock Data
            self.enabled_sports = self.slot_data.get("enabled_sports", ())
            self.restrict_sports_mix = self.slot_data.get("restrict_sports_mix", False)
            self.start_with_mushroom = self.slot_data.get("start_with_mushroom_cup", 0)
            self.exhibition_difficulties = self.slot_data.get("exhibition_difficulties", ())
            self.hard_tournament_difficulty = self.slot_data.get("hard_tournament_difficulty", 1)
            self.sports_mix_unlock = self.slot_data.get("sports_mix_unlock", 0)
            self.court_unlock_type = self.slot_data.get("court_unlock_type",0)
            self.cup_unlock_type = self.slot_data.get("cup_unlock_type", 0)
            self.exhibition_type = self.slot_data.get("exhibition_type", 0)

            # Deathlink Data
            self.deathlink_enabled = self.slot_data.get("deathlink", False)
            self.deathlink_action = self.slot_data.get("deathlink_action", 0)
            self.deathlink_consequence = self.slot_data.get("deathlink_consequence", 0)
            self.deathlink_o_get_points = self.slot_data.get("deathlink_opponent_get_points", 3)
            self.deathlink_o_scores_points = self.slot_data.get("deathlink_opponent_scores_points", 15)
            self.deathlink_boss_recovered = self.slot_data.get("deathlink_boss_health_recovered", 20)
            self.deathlink_dodge_health_lost = self.slot_data.get("deathlink_dodgeball_health_lost", 20)


            # Custom Tournament Settings Data
            self.alt_paths_enabled = self.slot_data.get("include_alt_paths", False)
            self.alt_paths_unlock_type = self.slot_data.get("alt_path_type", 0)
            self.alt_paths_always_spawn = self.slot_data.get("always_spawn_alt_paths", True)
            self.in_alt_path = False

            self.custom_basket_time = self.slot_data.get("basket_time", 2)
            self.enable_b_points = self.slot_data.get("enable_b_points_win", False)
            self.b_points_win = self.slot_data.get("b_points_win", 15)
            self.b_period = self.slot_data.get("b_period", 2)

            self.custom_dodge_time = self.slot_data.get("dodge_time", 3)
            self.d_period = self.slot_data.get("d_period", 2)
            self.d_max_health = self.slot_data.get("d_max_health", 100)


            self.v_points_win = self.slot_data.get("v_points_win", 15)
            self.v_period = self.slot_data.get("v_period", 2)

            self.custom_hockey_time = self.slot_data.get("hockey_time", 3)
            self.enable_h_points = self.slot_data.get("enable_h_points_win", False)
            self.h_points_win = self.slot_data.get("h_points_win", 15)
            self.h_period = self.slot_data.get("h_period", 2)

            # Party Mode Data
            self.party_modes = self.slot_data.get("party_mode", ())
            self.party_mode_opponent = self.slot_data.get("party_mode_opponent", 1)

            # Sanity Data
            self.character_sanity = self.slot_data.get("character_sanity", 0)
            self.send_both_character_sanity = self.slot_data.get("send_both_character_sanity", 0)
            self.court_sanity = self.slot_data.get("court_sanity", 0)
            self.special_sanity = self.slot_data.get("special_sanity", 0)

            # Cosmetic option data
            self.all_one_opponent = self.slot_data.get("oops_all_character", 0)
            self.replace_extra = self.slot_data.get("replace_extra", False)
            self.music_shuffle = self.slot_data.get("shuffle_music", 0)
            self.random_tint = self.slot_data.get("random_tint", False)
            self.tint_volleyball = self.slot_data.get("tint_volleyball", False)
            self.previous_stage = None

            self.custom_data = {"music": {}, "tints": {}}
            self.music_randomization_applied = False
            

            asyncio.create_task(self.update_death_link(self.deathlink_enabled))
            # Slot is known now — load/create the per-slot consumable save before items arrive.
            asyncio.create_task(self.load_handled_consumables(initialise=True))
            asyncio.create_task(self.load_custom_data(initialise=True))
            if self.locations_checked:
                asyncio.create_task(
                    self.send_msgs([{"cmd": "LocationChecks", "locations": sorted(self.locations_checked)}])
                )

            generation_version = self.slot_data.get("version", "0.0.1")

            # Client World mismatch handler
            if generation_version in COMPATIBLE_VERSIONS:
                logger.info(
                    f"This seed was generated on {generation_version}, however client version {CLIENT_VERSION} is compatible!"
                )
            elif CLIENT_VERSION != generation_version:
                logger.error(
                    f"\n=========================================\n"
                    f"VERSION MISMATCH DETECTED!\n"
                    f"Seed was generated on version: {generation_version}\n"
                    f"Your Client version: {CLIENT_VERSION}. This version is not compatible with version generated on!\n"
                    f"Please update, downgrade your client, or regenerate the seed as things may break!\n"
                    f"========================================="
                )
            else:
                logger.info(f"Version check passed! (v{CLIENT_VERSION})")

        elif cmd == "RoomInfo":
            new_seed = args.get("seed_name", "unknown")
            if self.seed != new_seed:
                # New seed — don't carry consumable or location state from the previous room.
                self.reset_local_item_state(clear_received=True, clear_consumed=True)
                self.reset_location_state()
            self.seed = new_seed

        elif cmd == "ReceivedItems":
            asyncio.create_task(self._handle_received_items_consumables(args))

        elif cmd in ("Retrieved", "SetReply"):
            consumable_key = self.consumable_storage_key
            custom_key = self.custom_storage_key

            if cmd == "Retrieved":
                if consumable_key and consumable_key in args.get("keys", {}):
                    self._on_consumables_storage_update(args["keys"][consumable_key])
                if custom_key and custom_key in args.get("keys", {}):
                    self._on_custom_storage_update(args["keys"][custom_key])

            elif cmd == "SetReply":
                if consumable_key and args.get("key") == consumable_key:
                    self._on_consumables_storage_update(args.get("value"))
                if custom_key and args.get("key") == custom_key:
                    self._on_custom_storage_update(args.get("value"))

    def make_gui(self):
        ui = super().make_gui()
        ui.base_title = f"Archipelago Mario Sports Mix Client (Version {CLIENT_VERSION}) | AP Version"
        return ui

    async def disconnect(self, allow_autoreconnect: bool = False):
        """Handles the user pressing the disconnect button."""

        self.game_interface.dolphin_client.disconnect()
        self.reset_game_session_state(game_active= True if dc.GAME_VERSION is not None else False)
        await super().disconnect(allow_autoreconnect)

    def update_connection_status(self):
        self.connection_state = self.game_interface.get_connection_state()

    def reset_game_session_state(self, game_active: bool = False) -> None:
        """Reset runtime-only state when the game process/title exits or restarts."""
        self.start_process = True
        self.handled_gecko_codes = False
        self.one_time_running = False
        self.item_processed = False
        self.awaiting_use = False
        self.forced_item_id = None
        self.last_match_score_total = None
        self.previous_held_item = -1
        self.pending_panel_replacement = False
        self.suppress_panel_until = 0.0
        self.boss_hp_handled = False
        self.boss_defeat_handled = False
        self.in_tournament_match = False
        self.last_tournament_location_name = None
        self.last_alt_path_location_name = None
        self.has_sent_death = True
        self.received_death = True
        self.previous_opponent_score = None
        self.game_interface.current_tournament = None if not game_active else self.game_interface.current_tournament
        self.game_session_active = game_active
        self.active_game_version = dc.GAME_VERSION if game_active else None
        self.music_randomization_applied = False
        self.custom_data = {"music": {}, "tints": {}}
        self._custom_data_load_event.clear()

    def reset_local_item_state(self, clear_received: bool = False, clear_consumed: bool = False) -> None:
        """Resets the item state whenever the user connects to a new slot"""

        if clear_received:
            self.items_received.clear()
        self.items_handled.clear()
        self.unlocked_modes.clear()
        self.unlocked_ex_diffs.clear()
        self.progressive_courts = 0
        self.progressive_cups = 0
        self.unlocked_cups.clear()
        self.unlocked_alt_paths.clear()
        self.progressive_alt_paths = 0
        self.unlocked_sports_crystals.clear()
        self.unlocked_courts.clear()
        self.unlocked_characters.clear()
        self.unlocked_costumes.clear()
        self.unlocked_panel_items.clear()
        self.unlocked_abilities.clear()

        if clear_consumed:
            self.filler_to_give.clear()
            self.traps_to_give.clear()
            self.queued_consumable_indices.clear()
            self.handled_consumable_indices.clear()
            self._consumables_load_event.clear()

    async def mark_consumable_handled(self, item_index: Optional[int]) -> None:
        """Mark a consumable (1 time or trap) item as handled so the client doesn't use it again"""

        if item_index is None:
            return

        self.queued_consumable_indices.discard(item_index)
        self.handled_consumable_indices.add(item_index)
        # Save after the effect is applied so a disconnect mid-queue doesn't eat the item.
        await self.save_handled_consumables()
        self.debug_log(f"Saved handled consumable index {item_index}")

    async def save_handled_consumables(self) -> None:
        """Saves the handled consumables to the AP Data Storage to retrieve upon future connection"""

        key = self.consumable_storage_key
        if key is None:
            return
        await self.send_msgs([{
            "cmd": "Set",
            "key": key,
            "default": [],
            "want_reply": True,
            "operations": [{
                "operation": "replace",
                "value": sorted(self.handled_consumable_indices)
            }]
        }])
        self.debug_log(f"Saving handled consumables: {sorted(self.handled_consumable_indices)}")

    async def save_custom_data(self) -> None:
        key = self.custom_storage_key
        if key is None:
            return
        await self.send_msgs([{
            "cmd": "Set",
            "key": key,
            "default": {},
            "want_reply": True,
            "operations": [{
                "operation": "replace",
                "value": self.custom_data
            }]
        }])
        self.debug_log(f"Saving customization data: {self.custom_data}")

    def reset_location_state(self) -> None:
        self.locations_checked.clear()
        self.checked_locations.clear()
        self.last_tournament_location_name = None
        self.last_alt_path_location_name = None

    def current_item_func(self):
        """Returns the ID of the item
        0: Green Shell, 1: Red Shell, 2: Mini Mushroom, 3: Bob-omb, 4: Super Star,
        5: Banana"""

        current_item = self.game_interface.dolphin_client.read_word(self.addresslib.p_item_held_addr)

        if current_item == self.minus_one:
            return -1 #"No Item"
        else:
            return current_item

    def ready_to_handle(self):
        """Return whether it is safe to apply received effects to the current game.

        Party modes do not use the standard sport timer/custom-timer rules, so
        they need their own readiness path.
        """
        match_status = self.game_interface.match_status()
        mode = self.game_interface.get_mode()
        paused = self.game_interface.dolphin_client.read_byte(self.addresslib.paused_addr)
        cutscene_active = self.game_interface.dolphin_client.read_byte(self.addresslib.cutscene_active_addr)
        loading_screen_active = self.game_interface.dolphin_client.read_word(self.addresslib.loading_screen_addr)
        human_players = self.game_interface.dolphin_client.read_byte(get_address(PlayerAddresses.human_players))

        is_paused = paused != 0
        is_cutscene = cutscene_active != 0
        # This address is zero while the loading screen is active.
        is_loading = loading_screen_active == 0
        is_demo = human_players == 0

        if is_paused or is_cutscene or is_loading or is_demo:
            #print(f"P {is_paused}, C {is_cutscene}, L {is_loading}, D {is_demo}")
            return False


        party_modes = {"Feed Petey", "Harmony Hustle", "Bob-omb Dodge", "Smash Skate"}
        if mode in party_modes:
            if match_status != 0:
                return False
            if mode == "Harmony Hustle":
                # Harmony Hustle is stupid and therefore has its own start address
                hh_started = self.game_interface.dolphin_client.read_byte(get_address(PartyMode.HarmonyHustle.started))
                return hh_started == 1
            return True

        court_id, _ = self.game_interface.get_court()
        timer = self.game_interface.dolphin_client.read_float(self.addresslib.timer_addr)
        max_time = self.game_interface.dolphin_client.read_float(self.addresslib.max_time_addr)
        set_break = self.game_interface.dolphin_client.read_pointer(
            get_address(MatchAddresses.set_break), Pointers.Match.set_break_offsets, "word"
        )

        ready_game = False

        if match_status == 0 and court_id not in not_match_prefix:
            if mode in ["Basketball", "Dodgeball", "Hockey"]:
                ready_game = timer < max_time
            else:
                if court_id == "s20":
                    try:
                        self.game_interface.dolphin_client.follow_pointers(self.addresslib.behemoth_hp_addr,
                                                            Pointers.Boss.behemoth_hp_offsets)
                        ready_game = True
                    except RuntimeError:
                        ready_game = False
                else:
                    try:
                        # Check if you can follow pointers to the address, if so, then ready
                        self.game_interface.dolphin_client.follow_pointers(self.addresslib.vbp_addr,
                                                            Pointers.VBP.v_last_held_offsets)
                        ready_game = True
                    except RuntimeError:
                        ready_game = False

            # if mode == "Basketball":
            #     target_time = custom_time if self.game_interface.current_tournament is not None \
            #         else self.game_interface.get_basketball_time()
            #     ready_game = timer < target_time
            #
            # elif mode == "Dodgeball":
            #     target_time = custom_time if self.game_interface.current_tournament is not None \
            #         else self.game_interface.get_dodgeball_time()
            #     ready_game = target_time == "Off" or timer < target_time
            #
            # elif mode == "Volleyball":
            #     if court_id == "s20":
            #         try:
            #             self.game_interface.dolphin_client.follow_pointers(self.addresslib.behemoth_hp_addr,
            #                                                 Pointers.Boss.behemoth_hp_offsets)
            #             ready_game = True
            #         except RuntimeError:
            #             ready_game = False
            #     else:
            #         try:
            #             # Check if you can follow pointers to the address, if so, then ready
            #             self.game_interface.dolphin_client.follow_pointers(self.addresslib.vbp_addr,
            #                                                 Pointers.VBP.v_last_held_offsets)
            #             ready_game = True
            #         except RuntimeError:
            #             ready_game = False
            # elif mode == "Hockey":
            #     target_time = custom_time if self.game_interface.current_tournament is not None \
            #         else self.game_interface.get_hockey_time()
            #     ready_game = timer < target_time

        if timer == 0 and self.mode_has_timer(mode):
            ready_game = False

        #print(f"RG {ready_game}, SB {set_break}, MTCH {match_started}")

        return ready_game and set_break == 0


    # === Item Receiving ===


    async def handle_received_items(self):
        """Handles the received non-consumable items"""

        sport_tuple = ("Basketball", "Dodgeball", "Volleyball", "Hockey", "Sports Mix")
        party_tuple = ("Feed Petey", "Harmony Hustle", "Bob-omb Dodge", "Smash Skate")

        characters_tuple = ("Mario", "Luigi", "Peach", "Daisy", "Yoshi", "Wario", "Waluigi", "Donkey Kong",
        "Diddy Kong", "Toad", "Bowser", "Bowser Jr", "Moogle", "Cactuar", "Ninja", "White Mage", "Slime", "Black Mage",
        "Mii (Male)", "Mii (Female)")

        costumes_tuple = ("Pink Yoshi", "Light Blue Yoshi", "Yellow Yoshi", "Blue Toad", "Green Toad", "Yellow Toad",
        "She-Slime", "Metal Slime",  "Tennis-wear Peach", "Tennis-wear Daisy", "Shadow White Ninja",
        "Pure White - White Mage", "Magic Red Black Mage")

        courts_tuple = (
            "Mario Stadium", "Koopa Troopa Beach", "Peach's Castle", "Toad Park", "DK Dock",
            "Luigi's Mansion", "Daisy Garden", "Wario Factory", "Bowser Jr. Blvd.", "Bowser's Castle",
            "Waluigi Pinball", "Ghoulish Galleon", "Star Ship", "Western Junction", "Behemoth Stage",


            "Classic Ocean", "Chocobo Rhythm", "Mario Athletic", "Mushroom Mix Medley",
            "Bloocheep Ocean", "Chocobo Pop", "Punk Athletic", "Blossom Mix Medley",
            "Punk Ocean", "Chocobo Beat", "Island Athletic", "Star Mix Medley",
            "Sherbet Sea", "Rowdy Raft", "Fire Mountain"
        )


        ability_tuple = ("Special Meter", )


        for index, network_item in enumerate(self.items_received):
            item_id = network_item.item
            item_name = id_to_name.get(item_id)
            if index not in self.items_handled:
                if item_name is None:
                    continue

                if item_name in sport_tuple or item_name in party_tuple:
                    self.unlocked_modes.add(item_name)
                    self.debug_log(f"Added {item_name} to unlocked_modes")

                # Format to Basketball:, Dodgeball:, etc
                # Changed for alt path names
                for sport in sport_tuple:
                    if item_name.startswith(f"{sport}:"):
                            if not "Alt".casefold() in item_name.casefold():
                                self.unlocked_cups.add(item_name)
                                self.debug_log(f"Added {item_name} to unlocked_cups")

                if "Alt".casefold() in item_name.casefold():
                    if "Progressive".casefold() in item_name.casefold():
                        self.progressive_alt_paths += 1
                        self.debug_log(f"Added {item_name} to progressive_alt_paths")
                    else:
                        self.unlocked_alt_paths.add(item_name)
                        self.debug_log(f"Added {item_name} to unlocked_alt_paths")

                if item_name.startswith("Exhibition"):
                    self.unlocked_ex_diffs.add(item_name)
                    self.debug_log(f"Added {item_name} to unlocked_ex_diffs")

                elif item_name == "Progressive Cup":
                    self.progressive_cups += 1
                    self.debug_log(f"Added {item_name} to progressive_cups")

                elif item_name == "Progressive Court":
                    self.progressive_courts += 1
                    self.debug_log(f"Added {item_name} to progressive_courts")

                elif item_name.startswith("Sports Crystal:"):
                    self.unlocked_sports_crystals.add(item_name)
                    self.debug_log(f"Added {item_name} to unlocked_sports_crystals")

                elif item_name in courts_tuple:
                    self.unlocked_courts.add(item_name)
                    self.debug_log(f"Added {item_name} to unlocked_courts")

                elif item_name in characters_tuple:
                    self.unlocked_characters.add(item_name)
                    self.debug_log(f"Added {item_name} to unlocked_characters")

                elif item_name in costumes_tuple:
                    self.unlocked_costumes.add(item_name)
                    self.debug_log(f"Added {item_name} to unlocked_costumes")

                elif item_name.startswith("?"):
                    self.unlocked_panel_items.add(item_name)
                    self.debug_log(f"Added {item_name} to unlocked_panel_items")

                elif item_name in ability_tuple:
                    self.unlocked_abilities.add(item_name)
                    self.debug_log(f"Added {item_name} to unlocked_abilities")

                self.items_handled.add(index)


        # Cups / Sports Mix
        # Courts
        await self.handle_court_unlocks()
        await self.handle_cup_unlocks()
        await self.handle_party_unlocks()
        if self.cup_unlock_type == 1:
            await self.handle_progressive_cup_unlocks()

        await self.handle_sports_mix_unlock()

        # Alternate Paths
        await self.handle_alt_path_unlocks()

        if self.court_unlock_type == 1:
            await self.handle_progressive_court_unlocks()

        # Characters
        await self.handle_all_characters()

        # Traps + Filler aren't here because they can only be received in game and this function gets awaited during
        # every connection state, if you were to receive a trap or filler in the menu it wouldn't work.

    def has_unlocked_mode(self, mode: str):
        """Used to lock courts & cups when the user doesn't have the mode
        Sports Mix always returns True as that is unlocked by items anyway, not by default"""

        if mode == "SM":
            return True

        elif mode in self.unlocked_modes:
            return True
        else:
            return False


    # === Character Unlocks ===


    async def handle_all_characters(self):
        """Handles the unlocking of characters using functions for characters with costume"""

        for char in character_names:
            # Format character name for value
            item_name = f"{char.replace('_', ' ').title()}"

            # Have separate values for characters with costumes, adding values can equal different combinations
            if char == "yoshi":
                value = self.yoshi_unlocks_value()
            elif char == "peach":
                value = self.peach_unlocks_value()
            elif char == "daisy":
                value = self.daisy_unlocks_value()
            elif char == "toad":
                value = self.toad_unlocks_value()
            elif char == "ninja":
                value = self.ninja_unlocks_value()
            elif char == "white_mage":
                value = self.white_mage_unlocks_value()
            elif char == "black_mage":
                value = self.black_mage_unlocks_value()
            elif char == "slime":
                value = self.slime_unlocks_value()
            else:
                # Else, value is 1 if the item name is in characters, if not it's 0
                value = 1 if item_name in self.unlocked_characters else 0


            sports_classes = [
                BasketballAddresses,
                DodgeballAddresses,
                VolleyballAddresses,
                HockeyAddresses
            ]

            for sport in sports_classes:
                try:
                    # Getting a character unlocks it for all sports, write it to all sports
                    addr = getattr(sport.Characters, char)
                    new_addr = get_address(addr)
                    self.game_interface.dolphin_client.write_byte(new_addr, value)
                    await self.check_write(new_addr, "byte", value)
                except AttributeError:
                    print(f"Warning: {char} not found in {sport.__name__}!")

    # Specific value functions for characters with costumes

    def yoshi_unlocks_value(self):
        # If they don't have the character item, character is locked
        if "Yoshi" not in self.unlocked_characters:
            value = 0
            return value


        value = 1
        if "Pink Yoshi" in self.unlocked_costumes: value += 4
        if "Light Blue Yoshi" in self.unlocked_costumes: value += 16
        if "Yellow Yoshi" in self.unlocked_costumes: value += 64
        return value

    def peach_unlocks_value(self):
        if "Peach" not in self.unlocked_characters:
            value = 0
            return value

        value = 1
        if "Tennis-wear Peach" in self.unlocked_costumes: value += 4
        return value

    def daisy_unlocks_value(self):
        if "Daisy" not in self.unlocked_characters:
            value = 0
            return value

        value = 1
        if "Tennis-wear Daisy" in self.unlocked_costumes: value += 4
        return value

    def toad_unlocks_value(self):
        if "Toad" not in self.unlocked_characters:
            value = 0
            return value

        value = 1
        if "Blue Toad" in self.unlocked_costumes: value += 4
        if "Green Toad" in self.unlocked_costumes: value += 16
        if "Yellow Toad" in self.unlocked_costumes: value += 64
        return value

    def ninja_unlocks_value(self):
        if "Ninja" not in self.unlocked_characters:
            value = 0
            return value

        value = 1
        if "Shadow White Ninja" in self.unlocked_costumes: value += 4
        return value

    def white_mage_unlocks_value(self):
        if "White Mage" not in self.unlocked_characters:
            value = 0
            return value

        value = 1
        if "Pure White - White Mage" in self.unlocked_costumes: value += 4
        return value

    def black_mage_unlocks_value(self):
        if "Black Mage" not in self.unlocked_characters:
            value = 0
            return value

        value = 1
        if "Magic Red Black Mage" in self.unlocked_costumes: value += 4
        return value

    def slime_unlocks_value(self):
        if "Slime" not in self.unlocked_characters:
            value = 0
            return value

        value = 1
        if "She-Slime" in self.unlocked_costumes: value += 4
        if "Metal Slime" in self.unlocked_costumes: value += 16
        return value


    # === Cup Unlocks ===


    async def handle_cup_unlocks(self):
        """Handles the unlocking of cups"""

        # Basketball
        b_normal = BasketballAddresses.Tournament.normal_cups
        b_hard = BasketballAddresses.Tournament.hard_cups

        # Dodgeball
        d_normal = DodgeballAddresses.Tournament.normal_cups
        d_hard = DodgeballAddresses.Tournament.hard_cups

        # Volleyball
        v_normal = VolleyballAddresses.Tournament.normal_cups
        v_hard = VolleyballAddresses.Tournament.hard_cups

        # Hockey
        h_normal = HockeyAddresses.Tournament.normal_cups
        h_hard = HockeyAddresses.Tournament.hard_cups

        # Sports Mix
        sports_mix = SportsMixAddresses.Tournament.cups

        cup_mapping = {
            # Basketball
            b_normal:   ["Basketball: Mushroom Cup (Normal)", "Basketball: Flower Cup (Normal)", "Basketball: Star Cup (Normal)"],
            b_hard:     ["Basketball: Mushroom Cup (Hard)", "Basketball: Flower Cup (Hard)", "Basketball: Star Cup (Hard)"],

            # Dodgeball
            d_normal:   ["Dodgeball: Mushroom Cup (Normal)", "Dodgeball: Flower Cup (Normal)", "Dodgeball: Star Cup (Normal)"],
            d_hard:     ["Dodgeball: Mushroom Cup (Hard)", "Dodgeball: Flower Cup (Hard)", "Dodgeball: Star Cup (Hard)"],

            # Volleyball
            v_normal:   ["Volleyball: Mushroom Cup (Normal)", "Volleyball: Flower Cup (Normal)", "Volleyball: Star Cup (Normal)"],
            v_hard:     ["Volleyball: Mushroom Cup (Hard)", "Volleyball: Flower Cup (Hard)", "Volleyball: Star Cup (Hard)"],

            # Hockey
            h_normal:   ["Hockey: Mushroom Cup (Normal)", "Hockey: Flower Cup (Normal)", "Hockey: Star Cup (Normal)"],
            h_hard:     ["Hockey: Mushroom Cup (Hard)", "Hockey: Flower Cup (Hard)", "Hockey: Star Cup (Hard)"],

            # Sports Mix
            sports_mix: ["Sports Mix: Mushroom Cup", "Sports Mix: Flower Cup", "Sports Mix: Star Cup"],
        }

        for address, cup in cup_mapping.items():
            value = 0
            # Grabs the first letter of the first cup in order to pass it to has_unlocked_mode
            sport = {"B": "Basketball", "D": "Dodgeball", "V": "Volleyball", "H": "Hockey", "S": "SM"}[cup[0][:1]]

            # Mushroom Cup
            # If the Mushroom Cup is in unlocked cups, add 1
            if cup[0] in self.unlocked_cups:
                value += 1

            # Flower Cup
            # If the Flower Cup is in unlocked cups, add 2
            if cup[1] in self.unlocked_cups:
                value += 2

            # Star Cup
            # If the Star Cup is in unlocked cups, add 4
            if cup[2] in self.unlocked_cups:
                value += 4

            # If no cups are unlocked (value is 0), set final_value to 8 which locks all cups, otherwise set
            # final value to value
            if value == 0 or not self.has_unlocked_mode(sport):
                final_value = 8
            else:
                final_value = value

            new_addr = get_address(address)
            self.game_interface.dolphin_client.write_byte(new_addr, final_value)
            await self.check_write(new_addr, "byte", final_value)

    async def handle_progressive_cup_unlocks(self):
        """Handles the order and unlocking of the Progressive Cup item
        The order changes dynamically in accordance to the user's options"""

        # Base Normal progression configuration (Tiers 1-3)
        cup_unlock_order = [
            {"type": "sport", "suffix": "Mushroom Cup (Normal)"},
            {"type": "sport", "suffix": "Flower Cup (Normal)"},
            {"type": "sport", "suffix": "Star Cup (Normal)"},
        ]

        # Change this variable if Hard mode is on
        hard_enabled = self.hard_tournament_difficulty == True

        if hard_enabled:
            if self.start_with_mushroom == 3:
                # Puts Mushroom Hard at tier 2 to match with creating 2 prog cups at the start
                cup_unlock_order.insert(1, {"type": "sport", "suffix": "Mushroom Cup (Hard)"})
                cup_unlock_order.extend([
                    {"type": "sport", "suffix": "Flower Cup (Hard)"},
                    {"type": "sport", "suffix": "Star Cup (Hard)"},
                ])
            else:
                # Pushes Hard mode tournaments to Tiers 4-6
                cup_unlock_order.extend([
                    {"type": "sport", "suffix": "Mushroom Cup (Hard)"},
                    {"type": "sport", "suffix": "Flower Cup (Hard)"},
                    {"type": "sport", "suffix": "Star Cup (Hard)"},
                ])
            # Places Sports Mix at Tiers 7-9
            cup_unlock_order.extend([
                {"type": "sm", "value": "Sports Mix: Mushroom Cup"},
                {"type": "sm", "value": "Sports Mix: Flower Cup"},
                {"type": "sm", "value": "Sports Mix: Star Cup"},
            ])
        else:
            # Places Sports Mix right after Normal tournaments at Tiers 4-6
            cup_unlock_order.extend([
                {"type": "sm", "value": "Sports Mix: Mushroom Cup"},
                {"type": "sm", "value": "Sports Mix: Flower Cup"},
                {"type": "sm", "value": "Sports Mix: Star Cup"},
            ])

        sports_list = ["Basketball", "Dodgeball", "Volleyball", "Hockey"]
        progressive_count = self.progressive_cups

        # Iterate up to the current total of items held
        for index in range(progressive_count):
            if index < len(cup_unlock_order):
                rule = cup_unlock_order[index]

                if rule["type"] == "sport":
                    for sport in sports_list:
                        formatted_name = f"{sport}: {rule['suffix']}"
                        if formatted_name not in self.unlocked_cups:
                            self.unlocked_cups.add(formatted_name)
                            self.log_once("prog_cup",
                                          f"Progressive Cup level up! Unlocked: {rule['suffix']}", False)

                elif rule["type"] == "sm":
                    if rule["value"] not in self.unlocked_cups:
                        self.unlocked_cups.add(rule["value"])
                        self.log_once("prog_cup",
                                      f"Progressive Cup level up! Unlocked: {rule['value']}", False)


    # === Sports Mix ===


    async def handle_sports_mix_unlock(self):
        """Handles the unlocking of Sports Mix based on the user's option"""

        sports_mix_unlocked = get_address(SportsMixAddresses.sports_mix_unlocked)
        if self.sports_mix_unlock == 0:
            if "Sports Mix" in self.unlocked_modes:
                self.unlocked_sports_mix = True
                self.game_interface.dolphin_client.write_byte(sports_mix_unlocked, 11)
                await self.check_write(sports_mix_unlocked, "byte", 11)
                self.log_once("sm_unlock", "Sports Mix unlocked by Sports Mix item", True)
            else:
                self.game_interface.dolphin_client.write_byte(sports_mix_unlocked, 3)

        elif self.sports_mix_unlock == 1:
            required_items = ["Sports Crystal: Red", "Sports Crystal: Green", "Sports Crystal: Yellow",
                              "Sports Crystal: Blue"]
            # If all main_sports crystals are unlocked
            if all(crystal in self.unlocked_sports_crystals for crystal in required_items):
                self.unlocked_sports_mix = True
                self.game_interface.dolphin_client.write_byte(sports_mix_unlocked, 11)
                await self.check_write(sports_mix_unlocked, "byte", 11)
                self.log_once("sm_unlock", "Sports Mix unlocked by Sports Crystals", True)
            else:
                self.game_interface.dolphin_client.write_byte(sports_mix_unlocked, 3)

    # === Alt Path Unlocks ===

    async def handle_alt_path_unlocks(self):
        """Handles unlocking Alt Paths"""

        mushroom_alt_paths_unlocked = get_address(TournamentAddresses.mushroom_alt_paths_unlocked)
        flower_alt_paths_unlocked = get_address(TournamentAddresses.flower_alt_paths_unlocked)
        star_alt_paths_unlocked = get_address(TournamentAddresses.star_alt_paths_unlocked)
        current_sport = self.game_interface.get_tournament_sport()
        
        alt_path_spawn = get_address(TournamentAddresses.alt_path_condition_fufilled)
        current_node = self.game_interface.get_player_current_node()
        outer_bridge_addr = get_address(TournamentAddresses.flower_outer_bridges_toggle)
        inner_bridge_addr = get_address(TournamentAddresses.flower_inner_bridges_toggle)

        current_cup = self.game_interface.get_tournament_cup()

        if current_node > 0x17 and not current_node == 0xFF:
            self.in_alt_path = True
        else:
            self.in_alt_path = False
        

        """self.log_once(
            "alt_paths",
            f"AltPath state: include={self.alt_paths_enabled}, type={self.alt_paths_unlock_type}, "
            f"sport_var={current_sport}, "
            f"unlocked={len(self.unlocked_alt_paths)}, progressive={len(self.progressive_alt_paths)}",
            True
        )"""


        # Flower Cup Bridges always accessible
        if current_node == 0x55:
            self.game_interface.dolphin_client.write_byte(outer_bridge_addr, 1)
            await self.check_write(outer_bridge_addr, "byte", 1)
        else:
            self.game_interface.dolphin_client.write_byte(outer_bridge_addr, 0)
            await self.check_write(outer_bridge_addr, "byte", 0)

        if current_node == 0x26:
            self.game_interface.dolphin_client.write_byte(inner_bridge_addr, 0)
            await self.check_write(inner_bridge_addr, "byte", 0)
        else:
            self.game_interface.dolphin_client.write_byte(inner_bridge_addr, 1)
            await self.check_write(inner_bridge_addr, "byte", 1)


        if self.alt_paths_enabled:

            if self.alt_paths_always_spawn and current_node <= 17:
                self.game_interface.dolphin_client.write_byte(alt_path_spawn, 1)
                await self.check_write(alt_path_spawn, "byte", 1)

            cups = ["Mushroom", "Flower", "Star"]
            sports = ["Basketball", "Dodgeball", "Volleyball", "Hockey"]
            
            # Values for Mushroom, Flower, and Star Cup
            basketball_values = [0, 0, 0]
            dodgeball_values = [0, 0, 0]
            volleyball_values = [0, 0, 0]
            hockey_values = [0, 0, 0]
            sports_mix_values = [0, 0, 0]
            global_values = [0, 0, 0]

            # I wish I didnt have to do this maaan
            sport_values = {
                                "Basketball": basketball_values,
                                "Dodgeball": dodgeball_values,
                                "Volleyball": volleyball_values,
                                "Hockey": hockey_values,
                                "Sports Mix": sports_mix_values
                            }
            sport_addresses = {
                                "Basketball": BasketballAddresses,
                                "Dodgeball": DodgeballAddresses,
                                "Volleyball": VolleyballAddresses,
                                "Hockey": HockeyAddresses,
                            }        

            if self.alt_paths_unlock_type == 0:

                for sport in sports:
                    for cup in cups:
                        if f"{sport}: {cup} Cup Alt Paths (Normal)" in self.unlocked_alt_paths:
                            if sport == "Basketball":
                                basketball_values[cups.index(cup)] += 1
                            elif sport == "Dodgeball":
                                dodgeball_values[cups.index(cup)] += 1
                            elif sport == "Volleyball":
                                volleyball_values[cups.index(cup)] += 1
                            elif sport == "Hockey":
                                hockey_values[cups.index(cup)] += 1

                for sport in sports:
                    for cup in cups:
                        if f"{sport}: {cup} Cup Alt Paths (Hard)" in self.unlocked_alt_paths:
                            if sport == "Basketball":
                                basketball_values[cups.index(cup)] += 2
                            elif sport == "Dodgeball":
                                dodgeball_values[cups.index(cup)] += 2
                            elif sport == "Volleyball":
                                volleyball_values[cups.index(cup)] += 2
                            elif sport == "Hockey":
                                hockey_values[cups.index(cup)] += 2

                for cup in cups:
                    if f"Sports Mix: {cup} Cup Alt Paths" in self.unlocked_alt_paths:
                        sports_mix_values[cups.index(cup)] = 8

                values_to_insert = sport_values[current_sport]
                
                self.game_interface.dolphin_client.write_byte(mushroom_alt_paths_unlocked, values_to_insert[0])
                self.game_interface.dolphin_client.write_byte(flower_alt_paths_unlocked, values_to_insert[1])
                self.game_interface.dolphin_client.write_byte(star_alt_paths_unlocked, values_to_insert[2])
                await self.check_write(mushroom_alt_paths_unlocked, "byte", values_to_insert[0])
                await self.check_write(flower_alt_paths_unlocked, "byte", values_to_insert[1])
                await self.check_write(star_alt_paths_unlocked, "byte", values_to_insert[2])


            elif self.alt_paths_unlock_type == 1:
                    
                for sport in sports:
                    for cup in cups:
                        if f"{sport}: {cup} Cup Alt Paths (Global)" in self.unlocked_alt_paths:
                            if sport == "Basketball":
                                basketball_values[cups.index(cup)] = 3
                            elif sport == "Dodgeball":
                                dodgeball_values[cups.index(cup)] = 3
                            elif sport == "Volleyball":
                                volleyball_values[cups.index(cup)] = 3
                            elif sport == "Hockey":
                                hockey_values[cups.index(cup)] = 3
                
                values_to_insert = sport_values[current_sport]
                
                self.game_interface.dolphin_client.write_byte(mushroom_alt_paths_unlocked, values_to_insert[0])
                self.game_interface.dolphin_client.write_byte(flower_alt_paths_unlocked, values_to_insert[1])
                self.game_interface.dolphin_client.write_byte(star_alt_paths_unlocked, values_to_insert[2])
                await self.check_write(mushroom_alt_paths_unlocked, "byte", values_to_insert[0])
                await self.check_write(flower_alt_paths_unlocked, "byte", values_to_insert[1])
                await self.check_write(star_alt_paths_unlocked, "byte", values_to_insert[2])                


            elif self.alt_paths_unlock_type == 2:

                for cup in cups:
                    if f"{cup} Cup Alt Paths (Normal)" in self.unlocked_alt_paths:
                        global_values[cups.index(cup)] += 1

                for cup in cups:
                    if f"{cup} Cup Alt Paths (Hard)" in self.unlocked_alt_paths:
                        global_values[cups.index(cup)] += 2

                self.game_interface.dolphin_client.write_byte(mushroom_alt_paths_unlocked, global_values[0])
                self.game_interface.dolphin_client.write_byte(flower_alt_paths_unlocked, global_values[1])
                self.game_interface.dolphin_client.write_byte(star_alt_paths_unlocked, global_values[2])

            elif self.alt_paths_unlock_type == 3:

                for cup in cups:
                    if f"{cup} Cup Alt Paths (Global)" in self.unlocked_alt_paths:
                        global_values[cups.index(cup)] = 3

                self.game_interface.dolphin_client.write_byte(mushroom_alt_paths_unlocked, global_values[0])
                self.game_interface.dolphin_client.write_byte(flower_alt_paths_unlocked, global_values[1])
                self.game_interface.dolphin_client.write_byte(star_alt_paths_unlocked, global_values[2])

            elif self.alt_paths_unlock_type == 4:

                progressive_alt_path_count = self.progressive_alt_paths

                if progressive_alt_path_count >= 1:
                    self.game_interface.dolphin_client.write_byte(mushroom_alt_paths_unlocked, 1)
                if progressive_alt_path_count >= 2:
                    self.game_interface.dolphin_client.write_byte(flower_alt_paths_unlocked, 1)
                if progressive_alt_path_count >= 3:
                    self.game_interface.dolphin_client.write_byte(star_alt_paths_unlocked, 1)
                if progressive_alt_path_count >= 4:
                    self.game_interface.dolphin_client.write_byte(mushroom_alt_paths_unlocked, 3)
                if progressive_alt_path_count >= 5:
                    self.game_interface.dolphin_client.write_byte(flower_alt_paths_unlocked, 3)
                if progressive_alt_path_count >= 6:
                    self.game_interface.dolphin_client.write_byte(star_alt_paths_unlocked, 3)

            elif self.alt_paths_unlock_type == 5:

                progressive_alt_path_count = self.progressive_alt_paths

                if progressive_alt_path_count >= 1:
                    self.game_interface.dolphin_client.write_byte(mushroom_alt_paths_unlocked, 3)
                if progressive_alt_path_count >= 2:
                    self.game_interface.dolphin_client.write_byte(flower_alt_paths_unlocked, 3)
                if progressive_alt_path_count >= 3:
                    self.game_interface.dolphin_client.write_byte(star_alt_paths_unlocked, 3)

            # Handles characters that block paths
            if current_cup in ["Mushroom", "Flower"]:
                self.game_interface.dolphin_client.write_byte(star_alt_paths_unlocked, 3)

            if self.in_alt_path:
                for sport in sports:
                    if sport != "Sports Mix":
                        sport_class = sport_addresses[sport]

                        ninja_attr = getattr(sport_class.Characters, "ninja")
                        ninja_addr = get_address(ninja_attr)
                        white_mage_attr = getattr(sport_class.Characters, "white_mage")
                        white_mage_addr = get_address(white_mage_attr)
                        black_mage_attr = getattr(sport_class.Characters, "black_mage")
                        black_mage_addr = get_address(black_mage_attr)
                        slime_attr = getattr(sport_class.Characters, "slime")
                        slime_addr = get_address(slime_attr)

                        self.game_interface.dolphin_client.write_byte(ninja_addr, 1)
                        await self.check_write(ninja_addr, "byte", 1)
                        self.game_interface.dolphin_client.write_byte(white_mage_addr, 1)
                        await self.check_write(white_mage_addr, "byte", 1)
                        self.game_interface.dolphin_client.write_byte(black_mage_addr, 1)
                        await self.check_write(black_mage_addr, "byte", 1)
                        self.game_interface.dolphin_client.write_byte(slime_addr, 1)
                        await self.check_write(slime_addr, "byte", 1)
        else:
            self.game_interface.dolphin_client.write_byte(mushroom_alt_paths_unlocked, 0)
            self.game_interface.dolphin_client.write_byte(flower_alt_paths_unlocked, 0)
            self.game_interface.dolphin_client.write_byte(star_alt_paths_unlocked, 0)

        

    # === Exhibition Unlocks ===


    async def handle_court_unlocks(self):
        """Handles the unlocking of courts"""

        # Link variables to the address in the correct class
        # Basketball
        b_mushroom = BasketballAddresses.Exhibition.mushroom_cup
        b_flower = BasketballAddresses.Exhibition.flower_cup
        b_star = BasketballAddresses.Exhibition.star_cup
        b_block = BasketballAddresses.Exhibition.question_mark_cup

        # Volleyball
        v_mushroom = VolleyballAddresses.Exhibition.mushroom_cup
        v_flower = VolleyballAddresses.Exhibition.flower_cup
        v_star = VolleyballAddresses.Exhibition.star_cup
        v_block = VolleyballAddresses.Exhibition.question_mark_cup

        # Dodgeball
        d_mushroom = DodgeballAddresses.Exhibition.mushroom_cup
        d_flower = DodgeballAddresses.Exhibition.flower_cup
        d_star = DodgeballAddresses.Exhibition.star_cup
        d_block = DodgeballAddresses.Exhibition.question_mark_cup

        # Hockey
        h_mushroom = HockeyAddresses.Exhibition.mushroom_cup
        h_flower = HockeyAddresses.Exhibition.flower_cup
        h_star = HockeyAddresses.Exhibition.star_cup
        h_block = HockeyAddresses.Exhibition.question_mark_cup

        # Link stages to variable
        stage_mapping = {
            # Basketball
            b_mushroom: ["Basketball", "Mario Stadium", "Koopa Troopa Beach", "DK Dock"],
            b_flower:   ["Basketball", "Luigi's Mansion", "Western Junction", "Daisy Garden"],
            b_star:     ["Basketball", "Bowser Jr. Blvd.", "Bowser's Castle", "Star Ship"],
            b_block:    ["Basketball", "Peach's Castle", "Wario Factory", "Ghoulish Galleon"],

            # Volleyball
            v_mushroom: ["Volleyball", "Mario Stadium", "Koopa Troopa Beach", "Peach's Castle"],
            v_flower:   ["Volleyball", "DK Dock", "Luigi's Mansion", "Western Junction"],
            v_star:     ["Volleyball", "Bowser Jr. Blvd.", "Bowser's Castle", "Star Ship"],
            v_block:    ["Volleyball", "Wario Factory", "Waluigi Pinball", "Ghoulish Galleon"],

            # Dodgeball
            d_mushroom: ["Dodgeball", "Mario Stadium", "Koopa Troopa Beach", "Peach's Castle"],
            d_flower:   ["Dodgeball", "DK Dock", "Toad Park", "Daisy Garden"],
            d_star:     ["Dodgeball", "Wario Factory", "Bowser's Castle", "Star Ship"],
            d_block:    ["Dodgeball", "Western Junction", "Waluigi Pinball", "Ghoulish Galleon"],

            # Hockey
            h_mushroom: ["Hockey", "Mario Stadium", "Toad Park", "Peach's Castle"],
            h_flower:   ["Hockey", "Western Junction", "Wario Factory", "Daisy Garden"],
            h_star:     ["Hockey", "Bowser Jr. Blvd.", "Waluigi Pinball", "Star Ship"],
            h_block:    ["Hockey", "Koopa Troopa Beach", "Ghoulish Galleon", "Bowser's Castle"],
        }

        for address, court in stage_mapping.items():
            value = 0

            # First Court
            # If the first court is in unlocked courts, add 1
            if court[1] in self.unlocked_courts:
                value += 1

            # Second Court
            # If the second court is in unlocked courts, add 2
            if court[2] in self.unlocked_courts:
                value += 2

            # Third Court
            # If the third court is in unlocked courts, add 4
            if court[3] in self.unlocked_courts:
                value += 4

            # If no courts are unlocked (value is 0) or the sport isn't unlocked, set final_value to 8 which locks
            # all courts, otherwise set final value to value
            if value == 0 or not self.has_unlocked_mode(court[0]):
                final_value = 8
            else:
                final_value = value

            new_addr = get_address(address)
            self.game_interface.dolphin_client.write_byte(new_addr, final_value)
            await self.check_write(new_addr, "byte", final_value)

    async def handle_progressive_court_unlocks(self):
        """Handles the Progressive Court item, this order will NOT change."""

        # The order the courts will unlock, from first to last
        court_unlock_order = [
            "Mario Stadium",
            "Koopa Troopa Beach",
            "Peach's Castle",
            "Toad Park",
            "DK Dock",
            "Western Junction",
            "Luigi's Mansion",
            "Wario Factory",
            "Daisy Garden",
            "Waluigi Pinball",
            "Bowser Jr. Blvd.",
            "Ghoulish Galleon",
            "Bowser's Castle",
            "Star Ship",
            "Behemoth Stage"
        ]

        # Count how many total Progressive Stage items the server has sent us
        progressive_count = self.progressive_courts

        # Iterate through ordered list up to the number of stages we have unlocked
        for index in range(progressive_count):
            # Safety check to prevent index errors if extra progressive items are somehow received
            if index >= len(court_unlock_order):
                break

            target_stage = court_unlock_order[index]

            # Add to unlocked_courts if it isn't already there
            if target_stage not in self.unlocked_courts:
                self.unlocked_courts.add(target_stage)
                logger.info(f"Progressive Court level up! Unlocked: {target_stage}")

    # Unstable function due to the unstable address, probably needs pointers
    def has_unlocked_difficulty(self):
        """Checks if the difficulty selected is unlocked. If not, stops all the stages from showing"""
        diff_on_menu = self.game_interface.dolphin_client.read_byte(get_address(MatchAddresses.ex_diff_on_menu))

        diff_to_item = {
            0: "Easy",
            1: "Normal",
            2: "Hard",
            3: "Expert"
        }

        diff_name = diff_to_item.get(diff_on_menu)
        diff_item = f"Exhibition {diff_name}"
        item_missing_message = f"Blocked stages from appearing! Missing: {diff_item}"
        diff_not_active_message = f"Blocked stages from appearing! Disabled difficulty: {diff_name}"

        if diff_item in self.unlocked_ex_diffs:
            return True
        elif diff_name not in self.exhibition_difficulties:
            self.log_once("has_unlocked_difficulty", diff_not_active_message, False)
            return False
        else:
            self.log_once("has_unlocked_difficulty", item_missing_message, False)
            return False


    # === Party Mode Unlocks ===


    async def handle_party_unlocks(self):
        """Handles the unlocking of Party Mode courts, could be merged with handle_court_unlocks"""

        fp_apple = PartyMode.FeedPetey.Tabs.apple_tab
        fp_watermelon = PartyMode.FeedPetey.Tabs.watermelon_tab

        hh_1 = PartyMode.HarmonyHustle.Tabs.one_note_tab
        hh_2 = PartyMode.HarmonyHustle.Tabs.two_note_tab
        hh_3 = PartyMode.HarmonyHustle.Tabs.three_note_tab

        bod_bomb = PartyMode.BobOmbDodge.Tabs.bob_omb_tab
        bod_cannon = PartyMode.BobOmbDodge.Tabs.cannon_tab

        ss_hockey = PartyMode.SmashSkate.Tabs.hockey_stick_tab
        ss_skate = PartyMode.SmashSkate.Tabs.skate_tab

        item_mapping = {
            fp_apple:      ["Feed Petey", "Daisy Garden", "DK Dock", "Wario Factory"],
            fp_watermelon: ["Feed Petey", "Daisy Garden", "DK Dock", "Wario Factory"],

            hh_1:          ["Harmony Hustle", "Classic Ocean", "Chocobo Rhythm", "Mario Athletic", "Mushroom Mix Medley"],
            hh_2:          ["Harmony Hustle", "Bloocheep Ocean", "Chocobo Pop", "Punk Athletic", "Blossom Mix Medley"],
            hh_3:          ["Harmony Hustle", "Punk Ocean", "Chocobo Beat", "Island Athletic", "Star Mix Medley"],

            bod_bomb:      ["Bob-omb Dodge", "Mario Stadium", "Ghoulish Galleon", "Western Junction"],
            bod_cannon:    ["Bob-omb Dodge", "Mario Stadium", "Ghoulish Galleon", "Western Junction"],

            ss_hockey:     ["Smash Skate", "Sherbet Sea", "Rowdy Raft", "Fire Mountain"],
            ss_skate:      ["Smash Skate", "Sherbet Sea", "Rowdy Raft", "Fire Mountain"],
        }

        for address, items in item_mapping.items():
            value = 0

            if items[1] in self.unlocked_courts:
                value += 1

            if items[2] in self.unlocked_courts:
                value += 2

            if items[3] in self.unlocked_courts:
                value += 4

            # Harmony Hustle has a fourth unlock in each tab; the other party
            # modes have only three, so only read index 4 when it exists.
            if len(items) > 4 and items[4] in self.unlocked_courts:
                value += 8

            # Note: If value is 0, nothing is unlocked.
            if value == 0 or not self.has_unlocked_mode(items[0]):
                final_value = 16
            else:
                final_value = value

            new_addr = get_address(address)
            self.game_interface.dolphin_client.write_byte(new_addr, final_value)
            await self.check_write(new_addr, "byte", final_value)


    # === Ability Unlocks ===


    async def handle_unlocked_abilities(self):
        """Awaits all functions to do with ability unlocking"""

        await self.handle_special_meter_unlock()

    async def handle_special_meter_unlock(self):
        """Handles the unlocking of the special meter"""


        if not self.ready_to_handle():
            self.debug_log("Special meter lock waiting; game not ready")
            return

        try:
            if "Special Meter" not in self.unlocked_abilities:
                self.game_interface.dolphin_client.write_pointer(self.addresslib.p_special_meter_addr,
                                                                 Pointers.Player.special_meter_offsets,
                                                                 "float", 0.0)

            else:
                self.log_once("special_meter", "Special meter unlocked; not locking meter", True)
        except Exception as e:
            self.debug_log(f"Special meter handling failed: {e}")


    # === Filler + ?-Panel Handling ===


    async def handle_one_time_items(self):
        """Handles the giving of filler items / items that begin with 1"""

        # Queue empty? Nothing to do.
        if not self.filler_to_give:
            return

        self.debug_log(f"Filler queue pending: size={len(self.filler_to_give)}, first={self.filler_to_give[0]}")

        # Game not in a valid state? Wait until later.
        if not self.ready_to_handle():
            self.debug_log(f"Waiting to give filler; game not ready. Queue size: {len(self.filler_to_give)}")
            return

        queued_filler = self.filler_to_give[0]
        if isinstance(queued_filler, tuple):
            item_index, filler = queued_filler
        else:
            item_index = None
            filler = queued_filler

        # Player already has an item? Don't overwrite it.
        current_item = self.current_item_func()
        special_charge = self.game_interface.dolphin_client.read_pointer(self.addresslib.p_special_meter_addr,
                                                                         Pointers.Player.special_meter_offsets,
                                                                         "float")

        if filler != "1 Coin" and current_item != -1:
            self.debug_log(f"Waiting to give {filler}; player already has item={current_item}")
            return
        elif filler == "Special Meter Charge" and special_charge == 1.0:
            self.debug_log("Waiting to give Special Meter Charge; player has a full special meter")
            return

        # Prevent question mark panel replacement while giving item
        self.one_time_running = True
        self.awaiting_use = True

        # Take the oldest queued filler item
        self.filler_to_give.popleft()
        logger.info(f"Processing from Queue: {filler}")
        self.debug_log(f"Processing filler index={item_index}, remaining filler queue={len(self.filler_to_give)}")

        # Coins are handled here because they do not use the item slot.
        if filler == "1 Coin":
            current_coins = self.game_interface.dolphin_client.read_word(self.addresslib.p_coins_addr)

            new_coins = min(current_coins + 1, 10)

            self.game_interface.dolphin_client.write_word(self.addresslib.p_coins_addr, new_coins)

            logger.info(f"Gave 1 Coin ({new_coins}/10)")
            self.debug_log(f"Coins changed from {current_coins} to {new_coins}")
            # The coin was written successfully, so reconnects should not grant it again.
            await self.mark_consumable_handled(item_index)
            return
        
        if filler == "Special Meter Charge":
            if "Special Meter" in self.unlocked_abilities:
                self.game_interface.dolphin_client.write_pointer(self.addresslib.p_special_meter_addr,
                                                                 Pointers.Player.special_meter_offsets,
                                                                 "float", 1.0)
                logger.info("Special Meter fully charged!")
                await self.mark_consumable_handled(item_index)
                return
            else:
                logger.info(f"Special Meter not unlocked, converting to 1 Super Star")
                filler = "1 Super Star"


        item_map = {
            "1 Green Shell": 0,
            "1 Red Shell": 1,
            "1 Mini Mushroom": 2,
            "1 Bob-omb": 3,
            "1 Super Star": 4,
            "1 Banana": 5,
        }

        if filler not in item_map:
            logger.warning(f"Unknown filler item: {filler}")
            # Unknown one-shot items are consumed so they do not block the queue forever.
            await self.mark_consumable_handled(item_index)
            return

        try:
            # Extract the integer ID (e.g., 0, 1, 2...)
            item_id = item_map[filler]
            self.forced_item_id = int(item_id)

            # Give the item
            self.game_interface.dolphin_client.write_word(self.addresslib.p_item_held_addr, self.forced_item_id)

            verify_item = self.current_item_func()
            await self.check_write(self.addresslib.p_item_held_addr, "word", self.forced_item_id)
            logger.info(f"Dolphin Write Success: {filler}")
            # Save after the Dolphin write, not when queued, so disconnects before this do not eat filler.
            await self.mark_consumable_handled(item_index)
            self.debug_log(f"Wrote held item id {item_id} for {filler}; addr={self.addresslib.p_item_held_addr:#x}, verify={verify_item}")

        finally:
            self.one_time_running = False

        await asyncio.sleep(0.1)

    def current_match_score_total(self):
        player_score = sum(self.game_interface.dolphin_client.read_word(get_address(address)) for address in player_score_addresses)
        opponent_score = sum(self.game_interface.dolphin_client.read_word(get_address(address)) for address in opponent_score_addresses)
        return player_score + opponent_score

    def update_scoring_item_suppression(self):
        score_total = self.current_match_score_total()

        if self.last_match_score_total is None:
            self.last_match_score_total = score_total
            return

        if score_total != self.last_match_score_total:
            self.last_match_score_total = score_total
            self.suppress_panel_until = asyncio.get_event_loop().time() + 5
            self.debug_log("Score changed; suppressing ?-panel item replacement briefly")

    def has_ended(self):
        """Check if the timer is at 0 for every sport except Volleyball"""
        timer = self.game_interface.dolphin_client.read_byte(self.addresslib.timer_addr)
        if self.game_interface.get_mode() == "Volleyball":
            return False

        elif timer == 0 and self.game_interface.get_mode() != "Volleyball":
            return True
        else:
            return False

    async def handle_question_mark_panel_items(self):
        """Handles the replacement of ?-Panel items
        VERY BUGGED, does kind of work but research is helping change this function to work fully"""

        self.update_scoring_item_suppression()
        item_data = self.current_item_func()
        self.debug_log(f"Panel check: item={item_data}, unlocked={len(self.unlocked_panel_items)},"
                       f"awaiting={self.awaiting_use}, forced={self.forced_item_id}, processed={self.item_processed}")

        # Handle replacement from game
        if asyncio.get_event_loop().time() < self.suppress_panel_until and self.forced_item_id is not None:
            self.game_interface.dolphin_client.write_word(self.addresslib.p_item_held_addr, self.forced_item_id)
            verify_item = self.current_item_func()
            self.debug_log(f"Forced item back to {self.forced_item_id}; previous={item_data}, verify={verify_item}")
            return

        # If we don't have an item, pause.
        if item_data == -1 and self.ready_to_handle():
            self.item_processed = False
            self.awaiting_use = False
            self.forced_item_id = None
            return

        # If we are currently forcing an item from a scoring replacement
        # or a one-time item, DO NOT let the ?-panel code claim credit for it.
        if self.awaiting_use or item_data == self.forced_item_id or self.item_processed:
            self.debug_log("Panel replacement skipped; forced/awaiting/processed state active")
            return

        # Standard pauses
        if (self.one_time_running or not self.ready_to_handle() or self.item_processed
                or self.game_interface.special_active()):
            self.debug_log("Panel replacement skipped; one-time item active, not ready, or already processed")
            return

        # Handle Empty List
        if not self.unlocked_panel_items:
            #
            self.game_interface.dolphin_client.write_word(self.addresslib.p_item_held_addr, self.minus_one)
            self.debug_log("There are no items available, replaced with -1 (self.minus_one)")
            logger.info("?-Panel Activated! No items available! Sucks to be you >;]")
            self.item_processed = True  # Mark processed so we don't spam the log
            return

        # Lookup Map
        item_map = {
            "Green Shell": 0,
            "Red Shell": 1,
            "Mini Mushroom": 2,
            "Bob-omb": 3,
            "Super Star": 4,
            "Banana": 5
        }

        # Random Selection & Execution
        random_item = random.choice(list(self.unlocked_panel_items))

        # Extract the base name (e.g., if item is "1 Banana", get "Banana")
        # This searches the keys of the map to find a match
        item_id = next((val for key, val in item_map.items() if key in random_item), None)

        if item_id is not None:
            item_id_int = int(item_id)
            self.game_interface.dolphin_client.write_word(self.addresslib.p_item_held_addr, item_id_int)
            verify_item = self.current_item_func()
            logger.info(f"?-Panel activated! Item replaced with {random_item}!")
            self.debug_log(f"Panel wrote item id {item_id_int}; addr={self.addresslib.p_item_held_addr:#x}, verify={verify_item}")
            await self.check_write(self.addresslib.p_item_held_addr, "word", item_id_int)
            self.item_processed = True
            self.awaiting_use = True
            self.forced_item_id = item_id_int
        else:
            self.debug_log(f"Panel selected {random_item}, but no item id matched")

        await asyncio.sleep(0.1)


    # === Trap Handling ===

    async def handle_traps(self):
        """Handles trap execution"""

        # If no traps in queue, bail
        if not self.traps_to_give:
            return

        if not self.ready_to_handle() or self.trap_running:
            self.debug_log(f"Waiting to trigger trap; game not ready. Queue size: {len(self.traps_to_give)}")
            return

        # Using lambdas allows us to map the method with its respective argument
        # without executing it during dictionary definition.
        trap_mapping = {
            "Freeze Character 1 Trap": lambda: self.run_freeze_trap(1),
            "Freeze Character 2 Trap": lambda: self.run_freeze_trap(2),
            "Freeze Character 3 Trap": lambda: self.run_freeze_trap(3),
            "Coins Trap": self.opponent_coins,
            "Timer Trap": self.half_timer,
            "Fast Trap": self.fast_trap,
            "Slow Trap": self.slow_trap,
            "Teleport Character 1 Trap": lambda: self.teleport_trap(1),
            "Teleport Character 2 Trap": lambda: self.teleport_trap(2),
            "Teleport Character 3 Trap": lambda: self.teleport_trap(3),
            #"Swap Trap": self.swap_trap,
        }

        queued_trap = self.traps_to_give.popleft()
        if isinstance(queued_trap, tuple):
            item_index, trap = queued_trap
        else:
            item_index = None
            trap = queued_trap

        logger.info(f"Triggering {trap}")
        self.debug_log(f"Processing trap index={item_index}, remaining trap queue={len(self.traps_to_give)}")

        # Handle Function-based traps
        if trap in trap_mapping:
            # If the trap is for character 3, but we're only playing 2-on-2, send trap to either char 1 or 2
            if trap == "Freeze Character 3 Trap" and self.game_interface.check_team_amount() == 2:
                random_int = randint(1, 2)
                logger.info(f"2-on-2 detected! Sending trap to character {random_int}")
                trap_to_send = f"Freeze Character {random_int} Trap"

                self.debug_log(f"Redirected Freeze Character 3 to character {random_int}")

            elif trap == "Teleport Character 3 Trap" and self.game_interface.check_team_amount() == 2:
                random_int = randint(1, 2)
                logger.info(f"2-on-2 detected! Sending trap to character {random_int}")
                trap_to_send = f"Teleport Character {random_int} Trap"

                self.debug_log(f"Redirected Teleport Character 3 to character {random_int}")
            else:
                trap_to_send = trap


            # For standalone methods, this runs them. For lambdas, it resolves the underlying coroutine.
            self.trap_running = True
            task = asyncio.create_task(trap_mapping[trap_to_send]())
            task.add_done_callback(self._on_trap_task_done)

            self.debug_log(f"Started trap task for {trap_to_send}")
            await self.mark_consumable_handled(item_index)

        else:
            logger.warning(f"Unknown trap item: {trap}")
            self.debug_log(f"Unknown trap {trap} consumed so it does not loop forever")
            await self.mark_consumable_handled(item_index)

        # Prevents multiple traps from firing at the exact same millisecond
        await asyncio.sleep(0.1)

    def _on_trap_task_done(self, task):
        """Sets trap_running to false when the trap task is done"""

        if task.exception():
            logger.exception("Trap task failed", exc_info=task.exception())
        self.trap_running = False

    async def run_freeze_trap(self, char_id: int):
        """Freezes the character in place for 5 seconds"""

        char = f"B{char_id}"
        offset_1 = getattr(Pointers.Player, char)
        offset_group = getattr(offset_1, "Position")

        x_addr = self.game_interface.dolphin_client.follow_pointers(self.addresslib.p_pos_addr, offset_group.x_offsets)
        z_addr = self.game_interface.dolphin_client.follow_pointers(self.addresslib.p_pos_addr, offset_group.z_offsets)


        # Capture location
        freeze_x = self.game_interface.dolphin_client.read_float(x_addr)
        freeze_z = self.game_interface.dolphin_client.read_float(z_addr)

        self.debug_log(f"Freeze Trap {char_id} started at ({freeze_x}, {freeze_z})")

        # Set timer
        end_time = asyncio.get_event_loop().time() + 5.0

        # Freeze Loop
        while asyncio.get_event_loop().time() < end_time:
            self.game_interface.dolphin_client.write_float(x_addr, freeze_x)
            self.game_interface.dolphin_client.write_float(z_addr, freeze_z)

            await asyncio.sleep(0.02)

        self.debug_log(f"Freeze Trap {char_id} finished.")

    async def opponent_coins(self):
        """Gives the opponent a random number of coins between 1 and 5"""

        current_coins = self.game_interface.dolphin_client.read_word(self.addresslib.o_coins_addr)
        random_int = randint(1,5)
        new_coins = current_coins + random_int
        # Coin count in MSM cannot go above 10
        final_coins = min(new_coins, 10)
        self.game_interface.dolphin_client.write_word(self.addresslib.o_coins_addr, final_coins)
        logger.info(f"The opponent now has {final_coins} coins!")
        self.debug_log(f"Opponent coins set to {final_coins}")

    async def half_timer(self):
        """Divides the current timer by 2 and writes that"""

        current_time = self.game_interface.dolphin_client.read_float(self.addresslib.timer_addr)
        new_time = current_time / 2
        self.game_interface.dolphin_client.write_float(self.addresslib.timer_addr, new_time)
        self.debug_log(f"Timer cut in half to {new_time}")

    async def fast_trap(self):
        """Speeds up the game to x3 speed for 5 seconds"""

        self.debug_log("Fast Trap started")
        addr = get_address(MatchAddresses.game_speed)
        speed = 3

        # Set timer
        end_time = asyncio.get_event_loop().time() + 5

        # Sometimes the game can set the value, keep it constant
        while asyncio.get_event_loop().time() < end_time:
            self.game_interface.dolphin_client.write_float(addr, speed)
            await asyncio.sleep(0.1)

        # Return to normal speed
        self.game_interface.dolphin_client.write_float(addr, 1) # 1 = Default speed

    async def slow_trap(self):
        """Slows down the game to x0.5 speed for 5 seconds"""

        self.debug_log("Slow Trap started")
        addr = get_address(MatchAddresses.game_speed)
        speed = 0.5

        # Set timer
        end_time = asyncio.get_event_loop().time() + 5

        # Sometimes the game can set the value, keep it constant
        while asyncio.get_event_loop().time() < end_time:
            self.game_interface.dolphin_client.write_float(addr, speed)
            await asyncio.sleep(0.1)

        # Return to normal speed
        self.game_interface.dolphin_client.write_float(addr, 1) # 1 = Default speed

    async def teleport_trap(self, char_id: int):
        """Teleports the player anywhere in the bounds of the map"""

        # Get random floats
        float_x = uniform(-11, 11)
        float_z = uniform(-24, 24)
        # Max possible values, if it's OOB the game will just force the player back in bounds
        # We don't change the y value because that stays permanent until the player jumps

        # Round to 1 decimal place
        tele_x = round(float_x, 1)
        tele_z = round(float_z, 1)

        char = f"B{char_id}"
        offset_1 = getattr(Pointers.Player, char)
        offset_group = getattr(offset_1, "Position")

        self.game_interface.dolphin_client.write_pointer(self.addresslib.p_pos_addr, offset_group.x_offsets,
                                                         "float", tele_x)

        self.game_interface.dolphin_client.write_pointer(self.addresslib.p_pos_addr, offset_group.z_offsets,
                                                         "float", tele_z)

        self.debug_log(f"Teleported character {char_id} to X: {tele_x}, Z: {tele_z}")

    # async def swap_trap(self):
    #     """Swaps which character the player is controlling"""
    #
    #     cpu_offsets = [
    #         Offsets.Player.B1.is_cpu,
    #         Offsets.Player.B2.is_cpu,
    #         Offsets.Player.B3.is_cpu,
    #     ]
    #
    #     addr = get_address(PlayerAddresses.is_cpu)
    #
    #     active_index = None
    #
    #     for i, offsets in enumerate(cpu_offsets):
    #         new_addr = self.game_interface.dolphin_client.follow_pointers(addr, offsets)
    #
    #         if self.game_interface.dolphin_client.read_word(new_addr) == 1:
    #             active_index = i
    #             break
    #
    #     if active_index is None:
    #         return
    #
    #     inactive_indices = [i for i in range(len(cpu_offsets)) if i != active_index]
    #     new_active_index = random.choice(inactive_indices)
    #
    #     # Disable current player
    #     current_addr = self.game_interface.dolphin_client.follow_pointers(addr, cpu_offsets[active_index])
    #     self.game_interface.dolphin_client.write_byte(current_addr, 1)
    #
    #     # Enable new player
    #     new_addr = self.game_interface.dolphin_client.follow_pointers(addr, cpu_offsets[new_active_index])
    #     self.game_interface.dolphin_client.write_byte(new_addr, 0)

    # === Custom Tournament Settings Stuff ===

    async def handle_custom_tournament_settings(self):
        """Awaits all functions to do with setting custom tournament settings"""

        await self.set_custom_tournament_timer()
        await self.set_period_amount()
        await self.has_points_win()
        await self.set_custom_dodge_health()

    def get_default_time(self):
        """Gets the default option value corresponding to the default timer value for the sport"""

        mode = self.game_interface.get_mode()
        if mode == "Basketball":
            return 2
        elif mode == "Dodgeball" or mode == "Hockey":
            return 3
        else:
            return None

    def get_custom_time(self):
        """Retrieves the custom timer amount from the option value"""
        b_option_to_timer = {
            0: 5400,
            1: 7200,
            2: 9000,
            3: 10800,
            4: 12600,
            5: 999999,
        }

        h_d_option_to_timer = {
            0: 7200,
            1: 9000,
            2: 10800,
            3: 12600,
            4: 14400,
            5: 999999,
        }
        mode = self.game_interface.get_mode()

        if mode == "Basketball":
            return b_option_to_timer.get(self.custom_basket_time)
        elif mode == "Dodgeball":
            return h_d_option_to_timer.get(self.custom_dodge_time)
        elif mode == "Hockey":
            return h_d_option_to_timer.get(self.custom_hockey_time)
        else:
            return 999999

    async def set_custom_tournament_timer(self):
        """Sets the custom timer depending on the sport and player's option.
        Volleyball doesn't have a timer."""
        new_time = None
        status = self.game_interface.match_status()

        if status in (2,3):
            self.handled_custom_timer = False

        if self.handled_custom_timer:
            return

        sport = self.game_interface.get_mode()

        if sport == "Volleyball": # Volleyball doesn't have a timer
            return


        if sport == "Basketball":
            # If the value set is the default value, don't do anything because we don't need to.
            if self.custom_basket_time != self.get_default_time():
                new_time = self.get_custom_time()

        elif sport == "Dodgeball":
            if self.custom_dodge_time != self.get_default_time():
                new_time = self.get_custom_time()

        elif sport == "Hockey":
            if self.custom_hockey_time != self.get_default_time():
                new_time = self.get_custom_time()

        if new_time is not None:
            self.game_interface.dolphin_client.write_float(self.addresslib.max_time_addr, new_time)
            self.game_interface.dolphin_client.write_float(self.addresslib.timer_addr, new_time)
            self.handled_custom_timer = True
            self.debug_log(f"Custom timer set to {new_time}")

    async def set_period_amount(self):
        """Sets the amount of periods/sets in the match according to the player's option"""
        addr = get_address(MatchAddresses.max_periods)

        # This is true when we're locking points, don't do anything.
        if self.locking_period:
            return

        sport = self.game_interface.get_mode()

        sport_to_var = {
            "Basketball": self.b_period,
            "Dodgeball": self.d_period,
            "Volleyball": self.v_period,
            "Hockey": self.h_period
        }

        target_value = sport_to_var.get(sport, None)

        if target_value is not None:
            self.game_interface.dolphin_client.write_byte(addr, target_value)

    async def has_points_win(self):
        """Check if the player has scored the required amount of points to win the period/set"""

        sport = self.game_interface.get_mode()
        curr_player_score = self.game_interface.dolphin_client.read_word(self.game_interface.get_player_score_addr(True))
        curr_opp_score = self.game_interface.dolphin_client.read_word(self.game_interface.get_opponent_score_addr
                                                                      (self.party_mode_opponent, True))
        _, court_name = self.game_interface.get_court()

        if sport == "Basketball":
            if self.enable_b_points:
                # Checks if the player OR opponent has reached the points to win, if so, set timer to 0 which ends
                # the period
                if court_name == "Bowser Jr. Blvd.":
                    multiplied = (self.b_points_win * 5) + 50
                    points_to_win = int(round(multiplied, 1))
                else:
                    points_to_win = self.b_points_win

                if curr_player_score >= points_to_win or curr_opp_score >= points_to_win:
                    self.game_interface.dolphin_client.write_float(self.addresslib.timer_addr, 0)


        elif sport == "Volleyball":
            if court_name == "Bowser Jr. Blvd.":
                multiplied = self.v_points_win * 2
                points_to_win = int(round(multiplied, 1))
            else:
                points_to_win = self.v_points_win

            # Changes the value of the points to win address since Volleyball does all this by itself
            self.game_interface.dolphin_client.write_byte(get_address(VolleyballAddresses.points_to_win),
                                                          points_to_win)

        elif sport == "Hockey":
            if self.enable_h_points:
                # Checks if the player OR opponent has reached the points to win, if so, set timer to 0 which ends
                # the period
                if court_name == "Bowser Jr. Blvd.":
                    multiplied = (self.h_points_win * 5) + 50
                    points_to_win = int(round(multiplied, 1))
                else:
                    points_to_win = self.h_points_win

                if curr_player_score >= points_to_win or curr_opp_score >= points_to_win:
                    self.game_interface.dolphin_client.write_float(self.addresslib.timer_addr, 0)

    async def set_custom_dodge_health(self):
        """Sets the custom health in dodgeball"""
        sport = self.game_interface.get_mode()

        if sport == "Dodgeball":
            if self.ready_to_handle():
                self.game_interface.dolphin_client.write_word(get_address(PlayerAddresses.dodge_max_health), self.d_max_health)
                self.game_interface.dolphin_client.write_word(get_address(OpponentAddresses.dodge_max_health), self.d_max_health)


    # === Goal/Boss Stuff ===


    async def has_boss_goaled(self):
        """Check if the player has goaled in the boss, if their goal isn't that boss, send the check for it"""
        # If we already sent the goal or location check for the boss, stop running
        if self.boss_defeat_handled:
            return

        if self.ready_to_handle():
            address_behemoth_hp = self.game_interface.dolphin_client.follow_pointers(self.addresslib.behemoth_hp_addr,
                                                                                     Pointers.Boss.behemoth_hp_offsets)

            # Behemoth Handling
            if self.is_behemoth:

                # Ensure pointer resolution didn't fail/return a bad address
                if address_behemoth_hp:
                    behemoth_hp = self.game_interface.dolphin_client.read_float(address_behemoth_hp)

                    if behemoth_hp is not None and behemoth_hp <= 0:
                        self.boss_defeat_handled = True

                        if self.goal_condition == 1:
                            await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                            self.debug_log("Goal Achieved: Defeat Behemoth!")
                        else:
                            await self.check_location("Defeat Behemoth!")

            # Behemoth King Handling
            elif self.is_behemoth_king:

                if address_behemoth_hp:
                    behemoth_hp = self.game_interface.dolphin_client.read_float(address_behemoth_hp)

                    if behemoth_hp is not None and behemoth_hp <= 0:
                        self.boss_defeat_handled = True

                        if self.goal_condition == 2:
                            await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                            self.debug_log("Goal Achieved: Defeat Behemoth King!")
                        else:
                            await self.check_location("Defeat Behemoth King!")

    async def check_boss_type(self):
        """Check which boss is currently being fought"""

        is_sports_mix = self.game_interface.is_sports_mix()
        _, court_name = self.game_interface.get_court()

        if court_name == "Behemoth Stage":
            if is_sports_mix:
                self.is_behemoth_king = True
                self.is_behemoth = False
                self.debug_log("Behemoth King Found")
            else:
                self.is_behemoth_king = False
                self.is_behemoth = True
                self.debug_log("Behemoth Found")


    async def handle_boss_hp(self):
        """Change the boss' HP depending on what boss it is and their custom health set"""

        match_status = self.game_interface.match_status()
        if match_status == 2:
            self.boss_hp_handled = False

        if not self.boss_hp_handled and self.ready_to_handle():
            max_behemoth_hp = self.game_interface.dolphin_client.follow_pointers(self.addresslib.behemoth_hp_addr,
                                                                                 Pointers.Boss.max_hp_offsets)
            behemoth_hp = self.game_interface.dolphin_client.follow_pointers(self.addresslib.behemoth_hp_addr,
                                                                             Pointers.Boss.behemoth_hp_offsets)
            if self.is_behemoth:
                self.game_interface.dolphin_client.write_float(max_behemoth_hp, self.behemoth_hp)
                self.game_interface.dolphin_client.write_float(behemoth_hp, self.behemoth_hp)
                self.debug_log(f"Behemoth HP set to {self.behemoth_hp}")
                self.boss_hp_handled = True

            elif self.is_behemoth_king:
                self.game_interface.dolphin_client.write_float(max_behemoth_hp, self.behemoth_king_hp)
                self.game_interface.dolphin_client.write_float(behemoth_hp, self.behemoth_king_hp)
                self.debug_log(f"Behemoth King HP set to {self.behemoth_king_hp}")
                self.boss_hp_handled = True

    async def has_cup_goaled(self):
        """Checks if the player has beaten the required amount of cups"""

        cups_won_total = len(self.cups_won)

        if self.goal_condition == 3:
            if cups_won_total >= self.win_cups_amount and not self.goal_handled:
                await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                self.debug_log(f"Goal Achieved: Win {self.win_cups_amount} Cups!")
                self.goal_handled = True

    async def has_ex_goaled(self):
        """Checks if the player has beaten the required amount of exhibition locations"""
        won_count = len(self.exhibitions_won)

        if self.goal_condition == 4:
            if won_count >= self.num_ex_locations and not self.goal_handled:
                await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                self.debug_log(f"Goal Achieved: Win {self.num_ex_locations} Exhibition Matches!")
                self.goal_handled = True

    async def has_party_goaled(self):
        """Checks if the player has beaten the required amount of party mode locations"""
        won_count = len(self.party_won)

        if self.goal_condition == 5:
            if won_count >= 30 and not self.goal_handled:
                await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                self.debug_log(f"Goal Achieved: Win Party Mode!")
                self.goal_handled = True


    # === Location Handling ===


    async def check_location(self, location_name: str):
        """Checks if you've already got the location, if not, notifies AP about getting the location"""

        location_id = LOCATION_NAME_TO_ID.get(location_name)

        if location_id is None:
            self.debug_log(f"No AP location found: {location_name}")
            return

        if location_id in self.locations_checked:
            self.debug_log(f"Location: {location_name} in locations checked!")
            return

        await self.send_msgs([{"cmd": "LocationChecks", "locations": [location_id]}])
        self.locations_checked.add(location_id)
        self.debug_log(f"Checked location: name={location_name}, id={location_id}")

    def get_current_cup_location_name(self) -> Optional[str]:
        """Get the correct location name for the sport, cup and round"""

        court_code, court_name = self.game_interface.get_court()
        sports_mix_activated = self.game_interface.is_sports_mix()
        sport = self.game_interface.get_mode()


        if court_code == "s20":
            self.debug_log(f"Stage {court_code} is Behemoth Stage, separate function handles that.")
            return None

        if court_code == "s39":
            self.debug_log(f"Stage {court_code} is the menu, player has probably been sent to the void.")
            return None

        if sport is None:
            self.debug_log(f"Could not build cup location from court={court_name}, sport={sport}")
            return None

        cup = self.game_interface.get_tournament_cup()
        round_number = self.game_interface.get_tournament_round()

        if cup is None or round_number is None:
            self.debug_log(f"Could not find tournament cup/round for sport={sport}, court_code={court_code}")
            return None

        difficulty = self.game_interface.get_tournament_difficulty()

        if difficulty is None and not sports_mix_activated:
            self.debug_log(f"Could not find tournament difficulty for cup={cup}")
            return None


        if sports_mix_activated:
            return f"Sports Mix: Beat {cup} Cup {round_number}"
        else:
            return f"{sport}: Beat {difficulty} {cup} Cup {round_number}"

    def get_current_alt_path_location_name(self) -> Optional[str]:
        """Same as above, but for alt paths"""

        current_node = self.game_interface.get_player_current_node()
        current_cup = self.game_interface.get_tournament_cup()
        current_difficulty = self.game_interface.get_tournament_difficulty()
        current_sport = self.game_interface.get_tournament_sport()

        current_node_name = self.game_interface.get_name_from_node(current_cup, current_node)

        if self.alt_paths_unlock_type == 0:
            if current_sport != "Sports Mix":
                return f"{current_sport} {current_cup} Cup Alt Path {current_difficulty} {current_node_name}"
            else:
                return f"Sports Mix {current_cup} Cup Alt Path {current_node_name}"
        elif self.alt_paths_unlock_type == 1:
            return f"{current_sport} {current_cup} Cup Alt Path {current_node_name}"
        elif self.alt_paths_unlock_type == 2 or self.alt_paths_unlock_type == 4:
            return f"{current_cup} Cup Alt Path {current_difficulty} {current_node_name}"
        elif self.alt_paths_unlock_type == 3 or self.alt_paths_unlock_type == 5:
            return f"{current_cup} Cup Alt Path {current_node_name}"
        else:
            return None

    async def check_pending_tournament_location(self):
        if self.last_tournament_location_name is None:
            return

        location_name = self.last_tournament_location_name
        self.last_tournament_location_name = None
        self.debug_log(f"Sending pending tournament location: {location_name}")
        await self.check_location(location_name)

    async def check_pending_alt_path_location(self):
        if self.last_alt_path_location_name is None:
            return

        location_name = self.last_alt_path_location_name
        self.last_alt_path_location_name = None
        self.debug_log(f"Sending pending alt path location: {location_name}")
        await self.check_location(location_name)

    async def handle_exhibition_win(self):
        """Handles sending the checks to do with exhibition wins"""

        # Already marked as tournament
        if self.in_tournament_match:
            return

        # If Sports Mix is running, standard Exhibition checks shouldn't fire
        if self.game_interface.is_sports_mix():
            return

        _, court_name = self.game_interface.get_court()
        match_status = self.game_interface.match_status()

        if match_status != 1:
            return

        sport = self.game_interface.get_mode()
        difficulty, difficulty_name = self.game_interface.get_exhibition_difficulty()

        if court_name is None or court_name == "Main Menu" or sport is None or difficulty is None:
            return

        difficulties_dict = {0: "Easy", 1: "Normal", 2: "Hard", 3: "Expert"}

        if self.goal_condition != 4:
            for i in range(4):
                if i <= difficulty: # Find all difficulties the same and below
                    diff_name = difficulties_dict.get(i)
                    item = f"Exhibition {diff_name}"
                    # Check if the difficulty is enabled and we have the item for it
                    if diff_name in self.exhibition_difficulties and item in self.unlocked_ex_diffs:
                        if self.exhibition_type == 0:
                            location_name = f"{sport} Ex: Beat {court_name} ({diff_name})"
                        else:
                            location_name = f"Exhibition: Beat {court_name} ({diff_name})"
                        await self.check_location(location_name)
        else:
            item = f"Exhibition {difficulty_name}"
            if difficulty_name in self.exhibition_difficulties and item in self.unlocked_ex_diffs:
                if self.exhibition_type == 0:
                    location_name = f"{sport} Ex: Beat {court_name} ({difficulty_name})"
                else:
                    location_name = f"Exhibition: Beat {court_name} ({difficulty_name})"
                await self.check_location(location_name)

    async def check_current_cup(self):
        """Checks what cup we are in via the tournament map"""
        current_cup = self.game_interface.get_tournament_cup()

        if current_cup.casefold() != "not in tournament":
            self.in_tournament_match = True
        else:
            self.in_tournament_match = False



    async def handle_cup_round_win(self):
        """Handles sending the checks for winning a round of a cup"""

        if not self.in_tournament_match or self.in_alt_path:
            return

        location_name = self.get_current_cup_location_name()

        if location_name is None:
            return

        match_status = self.game_interface.match_status()

        if match_status != 1:
            return

        self.last_tournament_location_name = location_name
        await self.check_location(location_name)
        self.last_tournament_location_name = None

    async def handle_alt_path_win(self):

        match_status = self.game_interface.match_status()

        if not self.in_tournament_match:
            return

        location_name = self.get_current_alt_path_location_name()

        if location_name == None:
            return 
        
        # self.log_once("alt_path",f"Current Alt Path Location: {location_name}", False)

        if match_status != 1:
            return

        self.last_alt_path_location_name = location_name
        await self.check_location(location_name)
        self.last_alt_path_location_name = None

    async def handle_party_wins(self):
        """Handles sending party mode wins"""
        match_status = self.game_interface.match_status()
        _, court_name = self.game_interface.get_court()
        mode = self.game_interface.get_mode()
        
        if self.in_tournament_match or match_status != 1 or mode is None:
            return
        
        if mode in ["Feed Petey", "Bob-omb Dodge", "Smash Skate"]:
            tab = f" ({self.game_interface.get_tab()})"
        else:
            tab = ""
        
        location = f"{mode}: Beat {court_name}{tab}"
        await self.check_location(location)


    # --- Sanity Location Handling ---

    # --- Character Sanity ---
    async def send_character_sanity_checks(self):
        """Handles sending checks for Character Sanity"""
        match_status = self.game_interface.match_status()

        if self.character_sanity == 0 or match_status != 1:
            return

        char_1 = self.game_interface.get_p_character(1)
        char_2 = self.game_interface.get_p_character(2)
        char_3 = self.game_interface.get_p_character(3)

        # Read costumes ONCE here
        costume_1 = self.game_interface.dolphin_client.read_byte(get_address(PlayerAddresses.costume_1))
        costume_2 = self.game_interface.dolphin_client.read_byte(get_address(PlayerAddresses.costume_2))
        costume_3 = self.game_interface.dolphin_client.read_byte(get_address(PlayerAddresses.costume_3))

        char_list = [char_1, char_2, char_3]
        costume_list = [costume_1, costume_2, costume_3]

        if self.send_both_character_sanity and self.character_sanity == 2:
            await self.send_character_character_sanity(*char_list)
            await self.send_costume_character_sanity(*char_list, *costume_list)

        else:
            if self.character_sanity == 1:
                await self.send_character_character_sanity(*char_list)

            elif self.character_sanity == 2:
                for char, costume in zip(char_list, costume_list):
                    if char in costume_database and costume != 0:
                        await self.send_costume_character_sanity(*char_list, *costume_list)
                    else:
                        await self.send_character_character_sanity(*char_list)

    async def send_character_character_sanity(self, char_1, char_2, char_3):
        """Sends the location for the character if Character Sanity is enabled"""

        if self.game_interface.get_mode() in ["Feed Petey", "Harmony Hustle", "Bob-omb Dodge", "Smash Skate"]:
            characters_to_check = [char_1]
        elif self.game_interface.check_team_amount() == 2:
            characters_to_check = [char_1, char_2]
        elif self.game_interface.check_team_amount() == 3:
            characters_to_check = [char_1, char_2, char_3]
        else:
            return

        for character in characters_to_check:
            if character != "None" and (character in self.unlocked_characters or character in ["Mii (Male)", "Mii (Female)"]):
                await self.check_location(f"Win as {character}")

    async def send_costume_character_sanity(self, char_1, char_2, char_3, costume_1, costume_2, costume_3):
        """Sends the location for the costume if Character Sanity is enabled"""

        characters_2 = [char_1, char_2]
        costumes_2   = [costume_1, costume_2]
        characters_3 = [char_1, char_2, char_3]
        costumes_3   = [costume_1, costume_2, costume_3]

        players = self.game_interface.check_team_amount()

        if self.game_interface.get_mode() in ["Feed Petey", "Harmony Hustle", "Bob-omb Dodge", "Smash Skate"]:
            zipped = zip([char_1], [costume_1])

        elif players == 2:
            zipped = zip(characters_2, costumes_2)

        else:
            zipped = zip(characters_3, costumes_3)


        for character, costume_byte in zipped:

            if character in costume_database and costume_byte not in (0, 255) and character != "None":
                costume_db = costume_database[character]

                # Fetch the string name
                costume_name = costume_db.get(costume_byte, None)

                if costume_name is not None:
                    if (character in self.unlocked_characters or character in ["Mii (Male)", "Mii (Female)"]) and costume_name in self.unlocked_costumes:
                        await self.check_location(f"Win as {costume_name}")

    # --- Court Sanity ---
    async def send_court_sanity_checks(self):
        """Sends the location if the player has won and has the court unlocked"""

        match_status = self.game_interface.match_status()

        if not self.court_sanity or match_status != 1:
            return

        court_id, court_name = self.game_interface.get_court()

        if court_name is not None and court_name in self.unlocked_courts:
            if court_id not in not_match_prefix:
                await self.check_location(f"Win on {court_name}")

    # --- Special Sanity ---
    async def send_special_sanity_checks(self):
        """Sends the location when the player has used a special and if the character is unlocked"""
        special_active = self.game_interface.special_active()

        if not self.special_sanity or not special_active:
            return


        character_word = self.game_interface.dolphin_client.read_word(get_address(MatchAddresses.using_special))

        # Only check for Blue Team
        character_int = {0: 1, 2: 2, 4: 3}.get(character_word, None)

        if character_int is not None:
            character_name = self.game_interface.get_p_character(character_int)

            if character_name in self.unlocked_characters or character_name in ["Mii (Male)", "Mii (Female)"]:
                await self.check_location(f"Use {character_name}'s Special")


    # === Blocking Functions ===


    async def handle_locked_tournament_court_points(self):
        """Locks the points in a tournament match if you don't have the required cup or court"""

        if not self.in_tournament_match or not self.ready_to_handle():
            return


        court_code, court_name = self.game_interface.get_court()
        sports_mix_activated = self.game_interface.is_sports_mix()
        sport = self.game_interface.get_mode()


        if court_name is None or sport is None:
            self.debug_log(f"Could not check tournament stage unlock for court_name={court_name}")
            return

        cup = self.game_interface.get_tournament_cup() + " Cup"
        round_number = self.game_interface.get_tournament_round()

        if cup is None or round_number is None:
            self.debug_log(f"Could not check locked tournament points for sport={sport}, court_code={court_code}")
            return

        difficulty = self.game_interface.get_tournament_difficulty()
        required_court = f"{court_name}"
        if sports_mix_activated:
            required_cup = f"Sports Mix: {cup}"
        else:
            required_cup = f"{sport}: {cup} ({difficulty})"

        if required_court in self.unlocked_courts and required_cup in self.unlocked_cups:
            self.locking_period = False
            return

        if required_court not in self.unlocked_courts and required_cup not in self.unlocked_cups:
            self.rate_log("locked_tournament", f"Blocked points for {sport} {cup} Round {round_number}. Missing {required_court} & {required_cup}", 10, False)
        elif required_court not in self.unlocked_courts:
            self.rate_log("locked_tournament", f"Blocked points for {sport} {cup} Round {round_number}. Missing {required_court}", 10, False)
        elif required_cup not in self.unlocked_cups:
            self.rate_log("locked_tournament", f"Blocked points for {sport} {cup}. Missing {required_cup}", 10, False)

        try:
            if self.ready_to_handle():
                await self.clear_player_score()
                await self.lock_period_1()
                await self.lock_special_meter()
        finally:
            pass

    async def handle_locked_exhibition_points(self):
        """Locks the points in an exhibition match if you don't have the required difficulty"""

        if self.in_tournament_match or not self.ready_to_handle():
            return

        _, diff_name = self.game_interface.get_exhibition_difficulty()


        if f"Exhibition {diff_name}" in self.unlocked_ex_diffs:
            self.locking_period = False
            return

        self.rate_log("locked_ex", f"Blocked points for match. Missing: Exhibition {diff_name}", 10, False)

        try:
            if self.ready_to_handle():
                await self.clear_player_score()
                await self.lock_period_1()
                await self.lock_special_meter()
        finally:
            pass

    async def handle_lock_behemoth_hp(self):
        """Locks the Behemoth health and Special Meter charge if in a behemoth fight without Behemoth Stage"""

        if not self.in_tournament_match or self.game_interface.match_status() != 0 or not self.ready_to_handle():
            return

        required_stage = "Behemoth Stage"
        if self.is_behemoth:
            boss = "Behemoth"
        elif self.is_behemoth_king:
            boss = "Behemoth King"
        else:
            boss = None

        if required_stage in self.unlocked_courts:
            return

        if boss is None:
            self.debug_log("Could not find boss, set to None")
            return

        self.rate_log("locked_behemoth", f"Locked points for {boss}, you do not have {required_stage}", 10, False)

        try:
            if self.ready_to_handle():
                await self.lock_behemoth_hp()
                await self.lock_special_meter()
        finally:
            pass

    def send_to_void(self):
        """Sends the player to the void (stage=s39ba, module=0x6D656E75)"""
        self.game_interface.dolphin_client.write_pointer(self.addresslib.current_module_addr,
                                                         Pointers.Match.current_module_offsets,
                                                         "word", 0x6D656E75)

        self.game_interface.dolphin_client.write_string(self.addresslib.current_court_addr, "s39ba")

    async def clear_player_score(self):
        """Locks the player's score at 0"""

        self.game_interface.dolphin_client.write_word(self.game_interface.get_player_score_addr(), 0)

    async def lock_period_1(self):
        """Locks the period/set counter at period 1"""

        self.locking_period = True
        self.game_interface.dolphin_client.write_byte(self.addresslib.current_period_addr, 0)
        self.game_interface.dolphin_client.write_byte(get_address(MatchAddresses.max_periods), 4)
        # Make sure the game doesn't end after 1 period

    async def lock_special_meter(self):
        """Locks the player's special meter at 0"""

        self.game_interface.dolphin_client.write_pointer(self.addresslib.p_special_meter_addr,
                                                         Pointers.Player.special_meter_offsets,
                                                         "float", 0.0)

    async def lock_behemoth_hp(self):
        """Function to lock Behemoth Health, called in handle_lock_behemoth_hp"""

        behemoth_hp = self.game_interface.dolphin_client.follow_pointers(self.addresslib.behemoth_hp_addr,
                                                                         Pointers.Boss.behemoth_hp_offsets)
        if self.is_behemoth:
            self.game_interface.dolphin_client.write_float(behemoth_hp, self.behemoth_hp)

        if self.is_behemoth_king:
            self.game_interface.dolphin_client.write_float(behemoth_hp, self.behemoth_king_hp)


    # === Location Tracking ===


    async def track_cups_won(self):
        """Tracks what cups the player has won"""

        added = False

        for location in self.checked_locations:
            name = LOCATION_ID_TO_NAME[location]
            if "Round 3" in name and name not in self.cups_won:
                self.cups_won.add(name)
                added = True
            else:
                added = False # Stop client spam

        won_count = len(self.cups_won)
        if won_count <= self.win_cups_amount and added and self.goal_condition == 3:
            # Only show this message if the goal condition is Win Cups, we've added a cup,and we're logging the max cups
            # won so far (So it doesn't log 1 Cups Won, 2, 3 all the way up to 12 or smth, only logs 12 Cups Won!)
            logger.info(f"{won_count}/{self.win_cups_amount} Cup{'' if won_count == 1 else 's'} Won!")

    async def unlock_behemoth(self):
        """Unlocks the Behemoth fight based off of track_cups_won"""

        won_addresses = {
            "Basketball": WonStarCups.basketball,
            "Volleyball": WonStarCups.volleyball,
            "Dodgeball": WonStarCups.dodgeball,
            "Hockey": WonStarCups.hockey
        }

        # Store the values for each sport
        sport_values = {}

        for location in self.cups_won:
            sport = {"B": "Basketball", "V": "Volleyball", "D": "Dodgeball", "H": "Hockey"}.get(location[:1])

            if not sport:
                continue

            if sport not in sport_values:
                sport_values[sport] = 0


            if "Normal" in location:
                sport_values[sport] |= 1
            elif "Hard" in location:
                sport_values[sport] |= 2

        for sport, dict_addr in won_addresses.items():

            final_addr = get_address(dict_addr)

            # Write the correct combined value (0, 1, 2 or 3) if the sport is enabled
            if sport in self.enabled_sports:
                value = sport_values.get(sport, 0)
                self.game_interface.dolphin_client.write_byte(final_addr, value)

            # Write 3 to say that we've completed the cups so the player can access Behemoth
            else:
                self.game_interface.dolphin_client.write_byte(final_addr, 3)

    @property
    def num_ex_locations(self):
        return MSMUtils.find_num_exhibition_locs(
            self.enabled_sports or (),
            self.exhibition_type or 0,
            self.exhibition_difficulties or (),
        )

    async def track_exhibitions_won(self):
        """Tracks what exhibition matches the player has won"""

        added = False

        for location in self.checked_locations:
            name = LOCATION_ID_TO_NAME[location]
            if "Ex:" in name and name not in self.exhibitions_won:
                self.exhibitions_won.add(name)
                added = True
            else:
                added = False # Stop client spam

        won_count = len(self.exhibitions_won)
        if won_count <= self.num_ex_locations and added and self.goal_condition == 4:
            # Only show this message if the goal condition is Ex Tour, we've added a location, and we're logging the max
            # won so far (So it doesn't log 1 Match Won, 2, 3 all the way up to 12 or smth, only logs 12 Matches Won!)
            logger.info(f"{won_count}/{self.num_ex_locations} Match{'' if won_count == 1 else 'es'} Won!")

    async def track_party_won(self):
        """Tracks what exhibition matches the player has won"""

        added = False

        for location in self.checked_locations:
            name = LOCATION_ID_TO_NAME[location]
            if any(["Feed Petey:", "Harmony Hustle:", "Bob-omb Dodge:", "Smash Skate:"]) in name:
                if name not in self.party_won:
                    self.party_won.add(name)
                    added = True
            else:
                added = False # Stop client spam

        won_count = len(self.party_won)
        if won_count <= 30 and added and (self.goal_condition == 5):
            # Only show this message if the goal condition is Palooza, we've added a location, and we're logging the max
            # won so far (So it doesn't log 1 Match Won, 2, 3 all the way up to 12 or smth, only logs 12 Matches Won!)
            logger.info(f"{won_count}/30 Match{'' if won_count == 1 else 'es'} Won!")


    # === Deathlink Stuff ===


    def timer_is_0(self):
        """Checks if the timer is 0 because volleyball is stupid"""
        mode = self.game_interface.get_mode()
        timer = self.game_interface.dolphin_client.read_float(self.addresslib.timer_addr)

        if mode == "Volleyball":
            return False
        else:
            if timer == 0:
                return True
            else:
                return False

    def timer_reset(self):
        """Checks if the timer has been reset"""

        mode = self.game_interface.get_mode()
        timer = self.game_interface.dolphin_client.read_float(self.addresslib.timer_addr)

        mode_to_function = {
            "Basketball": self.game_interface.get_basketball_time,
            "Dodgeball": self.game_interface.get_dodgeball_time,
            "Hockey": self.game_interface.get_hockey_time,
            "Feed Petey": 9000,
            "Bob-omb Dodge": 7200,
            "Smash Skate": 5400,
        }

        if self.in_tournament_match:
            if self.mode_has_timer(mode):
                if timer == self.get_custom_time():
                    return True
                else:
                    return False
            else:
                return False
        else:
            default_time = mode_to_function.get(mode, None)
            if default_time is not None:
                if mode == default_time:
                    return True
                else:
                    return False
            else:
                return False

    # Sending Deathlink
    async def handle_send_deathlink(self):
        """Gets awaited during in match and sends a deathlink depending on what the deathlink_action is"""

        possible_messages_0 = ["lost the match!", "isn't good enough!", "needs to take a break...",
                               "couldn't sport their mix..."]

        possible_messages_1 = ["got DUNKED on!", "can't handle the heat!", ]

        match_status = self.game_interface.match_status()

        if self.deathlink_enabled:

            if self.locking_period:
                # Failsafe in case the period change doesn't get applied and the player loses,shouldn't count as a death
                return

            # Lose Match Action
            if self.deathlink_action == 0:

                if not self.received_death:
                    if (self.is_behemoth or self.is_behemoth_king) and not self.has_sent_death:
                        await self.check_behemoth_deathlink()

                    elif (match_status == 2 or match_status == 3) and not self.timer_reset():
                        if not self.has_sent_death and self.slot is not None:
                            message = random.choice(possible_messages_0)  # Pick a random message to send
                            await self.send_death(f"{self.player_names[self.slot]} {message}")
                            self.has_sent_death = True
                            self.debug_log("Sent deathlink due to losing/tying the match")


            # Every number of Points Action
            elif self.deathlink_action == 1:
                if (self.is_behemoth or self.is_behemoth_king) and not self.has_sent_death:
                    await self.check_behemoth_deathlink()

                # Dodgeball logic
                elif self.game_interface.get_mode() == "Dodgeball":
                    if self.has_dodge_opponent_scored():
                        if self.slot is not None:
                            message = random.choice(possible_messages_1)
                            await self.send_death(f"{self.player_names[self.slot]} {message}")
                            self.debug_log("Sent deathlink due to the opponent scoring in dodgeball")

                # All other main_sports logic
                else:
                    if self.has_score_reached_threshold():
                        if self.slot is not None:
                            message = random.choice(possible_messages_1)
                            await self.send_death(f"{self.player_names[self.slot]} {message}")
                            self.debug_log("Sent deathlink due to the opponent scoring a threshold")

    async def check_behemoth_deathlink(self):
        """Checks if the player has lost during the Behemoth boss fight"""
        match_status = self.game_interface.match_status()

        if match_status == 2 or match_status == 3:
            type = " King" if self.is_behemoth_king else "" # If Behemoth King, change message accordingly
            if self.slot is not None:
                await self.send_death(f"{self.player_names[self.slot]} has lost to the might of the Behemoth{type}...")

    def has_score_reached_threshold(self) -> bool:
        """Check when the opponent has got the required amount of points (self.deathlink_o_scores_points) in
        everything but dodgeball - Used for DL-C Opponent gains points. Returns True if yes, False if no"""

        addr = self.game_interface.get_opponent_score_addr(self.party_mode_opponent, True)
        current_opponent_score = self.game_interface.dolphin_client.read_word(addr)
        mode = self.game_interface.get_mode()


        if self.previous_opponent_score is None:
            self.previous_opponent_score = current_opponent_score
            return False

        # If the score drops, a new match started.
        # Reset our tracker to the new lower score and return False.
        if current_opponent_score < self.previous_opponent_score:
            self.previous_opponent_score = current_opponent_score
            return False

        # Check the difference
        score_increase = current_opponent_score - self.previous_opponent_score

        if mode in ["Basketball", "Volleyball", "Dodgeball", "Hockey"]:
            needed = self.deathlink_o_scores_points
        else:
            needed = self.deathlink_o_scores_points * 20

        # If the threshold is met, update the tracker and return True
        if score_increase >= needed:
            # Reset the "previous" score to the current one so it can start counting up again
            self.previous_opponent_score = current_opponent_score
            return True

        # If the threshold isn't met yet, do nothing and return False
        return False

    def has_dodge_opponent_scored(self) -> bool:
        """Check when the opponent has got a point in Dodgeball - Used for DL-C Opponent gains points"""

        current_opponent_score = sum(
            self.game_interface.dolphin_client.read_word(get_address(addr))
            for addr in opponent_score_addresses
        )

        if self.previous_opponent_score is None:
            self.previous_opponent_score = current_opponent_score
            return False

        # If the score drops to 0, a new match started.
        # Reset the tracker to the new lower score and return False.
        if current_opponent_score < self.previous_opponent_score:
            self.previous_opponent_score = current_opponent_score
            return False

        # Check for a point increase
        if current_opponent_score > self.previous_opponent_score:

            # Update the tracker to this new score so it doesn't trigger again until the next point.
            self.previous_opponent_score = current_opponent_score
            return True

        # If the score is exactly the same, do nothing
        return False

    # Receiving Deathlink
    def on_deathlink(self, data: dict[str, Any]):
        super().on_deathlink(data)
        self.debug_log(f"Deathlink Received - Consequence={self.deathlink_consequence}")
        self.handle_received_deathlink()
        self.received_death = True  # Required so we don't send a deathlink when we get sent one

    def handle_received_deathlink(self):
        """Gets called when on_deathlink goes off and acts depending on deathlink_consequence
        NOTE: Dodgeball deathlinks get handled differently to everything else since it doesn't have a normal scoring system"""
        mode = self.game_interface.get_mode()

        if self.deathlink_enabled:
            if self.ready_to_handle():

                # Lose Match Consequence
                if self.deathlink_consequence == 0:
                    if self.is_behemoth or self.is_behemoth_king:
                        self.recover_boss_hp()
                    else:
                        # Force player to lose
                        # Harmony Hustle uses 1 score since it's teamwork
                        if mode != "Harmony Hustle":
                            # Volleyball is stupid
                            if mode == "Volleyball":
                                for score in opponent_score_addresses:
                                    self.game_interface.dolphin_client.write_word(get_address(score), 500)

                            else:
                                self.game_interface.dolphin_client.write_word(self.game_interface.get_opponent_score_addr
                                                                                (self.party_mode_opponent), 500)


                            # 4 = 5th Period
                            self.game_interface.dolphin_client.write_byte(self.addresslib.current_period_addr, 4)

                        # In all modes, updating the player's score should cause them to lose
                        self.game_interface.dolphin_client.write_word(self.game_interface.get_player_score_addr(), 0)

                        time.sleep(1)

                        # STUPID ASS VOLLEYBALL NEEDS TO KNOW WHEN THE TIMER IS **ONE** TO NOT SEND A DEATHLINK
                        self.game_interface.dolphin_client.write_float(self.addresslib.timer_addr,
                                                                       1 if mode == "Volleyball" else 0)


                # Opponent gains points
                elif self.deathlink_consequence == 1:
                    if self.is_behemoth or self.is_behemoth_king:
                        self.recover_boss_hp()
                    else:
                        if self.game_interface.get_mode() not in ["Dodgeball", "Bob-omb Dodge"]:
                            addr = self.game_interface.get_opponent_score_addr(self.party_mode_opponent)
                            points = self.game_interface.dolphin_client.read_word(addr)
                            new_points = points + self.deathlink_o_get_points
                            self.game_interface.dolphin_client.write_word(addr, new_points)
                            total_points = sum(self.game_interface.dolphin_client.read_word(get_address(addr)) for addr in opponent_score_addresses)
                            logger.info(f"Opponent now has {total_points} points!")
                        else:
                            # Lists start at 0, we need to take away one from the value
                            random_char = randint(0, self.game_interface.check_team_amount() - 1)

                            pointers = [Pointers.Player.B1.dodge_damage,
                                        Pointers.Player.B2.dodge_damage,
                                        Pointers.Player.B3.dodge_damage,]

                            addr = get_address(PlayerAddresses.various_shp_pointers)
                            curr_damage = self.game_interface.dolphin_client.read_pointer(addr, pointers[random_char],
                                                                                         "word")
                            new_damage = curr_damage + self.deathlink_dodge_health_lost
                            self.game_interface.dolphin_client.write_pointer(addr, pointers[random_char],
                                                                             "word", new_damage)
                            health = self.d_max_health - new_damage
                            # Find current the character selected by randint
                            chars = [PlayerAddresses.character_1,
                                     PlayerAddresses.character_2,
                                     PlayerAddresses.character_3,]

                            value = self.game_interface.dolphin_client.read_byte(chars[random_char])
                            character = id_to_char[value]

                            logger.info(f"Watch out! It may not look like it, but {character} is on {health} HP!")

    def recover_boss_hp(self):
        """Calculates the amount of HP recovered when sent a deathlink"""
        behemoth_text: JSONMessagePart = {"type": "color",
                                          "text": f"Behemoth{" King" if self.is_behemoth_king else ""}",
                                          "color": "red"}

        if self.is_behemoth:
            health_recovered = (self.deathlink_boss_recovered / 100) * self.behemoth_hp
            current_health = self.game_interface.dolphin_client.read_float(self.addresslib.behemoth_hp_addr)
            new_health = current_health + health_recovered
            self.game_interface.dolphin_client.write_float(self.addresslib.behemoth_hp_addr, new_health)
            logger.info(f"{behemoth_text} has powered up back to {new_health} HP!")

        elif self.is_behemoth_king:
            health_recovered = (self.deathlink_boss_recovered / 100) * self.behemoth_king_hp
            current_health = self.game_interface.dolphin_client.read_float(self.addresslib.behemoth_hp_addr)
            new_health = current_health + health_recovered
            self.game_interface.dolphin_client.write_float(self.addresslib.behemoth_hp_addr, new_health)
            logger.info(f"{behemoth_text} has powered up back to {new_health} HP!")

    async def reset_deathlink_status(self):
        """Resets the received and sent deathlink bools"""
        # Received Deathlink
        match_status = self.game_interface.match_status()
        court_id, _ = self.game_interface.get_court()
        mode = self.game_interface.get_mode()
        timer = self.game_interface.dolphin_client.read_float(self.addresslib.timer_addr)
        # If we're not in the state where we've died to deathlink, or we're in some kind of menu/cutscene,
        # set received_death to false
        if (match_status == 0 and (self.timer_reset() and self.mode_has_timer(mode))) or court_id in not_match_prefix:
            self.received_death = False

        if mode == "Volleyball" and match_status == 0 and timer != 1:
            self.received_death = False

        # Sent Deathlink
        # If we're not in the state where we've died to deathlink, or in some kind of menu/cutscene,
        # set received_death to false
        if match_status == 0 and not self.timer_is_0():
            self.has_sent_death = False


    # === Meme Options ===

    async def randomize_music(self):

        shuffle_mode = self.music_shuffle
        if self.music_randomization_applied:
            return

        if shuffle_mode == 0:
            return

        await self.load_custom_data()

        classes = [
            MusicFiles.MenuSongs,
            MusicFiles.StageSongs,
            MusicFiles.PartySongs,
            MusicFiles.TournamentSongs,
            MusicFiles.MiscSongs,
            MusicFiles.HarmonyHustlePreviews,
        ]

        music_data = self.custom_data.get("music", {})
        
        if music_data:
            for song, new_song in music_data.items():
                self.game_interface.replace_music_file(song, new_song)
            self.music_randomization_applied = True
            return

        if shuffle_mode == 1:
            for cls in classes:
                class_songs = self.game_interface.get_songs_from_class(cls)
                class_pool = list(class_songs)
                for song in class_songs:
                    new_song = random.choice(class_pool)
                    self.custom_data["music"][song] = new_song
                    self.game_interface.replace_music_file(song, new_song)
                    # self.log_once("music", f"Replaced {song} with {new_song}", False)
                    class_pool.remove(new_song)

            await self.save_custom_data()
            self.music_randomization_applied = True

        elif shuffle_mode == 2:

            songs_to_replace = []

            for cls in classes:
                for song in self.game_interface.get_songs_from_class(cls):
                    if song not in songs_to_replace:
                        songs_to_replace.append(song)
            
            song_pool = list(songs_to_replace)

            for song in songs_to_replace:
                new_song = random.choice(song_pool)
                self.custom_data["music"][song] = new_song
                self.game_interface.replace_music_file(song, new_song)
                # self.log_once("music", f"Replaced {song} with {new_song}", False)
                song_pool.remove(new_song)
            await self.save_custom_data()
            self.music_randomization_applied = True


    async def replace_all_opponent_characters(self):

        if self.all_one_opponent != 0:
            for i in range(7):
                character_attr = getattr(TournamentAddresses, f"cpu_{i+1}_character")
                teammate_1_attr = getattr(TournamentAddresses, f"cpu_{i+1}_teammate_1")
                teammate_2_attr = getattr(TournamentAddresses, f"cpu_{i+1}_teammate_2")
                
                cpu_main_char = get_address(character_attr)
                cpu_teammate_1 = get_address(teammate_1_attr)
                cpu_teammate_2 = get_address(teammate_2_attr)

                self.game_interface.dolphin_client.write_byte(cpu_main_char, self.all_one_opponent - 1)
                self.game_interface.dolphin_client.write_byte(cpu_teammate_1, self.all_one_opponent - 1)
                self.game_interface.dolphin_client.write_byte(cpu_teammate_2, self.all_one_opponent - 1)

            red_team_to_replace = 2

            hockey_no_goalie = ["s03", "s04"]

            if self.game_interface.check_team_amount() == 3:
                red_team_to_replace += 1
            if self.game_interface.get_mode() in ["Dodgeball", "Hockey"] and self.replace_extra and self.game_interface.get_court()[0] not in hockey_no_goalie:
                red_team_to_replace += 1
            
            for i in range(red_team_to_replace):
                character_attr = getattr(MatchAddresses, f"red_character_{i+1}")
                character_addr = get_address(character_attr)
                self.game_interface.dolphin_client.write_byte(character_addr, self.all_one_opponent - 1)

            if self.game_interface.get_mode() in ["Feed Petey", "Harmony Hustle", "Bob-omb Dodge", "Smash Skate"] and not self.in_alt_path:
                self.game_interface.dolphin_client.write_byte(get_address(PlayerAddresses.character_2), self.all_one_opponent - 1)

    async def randomize_tints(self):
        # self.log_once("tints", f"{self.random_tint}", False)
        if not self.random_tint:
            return

        stages = ["s01", "s02", "s03", "s04", "s05", "s06", "s07", "s09", "s10",
                  "s11", "s12", "s15", "s16", "s17", "s20", "s21", "s31", "s32", 
                  "s33", "s34", "s39", "s40", "s41", "s42", "s55", "s56", "s57",
                  "s70", "s71", "s72", "s85", "s86", "s87"
                  ]

        await self.load_custom_data()

        tint_data = self.custom_data.get("tints", {})

        if not tint_data:
            for stage in stages:
                
                red_value = random.randint(0x40, 0xFF)
                green_value = random.randint(0x40, 0xFF)
                blue_value = random.randint(0x40, 0xFF)
                self.custom_data["tints"][stage] = [red_value, green_value, blue_value]
            await self.save_custom_data()
            tint_data = self.custom_data["tints"]

        current_stage = self.game_interface.get_court()[0]

        if current_stage not in stages:
            return

        stage_tint = tint_data.get(current_stage)

        red_value = int(stage_tint[0])
        green_value = int(stage_tint[1])
        blue_value = int(stage_tint[2])
        rgba_value = red_value * 0x1000000 + green_value * 0x10000 + blue_value * 0x100 + 0xFF

        current_tint = self.game_interface.dolphin_client.read_word(get_address(MatchAddresses.stage_tint))

        if not self.previous_stage:
            self.previous_stage = current_stage

        if self.previous_stage != current_stage:
            self.previous_stage = current_stage
            current_tint = 0xFFFFFFFF

        if self.game_interface.get_mode() == "Volleyball" and not self.tint_volleyball:
            return
        
        if current_tint == 0xFFFFFFFF:
            self.game_interface.dolphin_client.write_word(get_address(MatchAddresses.stage_tint), rgba_value)
            # self.log_once("tints", f"Tint for stage {current_stage} applied: {hex(rgba_value)}", False)

        
    # === QOL Stuff ===

    async def restrict_sports_mix_sports (self):

        # Placeholder
        restrict_sm = self.restrict_sports_mix

        if not restrict_sm or not self.enabled_sports or self.enabled_sports == ["Sports Mix"] or "Sports Mix" not in self.enabled_sports:
            return

        if self.game_interface.get_tournament_sport() != "Sports Mix":
            return

        available_sports = list(self.enabled_sports)
        available_sports.remove("Sports Mix")

        current_cup = self.game_interface.get_tournament_cup()

        sports_to_value = {"Basketball": 0, "Volleyball": 1, "Dodgeball": 2, "Hockey": 3}

        # Make sure that the tournament isnt just all one sport if possible
        banned_sport = None
        
        for i in range(3):

            new_sport = random.choice([sport for sport in available_sports if sport != banned_sport])

            for j in range(2**(2-i)):

                round = i + 1
                match = j + 1

                mode_address = get_address(getattr(TournamentAddresses, f"round_{round}_match_{match}_mode"))
                stage_address = get_address(getattr(TournamentAddresses, f"round_{round}_match_{match}_stage"))
                mode = self.game_interface.dolphin_client.read_byte(mode_address)

                # Check the 16th's place to see if already rando'd or not (also do you even call it the 16th's place idk)
                
                
                if not ((mode >> 4) == 1 or (mode >> 4) == 9):
                    new_stage = int(tournament_round_stages[new_sport][current_cup][round - 1][-2:])

                    self.game_interface.dolphin_client.write_byte(mode_address, sports_to_value[new_sport] + 0x10)
                    self.game_interface.dolphin_client.write_byte(stage_address, new_stage)

            # Just in case someone enables 1 sport and Sports Mix only for some reason (but why tho)
            if len(available_sports) > 1:
                banned_sport = new_sport

        
        if self.previous_node == self.game_interface.get_player_current_node():
            self.game_interface.dolphin_client.write_byte(get_address(TournamentAddresses.alt_path_mode), sports_to_value[self.current_sm_alt_sport] + 0x10)
            return
        elif self.game_interface.get_player_current_node() >= 0x17 and not self.game_interface.get_player_current_node() == 0xFF:
            if not self.game_interface.is_in_match():
                new_alt_sport = random.choice([sport for sport in available_sports if sport != self.current_sm_alt_sport])
                self.current_sm_alt_sport = new_alt_sport
                self.game_interface.dolphin_client.write_byte(get_address(TournamentAddresses.alt_path_mode), sports_to_value[new_alt_sport] + 0x10)
                self.previous_node = self.game_interface.get_player_current_node()


    async def spawn_control (self):

        is_tournament = True if self.game_interface.get_tournament_cup() != "Not in Tournament" else False
        is_loading = True if self.game_interface.get_tournament_round() == "Not in Tournament" else False
        game_loaded_positions = False if self.game_interface.get_player_current_node() == 0xFF else True

        # self.log_once("sc", f"Spawn Control: is_tournament = {is_tournament}, is_loading = {is_loading}, game_loaded_positions = {game_loaded_positions}, spawn_side_choice = {self.spawn_side_choice}", False)
        if is_tournament and is_loading and self.spawn_side_choice == 0 and not game_loaded_positions:

            player_extension = self.game_interface.dolphin_client.read_byte(get_address(PlayerInputs.P1_Extension))
            dpad_inputs = self.game_interface.dolphin_client.read_byte(get_address(PlayerInputs.P1_Dpad_Inputs))

            holding_left = False
            holding_right = False

            if player_extension == 0:
               
                holding_left = (dpad_inputs & 0x08) != 0
                holding_right = (dpad_inputs & 0x04) != 0

            elif player_extension == 1:
            
                holding_left = (dpad_inputs & 0x01) != 0
                holding_right = (dpad_inputs & 0x02) != 0

            if holding_left:
                self.spawn_side_choice = 1
            elif holding_right:
                self.spawn_side_choice = 2

        elif is_tournament and not is_loading and self.spawn_side_choice != 0 and game_loaded_positions:

            
            if self.spawn_side_choice == 1:
                player_spawn_pos = random.choice([1,2,3,4])
            elif self.spawn_side_choice == 2:
                player_spawn_pos = random.choice([5,6,7,8])
            else:
                self.spawn_side_choice = 0
                return

            self.game_interface.dolphin_client.write_byte(get_address(TournamentAddresses.player_current_node), player_spawn_pos)

            for i in range (7):
                cpu_spawn_pos = (player_spawn_pos + i + 1) % 8
                if cpu_spawn_pos == 0:
                    cpu_spawn_pos = 8

                self.game_interface.dolphin_client.write_byte(get_address(getattr(TournamentAddresses, f"cpu_{i+1}_current_node")), cpu_spawn_pos)

            self.spawn_side_choice = 0
            

                
    

    
            





        
        

    # === Misc stuff idk where to put ===


    async def dolphin_sync_task(self):
        """The main loop managing the connection to Dolphin and game-state logic routing"""

        while not self.exit_event.is_set():
            try:
                # Handle initial connection hook
                if not self.game_interface.dolphin_client.is_hooked():
                    if self.game_session_active:
                        self.reset_game_session_state(game_active=True)
                    await self.game_interface.dolphin_client.attempt_to_hook()


                if self.game_interface.dolphin_client.is_hooked():
                    if not self.game_interface.dolphin_client.check_region():
                        self.game_interface.dolphin_client.check_region()
                        await asyncio.sleep(1)
                        continue


                if not self.server or not self.server.socket or self.server.socket.closed:
                    message = "Waiting for player to connect to Archipelago server..."
                    self.start_process = True
                    if self.last_error_message != message:
                        logger.info(message)
                        self.last_error_message = message
                    await asyncio.sleep(1)
                    continue

                if not self.slot:
                    await asyncio.sleep(1)
                    continue

                if self.start_process:
                    unlock_tabs(self.hard_tournament_difficulty)
                    self.start_process = False

                self.last_error_message = None

                # Route Game State Execution
                self.update_connection_status()

                if self.connection_state == ConnectionState.IN_MATCH:
                    await self.handle_in_match()
                elif self.connection_state == ConnectionState.IN_BOSS:
                    await self.handle_in_boss()
                elif self.connection_state == ConnectionState.IN_TOURNAMENT_MAP:
                    await self.handle_in_tournament_map()
                elif self.connection_state == ConnectionState.IN_MENU:
                    await self.handle_in_main_menu()
                elif self.connection_state in (ConnectionState.FEED_PETEY, ConnectionState.HARMONY_HUSTLE,
                                               ConnectionState.BOB_OMB_DODGE, ConnectionState.SMASH_SKATE):
                    await self.handle_in_party_modes()
                else:
                    await asyncio.sleep(1)
                    continue

                await asyncio.sleep(0.1)

            except Exception as e:
                if "Dolphin" in str(e):
                    logger.error(f"Dolphin Connection Error: {e}")
                    self.update_connection_status()
                else:
                    logger.error(f"Sync Task Error:\n{traceback.format_exc()}")
                await asyncio.sleep(3)

    async def stop_stupid_unlock_notifs(self):
        """Stop SOME of the unlock messages from appearing constantly"""
        games_played_address_list = [GamesPlayed.basketball, GamesPlayed.dodgeball,
                                     GamesPlayed.volleyball, GamesPlayed.hockey]

        for address in games_played_address_list:
            new_addr = get_address(address)
            value = self.game_interface.dolphin_client.read_word(new_addr)
            if value != 0:
                self.game_interface.dolphin_client.write_word(new_addr, 0)

    async def handle_gecko_codes(self):
        """Handle the gecko code patches for each region"""

        current_module = self.game_interface.dolphin_client.read_pointer(self.addresslib.current_module_addr,
                                                                         Pointers.Match.current_module_offsets, "word")

        if current_module == 0x6D656E75 and not self.handled_gecko_codes:
            # print(f"Game Version: {dc.GAME_VERSION}")
            # print(f"Current Module Value (Hex): {hex(value)}")

            if dc.GAME_VERSION == "PAL":
                for address, code in GeckoCodes.gecko_codes_pal.items():
                    self.game_interface.dolphin_client.write_bytes(address, code)

            elif dc.GAME_VERSION == "NTSC-U":
                for address, code in GeckoCodes.gecko_codes_ntscu.items():
                    self.game_interface.dolphin_client.write_bytes(address, code)

            self.debug_log("Gecko Codes Handled")
            self.handled_gecko_codes = True

    async def check_write(self, addr: int, type: str, correct_value: Any) -> bool:
        """Checks if the address has the correct value to it"""
        read = None
        match type.lower().strip():
            case "byte":
                read = self.game_interface.dolphin_client.read_byte
            case "word":
                read = self.game_interface.dolphin_client.read_word
            case "string":
                read = self.game_interface.dolphin_client.read_string
            case "float":
                read = self.game_interface.dolphin_client.read_float
            case _:
                read = None

        if read is not None:
            if type.lower().strip() == "string":
                read_value = read(addr)
            else:
                read_value = read(addr)

            if read_value == correct_value:
                return True
            else:
                logger.error(f"WARNING: It doesn't seem like things are working!\n"
                            f"Please do the following:\n"
                            f"Config -> Interface -> Enable Debugging UI\n"
                            f"In the top bar: JIT -> Clear Cache\n"
                            f"addr={hex(addr)}, type={type}, read_val={read_value}, corr_val={correct_value}")
                return False
        else:

            self.rate_log(
                "check_write", f"Uh oh, I'm stupid! This read type doesn't exist! Please ping @electrostarz\n"
                f"type={type}", 10, False
            )
            return False

    @staticmethod
    def mode_has_timer(mode: str):
        if mode in ["Volleyball", "Harmony Hustle"]:
            return False
        else:
            return True


    # === Where to handle what ===


    async def handle_in_match(self):
        """What functions should be handled during a match"""
        # Music Randomizer
        await self.randomize_music()
        await self.randomize_tints()
        await self.replace_all_opponent_characters()

        # Sports Mix Restriction
        await self.restrict_sports_mix_sports()

        # Opponents Setter
        await self.replace_all_opponent_characters()

        # Custom Tournament Settings
        await self.check_current_cup()
        await self.handle_alt_path_unlocks()
        if self.in_tournament_match and not self.in_alt_path:
            await self.handle_custom_tournament_settings()
            

        # Cup Goal
        await self.track_cups_won()
        if self.goal_condition == 3:
            await self.has_cup_goaled()

        # Exhibition Goal
        if self.goal_condition == 4:
            await self.track_exhibitions_won()
            await self.has_ex_goaled()

        # Deathlink
        await self.handle_send_deathlink()
        await self.reset_deathlink_status()

        # Lock points if you don't have the stage/cup/difficulty and not in an alt path
        if not self.in_alt_path:
            await self.handle_locked_tournament_court_points()
            await self.handle_locked_exhibition_points()

        # Locations
        await self.handle_exhibition_win()
        await self.handle_cup_round_win()
        await self.handle_alt_path_win()
        await self.send_character_sanity_checks()

        if not self.in_alt_path:
            await self.send_court_sanity_checks()

        await self.send_special_sanity_checks()

        await self.unlock_behemoth()

        # Items
        await self.handle_one_time_items()
        await self.handle_traps()
        await self.handle_question_mark_panel_items()
        await self.handle_unlocked_abilities()

        self.toggle_log("rth", "Ready to handle!", "Not ready to handle", self.ready_to_handle(), True)

        self.handled_gecko_codes = False

        await asyncio.sleep(0.1)


    async def handle_in_boss(self):
        """What functions should be handled in the boss"""
        # Music Randomizer
        await self.randomize_music()
        await self.randomize_tints()
        await self.replace_all_opponent_characters()
        

        # Boss stuff
        await self.handle_boss_hp()
        await self.check_boss_type()
        await self.handle_lock_behemoth_hp()
        await self.has_boss_goaled()

        await self.send_special_sanity_checks()

        # Items
        await self.handle_one_time_items()
        await self.handle_traps()
        await self.handle_question_mark_panel_items()
        await self.handle_unlocked_abilities()

        self.handled_gecko_codes = False

        await asyncio.sleep(0.1)


    async def handle_in_tournament_map(self):
        """What functions should be handled in a tournament map"""

        # Music Randomizer
        await self.randomize_music()
        await self.randomize_tints()
        await self.replace_all_opponent_characters()
        await self.spawn_control()
        

        # Sports Mix Restriction
        await self.restrict_sports_mix_sports()

        # Opponents Setter
        await self.replace_all_opponent_characters()

        await self.check_current_cup()
        await self.handle_alt_path_unlocks()
        await self.check_pending_tournament_location()
        await self.unlock_behemoth()

        self.handled_gecko_codes = False
        self.handled_custom_timer = False
        
        await asyncio.sleep(0.1)


    async def handle_in_party_modes(self):
        # Music Randomizer
        await self.randomize_music()
        await self.randomize_tints()
        await self.replace_all_opponent_characters()
        

        # Opponents Setter
        await self.replace_all_opponent_characters()

        # Party Goal
        if self.goal_condition == 5:
            await self.track_party_won()
            await self.has_party_goaled()

        # Deathlink
        await self.handle_send_deathlink()
        await self.handle_alt_path_unlocks()

        # Locations
        await self.handle_alt_path_win()
        await self.send_character_sanity_checks()

        if not self.in_alt_path:
            await self.handle_party_wins()
            await self.send_court_sanity_checks()

        # Fillers and Traps are not handled here because most don't work in the modes.

        self.handled_gecko_codes = False
        self.handled_custom_timer = False


    async def handle_in_main_menu(self):
        """What functions should be handled in the main menu"""
        # Music Randomizer
        await self.randomize_music()
        await self.randomize_tints()
        await self.replace_all_opponent_characters()
        await self.spawn_control()

        # Sports Mix Restriction
        await self.restrict_sports_mix_sports()

        # Cup Goal
        await self.track_cups_won()
        if self.goal_condition == 3:
            await self.has_cup_goaled()

        # Exhibition Goal
        if self.goal_condition == 4:
            await self.track_exhibitions_won()
            await self.has_ex_goaled()

        # Party Goal
        if self.goal_condition == 5:
            await self.track_party_won()
            await self.has_party_goaled()


        await self.handle_received_items()
        await self.check_pending_tournament_location()
        await self.stop_stupid_unlock_notifs()
        await self.unlock_behemoth()

        await self.handle_gecko_codes()

        self.has_sent_death = False

        self.forced_item_id = None
        self.handled_custom_timer = False

        self.in_tournament_match = False
        self.boss_hp_handled = False
        self.is_behemoth = False
        self.is_behemoth_king = False
        self.game_interface.current_tournament = None

        await asyncio.sleep(0.1)
