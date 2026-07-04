import asyncio
import logging
import random
import traceback
from collections import deque
from random import randint, uniform
from typing import Dict, Set, Optional, Any

import Utils
from CommonClient import ClientCommandProcessor, CommonContext
from MultiServer import mark_raw
from NetUtils import ClientStatus
from .MSMInterface import MSMInterface, ConnectionState
from ..items import item_table
from ..locations import LOCATION_NAME_TO_ID
from .MSMFunctions import *
from . import dolphin_connection as dc
from .memory_addresses_pal import *
from .common_address_library import AddressLib

id_to_name = {data.id: name for name, data in item_table.items()}
CLIENT_VERSION = "1.0.7"
COMPATIBLE_VERSIONS = ["1.0.0", "1.0.1", "1.0.2", "1.0.3", "1.0.4", "1.0.5", "1.0.6"]


status_messages = {
    ConnectionState.IN_MATCH: "In Match",
    ConnectionState.IN_BOSS: "In Boss",
    ConnectionState.IN_MENU: "In Main Menu",
    ConnectionState.IN_TOURNAMENT_MAP: "In Tournament Map",
    ConnectionState.DISCONNECTED: "Unable to connect to the Dolphin instance, attempting to reconnect...",
    ConnectionState.CONNECTED: "Connected to Dolphin!",
}

character_names = [
    "mario", "luigi", "peach", "daisy", "yoshi", "wario", "waluigi",
    "donkey_kong", "diddy_kong", "toad", "bowser", "bowser_jr",
    "moogle", "white_mage", "black_mage", "ninja", "cactuar", "slime"
]

stage_names = {
    "s01": "Mario Stadium",
    "s02": "Koopa Troopa Beach",
    "s03": "Peach's Castle",
    "s04": "Toad Park",
    "s05": "DK Dock",
    "s06": "Luigi's Mansion",
    "s07": "Daisy Garden",
    "s09": "Wario Factory",
    "s10": "Bowser Jr. Blvd.",
    "s11": "Bowser's Castle",
    "s12": "Waluigi Pinball",
    "s16": "Star Ship",
    "s15": "Ghoulish Galleon",
    "s17": "Western Junction",
    "s39": "Menu",
}

tournament_round_stages = {
    "Basketball": {
        "Mushroom Cup": ["s01", "s02", "s05"],
        "Flower Cup": ["s06", "s17", "s07"],
        "Star Cup": ["s10", "s11", "s16"],
    },
    "Dodgeball": {
        "Mushroom Cup": ["s01", "s02", "s03"],
        "Flower Cup": ["s05", "s04", "s07"],
        "Star Cup": ["s09", "s11", "s16"],
    },
    "Volleyball": {
        "Mushroom Cup": ["s01", "s02", "s03"],
        "Flower Cup": ["s05", "s06", "s17"],
        "Star Cup": ["s10", "s11", "s16"],
    },
    "Hockey": {
        "Mushroom Cup": ["s01", "s04", "s03"],
        "Flower Cup": ["s17", "s09", "s07"],
        "Star Cup": ["s10", "s12", "s16"],
    },
}

tournament_map_cups = {
    "s31": "Mushroom Cup",
    "s32": "Flower Cup",
    "s33": "Star Cup",
}

char_to_id = {
    255: "None",
    0: "Mario", 1: "Luigi", 2: "Peach", 3: "Daisy", 4: "Yoshi",
    5: "Wario", 6: "Waluigi", 7: "Donkey Kong", 8: "Diddy Kong", 9: "Toad",
    10: "Bowser", 11: "Bowser Jr", 12: "Moogle", 13: "Cactuar",
    14: "Ninja", 15: "White Mage", 16: "Slime", 17: "Black Mage",
    19: "Mii (Male)", 20: "Mii (Female)",
}

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

logger = logging.getLogger("Client")
# AP server storage is room-wide, so filler/trap save keys need seed + slot in the name.
CONSUMABLE_STORAGE_CATEGORY = "msm_consumables"
LOCATION_STORAGE_CATEGORY = "msm_locations"
# Build the reverse lookup once so persisted AP location IDs can be shown as local names.
LOCATION_ID_TO_NAME = {location_id: name for name, location_id in LOCATION_NAME_TO_ID.items()}


class MSMCommandProcessor(ClientCommandProcessor):
    ctx: "MSMContext"

    def __init__(self, ctx: "MSMContext"):
        super().__init__(ctx)

    # @mark_raw
    # def _cmd_check(self, location_name: str):
    #     """Check a location - Used for dev purposes, or if you're lazy ig"""
    #     asyncio.create_task(self.ctx.check_location(location_name))

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
            log_message = f"[Memory Read - PAL] {addr_type} at {hex(final_address)}. Result: {result}"
        elif dc.GAME_VERSION == "NTSC-U" and is_exception(address):
            log_message = f"[Memory Read - NTSC-U] {addr_type} at {hex(final_address)} (In Exceptions). Result: {result}"
        elif dc.GAME_VERSION == "NTSC-U":
            log_message = f"[Memory Read - NTSC-U] {addr_type} at {hex(final_address)} (Original Address: {address}). Result: {result}"
        else:
            log_message = None

        logger.info(log_message)
        return log_message

    def _cmd_status(self):
        """Display the current dolphin connection status."""
        logger.info(f"Connection Status: {status_messages[self.ctx.connection_state]}")

    def _cmd_reapply_unlocks(self):
        """Reapply unlocks if you don't have them!"""
        asyncio.create_task(self.ctx.handle_received_items())
        logger.info("Reapplied unlocks!")

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
        :param type: Any from Sports, Stages, Cups, Characters/Chars/Char, Costumes/Costs/Cost, ex Abilities, Panel, Crystals"""

        type_to_cmd = {
            "sports": self.unlocked_sports,
            "stages": self.unlocked_stages,
            "cups": self.unlocked_cups,
            "characters": self.unlocked_characters,
            "ex": self.unlocked_ex,
            "exhibition": self.unlocked_ex,
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

    def unlocked_sports(self):
        """Display what sports you have unlocked."""
        unlocked_sports = self.ctx.unlocked_sports
        final_items = []
        if unlocked_sports:
            for sport in unlocked_sports:
                final_items.append(sport)
            logger.info(f"Unlocked Sports: {final_items}")
        else:
            logger.info("No unlocked sports")

    def unlocked_ex(self):
        """Display what exhibitions you have unlocked."""
        unlocked_ex_diffs = self.ctx.unlocked_ex_diffs
        final_items = []
        if unlocked_ex_diffs:
            for diff in unlocked_ex_diffs:
                final_items.append(diff.replace("Exhibition ", ""))
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

    def unlocked_stages(self):
        """Display what stages you have unlocked."""
        unlocked_courts = self.ctx.unlocked_courts
        final_items = []
        if unlocked_courts:
            for item in unlocked_courts:
                final_items.append(item)
            logger.info(f"Unlocked Stages: {final_items}")
        else:
            logger.info("No unlocked stages")

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
                final_items.append(item.replace("Sports Crystal: ", ""))
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

class MSMContext(CommonContext):
    tags = {"AP"}
    game = "Mario Sports Mix"
    game_interface: MSMInterface
    connection_state = ConnectionState.DISCONNECTED
    command_processor = MSMCommandProcessor
    items_handling = 0b111
    want_slot_data = True
    items_handled = []
    last_error_message: Optional[str] = None

    slot_data: Dict[str, Utils.Any] = {}

    # Here as placeholders, all will be replaced upon connection by slot data

    start_with_mushroom: Any = int
    sports_mix_unlock: Any = int
    court_unlock_type: Any = int
    cup_unlock_type: Any = int
    behemoth_hp: Any = float
    behemoth_king_hp: Any = float
    is_behemoth = False
    is_behemoth_king = False
    goal_condition: Any = int
    win_cups_amount: Any = int
    exhibition_difficulties: Any
    hard_tournament_difficulty: Any = bool

    # Deathlink Stuff
    deathlink_enabled: Any = False
    deathlink_action: Any
    deathlink_consequence: Any
    deathlink_o_get_points: Any
    deathlink_o_scores_points: Any
    deathlink_boss_recovered: Any
    deathlink_dodge_health_lost: Any

    # Custom Tournament Settings
    custom_basket_time: Any
    enable_b_points: Any
    b_points_win: Any
    b_period: Any

    custom_dodge_time: Any
    d_period: Any
    d_max_health: Any

    v_points_win: Any
    v_period: Any

    custom_hockey_time: Any
    enable_h_points: Any
    h_points_win: Any
    h_period: Any

    # Sanity stuff
    character_sanity: Any
    send_both_character_sanity: Any = False
    special_sanity: Any
    court_sanity: Any
    score_sanity: Any
    score_sanity_max: Any
    score_sanity_points_req: Any

    def __init__(self, server_address: str, password: str):
        super().__init__(server_address, password)
        self.game_interface = MSMInterface(logger)
        self.command_processor.ctx = self
        self.items_received = []
        self.items_handled = set()
        self.seed: Optional[str] = None

        # AP gives every received item a position/index in the received item list.
        # Use that index, not the item name, so duplicate filler items are handled separately.
        # AP gives every received item a stable index in the received-item list.
        # I use that index (not the item name) so duplicate filler items are tracked separately.
        self.queued_consumable_indices: Set[int] = set()
        self.handled_consumable_indices: Set[int] = set()
        # Set when a Get/SetReply for handled consumables has been applied this session.
        self._consumables_load_event = asyncio.Event()
        self.start_process = True
        self.handled_gecko_codes = False
        self.game_session_active = False
        self.active_game_version = None
        self.unlocked_sports_mix = False
        self.locking_period = False

        self.one_time_running = False
        self.item_processed = False
        self.awaiting_use = False
        self.forced_item_id = None
        self.last_match_score_total: Optional[int] = None
        self.previous_held_item: Optional[int] = -1
        self.pending_panel_replacement = False
        self.suppress_panel_until = 0.0

        self.boss_hp_handled = False
        self.boss_defeat_handled = False

        self.in_tournament_match = False
        self.last_tournament_location_name: Optional[str] = None
        self.cups_won: set[int] = set()

        self.minus_one = 0xFFFFFFFF

        # Deathlink Stuff
        self.has_sent_death = True
        self.received_death = True
        self.previous_opponent_score = None

        # Custom Tournament Settings Stuff
        self.handled_custom_timer = False

        # Lists for items
        self.unlocked_sports = []
        self.unlocked_cups = []
        self.unlocked_ex_diffs = []
        self.progressive_courts = []
        self.progressive_cups = []
        self.unlocked_sports_crystals = []
        self.unlocked_courts = []
        self.unlocked_characters = []
        self.unlocked_costumes = []
        self.unlocked_panel_items = []
        self.unlocked_abilities = []
        self.filler_to_give = deque()
        self.traps_to_give = deque()

        # Address Library
        self.addresslib = AddressLib()

        # Debug Stuff
        self.DEBUGGING = False
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

    @staticmethod
    async def delay_log(message: str, delay: int):
        logger.info(f"{message}")
        await asyncio.sleep(delay)

    # --- Consumable persistence (filler + traps) ---
    # These are one-shot items tracked by AP received-item index and saved to server storage
    # so reconnects don't hand them out again. Key is scoped per slot.

    @property
    def consumable_storage_key(self) -> Optional[str]:
        if self.seed is None or self.slot is None:
            return None
        return f"{CONSUMABLE_STORAGE_CATEGORY}_{self.slot}"

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

    async def load_handled_consumables(self, initialize: bool = False) -> None:
        """Load handled filler/trap indices from AP storage before queuing ReceivedItems."""
        key = self.consumable_storage_key
        if key is None or self._consumables_load_event.is_set():
            return

        self._consumables_load_event.clear()
        if initialize:
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

    async def _handle_received_items_consumables(self, args: dict) -> None:
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

            if item_name.startswith("1"):
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
        if cmd == "Connected":
            new_team = args["team"]
            new_slot = args["slot"]
            ap_locations_checked = args["checked_locations"]
            self.locations_checked.update(ap_locations_checked)
            if self.team is not None and self.slot is not None and (self.team, self.slot) != (new_team, new_slot):
                # Clear before CommonContext handles Connected so it cannot send stale local checks for the new slot.
                self.reset_local_item_state(clear_received=True, clear_consumed=True)
                self.reset_location_state()

        super().on_package(cmd, args)
        if cmd == "Connected":
            self.slot_data = args.get("slot_data", {})

            # Goal Data
            self.goal_condition = self.slot_data.get("goal_condition")
            self.behemoth_hp = self.slot_data.get("behemoth_hp")
            self.behemoth_king_hp = self.slot_data.get("behemoth_king_hp")
            self.win_cups_amount = self.slot_data.get("win_cups_amount")

            # Unlock Data
            self.start_with_mushroom = self.slot_data.get("start_with_mushroom_cup")
            self.exhibition_difficulties = self.slot_data.get("exhibition_difficulty")
            self.hard_tournament_difficulty = self.slot_data.get("hard_tournament_difficulty")
            self.sports_mix_unlock = self.slot_data.get("sports_mix_unlock")
            self.court_unlock_type = self.slot_data.get("court_unlock_type")
            self.cup_unlock_type = self.slot_data.get("cup_unlock_type")

            # Deathlink Data
            self.deathlink_enabled = self.slot_data.get("deathlink")
            self.deathlink_action = self.slot_data.get("deathlink_action")
            self.deathlink_consequence = self.slot_data.get("deathlink_consequence")
            self.deathlink_o_get_points = self.slot_data.get("deathlink_opponent_get_points")
            self.deathlink_o_scores_points = self.slot_data.get("deathlink_opponent_scores_points")
            self.deathlink_boss_recovered = self.slot_data.get("deathlink_boss_health_recovered")
            self.deathlink_dodge_health_lost = self.slot_data.get("deathlink_dodgeball_health_lost")


            # Custom Tournament Settings Data
            self.custom_basket_time = self.slot_data.get("basket_time")
            self.enable_b_points = self.slot_data.get("enable_b_points_win")
            self.b_points_win = self.slot_data.get("b_points_win")
            self.b_period = self.slot_data.get("b_period")

            self.custom_dodge_time = self.slot_data.get("dodge_time")
            self.d_period = self.slot_data.get("d_period")
            self.d_max_health = self.slot_data.get("d_max_health")


            self.v_points_win = self.slot_data.get("v_points_win")
            self.v_period = self.slot_data.get("v_period")

            self.custom_hockey_time = self.slot_data.get("hockey_time")
            self.enable_h_points = self.slot_data.get("enable_h_points_win")
            self.h_points_win = self.slot_data.get("h_points_win")
            self.h_period = self.slot_data.get("h_period")


            # Sanity Data
            self.character_sanity = self.slot_data.get("character_sanity")
            self.send_both_character_sanity = self.slot_data.get("send_both_character_sanity")
            

            asyncio.create_task(self.update_death_link(self.deathlink_enabled))
            # Slot is known now — load/create the per-slot consumable save before items arrive.
            asyncio.create_task(self.load_handled_consumables(initialize=True))
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
            key = self.consumable_storage_key
            if key:
                if cmd == "Retrieved" and key in args.get("keys", {}):
                    self._on_consumables_storage_update(args["keys"][key])
                elif cmd == "SetReply" and args.get("key") == key:
                    self._on_consumables_storage_update(args.get("value"))

    def make_gui(self):
        ui = super().make_gui()
        ui.base_title = "Archipelago Mario Sports Mix Client"
        return ui

    async def disconnect(self, allow_auto_reconnect: bool = False):
        self.game_interface.dolphin_client.disconnect()
        self.reset_game_session_state(game_active= True if dc.GAME_VERSION is not None else False)
        await super().disconnect(allow_auto_reconnect)

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
        self.has_sent_death = True
        self.received_death = True
        self.previous_opponent_score = None
        self.game_interface.current_tournament = None
        self.game_session_active = game_active
        self.active_game_version = dc.GAME_VERSION if game_active else None

    def reset_local_item_state(self, clear_received: bool = False, clear_consumed: bool = False) -> None:
        if clear_received:
            self.items_received.clear()
        self.items_handled.clear()
        self.unlocked_sports.clear()
        self.unlocked_ex_diffs.clear()
        self.progressive_courts.clear()
        self.unlocked_cups.clear()
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
        if item_index is None:
            return

        self.queued_consumable_indices.discard(item_index)
        self.handled_consumable_indices.add(item_index)
        # Save after the effect is applied so a disconnect mid-queue doesn't eat the item.
        await self.save_handled_consumables()
        self.debug_log(f"Saved handled consumable index {item_index}")

    async def save_handled_consumables(self) -> None:
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

    def reset_location_state(self) -> None:
        self.locations_checked.clear()
        self.checked_locations.clear()
        self.last_tournament_location_name = None

    def current_item_func(self):
        current_item = self.game_interface.dolphin_client.read_word(self.addresslib.p_item_held_addr)

        if current_item == self.minus_one:
            result = -1 #"No Item"
        elif current_item == 0:
            result = 0 #"Green Shell"
        elif current_item == 1:
            result = 1 #"Red Shell"
        elif current_item == 2:
            result = 2 #"Mini Mushroom"
        elif current_item == 3:
            result = 3 #"Bob-omb"
        elif current_item == 4:
            result = 4 #"Super Star"
        elif current_item == 5:
            result = 5 #"Banana"
        else:
            result = -1 #"No Item"

        return result

    def ready_to_handle(self):
        match_status = self.game_interface.dolphin_client.read_byte(self.addresslib.match_status_addr)
        string_stage = self.game_interface.dolphin_client.read_string(self.addresslib.current_stage_addr)
        current_stage = string_stage[0:3]
        paused = self.game_interface.dolphin_client.read_byte(self.addresslib.paused_addr)
        timer = self.game_interface.dolphin_client.read_float(self.addresslib.timer_addr)
        cutscene_active = self.game_interface.dolphin_client.read_byte(self.addresslib.cutscene_active_addr)
        loading_screen_active = self.game_interface.dolphin_client.read_word(self.addresslib.loading_screen_addr)
        human_players = self.game_interface.dolphin_client.read_byte(get_address(PlayerAddresses.human_players))
        basket_ex_timer = self.game_interface.get_basketball_time()
        dodge_ex_timer = self.game_interface.get_dodgeball_time()
        hockey_ex_timer = self.game_interface.get_hockey_time()
        not_match_prefix = ["s39", "s34", "s21", "s31", "s32", "s33"]
        ready_game = bool
        custom_time = self.get_custom_time()
        set_break_addr = self.game_interface.dolphin_client.follow_pointers(get_address(MatchAddresses.set_break),
                                                                            Pointers.Match.set_break_offsets)
        set_break = self.game_interface.dolphin_client.read_word(set_break_addr)

        if match_status == 0 and current_stage not in not_match_prefix and custom_time is not None:
            if self.game_interface.check_sport() == "Basketball":
                if self.game_interface.current_tournament is not None:
                    if timer < custom_time:
                        ready_game = True
                    else:
                        ready_game = False
                else:
                    if timer < basket_ex_timer:
                        ready_game = True
                    else:
                        ready_game = False

            elif self.game_interface.check_sport() == "Dodgeball":
                if self.game_interface.current_tournament is not None:
                    if timer < custom_time:
                        ready_game = True
                    else:
                        ready_game = False
                else:
                    if dodge_ex_timer == "Off":
                        ready_game = True
                    else:
                        if timer < dodge_ex_timer:
                            ready_game = True
                        else:
                            ready_game = False

            elif self.game_interface.check_sport() == "Volleyball":
                if current_stage == "s20":
                    try:
                        self.game_interface.dolphin_client.follow_pointers(self.addresslib.behemoth_hp_addr,
                                                            Pointers.Boss.behemoth_hp_offsets)
                        ready_game = True
                    except RuntimeError:
                        ready_game = False
                else:
                    try:
                        # Check if you can follow pointers to the address, if so, then ready
                        self.game_interface.dolphin_client.follow_pointers(self.addresslib.volley_last_held_addr,
                                                            Pointers.VBP.v_last_held_offsets)
                        ready_game = True
                    except RuntimeError:
                        ready_game = False
            elif self.game_interface.check_sport() == "Hockey":
                if self.game_interface.current_tournament is not None:
                    if timer < custom_time:
                        ready_game = True
                    else:
                        ready_game = False
                else:
                    if timer < hockey_ex_timer:
                        ready_game = True
                    else:
                        ready_game = False
            else:
                ready_game = False

        if paused == 0:
            is_paused = False
        else:
            is_paused = True

        if cutscene_active == 0:
            is_cutscene = False
        else:
            is_cutscene = True

        if loading_screen_active == 0:
            is_loading = True
        else:
            is_loading = False

        if set_break == 0:
            is_set_break = False
        else:
            is_set_break = True

        if human_players == 0: # 0 = Demo
            is_demo = True
        else:
            is_demo = False

        if timer == 0 and self.game_interface.check_sport() != "Volleyball":
            ready_game = False

        if ready_game and not is_cutscene and not is_paused and not is_loading and not is_set_break and not is_demo:
            return True
        else:
            return False


    # === Item Receiving ===


    async def handle_received_items(self):
        sport_tuple = ("Basketball", "Dodgeball", "Volleyball", "Hockey", "Sports Mix")
        characters_tuple = ("Mario", "Luigi", "Peach", "Daisy", "Yoshi", "Wario", "Waluigi", "Donkey Kong",
        "Diddy Kong", "Toad", "Bowser", "Bowser Jr", "Moogle", "Cactuar", "Ninja", "White Mage", "Slime", "Black Mage")
        costumes_tuple = ("Pink Yoshi", "Light Blue Yoshi", "Yellow Yoshi", "Blue Toad", "Green Toad", "Yellow Toad",
        "She-Slime", "Metal Slime",  "Tennis-wear Peach", "Tennis-wear Daisy", "Shadow White Ninja",
        "Pure White - White Mage", "Magic Red Black Mage")
        stages_tuple = ("Mario Stadium", "Koopa Troopa Beach", "Peach's Castle", "Toad Park", "DK Dock",
        "Luigi's Mansion", "Daisy Garden", "Wario Factory", "Bowser Jr. Blvd.", "Bowser's Castle", "Waluigi Pinball",
        "Ghoulish Galleon", "Star Ship", "Western Junction", "Behemoth Stage")
        ability_tuple = ("Special Meter", )


        for index, network_item in enumerate(self.items_received):
            item_id = network_item.item
            item_name = id_to_name.get(item_id)
            if index not in self.items_handled:
                if item_name is None:
                    continue

                if item_name in sport_tuple:
                    self.unlocked_sports.append(item_name)
                    self.debug_log(f"Added {item_name} to unlocked_sports")

                # Format to Basketball:, Dodgeball:, etc
                for sport in sport_tuple:
                    if item_name.startswith(f"{sport}:"):
                        self.unlocked_cups.append(item_name)
                        self.debug_log(f"Added {item_name} to unlocked_cups")

                if item_name.startswith("Exhibition"):
                    self.unlocked_ex_diffs.append(item_name)
                    self.debug_log(f"Added {item_name} to unlocked_ex_diffs")

                elif item_name == "Progressive Cup":
                    self.progressive_cups.append(item_name)
                    self.debug_log(f"Added {item_name} to progressive_cups")

                elif item_name == "Progressive Court":
                    self.progressive_courts.append(item_name)
                    self.debug_log(f"Added {item_name} to progressive_courts")

                elif item_name.startswith("Sports Crystal:"):
                    self.unlocked_sports_crystals.append(item_name)
                    self.debug_log(f"Added {item_name} to unlocked_sports_crystals")

                elif item_name in stages_tuple:
                    self.unlocked_courts.append(item_name)
                    self.debug_log(f"Added {item_name} to unlocked_courts")

                elif item_name in characters_tuple:
                    self.unlocked_characters.append(item_name)
                    self.debug_log(f"Added {item_name} to unlocked_characters")

                elif item_name in costumes_tuple:
                    self.unlocked_costumes.append(item_name)
                    self.debug_log(f"Added {item_name} to unlocked_costumes")

                elif item_name.startswith("?"):
                    self.unlocked_panel_items.append(item_name)
                    self.debug_log(f"Added {item_name} to unlocked_panel_items")

                elif item_name in ability_tuple:
                    self.unlocked_abilities.append(item_name)
                    self.debug_log(f"Added {item_name} to unlocked_abilities")

                self.items_handled.add(index)


        # Cups / Sports Mix
        # Courts
        await self.handle_court_unlocks()
        await self.handle_cup_unlocks()
        if self.cup_unlock_type == 1:
            await self.handle_progressive_cup_unlocks()

        await self.handle_sports_mix_unlock()


        if self.court_unlock_type == 1:
            await self.handle_progressive_court_unlocks()

        # Characters
        await self.handle_all_characters()

        # Traps + Filler aren't here because they can only be received in game and this function gets awaited during
        # every connection state, if you were to receive a trap or filler in the menu it wouldn't work.

    # Can't make this yet until there's a way to lock sports
    #async def handle_unlocked_sports(self):


    # === Character Unlocks ===


    async def handle_all_characters(self):
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
                    self.check_write(new_addr, "byte", value)
                except AttributeError:
                    print(f"Warning: {char} not found in {sport.__name__}!")

    # Specific value functions for characters with costumes

    def yoshi_unlocks_value(self):
        # If they don't have the character item, character is locked
        if "Yoshi" not in self.unlocked_characters:
            value = 0
            return value
        else:

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
            b_normal: ["Basketball: Mushroom Cup (Normal)", "Basketball: Flower Cup (Normal)", "Basketball: Star Cup (Normal)"],
            b_hard: ["Basketball: Mushroom Cup (Hard)", "Basketball: Flower Cup (Hard)", "Basketball: Star Cup (Hard)"],

            # Dodgeball
            d_normal: ["Dodgeball: Mushroom Cup (Normal)", "Dodgeball: Flower Cup (Normal)", "Dodgeball: Star Cup (Normal)"],
            d_hard: ["Dodgeball: Mushroom Cup (Hard)", "Dodgeball: Flower Cup (Hard)", "Dodgeball: Star Cup (Hard)"],

            # Volleyball
            v_normal: ["Volleyball: Mushroom Cup (Normal)", "Volleyball: Flower Cup (Normal)", "Volleyball: Star Cup (Normal)"],
            v_hard: ["Volleyball: Mushroom Cup (Hard)", "Volleyball: Flower Cup (Hard)", "Volleyball: Star Cup (Hard)"],

            # Hockey
            h_normal: ["Hockey: Mushroom Cup (Normal)", "Hockey: Flower Cup (Normal)", "Hockey: Star Cup (Normal)"],
            h_hard: ["Hockey: Mushroom Cup (Hard)", "Hockey: Flower Cup (Hard)", "Hockey: Star Cup (Hard)"],

            # Sports Mix
            sports_mix: ["Sports Mix: Mushroom Cup", "Sports Mix: Flower Cup", "Sports Mix: Star Cup"],
        }

        for address, cup in cup_mapping.items():
            value = 0

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
            final_value = 8 if value == 0 else value

            new_addr = get_address(address)
            self.game_interface.dolphin_client.write_byte(new_addr, final_value)
            self.check_write(new_addr, "byte", final_value)

    async def handle_progressive_cup_unlocks(self):
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
        progressive_count = len(self.progressive_cups)

        # Iterate up to the current total of items held
        for index in range(progressive_count):
            if index < len(cup_unlock_order):
                rule = cup_unlock_order[index]

                if rule["type"] == "sport":
                    for sport in sports_list:
                        formatted_name = f"{sport}: {rule['suffix']}"
                        if formatted_name not in self.unlocked_cups:
                            self.unlocked_cups.append(formatted_name)
                            self.log_once("prog_cup",
                                          f"Progressive Cup level up! Unlocked: {rule['suffix']}", False)

                elif rule["type"] == "sm":
                    if rule["value"] not in self.unlocked_cups:
                        self.unlocked_cups.append(rule["value"])
                        self.log_once("prog_cup",
                                      f"Progressive Cup level up! Unlocked: {rule['value']}", False)


    # === Sports Mix ===


    async def handle_sports_mix_unlock(self):
        sports_mix_unlocked = get_address(SportsMixAddresses.sports_mix_unlocked)
        if self.sports_mix_unlock == 0:
            if "Sports Mix" in self.unlocked_sports:
                self.unlocked_sports_mix = True
                self.game_interface.dolphin_client.write_byte(sports_mix_unlocked, 11)
                self.check_write(sports_mix_unlocked, "byte", 11)
                self.debug_log("Sports Mix unlocked by Sports Mix item")

        elif self.sports_mix_unlock == 1:
            required_items = ["Sports Crystal: Red", "Sports Crystal: Green", "Sports Crystal: Yellow",
                              "Sports Crystal: Blue"]
            # If all sports crystals are unlocked
            if all(crystal in self.unlocked_sports_crystals for crystal in required_items):
                self.unlocked_sports_mix = True
                self.game_interface.dolphin_client.write_byte(sports_mix_unlocked, 11)
                self.check_write(sports_mix_unlocked, "byte", 11)
                self.debug_log("Sports Mix unlocked by Sports Crystals")


    # === Exhibition Unlocks ===


    async def handle_court_unlocks(self):
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
            b_mushroom: ["Mario Stadium", "Koopa Troopa Beach", "DK Dock"],
            b_flower: ["Luigi's Mansion", "Western Junction", "Daisy Garden"],
            b_star: ["Bowser Jr. Blvd.", "Bowser's Castle", "Star Ship"],
            b_block: ["Peach's Castle", "Wario Factory", "Ghoulish Galleon"],

            # Volleyball
            v_mushroom: ["Mario Stadium", "Koopa Troopa Beach", "Peach's Castle"],
            v_flower: ["DK Dock", "Luigi's Mansion", "Western Junction"],
            v_star: ["Bowser Jr. Blvd.", "Bowser's Castle", "Star Ship"],
            v_block: ["Wario Factory", "Waluigi Pinball", "Ghoulish Galleon"],

            # Dodgeball
            d_mushroom: ["Mario Stadium", "Koopa Troopa Beach", "Peach's Castle"],
            d_flower: ["DK Dock", "Toad Park", "Daisy Garden"],
            d_star: ["Wario Factory", "Bowser's Castle", "Star Ship"],
            d_block: ["Western Junction", "Waluigi Pinball", "Ghoulish Galleon"],

            # Hockey
            h_mushroom: ["Mario Stadium", "Toad Park", "Peach's Castle"],
            h_flower: ["Western Junction", "Wario Factory", "Daisy Garden"],
            h_star: ["Bowser Jr. Blvd.", "Waluigi Pinball", "Star Ship"],
            h_block: ["Koopa Troopa Beach", "Ghoulish Galleon", "Bowser's Castle"],
        }

        for address, stage in stage_mapping.items():
            value = 0

            # First Stage
            # If the first stage is in unlocked stages, add 1
            if stage[0] in self.unlocked_courts:
                value += 1

            # Second Stage
            # If the second stage is in unlocked stages, add 2
            if stage[1] in self.unlocked_courts:
                value += 2

            # Third Stage
            # If the third stage is in unlocked stages, add 4
            if stage[2] in self.unlocked_courts:
                value += 4

            # If no stages are unlocked (value is 0) or the difficulty isn't unlocked, set final_value to 8 which locks
            # all stages, otherwise set final value to value
            if value == 0:# or not self.has_unlocked_difficulty():
                final_value = 8
            else:
                final_value = value

            new_addr = get_address(address)
            self.game_interface.dolphin_client.write_byte(new_addr, final_value)
            self.check_write(new_addr, "byte", final_value)

    async def handle_progressive_court_unlocks(self):

        # The order the stages will unlock, from first to last
        court_unlock_order = [
            "Mario Stadium",
            "Koopa Troopa Beach",
            "Toad Park",
            "DK Dock",
            "Peach's Castle",
            "Daisy Garden",
            "Luigi's Mansion",
            "Wario Factory",
            "Bowser Jr. Blvd.",
            "Bowser's Castle",
            "Waluigi Pinball",
            "Western Junction",
            "Ghoulish Galleon",
            "Star Ship",
            "Behemoth Stage"
        ]

        # Count how many total Progressive Stage items the server has sent us
        progressive_count = len(self.progressive_courts)

        # Iterate through ordered list up to the number of stages we have unlocked
        for index in range(progressive_count):
            # Safety check to prevent index errors if extra progressive items are somehow received
            if index >= len(court_unlock_order):
                break

            target_stage = court_unlock_order[index]

            # Add to unlocked_courts if it isn't already there
            if target_stage not in self.unlocked_courts:
                self.unlocked_courts.append(target_stage)
                logger.info(f"Progressive Court level up! Unlocked: {target_stage}")

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


    # === Ability Unlocks ===


    async def handle_unlocked_abilities(self):
        await self.handle_special_meter_unlock()

    async def handle_special_meter_unlock(self):
        if not self.ready_to_handle():
            self.debug_log("Special meter lock waiting; game not ready")
            return

        try:
            special_meter = self.game_interface.dolphin_client.follow_pointers(self.addresslib.p_special_meter_addr,
                                                                            Pointers.Player.special_meter_offsets)

            if "Special Meter" not in self.unlocked_abilities:
                self.game_interface.dolphin_client.write_float(special_meter, 0.0)

            else:
                self.log_once("special_meter", "Special meter unlocked; not locking meter", True)
        except Exception as e:
            self.debug_log(f"Special meter handling failed: {e}")


    # === Filler + ?-Panel Handling ===


    async def handle_one_time_items(self):
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
        if filler != "1 Coin" and current_item != -1:
            self.debug_log(f"Waiting to give {filler}; player already has item={current_item}")
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
            self.check_write(self.addresslib.p_item_held_addr, "word", self.forced_item_id)
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
        if self.game_interface.check_sport() == "Volleyball":
            return False

        elif timer == 0 and self.game_interface.check_sport() != "Volleyball":
            return True
        else:
            return False

    async def handle_question_mark_panel_items(self):
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
        random_item = random.choice(self.unlocked_panel_items)

        # Extract the base name (e.g., if item is "1 Banana", get "Banana")
        # This searches the keys of the map to find a match
        item_id = next((val for key, val in item_map.items() if key in random_item), None)

        if item_id is not None:
            item_id_int = int(item_id)
            self.game_interface.dolphin_client.write_word(self.addresslib.p_item_held_addr, item_id_int)
            verify_item = self.current_item_func()
            logger.info(f"?-Panel activated! Item replaced with {random_item}!")
            self.debug_log(f"Panel wrote item id {item_id_int}; addr={self.addresslib.p_item_held_addr:#x}, verify={verify_item}")
            self.check_write(self.addresslib.p_item_held_addr, "word", item_id_int)
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

        if not self.ready_to_handle():
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
            # If the trap is to freeze character 3, but we're only playing 2-on-2, send trap to either char 1 or 2
            if trap == "Freeze Character 3 Trap" and self.game_interface.check_player_amount() == 2:
                random_int = randint(1, 2)
                logger.info(f"2-on-2 detected! Sending trap to character {random_int}")
                redirected_trap = f"Freeze Character {random_int} Trap"

                # Execute the lambda wrapper function inside the task creation
                asyncio.create_task(trap_mapping[redirected_trap]())
                self.debug_log(f"Redirected Freeze Character 3 to character {random_int}")
                await self.mark_consumable_handled(item_index)
            elif trap == "Teleport Character 3 Trap" and self.game_interface.check_player_amount() == 2:
                random_int = randint(1, 2)
                logger.info(f"2-on-2 detected! Sending trap to character {random_int}")
                redirected_trap = f"Teleport Character {random_int} Trap"

                # Execute the lambda wrapper function inside the task creation
                asyncio.create_task(trap_mapping[redirected_trap]())
                self.debug_log(f"Redirected Teleport Character 3 to character {random_int}")
                await self.mark_consumable_handled(item_index)
            else:
                # For standalone methods, this runs them. For lambdas, it resolves the underlying coroutine.
                asyncio.create_task(trap_mapping[trap]())

                self.debug_log(f"Started trap task for {trap}")
                await self.mark_consumable_handled(item_index)
        else:
            logger.warning(f"Unknown trap item: {trap}")
            self.debug_log(f"Unknown trap {trap} consumed so it does not loop forever")
            await self.mark_consumable_handled(item_index)

        # Prevents multiple traps from firing at the exact same millisecond
        await asyncio.sleep(0.1)

    async def run_freeze_trap(self, char_id: int):
        """Freezes the character in place for 5 seconds"""

        char = f"B{char_id}"
        offset_1 = getattr(Pointers.Player, char)
        offset_group = getattr(offset_1, "Position")

        x_addr = self.game_interface.dolphin_client.follow_pointers(self.addresslib.p_pos_addr, offset_group.x_offsets)
        y_addr = self.game_interface.dolphin_client.follow_pointers(self.addresslib.p_pos_addr, offset_group.y_offsets)
        z_addr = self.game_interface.dolphin_client.follow_pointers(self.addresslib.p_pos_addr, offset_group.z_offsets)


        # Capture location
        freeze_x = self.game_interface.dolphin_client.read_float(x_addr)
        freeze_y = 0.1  # Setting it to 0 causes infinite spin glitch
        freeze_z = self.game_interface.dolphin_client.read_float(z_addr)

        self.debug_log(f"Freeze Trap {char_id} started at ({freeze_x}, {freeze_z})")

        # Set timer
        end_time = asyncio.get_event_loop().time() + 5.0

        # Freeze Loop
        while asyncio.get_event_loop().time() < end_time:
            self.game_interface.dolphin_client.write_float(x_addr, freeze_x)
            self.game_interface.dolphin_client.write_float(y_addr, freeze_y)
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

        # Freeze Loop
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

        # Freeze Loop
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

        x_addr = self.game_interface.dolphin_client.follow_pointers(self.addresslib.p_pos_addr, offset_group.x_offsets)
        z_addr = self.game_interface.dolphin_client.follow_pointers(self.addresslib.p_pos_addr, offset_group.z_offsets)

        self.game_interface.dolphin_client.write_float(x_addr, tele_x)
        self.game_interface.dolphin_client.write_float(z_addr, tele_z)
        self.debug_log(f"Teleported character {char_id} to X: {tele_x}, Z: {tele_z}")

    # async def swap_trap(self):
    #     """Swaps which character the player is controlling"""
    #
    #     cpu_offsets = [
    #         Pointers.Player.B1.is_cpu,
    #         Pointers.Player.B2.is_cpu,
    #         Pointers.Player.B3.is_cpu,
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
        await self.set_custom_timer()
        await self.set_period_amount()
        await self.has_points_win()
        await self.set_custom_dodge_health()

    def get_default_time(self):
        """Gets the default option value corresponding to the default timer value for the sport"""

        sport = self.game_interface.check_sport()
        if sport == "Basketball":
            return 2
        elif sport == "Dodgeball" or sport == "Hockey":
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
            4: 12600
        }

        h_d_option_to_timer = {
            0: 7200,
            1: 9000,
            2: 10800,
            3: 12600,
            4: 14400
        }
        sport = self.game_interface.check_sport()

        if sport == "Basketball":
            return b_option_to_timer.get(self.custom_basket_time)
        elif sport == "Dodgeball":
            return h_d_option_to_timer.get(self.custom_dodge_time)
        elif sport == "Hockey":
            return h_d_option_to_timer.get(self.custom_hockey_time)
        else:
            return 99999

    async def set_custom_timer(self):
        """Sets the custom timer depending on the sport and player's option.
        Volleyball doesn't have a timer."""
        new_time = None
        status = self.game_interface.match_status()

        if status in (2,3):
            self.handled_custom_timer = False

        if self.handled_custom_timer:
            return

        sport = self.game_interface.check_sport()

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

        # This is true when we're locking points
        if self.locking_period:
            self.game_interface.dolphin_client.write_byte(addr, 4) # Make sure the game doesn't end after 1 period
            return

        sport = self.game_interface.check_sport()

        sport_to_var = {
            "Basketball": self.b_period,
            "Dodgeball": self.d_period,
            "Volleyball": self.v_period,
            "Hockey": self.h_period
        }

        target_value = sport_to_var.get(sport)

        self.game_interface.dolphin_client.write_byte(addr, target_value)

    async def has_points_win(self):
        """Check if the player has scored the required amount of points to win the period/set"""

        sport = self.game_interface.check_sport()
        period = self.game_interface.dolphin_client.read_byte(self.addresslib.current_period)
        curr_player_score = self.game_interface.dolphin_client.read_word(get_address(player_score_addresses[period]))
        curr_opp_score = self.game_interface.dolphin_client.read_word(get_address(opponent_score_addresses[period]))

        if sport == "Basketball":
            if self.enable_b_points:
                # Checks if the player OR opponent has reached the points to win, if so, set timer to 0 which ends
                # the period
                if curr_player_score >= self.b_points_win or curr_opp_score >= self.b_points_win:
                    self.game_interface.dolphin_client.write_float(self.addresslib.timer_addr, 0)


        elif sport == "Volleyball":
            # Changes the value of the points to win address since Volleyball does all this by itself
            self.game_interface.dolphin_client.write_byte(get_address(VolleyballAddresses.points_to_win),
                                                          self.v_points_win)

        elif sport == "Hockey":
            if self.enable_h_points:
                # Checks if the player OR opponent has reached the points to win, if so, set timer to 0 which ends
                # the period
                if curr_player_score >= self.h_points_win or curr_opp_score >= self.h_points_win:
                    self.game_interface.dolphin_client.write_float(self.addresslib.timer_addr, 0)

    async def set_custom_dodge_health(self):
        """Sets the custom health in dodgeball"""
        sport = self.game_interface.check_sport()

        if sport == "Dodgeball":
            if self.ready_to_handle():
                self.game_interface.dolphin_client.write_word(get_address(PlayerAddresses.dodge_max_health), self.d_max_health)
                self.game_interface.dolphin_client.write_word(get_address(OpponentAddresses.dodge_max_health), self.d_max_health)


    # === Goal/Boss Stuff ===

    async def has_cup_goaled(self):
        cups_won_total = len(self.cups_won)

        if self.goal_condition == 3:
            if cups_won_total >= self.win_cups_amount:
                await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                self.debug_log(f"Goal Achieved: Win {self.win_cups_amount} Cups!")

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

                    if behemoth_hp <= 0:
                        self.boss_defeat_handled = True  # Lock execution immediately

                        if self.goal_condition == 1:
                            await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                            self.debug_log("Goal Achieved: Defeated Behemoth!")
                        else:
                            await self.check_location("Defeat Behemoth!")

            # Behemoth King Handling
            elif self.is_behemoth_king:

                if address_behemoth_hp:
                    behemoth_hp = self.game_interface.dolphin_client.read_float(address_behemoth_hp)

                    if behemoth_hp <= 0:
                        self.boss_defeat_handled = True  # Lock execution immediately

                        if self.goal_condition == 2:
                            await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                            self.debug_log("Goal Achieved: Defeated Behemoth King!")
                        else:
                            await self.check_location("Defeat Behemoth King!")

    async def check_boss_type(self):
        """Check which boss is currently being fought"""

        is_sports_mix = self.game_interface.check_sports_mix()
        current_stage = self.game_interface.dolphin_client.read_string(self.addresslib.current_stage_addr)
        match_status = self.game_interface.dolphin_client.read_byte(self.addresslib.match_status_addr)

        if current_stage == "s20VO":
            if is_sports_mix:
                self.is_behemoth_king = True
                self.is_behemoth = False
                self.debug_log("Behemoth King Found")
            else:
                self.is_behemoth_king = False
                self.is_behemoth = True
                self.debug_log("Behemoth Found")

            if match_status == 2:
                self.boss_hp_handled = False

    async def handle_boss_hp(self):
        """Change the boss' HP depending on what boss it is and their custom health set"""

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


    # === Location Handling ===


    async def check_location(self, location_name: str):
        """Checks if you've already got the location, if not, notifies AP about getting the location"""

        location_id = LOCATION_NAME_TO_ID.get(location_name)

        if location_id is None:
            self.debug_log(f"No AP location found: {location_name}")
            return

        if location_id in self.locations_checked:
            self.debug_log(f"Location in locations checked!")
            return

        await self.send_msgs([{"cmd": "LocationChecks", "locations": [location_id]}])
        self.locations_checked.add(location_id)
        self.debug_log(f"Checked location: {location_name}")

    def get_tournament_cup_and_round(self, sport: str, stage_code: str):
        """Gets the current cup and round (if applicable)"""

        current_cup = self.game_interface.current_tournament

        if current_cup in tournament_round_stages.get(sport, {}):
            stages = tournament_round_stages[sport][current_cup]
            if stage_code in stages:
                return current_cup, stages.index(stage_code) + 1

            self.debug_log(f"Stage {stage_code} was not found in current tournament cup {current_cup}")
            return None, None

        for cup, stages in tournament_round_stages.get(sport, {}).items():
            if stage_code in stages:
                return cup, stages.index(stage_code) + 1

        return None, None

    def get_current_cup_location_name(self) -> Optional[str]:
        """Get the correct location name for the sport, cup and round"""

        current_stage = self.game_interface.dolphin_client.read_string(self.addresslib.current_stage_addr)

        stage_code = current_stage[:3]
        sports_mix_activated = self.game_interface.check_sports_mix()
        sport = self.game_interface.check_sport()


        if stage_code == "s20":
            self.debug_log(f"Stage {stage_code} is Behemoth Stage, separate function handles that.")
            return None

        if stage_code == "s39":
            self.debug_log(f"Stage {stage_code} is the menu, player has probably been sent to the void.")
            return None

        if sport is None:
            self.debug_log(f"Could not build cup location from stage={current_stage}, sport={sport}")
            return None

        cup, round_number = self.get_tournament_cup_and_round(sport, stage_code)

        if cup is None or round_number is None:
            self.debug_log(f"Could not find tournament cup/round for sport={sport}, stage_code={stage_code}")
            return None

        difficulty = self.game_interface.get_tournament_difficulty(cup)

        if difficulty is None and not sports_mix_activated:
            self.debug_log(f"Could not find tournament difficulty for cup={cup}")
            return None

        if sports_mix_activated:
            return f"Sports Mix: Beat {cup} Round {round_number}"
        else:
            return f"{sport}: Beat {difficulty} {cup} Round {round_number}"

    async def check_pending_tournament_location(self):
        if self.last_tournament_location_name is None:
            return

        location_name = self.last_tournament_location_name
        self.last_tournament_location_name = None
        self.debug_log(f"Sending pending tournament location: {location_name}")
        await self.check_location(location_name)

    async def handle_exhibition_win(self):
        """Handles sending the checks to do with exhibition wins"""

        # Already marked as tournament
        if self.in_tournament_match:
            return

        # If Sports Mix is running, standard Exhibition checks shouldn't fire
        if self.game_interface.check_sports_mix():
            return

        current_stage = self.game_interface.dolphin_client.read_string(self.addresslib.current_stage_addr)
        match_status = self.game_interface.match_status()

        if match_status != 1:
            return

        stage_code = current_stage[:3]
        stage = stage_names.get(stage_code)
        sport = self.game_interface.check_sport()
        difficulty, _ = self.game_interface.get_exhibition_difficulty()

        if stage is None or stage == "Menu" or sport is None or difficulty is None:
            return

        difficulties_dict = {0: "Easy", 1: "Normal", 2: "Hard", 3: "Expert"}
        # Make option for just expert sending all diffs or sending previous diffs
        for i in range(0,4):
            if i <= difficulty: # Find all difficulties the same and below
                diff_name = difficulties_dict.get(i)
                item = f"Exhibition {diff_name}"
                # Check if the difficulty is enabled and we have the item for it
                if diff_name in self.exhibition_difficulties and item in self.unlocked_ex_diffs:
                    location_name = f"{sport} Ex: Beat {stage} ({diff_name})"
                    await self.check_location(location_name)

    async def check_current_cup(self):
        """Checks what cup we are in via the tournament map"""

        current_stage = self.game_interface.dolphin_client.read_string(self.addresslib.current_stage_addr)
        stage_code = current_stage[:3]

        # Check standard bracket maps first
        cup = tournament_map_cups.get(stage_code)
        if cup is not None:
            self.game_interface.current_tournament = cup
            self.in_tournament_match = True
            self.debug_log(f"Current tournament cup set to {cup} via map screen.")
            return

        # Sports Mix Override
        sports_mix_activated = self.game_interface.check_sports_mix()
        sport = self.game_interface.check_sport()

        if sports_mix_activated and sport:
            # If we are actively playing a court that belongs to a tournament path,
            # lock the script into Tournament Mode so Exhibition logic cannot hijack it.
            for possible_cup, stages in tournament_round_stages.get(sport, {}).items():
                if stage_code in stages:
                    self.game_interface.current_tournament = possible_cup
                    self.in_tournament_match = True  # <--- FORCED TRUE
                    self.debug_log(
                        f"Sports Mix Match Detected! Locking tournament mode. Cup: {possible_cup}, Stage: {stage_code}")
                    return

    async def handle_cup_round_win(self):
        """Handles sending the checks for winning a round of a cup"""

        if not self.in_tournament_match:
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


    # === Blocking Functions ===


    async def handle_locked_tournament_stage_points(self):
        """Locks the points in a tournament match if you don't have the required cup or stage"""

        if not self.in_tournament_match or not self.ready_to_handle():
            return

        current_stage = self.game_interface.dolphin_client.read_string(self.addresslib.current_stage_addr)
        stage_code = current_stage[:3]
        stage = stage_names.get(stage_code)
        sports_mix_activated = self.game_interface.check_sports_mix()
        sport = self.game_interface.check_sport()


        if stage is None or sport is None:
            self.debug_log(f"Could not check tournament stage unlock for stage={current_stage}")
            return

        cup, round_number = self.get_tournament_cup_and_round(sport, stage_code)

        if cup is None or round_number is None:
            self.debug_log(f"Could not check locked tournament points for sport={sport}, stage_code={stage_code}")
            return

        difficulty = self.game_interface.get_tournament_difficulty(cup)
        required_stage = f"{stage}"
        if sports_mix_activated:
            required_cup = f"Sports Mix: {cup}"
        else:
            required_cup = f"{sport}: {cup} ({difficulty})"

        if required_stage in self.unlocked_courts and required_cup in self.unlocked_cups:
            self.locking_period = False
            return

        if required_stage not in self.unlocked_courts and required_cup not in self.unlocked_cups:
            self.rate_log("locked_tournament", f"Blocked points for {sport} {cup} Round {round_number}. Missing {required_stage} & {required_cup}", 10, False)
        elif required_stage not in self.unlocked_courts:
            self.rate_log("locked_tournament", f"Blocked points for {sport} {cup} Round {round_number}. Missing {required_stage}", 10, False)
        elif required_cup not in self.unlocked_cups:
            self.rate_log("locked_tournament", f"Blocked points for {sport} {cup}. Missing {required_cup}", 10, False)

        try:
            await self.clear_player_score()
            await self.lock_period_1()
            await self.lock_special_meter()
        finally:
            pass

    async def handle_locked_exhibition_points(self):
        """Locks the points in an exhibition match if you don't have the required difficulty
        This is just backup in case the has_unlocked_difficulty doesn't work."""

        if self.in_tournament_match or not self.ready_to_handle():
            return

        _, diff_name = self.game_interface.get_exhibition_difficulty()


        if f"Exhibition {diff_name}" in self.unlocked_ex_diffs:
            self.locking_period = False
            return

        self.rate_log("locked_ex", f"Blocked points for match. Missing: Exhibition {diff_name}", 10, False)

        try:
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
            await self.lock_behemoth_hp()
            await self.lock_special_meter()
        finally:
            pass

    def send_to_void(self):
        """Sends the player to the void (stage=s39ba, module=0x6D656E75)"""
        current_module_addr = self.game_interface.dolphin_client.follow_pointers(self.addresslib.current_module_addr,
                                                                            Pointers.Match.current_module_offsets)

        self.game_interface.dolphin_client.write_string(self.addresslib.current_stage_addr, "s39ba")
        self.game_interface.dolphin_client.write_word(current_module_addr, 0x6D656E75)

    async def clear_player_score(self):
        """Locks the player's score at 0"""

        for address in player_score_addresses:
            new_addr = get_address(address)
            self.game_interface.dolphin_client.write_word(new_addr, 0)

    async def lock_period_1(self):
        """Locks the period/set counter at period 1"""
        self.locking_period = True
        self.game_interface.dolphin_client.write_byte(self.addresslib.current_period, 0)

    async def lock_special_meter(self):
        """Locks the player's special meter at 0"""

        special_meter = self.game_interface.dolphin_client.follow_pointers(self.addresslib.p_special_meter_addr,
                                                                           Pointers.Player.special_meter_offsets)

        self.game_interface.dolphin_client.write_float(special_meter, 0)

    async def lock_behemoth_hp(self):
        """Function to lock Behemoth Health, called in handle_lock_behemoth_hp"""

        behemoth_hp = self.game_interface.dolphin_client.follow_pointers(self.addresslib.behemoth_hp_addr,
                                                                         Pointers.Boss.behemoth_hp_offsets)
        if self.is_behemoth:
            self.game_interface.dolphin_client.write_float(behemoth_hp, self.behemoth_hp)

        if self.is_behemoth_king:
            self.game_interface.dolphin_client.write_float(behemoth_hp, self.behemoth_king_hp)


    # --- Sanity Location Handling ---


    async def send_character_sanity_checks(self):
        """Handles sending checks for Character Sanity"""
        value = self.game_interface.dolphin_client.read_byte(self.addresslib.match_status_addr)

        if self.character_sanity == 0 or value != 1:
            return

        ch_byte_1 = self.game_interface.dolphin_client.read_byte(get_address(PlayerAddresses.character_1))
        ch_byte_2 = self.game_interface.dolphin_client.read_byte(get_address(PlayerAddresses.character_2))
        ch_byte_3 = self.game_interface.dolphin_client.read_byte(get_address(PlayerAddresses.character_3))

        # Grab character names (If byte is missing, defaults to "None")
        char_1 = char_to_id.get(ch_byte_1, "None")
        char_2 = char_to_id.get(ch_byte_2, "None")
        char_3 = char_to_id.get(ch_byte_3, "None")

        # Read costumes ONCE here
        costume_1 = self.game_interface.dolphin_client.read_byte(get_address(PlayerAddresses.costume_1))
        costume_2 = self.game_interface.dolphin_client.read_byte(get_address(PlayerAddresses.costume_2))
        costume_3 = self.game_interface.dolphin_client.read_byte(get_address(PlayerAddresses.costume_3))

        char_list = [char_1, char_2, char_3]
        costume_list = [costume_1, costume_2, costume_3]
                                                # This is changed because of my async, it uses some different values,
                                                # change it back to 2 when releasing!
        if self.send_both_character_sanity and (self.character_sanity == 2 or self.character_sanity == 3):
            await self.send_character_character_sanity(char_1, char_2, char_3)
            await self.send_costume_character_sanity(char_1, char_2, char_3, costume_1, costume_2, costume_3)

        else:
            if self.character_sanity == 1:
                await self.send_character_character_sanity(char_1, char_2, char_3)
            elif self.character_sanity == 2:

                for char, costume in zip(char_list, costume_list):
                    if char in costume_database and costume != 0:
                        await self.send_costume_character_sanity(char_1, char_2, char_3, costume_1, costume_2, costume_3)
                    else:
                        await self.send_character_character_sanity(char_1, char_2, char_3)

    async def send_character_character_sanity(self, char_1, char_2, char_3):
        """Sends the location for the character if Character Sanity is enabled"""

        if self.game_interface.check_player_amount() == 2:
            for character in [char_1, char_2]:
                if character != "None":
                    await self.check_location(f"Win as {character}")

        elif self.game_interface.check_player_amount() == 3:
            for character in [char_1, char_2, char_3]:
                if character != "None":
                    await self.check_location(f"Win as {character}")

    async def send_costume_character_sanity(self, char_1, char_2, char_3, costume_1, costume_2, costume_3):
        """Sends the location for the costume if Character Sanity is enabled"""

        characters_2 = [char_1, char_2]
        costumes_2   = [costume_1, costume_2]
        characters_3 = [char_1, char_2, char_3]
        costumes_3   = [costume_1, costume_2, costume_3]

        if self.game_interface.check_player_amount() == 2:
            for character, costume_byte in zip(characters_2, costumes_2):

                if character in costume_database and costume_byte not in (0, 255) and character != "None":
                    costume_db = costume_database[character]

                    # Fetch the string name
                    costume_name = costume_db.get(costume_byte)

                    if costume_name:
                        await self.check_location(f"Win as {costume_name}")

        elif self.game_interface.check_player_amount() == 3:
            for character, costume_byte in zip(characters_3, costumes_3):

                if character in costume_database and costume_byte not in (0, 255) and character != "None":
                    costume_db = costume_database[character]

                    # Fetch the string name
                    costume_name = costume_db.get(costume_byte)

                    if costume_name:
                        await self.check_location(f"Win as {costume_name}")


    # === Deathlink Stuff ===


    def timer_is_0(self):
        """Checks if the timer is 0 because volleyball is stupid"""
        sport = self.game_interface.check_sport()
        timer = self.game_interface.dolphin_client.read_byte(self.addresslib.timer_addr)

        if sport == "Volleyball":
            return False
        else:
            if timer == 0:
                return True
            else:
                return False

    def timer_reset(self):
        sport = self.game_interface.check_sport()
        timer = self.game_interface.dolphin_client.read_byte(self.addresslib.timer_addr)

        if self.in_tournament_match:
            if sport != "Volleyball":
                if timer == self.get_custom_time():
                    return True
                else:
                    return False
            else:
                return False
        else:
            if sport == "Basketball":
                if timer == self.game_interface.get_basketball_time():
                    return True
                else:
                    return False
            elif sport == "Dodgeball":
                if timer == self.game_interface.get_dodgeball_time():
                    return True
                else:
                    return False
            elif sport == "Hockey":
                if timer == self.game_interface.get_hockey_time():
                    return True
                else:
                    return False
            else:
                return False

    # Sending Deathlink
    async def handle_send_deathlink(self):
        """Gets awaited during in match and sends a deathlink depending on what the deathlink_action is"""

        possible_messages_0 = ["lost the match!", "isn't good enough!", "has a MASSIVE skill issue!",
                               "needs to take a break...", "couldn't sport their mix..."]

        possible_messages_1 = ["got DUNKED on!", "can't handle the heat!", ]

        match_status = self.game_interface.dolphin_client.read_byte(self.addresslib.match_status_addr)

        # If we're not in the state where we've died to deathlink, or in some kind of menu/cutscene,
        # set received_death to false
        if self.timer_reset() or (match_status == 0 and not self.timer_is_0()):
            self.received_death = False
            self.has_sent_death = False

        if self.deathlink_enabled:

            if self.locking_period:
                # Failsafe in case the period change doesn't get applied and the player loses,shouldn't count as a death
                return

            # Lose Match Action
            if self.deathlink_action == 0:
                if self.is_behemoth or self.is_behemoth_king:
                    await self.check_behemoth_deathlink()

                elif not self.received_death:
                    if (match_status == 2 or match_status == 3) and (not self.timer_reset() or not self.timer_is_0()):
                        if not self.has_sent_death and self.slot is not None:
                            message = random.choice(possible_messages_0)  # Pick a random message to send
                            await self.send_death(f"{self.player_names[self.slot]} {message}")
                            self.has_sent_death = True
                            self.debug_log("Sent deathlink due to losing/tying the match")


            # Every number of Points Action
            elif self.deathlink_action == 1:
                if self.is_behemoth or self.is_behemoth_king:
                    await self.check_behemoth_deathlink()

                # Dodgeball logic
                elif self.game_interface.check_sport() == "Dodgeball":
                    if self.has_dodge_opponent_scored():
                        if self.slot is not None:
                            message = random.choice(possible_messages_1)
                            await self.send_death(f"{self.player_names[self.slot]} {message}")
                            self.debug_log("Sent deathlink due to the opponent scoring in dodgeball")

                # All other sports logic
                else:
                    if self.has_score_reached_threshold():
                        if self.slot is not None:
                            message = random.choice(possible_messages_1)
                            await self.send_death(f"{self.player_names[self.slot]} {message}")
                            self.debug_log("Sent deathlink due to the opponent scoring a threshold")

    async def check_behemoth_deathlink(self):
        """Checks if the player has lost during the Behemoth boss fight"""
        match_status = self.game_interface.dolphin_client.read_byte(self.addresslib.match_status_addr)

        if match_status == 2 or match_status == 3:
            type = " King" if self.is_behemoth_king else "" # If Behemoth King, change message accordingly
            if self.slot is not None:
                await self.send_death(f"{self.player_names[self.slot]} has lost to the might of the Behemoth{type}...")

    def has_score_reached_threshold(self) -> bool:
        """Check when the opponent has got the required amount of points (self.deathlink_o_scores_points) in
        everything but dodgeball - Used for DL-C Opponent gains points. Returns True if yes, False if no"""

        current_opponent_score = sum(
            self.game_interface.dolphin_client.read_word(get_address(addr)) for addr in opponent_score_addresses)

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

        # If the threshold is met, update the tracker and return True
        if score_increase >= self.deathlink_o_scores_points:
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

        # Check for ANY point increase
        if current_opponent_score > self.previous_opponent_score:
            # The opponent scored 1 point!
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

    def handle_received_deathlink(self):
        """Gets called when on_deathlink goes off and acts depending on deathlink_consequence
        NOTE: Dodgeball deathlinks get handled differently to everything else since it doesn't have a normal scoring system"""

        if self.deathlink_enabled:
            if self.ready_to_handle():
                match_status = self.game_interface.dolphin_client.read_byte(self.addresslib.match_status_addr)
                current_stage_value = self.game_interface.dolphin_client.read_string(self.addresslib.current_stage_addr)
                current_stage = current_stage_value[:3]
                not_match_prefix = ["s39", "s34", "s21", "s31", "s32", "s33"]

                # Lose Match Consequence
                if self.deathlink_consequence == 0:
                    if self.is_behemoth or self.is_behemoth_king:
                        self.recover_boss_hp()
                    else:
                        # Force opponent to win
                        self.game_interface.dolphin_client.write_byte(self.addresslib.current_period, 4)# 4 = 5th Period
                        for address in opponent_score_addresses:
                            addr = get_address(address)
                            self.game_interface.dolphin_client.write_word(addr, 100) # Write 100 for all scores
                        self.game_interface.dolphin_client.write_float(self.addresslib.timer_addr, 0) # Set timer to 0
                        self.received_death = True # Required so we don't send a deathlink when we get sent one
                        # If we're not in the state where we've died to deathlink, or in some kind of menu/cutscene,
                        # set received_death to false
                        if (match_status != 2 and match_status != 3) or current_stage in not_match_prefix:
                            self.received_death = False

                # Opponent gains points
                elif self.deathlink_consequence == 1:
                    if self.is_behemoth or self.is_behemoth_king:
                        self.recover_boss_hp()
                    else:
                        if self.game_interface.check_sport() != "Dodgeball":
                            value = self.game_interface.dolphin_client.read_byte(self.addresslib.current_period)
                            addr = get_address(opponent_score_addresses[value]) # Get the address for current period
                            points = self.game_interface.dolphin_client.read_word(addr)
                            new_points = points + self.deathlink_o_get_points
                            self.game_interface.dolphin_client.write_word(addr, new_points)
                            total_points = sum(self.game_interface.dolphin_client.read_word(get_address(addr)) for addr in opponent_score_addresses)
                            logger.info(f"Opponent now has {total_points} points!")
                        else:
                            # Lists start at 0, we need to take away one from the value
                            random_char = randint(0, self.game_interface.check_player_amount() - 1)

                            offsets = [Pointers.Player.B1.dodge_damage,
                                       Pointers.Player.B2.dodge_damage,
                                       Pointers.Player.B3.dodge_damage,]

                            addr = get_address(PlayerAddresses.various_shp_pointers)
                            # Find the address of the damage we want to change.
                            final_addr = self.game_interface.dolphin_client.follow_pointers(addr, offsets[random_char])
                            curr_damage = self.game_interface.dolphin_client.read_word(final_addr)
                            new_damage = curr_damage + self.deathlink_dodge_health_lost
                            self.game_interface.dolphin_client.write_word(final_addr, new_damage)
                            health = self.d_max_health - new_damage
                            # Find current the character selected by randint
                            chars = [PlayerAddresses.character_1,
                                     PlayerAddresses.character_2,
                                     PlayerAddresses.character_3,]

                            # Get the character
                            value = self.game_interface.dolphin_client.read_byte(chars[random_char])
                            character = char_to_id[value]

                            # Format the message so the user knows which character is on what health
                            logger.info(f"Watch out! It may not look like it, but {character} (B{random_char+1}) is on {health} HP!")

    def recover_boss_hp(self):
        """Calculates the amount of HP recovered when sent a deathlink

        Gets n% of max Behemoth HP where n = self.deathlink_boss_recovered"""

        if self.is_behemoth:
            health_recovered = (self.deathlink_boss_recovered / 100) * self.behemoth_hp
            current_health = self.game_interface.dolphin_client.read_float(self.addresslib.behemoth_hp_addr)
            new_health = current_health + health_recovered
            self.game_interface.dolphin_client.write_float(self.addresslib.behemoth_hp_addr, new_health)
            logger.info(f"Behemoth has powered up back to {new_health} HP!")

        elif self.is_behemoth_king:
            health_recovered = (self.deathlink_boss_recovered / 100) * self.behemoth_king_hp
            current_health = self.game_interface.dolphin_client.read_float(self.addresslib.behemoth_hp_addr)
            new_health = current_health + health_recovered
            self.game_interface.dolphin_client.write_float(self.addresslib.behemoth_hp_addr, new_health)
            logger.info(f"Behemoth King has powered up back to {new_health} HP!")


    # === Misc stuff idk where to put ===


    async def dolphin_sync_task(self) -> None:
        """The main loop managing the connection to Dolphin and game-state logic routing"""

        while not self.exit_event.is_set():
            try:
                # Handle initial connection hook
                if not self.game_interface.dolphin_client.is_hooked_class():
                    if self.game_session_active:
                        self.reset_game_session_state(game_active=True)
                    await self.game_interface.dolphin_client.attempt_to_hook()


                if self.game_interface.dolphin_client.is_hooked_class():
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
                    # Use this if anything NEEDS to be done upon connection
                    unlock_ex_tabs()
                    unlock_tournament_tabs_option(self.hard_tournament_difficulty)
                    self.start_process = False

                self.last_error_message = None

                # Route Game State Execution
                self.update_connection_status()
                connection_state = self.game_interface.get_connection_state()

                if connection_state == ConnectionState.IN_MATCH:
                    await self.handle_in_match()
                elif connection_state == ConnectionState.IN_BOSS:
                    await self.handle_in_boss()
                elif connection_state == ConnectionState.IN_TOURNAMENT_MAP:
                    await self.handle_in_tournament_map()
                elif connection_state == ConnectionState.IN_MENU:
                    await self.handle_in_main_menu()
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
        """Stop SOME of the unlock messages from appearing constantly
        This doesn't block cups won because the game MAY need that for Behemoth tracking idk
        """
        games_played_address_list = [GamesPlayed.basketball, GamesPlayed.dodgeball,
                                     GamesPlayed.volleyball, GamesPlayed.hockey]

        for address in games_played_address_list:
            new_addr = get_address(address)
            value = self.game_interface.dolphin_client.read_word(new_addr)
            if value != 0:
                self.game_interface.dolphin_client.write_word(new_addr, 0)

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

        current_cups_count = len(self.cups_won)
        if current_cups_count <= self.win_cups_amount and added and self.goal_condition == 3:
            # Only show this message if the goal condition is Win Cups, we've added a cup,and we're logging the max cups
            # won so far (So it doesn't log 1 Cups Won, 2, 3 all the way up to 12 or smth, only logs 12 Cups Won!)
            logger.info(f"{current_cups_count}/{self.win_cups_amount} Cups Won!")

    async def apply_cups_won(self):
        """Applies the cups the player has won to the ingame cup tracker, no clue if this does anything
        but may be used for future things if my logic is correct"""

        b_mush = CupsWonMultiple.Basketball.mushroom_cup
        b_flow = CupsWonMultiple.Basketball.flower_cup
        b_star = CupsWonMultiple.Basketball.star_cup

        d_mush = CupsWonMultiple.Dodgeball.mushroom_cup
        d_flow = CupsWonMultiple.Dodgeball.flower_cup
        d_star = CupsWonMultiple.Dodgeball.star_cup

        v_mush = CupsWonMultiple.Volleyball.mushroom_cup
        v_flow = CupsWonMultiple.Volleyball.flower_cup
        v_star = CupsWonMultiple.Volleyball.star_cup

        h_mush = CupsWonMultiple.Hockey.mushroom_cup
        h_flow = CupsWonMultiple.Hockey.flower_cup
        h_star = CupsWonMultiple.Hockey.star_cup

        cup_mapping = {
            b_mush: ["Basketball", "Mushroom"],
            b_flow: ["Basketball", "Flower"],
            b_star: ["Basketball", "Star"],

            d_mush: ["Dodgeball", "Mushroom"],
            d_flow: ["Dodgeball", "Flower"],
            d_star: ["Dodgeball", "Star"],

            v_mush: ["Volleyball", "Mushroom"],
            v_flow: ["Volleyball", "Flower"],
            v_star: ["Volleyball", "Star"],

            h_mush: ["Hockey", "Mushroom"],
            h_flow: ["Hockey", "Flower"],
            h_star: ["Hockey", "Star"],
        }

        if self.cups_won is not None:
            # Loop through each individual cup memory address we need to update
            for address, types in cup_mapping.items():
                sport = types[0] # Grabs "Basketball", "Hockey" etc since 0 = 1st item of list
                cup = types[1] # Grabs "Mushroom", "Flower" etc since 1 = 2nd item of list

                # Reset the counter
                value = 0

                # Count how many checked locations match this specific sport and cup
                for location in self.cups_won:
                    if sport in location and cup in location:
                        value += 1

                # Convert to bytes since the address is a halfword (2 Bytes)
                final_val = value.to_bytes(2, byteorder="big")

                # Write to memory
                self.game_interface.dolphin_client.write_bytes(get_address(address), final_val)

    async def handle_gecko_codes(self):
        """Handle the gecko code patches for each region"""

        current_module = self.game_interface.dolphin_client.follow_pointers(self.addresslib.current_module_addr,
                                                                            Pointers.Match.current_module_offsets)
        value = self.game_interface.dolphin_client.read_word(current_module)

        if value == 0x6D656E75 and not self.handled_gecko_codes:
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

    def check_write(self, addr: int, type: str, correct_value: Any):
        """Checks if the address has the correct value to it"""
        read = None
        match type.lower():
            case "byte": read = self.game_interface.dolphin_client.read_byte
            case "word": read = self.game_interface.dolphin_client.read_word
            case "string": read = self.game_interface.dolphin_client.read_string
            case "float": read = self.game_interface.dolphin_client.read_float
            case _: read = None

        if read is not None:
            read_value = read(addr)
            if read_value == correct_value:
                return True
            else:
                logger.error(f"WARNING: It doesn't seem like things are working! You may need to restart Dolphin.\n"
                             f"If you can, please remember what you did prior as this may help solve this bug overall\n"
                             f"addr={hex(addr)}, type={type}, read_val={read_value}, corr_val={correct_value}")
                return False
        else:
            self.delay_log(f"Uh oh, I'm stupid! This read type doesn't exist! Please ping @electrostarz\n"
                           f"type={type}", 10)
            return False


    # === Where to handle what ===


    async def handle_in_match(self):
        """What functions should be handled during a match"""
        # Cup Goal
        await self.has_cup_goaled()

        await self.track_cups_won()
        await self.apply_cups_won()

        # Custom Tournament Settings
        if self.in_tournament_match:
            await self.handle_custom_tournament_settings()

        # Deathlink
        await self.handle_send_deathlink()

        # Lock points if you don't have the stage/cup/difficulty
        await self.handle_locked_tournament_stage_points()
        await self.handle_locked_exhibition_points()

        # Locations
        await self.handle_exhibition_win()
        await self.handle_cup_round_win()
        await self.send_character_sanity_checks()

        # Items
        await self.handle_one_time_items()
        await self.handle_traps()
        await self.handle_question_mark_panel_items()
        await self.handle_unlocked_abilities()

        self.handled_gecko_codes = False

        await asyncio.sleep(0.1)


    async def handle_in_boss(self):
        """What functions should be handled in the boss"""

        await self.handle_boss_hp()
        await self.check_boss_type()
        await self.handle_lock_behemoth_hp()
        await self.has_boss_goaled()

        # Items
        await self.handle_one_time_items()
        await self.handle_traps()
        await self.handle_question_mark_panel_items()
        await self.handle_unlocked_abilities()

        self.handled_gecko_codes = False

        await asyncio.sleep(0.1)


    async def handle_in_tournament_map(self):
        """What functions should be handled in a tournament map"""

        await self.check_current_cup()
        await self.check_pending_tournament_location()

        self.handled_gecko_codes = False
        self.handled_custom_timer = False
        
        await asyncio.sleep(0.1)


    async def handle_in_main_menu(self):
        """What functions should be handled in the main menu"""
        await self.has_cup_goaled()
        await self.track_cups_won()
        await self.apply_cups_won()

        await self.handle_received_items()
        await self.check_pending_tournament_location()
        await self.stop_stupid_unlock_notifs()

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
