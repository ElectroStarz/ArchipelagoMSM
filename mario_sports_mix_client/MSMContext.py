import asyncio
import logging
import random
import traceback
from collections import deque
from random import randint
from typing import Dict, Set, Optional, Any, List

import Utils
from CommonClient import ClientCommandProcessor, CommonContext
from NetUtils import ClientStatus
from .MSMInterface import MSMInterface, ConnectionState
from ..items import item_table
from ..locations import LOCATION_NAME_TO_ID
from .MSMFunctions import *
from . import dolphin_connection as dc
from .memory_addresses_pal import *
from .common_address_library import AddressLib

id_to_name = {data.id: name for name, data in item_table.items()}
CLIENT_VERSION = "0.3.1"
COMPATIBLE_VERSIONS = ["0.3.0"]


status_messages = {
    ConnectionState.IN_MATCH: "In Match",
    ConnectionState.IN_BOSS: "In Boss",
    ConnectionState.IN_MENU: "In Main Menu",
    ConnectionState.DISCONNECTED: "Unable to connect to the Dolphin instance, attempting to reconnect...",
    ConnectionState.CONNECTED: "Connected to Dolphin!",
    ConnectionState.IN_TOURNAMENT_MAP: "In Tournament Map",
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
CONSUMABLE_STORAGE_CATEGORY = "mario_sports_mix_client"
LOCATION_STORAGE_CATEGORY = "mario_sports_mix_locations"
# Build the reverse lookup once so persisted AP location IDs can be shown as local names.
LOCATION_ID_TO_NAME = {location_id: name for name, location_id in LOCATION_NAME_TO_ID.items()}


class MSMCommandProcessor(ClientCommandProcessor):
    ctx: "MSMContext"

    def __init__(self, ctx: "MSMContext"):
        super().__init__(ctx)

    def _cmd_debug_mode(self):
        """Toggle debugging on and off (Default off)"""
        if not self.ctx.DEBUGGING:
            self.ctx.DEBUGGING = True
            logger.info("Debugging on")
            self.ctx.debug_log("This is what a debug message will look like!")
        else:
            self.ctx.DEBUGGING = False
            logger.info("Debugging off")

    def _cmd_change_debug_amount(self, amount: str):
        """Change the amount of debug messages that are stored so they don't repeat"""
        try:
            new_amount = int(amount)
            from collections import deque
            self.ctx.last_debug_messages = deque(self.ctx.last_debug_messages, maxlen=new_amount)
        except ValueError:
            logger.info(f"Error: '{amount} is not a valid number! Please enter an integer.")

    def _cmd_read_address(self, address: str, addr_type: str = "Word", *pointers: str):
        """Read the value of any address - Used for diagnostic purposes.
        address should look like 0x80000000 (8 digits after 0x), pointers should look like 0x1F4, 0x8, addr_type defaults to Word"""

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

        match addr_type:
            case "Byte":
                result = client.read_byte(final_address)
            case "Halfword":
                result = client.read_bytes(final_address, 2)
            case "Word":
                result = client.read_word(final_address)
            case "Float":
                result = client.read_float(final_address)
            case "String":
                result = client.read_string(final_address)
            case _:
                error_msg = f"Error: Unsupported address type '{addr_type}'"
                logger.error(error_msg)
                return error_msg

        # Format final_address with hex() makes it easier to read back.
        log_message = f"[Memory Read] {addr_type} at {hex(final_address)}. Result: {result}"

        logger.info(log_message)
        return log_message




    def _cmd_status(self):
        """Display the current dolphin connection status."""
        logger.info(f"Connection Status: {status_messages[self.ctx.connection_state]}")

    def _cmd_reapply_unlocks(self):
        """Reapply unlocks if you don't have them!"""
        asyncio.create_task(self.ctx.handle_received_items())
        logger.info("Reapplied unlocks!")

    def _cmd_reset_cached(self):
        """Manually reset the cached values if address errors are coming up when switching regions"""
        self.ctx.addresslib.reset_all_addresses()
        logger.info("Reset cached values!")

    def _cmd_deathlink(self):
        """Toggle deathlink from client. Overrides default setting."""
        self.ctx.deathlink_enabled = not self.ctx.deathlink_enabled
        Utils.async_start(self.ctx.update_death_link(self.ctx.deathlink_enabled))
        logger.info(f"Deathlink {'enabled' if self.ctx.deathlink_enabled else 'disabled'}!")

    def _cmd_unlocked_characters(self):
        """Display what characters you have unlocked."""
        unlocked_characters = self.ctx.unlocked_characters
        final_items = []
        if unlocked_characters:
            for char in unlocked_characters:
                final_items.append(char)
            logger.info(f"Unlocked Characters: {final_items}")
        else:
            logger.info("No unlocked characters")

    def _cmd_unlocked_costumes(self):
        """Display what costumes you have unlocked"""
        unlocked_costumes = self.ctx.unlocked_costumes
        final_items = []
        if unlocked_costumes:
            for costume in unlocked_costumes:
                final_items.append(costume)
            logger.info(f"Unlocked Costumes: {final_items}")
        else:
            logger.info("No unlocked costumes")

    def _cmd_unlocked_cups(self):
        """Display what cups you have unlocked."""
        unlocked_cups = self.ctx.unlocked_cups
        final_items = []
        if unlocked_cups:
            for cup in unlocked_cups:
                final_items.append(cup)
            logger.info(f"Unlocked Cups: {final_items}")
        else:
            logger.info("No unlocked cups")

    def _cmd_unlocked_stages(self):
        """Display what stages you have unlocked."""
        unlocked_stages = self.ctx.unlocked_stages
        final_items = []
        if unlocked_stages:
            for item in unlocked_stages:
                final_items.append(item)
            logger.info(f"Unlocked Stages: {final_items}")
        else:
            logger.info("No unlocked stages")

    def _cmd_unlocked_abilities(self):
        """Display what abilities you have unlocked."""
        unlocked_abilities = self.ctx.unlocked_abilities
        final_items = []
        if unlocked_abilities:
            for ability in unlocked_abilities:
                final_items.append(ability)
            logger.info(f"Unlocked Abilities: {final_items}")
        else:
            logger.info("No unlocked abilities")

    def _cmd_unlocked_panel(self):
        """Display what ?-Panel items you have unlocked."""
        unlocked_panel = self.ctx.unlocked_panel_items
        final_items = []
        if unlocked_panel:
            for item in unlocked_panel:
                final_items.append(item.replace("?-Panel:", ""))
            logger.info(f"Unlocked Panel Items: {final_items}")
        else:
            logger.info("No unlocked ?-Panel items")

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
        logger.info(f"Current Item: {item_map[current_item]} - ID is {current_item}")

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
    sports_mix_unlock = int
    behemoth_hp = float
    behemoth_king_hp = float
    is_behemoth = False
    is_behemoth_king = False
    goal_condition = int
    #win_cups_amount = int
    hard_tournament_difficulty = bool

    # Deathlink Stuff
    deathlink_enabled: bool = False
    deathlink_action = int
    deathlink_consequence = int
    deathlink_o_get_points = int
    deathlink_o_scores_points = int
    deathlink_boss_recovered = int
    deathlink_dodge_health_lost = int

    # Sanity stuff
    character_sanity = int
    send_both_character_sanity = bool
    special_sanity = bool
    court_sanity = bool
    score_sanity = bool
    score_sanity_max = int
    score_sanity_points_req = int

    def __init__(self, server_address: str, password: str):
        super().__init__(server_address, password)
        self.game_interface = MSMInterface(logger)
        self.command_processor.ctx = self
        self.items_received = []
        self.items_handled = []
        self.seed: Optional[str] = None

        # Consumables use AP's received-item index as their ID. Keep these as indices, not item names
        # because duplicate filler and trap items are allowed but each copy should only fire once.
        self.queued_consumable_indices: Set[int] = set()
        self.consumed_item_indices: Set[int] = set()
        self.consumed_item_storage_key: Optional[str] = None
        self.location_storage_key: Optional[str] = None

        self.start_process = True
        self.handled_gecko_codes = False
        self.game_session_active = False
        self.active_game_version = None
        self.unlocked_sports_mix = False

        self.one_time_running = False
        self.item_processed = False
        self.awaiting_use = False
        self.forced_item_id = None
        self.last_match_score_total: Optional[int] = None
        self.suppress_panel_until = 0.0
        self.boss_hp_handled = False
        self.boss_defeat_handled = False
        self.in_tournament_match = False
        self.last_tournament_location_name: Optional[str] = None

        self.minus_one = 0xFFFFFFFF

        # Deathlink Stuff
        self.has_sent_death = False
        self.received_death = False
        self.previous_opponent_score = None

        # Lists for items
        self.unlocked_sports = []
        self.unlocked_cups = []
        self.unlocked_sports_crystals = []
        self.unlocked_stages = []
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
        self.amount_debug: int = 5
        self.last_debug_messages = deque(maxlen=self.amount_debug)  # Stores up to 5 messages at a time at default

    def debug_log(self, message: str) -> None:
        if self.DEBUGGING:
            if message not in self.last_debug_messages:
                self.last_debug_messages.append(message)
                logger.info(f"[MSM Debug] {message}")

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(MSMContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            new_team = args["team"]
            new_slot = args["slot"]
            if self.team is not None and self.slot is not None and (self.team, self.slot) != (new_team, new_slot):
                # Clear before CommonContext handles Connected so it cannot send stale local checks for the new slot.
                self.reset_local_item_state(clear_received=True)
                self.reset_location_state()

        super().on_package(cmd, args)
        if cmd == "Connected":
            self.slot_data = args["slot_data"]

            # Goal Data
            self.goal_condition = self.slot_data["goal_condition"]
            self.behemoth_hp = self.slot_data["behemoth_hp"]
            self.behemoth_king_hp = self.slot_data["behemoth_king_hp"]
            #self.win_cups_amount = self.slot_data["win_cups_amount"]

            # Unlock Data
            self.hard_tournament_difficulty = self.slot_data["hard_tournament_difficulty"]
            self.sports_mix_unlock = self.slot_data["sports_mix_unlock"]

            # Deathlink Data
            self.deathlink_enabled = self.slot_data["deathlink"]
            self.deathlink_action = self.slot_data["deathlink_action"]
            self.deathlink_consequence = self.slot_data["deathlink_consequence"]
            self.deathlink_o_get_points = self.slot_data["deathlink_opponent_get_points"]
            self.deathlink_o_scores_points = self.slot_data["deathlink_opponent_scores_points"]
            self.deathlink_boss_recovered = self.slot_data["deathlink_boss_health_recovered"]
            self.deathlink_dodge_health_lost = self.slot_data["deathlink_dodgeball_health_lost"]

            # Sanity Data
            self.character_sanity = self.slot_data["character_sanity"]
            self.send_both_character_sanity = self.slot_data["send_both_character_sanity"]
            

            Utils.async_start(self.update_death_link(self.deathlink_enabled))

            self.load_consumed_item_indices()
            self.load_handled_locations()
            if self.locations_checked:
                Utils.async_start(
                    self.send_msgs([{"cmd": "LocationChecks", "locations": sorted(self.locations_checked)}])
                )

            generation_version = self.slot_data.get("version", "0.0.1")

            # Client World mismatch handler
            if CLIENT_VERSION in COMPATIBLE_VERSIONS:
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
                # A new room/seed must not inherit item or location state from the previous lobby.
                self.reset_local_item_state(clear_received=True)
                self.reset_location_state()
            self.seed = new_seed

            self.load_consumed_item_indices()

        elif cmd == "ReceivedItems":
            self.load_consumed_item_indices()
            start_index = args["index"]
            if start_index == 0:
                # CommonContext has just replaced items_received with the full inventory snapshot.
                # Keep that list and rebuild only the item-derived local state from it.
                self.reset_local_item_state(clear_consumed=False, clear_received=False)
            self.debug_log(
                f"ReceivedItems packet start={start_index}, count={len(args['items'])}, "
                f"queued={len(self.queued_consumable_indices)}, consumed={len(self.consumed_item_indices)}"
            )

            for offset, item in enumerate(args["items"]):
                item_index = start_index + offset
                if item_index in self.consumed_item_indices or item_index in self.queued_consumable_indices:
                    self.debug_log(f"Skipping already queued/consumed item index {item_index}")
                    continue

                item_id = item.item if hasattr(item, "item") else item[0]
                item_name = id_to_name.get(item_id)

                if not item_name:
                    self.debug_log(f"Skipping unknown item id {item_id} at index {item_index}")
                    continue

                # Add new one-shot item types here if they should wait for an in-match state before firing.
                # The queue stores (received index, name) so reconnects do not add the same item twice.

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

            Utils.async_start(self.handle_received_items())

    def make_gui(self):
        ui = super().make_gui()
        ui.base_title = "Archipelago Mario Sports Mix Client"
        return ui

    async def disconnect(self, allow_auto_reconnect: bool = False):
        self.game_interface.dolphin_client.disconnect()
        self.reset_game_session_state()
        await super().disconnect(allow_auto_reconnect)

    def update_connection_status(self):
        self.connection_state = self.game_interface.get_connection_state()

    def reset_game_session_state(self, game_active: bool = False) -> None:
        """Reset runtime-only state when the game process/title exits or restarts."""
        self.addresslib.reset_all_addresses()
        self.game_interface.addresslib.reset_all_addresses()
        self.start_process = True
        self.handled_gecko_codes = False
        self.one_time_running = False
        self.item_processed = False
        self.awaiting_use = False
        self.forced_item_id = None
        self.last_match_score_total = None
        self.suppress_panel_until = 0.0
        self.boss_hp_handled = False
        self.boss_defeat_handled = False
        self.in_tournament_match = False
        self.last_tournament_location_name = None
        self.has_sent_death = False
        self.received_death = False
        self.previous_opponent_score = None
        self.game_interface.current_tournament = None
        self.game_session_active = game_active
        self.active_game_version = dc.GAME_VERSION if game_active else None

    def get_consumed_item_storage_key(self) -> Optional[str]:
        if self.seed is None or self.team is None or self.slot is None:
            return None

        # Scope one-shot item state to the AP room and slot so traps/filler do not leak between lobbies.
        return f"{self.seed}_{self.team}_{self.slot}_consumed_items"

    def reset_local_item_state(self, clear_consumed: bool = True, clear_received: bool = False) -> None:
        if clear_received:
            self.items_received.clear()
        self.items_handled.clear()
        self.unlocked_sports.clear()
        self.unlocked_cups.clear()
        self.unlocked_sports_crystals.clear()
        self.unlocked_stages.clear()
        self.unlocked_characters.clear()
        self.unlocked_costumes.clear()
        self.unlocked_panel_items.clear()
        self.unlocked_abilities.clear()
        self.filler_to_give.clear()
        self.traps_to_give.clear()
        self.queued_consumable_indices.clear()

        if clear_consumed:
            self.consumed_item_indices.clear()
            self.consumed_item_storage_key = None

    def load_consumed_item_indices(self) -> None:
        storage_key = self.get_consumed_item_storage_key()
        if storage_key is None:
            self.debug_log("Consumable storage key is not ready yet")
            return
        key: str = storage_key
        if key == self.consumed_item_storage_key:
            return

        if self.consumed_item_storage_key is not None:
            self.debug_log(f"Switching consumable storage from {self.consumed_item_storage_key} to {key}")
            self.filler_to_give.clear()
            self.traps_to_give.clear()
            self.queued_consumable_indices.clear()
            self.consumed_item_indices.clear()

        # These are items that already fired in a previous client session.
        storage_category: Dict[str, list] = Utils.persistent_load().setdefault(CONSUMABLE_STORAGE_CATEGORY, {})
        self.consumed_item_indices.update(map(int, storage_category.get(key, [])))
        self.queued_consumable_indices.difference_update(self.consumed_item_indices)
        self.consumed_item_storage_key = key
        self.debug_log(f"Loaded {len(self.consumed_item_indices)} consumed consumable indices from storage")

    def mark_consumable_handled(self, item_index: Optional[int]) -> None:
        if item_index is None:
            return

        self.queued_consumable_indices.discard(item_index)
        if item_index in self.consumed_item_indices:
            self.debug_log(f"Consumable index {item_index} was already marked handled")
            return

        self.consumed_item_indices.add(item_index)
        self.debug_log(f"Marked consumable index {item_index} handled")

        storage_key = self.get_consumed_item_storage_key()
        if storage_key is not None:
            # Save after the Dolphin write/trap trigger, not when the item is first queued.
            self.consumed_item_storage_key = storage_key
            Utils.persistent_store(
                CONSUMABLE_STORAGE_CATEGORY,
                storage_key,
                sorted(self.consumed_item_indices),
            )
            self.debug_log(f"Saved {len(self.consumed_item_indices)} consumed consumable indices")
        else:
            self.debug_log("Handled consumable in memory only; storage key is not ready")

    def get_location_storage_key(self) -> Optional[str]:
        if self.seed is None or self.team is None or self.slot is None:
            return None

        # Scope location checks the same way AP scopes player state: generation, team, and slot.
        return f"{self.seed}_{self.team}_{self.slot}_checked_locations"

    def reset_location_state(self) -> None:
        self.locations_checked.clear()
        self.location_storage_key = None
        self.last_tournament_location_name = None

    def load_handled_locations(self) -> None:
        storage_key = self.get_location_storage_key()
        if storage_key is None:
            self.debug_log("Location storage key is not ready yet")
            return
        key: str = storage_key

        if key != self.location_storage_key:
            self.locations_checked.clear()

        storage_category: Dict[str, list] = Utils.persistent_load().setdefault(LOCATION_STORAGE_CATEGORY, {})
        saved_locations = set(map(int, storage_category.get(key, [])))
        server_locations = set(self.checked_locations)
        # Merge local checks with the server's known checks, then discard IDs this client no longer recognises.
        valid_locations = {
            location_id for location_id in saved_locations | server_locations
            if location_id in LOCATION_ID_TO_NAME
        }

        self.locations_checked.update(valid_locations)
        self.location_storage_key = key
        self.save_handled_locations()
        self.debug_log(f"Loaded {len(self.locations_checked)} handled locations from storage/server state")

    def save_handled_locations(self) -> None:
        storage_key = self.get_location_storage_key()
        if storage_key is None:
            self.debug_log("Handled locations in memory only; storage key is not ready")
            return

        self.location_storage_key = storage_key
        # Persist IDs rather than names so display text can change without breaking saved progress.
        Utils.persistent_store(
            LOCATION_STORAGE_CATEGORY,
            storage_key,
            sorted(self.locations_checked),
        )

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
            result = -1

        return result


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


        for network_item in self.items_received:
            item_id = network_item.item
            item_name = id_to_name.get(item_id)
            if network_item not in self.items_handled:
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

                if item_name.startswith("Sports Crystal:"):
                    self.unlocked_sports_crystals.append(item_name)
                    self.debug_log(f"Added {item_name} to unlocked_sports_crystals")

                elif item_name in stages_tuple:
                    self.unlocked_stages.append(item_name)
                    self.debug_log(f"Added {item_name} to unlocked_stages")

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

                self.items_handled.append(network_item)


        # Cups / Sports Mix
        await self.handle_cup_unlocks()
        await self.handle_sports_mix_unlock()

        # Stages
        await self.handle_stage_unlocks()

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
        # If they don't have the character item, character is locked
        if "Peach" not in self.unlocked_characters:
            value = 0
            return value

        value = 1
        if "Tennis-wear Peach" in self.unlocked_costumes: value += 4
        return value

    def daisy_unlocks_value(self):
        # If they don't have the character item, character is locked
        if "Daisy" not in self.unlocked_characters:
            value = 0
            return value

        value = 1
        if "Tennis-wear Daisy" in self.unlocked_costumes: value += 4
        return value

    def toad_unlocks_value(self):
        # If they don't have the character item, character is locked
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
        # If they don't have the character item, character is locked
        if "Slime" not in self.unlocked_characters:
            value = 0
            return value

        value = 1
        if "She-slime" in self.unlocked_costumes: value += 4
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


    # === Sports Mix ===


    async def handle_sports_mix_unlock(self):
        sports_mix_unlocked = get_address(SportsMixAddresses.sports_mix_unlocked)
        if self.sports_mix_unlock == 0:
            if "Sports Mix" in self.unlocked_sports:
                self.unlocked_sports_mix = True
                self.game_interface.dolphin_client.write_byte(sports_mix_unlocked, 11)
                self.debug_log("Sports Mix unlocked by Sports Mix item")

        elif self.sports_mix_unlock == 1:
            if ("Sports Crystal: Red" and "Sports Crystal: Green" and "Sports Crystal: Yellow" and
                    "Sports Crystal: Blue") in self.unlocked_sports_crystals:
                self.unlocked_sports_mix = True
                self.game_interface.dolphin_client.write_byte(sports_mix_unlocked, 11)
                self.debug_log("Sports Mix unlocked by Sports Crystals")


    # === Exhibition Unlocks ===


    async def handle_stage_unlocks(self):
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
            if stage[0] in self.unlocked_stages:
                value += 1

            # Second Stage
            # If the second stage is in unlocked stages, add 2
            if stage[1] in self.unlocked_stages:
                value += 2

            # Third Stage
            # If the third stage is in unlocked stages, add 4
            if stage[2] in self.unlocked_stages:
                value += 4

            # If no stages are unlocked (value is 0), set final_value to 8 which locks all stages, otherwise set
            # final value to value
            final_value = 8 if value == 0 else value

            new_addr = get_address(address)
            self.game_interface.dolphin_client.write_byte(new_addr, final_value)


    # === Ability Unlocks ===


    async def handle_unlocked_abilities(self):
        await self.handle_special_meter_unlock()

    async def handle_special_meter_unlock(self):
        if not self.game_interface.ready_to_handle():
            self.debug_log("Special meter lock waiting; game not ready")
            return

        try:
            special_meter = self.game_interface.dolphin_client.follow_pointers(self.addresslib.p_special_meter_addr,
                                                                            Offsets.Player.special_meter_offsets)
            self.debug_log(f"Special meter pointer resolved: base={self.addresslib.p_special_meter_addr:#x}, final={special_meter:#x}")
            if "Special Meter" not in self.unlocked_abilities:
                value = self.game_interface.dolphin_client.read_float(special_meter)
                self.debug_log(f"Special meter current value: {value}")
                if value != 0:
                    self.game_interface.dolphin_client.write_float(special_meter, 0.0)
                    verify_value = self.game_interface.dolphin_client.read_float(special_meter)
                    self.debug_log(f"Changed Special Meter to 0; verify={verify_value}")
            else:
                self.debug_log("Special meter unlocked; not locking meter")
        except Exception as e:
            self.debug_log(f"Special meter handling failed: {e}")


    # === Filler + ?-Panel Handling ===


    async def handle_one_time_items(self):
        # Queue empty? Nothing to do.
        if not self.filler_to_give:
            return

        self.debug_log(f"Filler queue pending: size={len(self.filler_to_give)}, first={self.filler_to_give[0]}")

        # Game not in a valid state? Wait until later.
        if not self.game_interface.ready_to_handle():
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
            self.mark_consumable_handled(item_index)
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
            self.mark_consumable_handled(item_index)
            return

        try:
            # Extract the integer ID (e.g., 0, 1, 2...)
            item_id = item_map[filler]
            self.forced_item_id = int(item_id)

            # Give the item
            self.game_interface.dolphin_client.write_word(self.addresslib.p_item_held_addr, self.forced_item_id)

            verify_item = self.current_item_func()
            logger.info(f"Dolphin Write Success: {filler}")
            self.mark_consumable_handled(item_index)
            self.debug_log(f"Wrote held item id {item_id} for {filler}; addr={self.addresslib.p_item_held_addr:#x}, verify={verify_item}")

        finally:
            self.one_time_running = False
            await asyncio.sleep(1)

    async def handle_replace_due_to_scoring(self):
        item_data = self.current_item_func()

        if item_data == -1 and self.game_interface.ready_to_handle():
            # Slot is empty, stop forcing
            self.awaiting_use = False
            self.forced_item_id = None

        elif self.awaiting_use and self.forced_item_id is not None and item_data != self.forced_item_id:
            # Game tried to overwrite our item, force it back
            self.game_interface.dolphin_client.write_word(self.addresslib.p_item_held_addr, self.forced_item_id)
            verify_item = self.current_item_func()
            self.debug_log(f"Forced item back to {self.forced_item_id}; previous={item_data}, verify={verify_item}")
            await asyncio.sleep(1)

    def current_match_score_total(self):
        player_score = sum(self.game_interface.dolphin_client.read_word(get_address(address)) for address in player_score_addresses)
        opponent_score = sum(self.game_interface.dolphin_client.read_word(get_address(address)) for address in opponent_score_addresses)
        return player_score + opponent_score

    def update_scoring_item_suppression(self):
        score_total = self.current_match_score_total()
        timer = self.game_interface.dolphin_client.read_byte(self.addresslib.timer_addr)

        if self.last_match_score_total is None:
            self.last_match_score_total = score_total
            return

        if score_total != self.last_match_score_total or (self.game_interface.check_sport() != "Volleyball" and timer == 0):
            self.last_match_score_total = score_total
            self.suppress_panel_until = asyncio.get_event_loop().time() + 3
            self.debug_log("Event Occurred; suppressing ?-panel item replacement briefly")

    def is_paused(self):
        value = self.game_interface.dolphin_client.read_byte(self.addresslib.paused_addr)
        if value == 1:
            return True
        else:
            return False

    async def handle_question_mark_panel_items(self):
        self.update_scoring_item_suppression()
        item_data = self.current_item_func()
        self.debug_log(f"Panel check: item={item_data}, unlocked={len(self.unlocked_panel_items)},"
                       f"awaiting={self.awaiting_use}, forced={self.forced_item_id}, processed={self.item_processed}")

        if asyncio.get_event_loop().time() < self.suppress_panel_until and self.game_interface.ready_to_handle():
            self.game_interface.dolphin_client.write_word(self.addresslib.p_item_held_addr, self.minus_one)
            verify_item = self.current_item_func()
            self.debug_log(f"Panel suppressed; cleared item at {self.addresslib.p_item_held_addr:#x}, verify={verify_item}")
            return

        # If we don't have an item, pause.
        if item_data == -1 and self.game_interface.ready_to_handle() and not self.is_paused():
            self.item_processed = False
            return

        # If we are currently forcing an item from a scoring replacement
        # or a one-time item, DO NOT let the ?-panel code claim credit for it.
        if self.awaiting_use or item_data == self.forced_item_id or self.item_processed:
            self.debug_log("Panel replacement skipped; forced/awaiting/processed state active")
            return

        # Standard pauses
        if self.one_time_running or not self.game_interface.ready_to_handle() or self.item_processed or self.is_paused():
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
        # This searches the keys of our map to find a match
        item_id = next((val for key, val in item_map.items() if key in random_item), None)


        if item_id is not None:
            item_id_int = int(item_id)
            self.game_interface.dolphin_client.write_word(self.addresslib.p_item_held_addr, item_id_int)
            verify_item = self.current_item_func()
            logger.info(f"?-Panel activated! Item replaced with {random_item}!")
            self.debug_log(f"Panel wrote item id {item_id_int}; addr={self.addresslib.p_item_held_addr:#x}, verify={verify_item}")
            self.item_processed = True
            self.awaiting_use = True
            self.forced_item_id = item_id_int
        else:
            self.debug_log(f"Panel selected {random_item}, but no item id matched")


    # === Trap Handling ===


    async def handle_traps(self):
        # If no traps in queue, bail
        if not self.traps_to_give:
            return

        if not self.game_interface.ready_to_handle():
            self.debug_log(f"Waiting to trigger trap; game not ready. Queue size: {len(self.traps_to_give)}")
            return

        # Add new traps here. If the trap has an item in items.py but not in this map, it will be skipped once.
        trap_mapping = {
            "Freeze Character 1 Trap": self.run_freeze_trap_1,
            "Freeze Character 2 Trap": self.run_freeze_trap_2,
            "Freeze Character 3 Trap": self.run_freeze_trap_3,
            "Coins Trap": self.opponent_coins,
            "Timer Trap": self.half_timer,
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
                random_int = randint(1,2)
                logger.info(f"2-on-2 detected! Sending trap to character {random_int}")
                redirected_trap = f"Freeze Character {random_int} Trap"
                asyncio.create_task(trap_mapping[redirected_trap]())
                self.debug_log(f"Redirected Freeze Character 3 to {redirected_trap}")
                self.mark_consumable_handled(item_index)
            else:
                asyncio.create_task(trap_mapping[trap]())
                self.debug_log(f"Started trap task for {trap}")
                self.mark_consumable_handled(item_index)
        else:
            logger.warning(f"Unknown trap item: {trap}")
            self.debug_log(f"Unknown trap {trap} consumed so it does not loop forever")
            self.mark_consumable_handled(item_index)

        # Prevents multiple traps from firing at the exact same millisecond
        await asyncio.sleep(0.5)

    async def run_freeze_trap_1(self):
        if not self.game_interface.ready_to_handle():
            return

        # 1. Get the actual memory addresses for X, Y, and Z
        # We do this ONCE before the loop starts
        addr_x = self.game_interface.dolphin_client.follow_pointers(self.addresslib.p_pos_addr, Offsets.Player.B1.Position.x_offsets)
        addr_y = self.game_interface.dolphin_client.follow_pointers(self.addresslib.p_pos_addr, Offsets.Player.B1.Position.y_offsets)
        addr_z = self.game_interface.dolphin_client.follow_pointers(self.addresslib.p_pos_addr, Offsets.Player.B1.Position.z_offsets)

        # Capture location
        freeze_x = self.game_interface.dolphin_client.read_float(addr_x)
        freeze_y = 0.1  # Setting it to 0 causes infinite spin glitch
        freeze_z = self.game_interface.dolphin_client.read_float(addr_z)

        self.debug_log(f"Freeze Trap 1 started at ({freeze_x}, {freeze_z})")

        # Set timer
        end_time = asyncio.get_event_loop().time() + 5.0

        # Freeze Loop
        while asyncio.get_event_loop().time() < end_time:
            # Write to THREE DIFFERENT addresses
            self.game_interface.dolphin_client.write_float(addr_x, freeze_x)
            self.game_interface.dolphin_client.write_float(addr_y, freeze_y)
            self.game_interface.dolphin_client.write_float(addr_z, freeze_z)

        self.debug_log("Freeze Trap 1 finished.")

    async def run_freeze_trap_2(self):
        if not self.game_interface.ready_to_handle():
            return

        addr_x = self.game_interface.dolphin_client.follow_pointers(self.addresslib.p_pos_addr, Offsets.Player.B2.Position.x_offsets)
        addr_y = self.game_interface.dolphin_client.follow_pointers(self.addresslib.p_pos_addr, Offsets.Player.B2.Position.y_offsets)
        addr_z = self.game_interface.dolphin_client.follow_pointers(self.addresslib.p_pos_addr, Offsets.Player.B2.Position.z_offsets)

        # Capture location
        freeze_x = self.game_interface.dolphin_client.read_float(addr_x)
        freeze_y = 0.1  # Setting it to 0 causes infinite spin glitch
        freeze_z = self.game_interface.dolphin_client.read_float(addr_z)

        self.debug_log(f"Freeze Trap 2 started at ({freeze_x}, {freeze_z})")

        # Set timer
        end_time = asyncio.get_event_loop().time() + 5.0

        # Freeze Loop
        while asyncio.get_event_loop().time() < end_time:
            # Write to THREE DIFFERENT addresses
            self.game_interface.dolphin_client.write_float(addr_x, freeze_x)
            self.game_interface.dolphin_client.write_float(addr_y, freeze_y)
            self.game_interface.dolphin_client.write_float(addr_z, freeze_z)

        self.debug_log("Freeze Trap 2 finished.")

    async def run_freeze_trap_3(self):
        if not self.game_interface.ready_to_handle():
            return

        addr_x = self.game_interface.dolphin_client.follow_pointers(self.addresslib.p_pos_addr, Offsets.Player.B3.Position.x_offsets)
        addr_y = self.game_interface.dolphin_client.follow_pointers(self.addresslib.p_pos_addr, Offsets.Player.B3.Position.y_offsets)
        addr_z = self.game_interface.dolphin_client.follow_pointers(self.addresslib.p_pos_addr, Offsets.Player.B3.Position.z_offsets)

        # Capture location
        freeze_x = self.game_interface.dolphin_client.read_float(addr_x)
        freeze_y = 0.1  # Setting it to 0 causes infinite spin glitch
        freeze_z = self.game_interface.dolphin_client.read_float(addr_z)

        self.debug_log(f"Freeze Trap 3 started at ({freeze_x}, {freeze_z})")

        # Set timer
        end_time = asyncio.get_event_loop().time() + 5.0

        # Freeze Loop
        while asyncio.get_event_loop().time() < end_time:
            # Write to THREE DIFFERENT addresses
            self.game_interface.dolphin_client.write_float(addr_x, freeze_x)
            self.game_interface.dolphin_client.write_float(addr_y, freeze_y)
            self.game_interface.dolphin_client.write_float(addr_z, freeze_z)

        self.debug_log("Freeze Trap 3 finished.")

    async def opponent_coins(self):
        if self.game_interface.ready_to_handle():
            current_coins = self.game_interface.dolphin_client.read_word(self.addresslib.o_coins_addr)
            random_int = randint(1,5)
            new_coins = current_coins + random_int
            # Coin count in MSM cannot go above 10
            final_coins = min(new_coins, 10)
            self.game_interface.dolphin_client.write_word(self.addresslib.o_coins_addr, final_coins)
            self.debug_log(f"Opponent coins set to {final_coins}")

    async def half_timer(self):
        if self.game_interface.ready_to_handle():
            current_time = self.game_interface.dolphin_client.read_float(self.addresslib.timer_addr)
            new_time = current_time / 2
            self.game_interface.dolphin_client.write_float(self.addresslib.timer_addr, new_time)
            self.debug_log(f"Timer cut in half to {new_time}")


    # === Goal/Boss Stuff ===


    # Need to wait until AtLeast gets put into AP 0.6.8
    # async def has_cup_goaled(self):
    #     cups_won_addresses = [CupsWonMultiple.Basketball, CupsWonMultiple.Dodgeball, CupsWonMultiple.Volleyball,
    #                           CupsWonMultiple.Hockey]
    #
    #     cups_won_total = sum(self.game_interface.dolphin_client.read_word(get_address(addr) for addr in cups_won_addresses))
    #
    #     if self.goal_condition == 3:
    #         if cups_won_total == self.win_cups_amount:
    #             await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
    #             self.debug_log(f"Goal Achieved: Win {self.win_cups_amount} Cups!")


    async def has_boss_goaled(self):
        """Check if the player has goaled in the boss, if their goal isn't that boss, send the check for it"""
        # If we already sent the goal or location check for the boss, stop running
        if self.boss_defeat_handled:
            return

        if self.game_interface.ready_to_handle():
            address_behemoth_hp = self.game_interface.dolphin_client.follow_pointers(self.addresslib.behemoth_hp_addr,
                                                                                     Offsets.Boss.behemoth_hp_offsets)

            # Behemoth Handling
            if self.is_behemoth:

                # Ensure pointer resolution didn't fail/return a bad address
                if address_behemoth_hp:
                    behemoth_hp = self.game_interface.dolphin_client.read_float(address_behemoth_hp)

                    if behemoth_hp is not None and behemoth_hp <= 0:
                        self.boss_defeat_handled = True  # Lock execution immediately

                        if self.goal_condition == 0:
                            await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                            self.debug_log("Goal Achieved: Defeated Behemoth!")
                        else:
                            await self.check_location("Defeated Behemoth!")

            # Behemoth King Handling
            elif self.is_behemoth_king:

                if address_behemoth_hp:
                    behemoth_hp = self.game_interface.dolphin_client.read_float(address_behemoth_hp)

                    if behemoth_hp is not None and behemoth_hp <= 0:
                        self.boss_defeat_handled = True  # Lock execution immediately

                        if self.goal_condition == 1:
                            await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                            self.debug_log("Goal Achieved: Defeated Behemoth King!")
                        else:
                            await self.check_location("Defeated Behemoth King!")

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

        if current_stage == "s20VO":
            if match_status == 2:
                self.boss_hp_handled = False

    async def handle_boss_hp(self):
        """Change the boss' HP depending on what boss it is and their custom health set"""

        if not self.boss_hp_handled and self.game_interface.ready_to_handle():
            max_behemoth_hp = self.game_interface.dolphin_client.follow_pointers(self.addresslib.behemoth_hp_addr,
                                                                                 Offsets.Boss.max_hp_offsets)
            behemoth_hp = self.game_interface.dolphin_client.follow_pointers(self.addresslib.behemoth_hp_addr,
                                                                             Offsets.Boss.behemoth_hp_offsets)
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

    async def handle_lock_behemoth_hp(self):
        """Locks the Behemoth health and Special Meter charge if in a behemoth fight without Behemoth Stage"""

        if not self.in_tournament_match or self.game_interface.match_status() != 0 or not self.game_interface.ready_to_handle():
            return

        required_stage = "Behemoth Stage"
        if self.is_behemoth:
            boss = "Behemoth"
        elif self.is_behemoth_king:
            boss = "Behemoth King"
        else:
            boss = None

        if required_stage in self.unlocked_stages:
            return

        if boss is None:
            self.debug_log("Could not find boss, set to None")
            return

        self.debug_log(f"Locked points for {boss}, you do not have {required_stage}")

        try:
            self.lock_behemoth_hp()
            self.lock_special_meter()
        finally:
            pass

    def lock_behemoth_hp(self):
        """Function to lock Behemoth Health, called in handle_lock_behemoth_hp"""

        behemoth_hp = self.game_interface.dolphin_client.follow_pointers(self.addresslib.behemoth_hp_addr,
                                                                         Offsets.Boss.behemoth_hp_offsets)
        value = self.game_interface.dolphin_client.read_float(behemoth_hp)
        if self.is_behemoth:
            if value != self.behemoth_hp:
                self.game_interface.dolphin_client.write_float(behemoth_hp, self.behemoth_hp)

        if self.is_behemoth_king:
            if value != self.behemoth_king_hp:
                self.game_interface.dolphin_client.write_float(behemoth_hp, self.behemoth_king_hp)


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

        self.locations_checked.add(location_id)
        self.save_handled_locations()
        self.debug_log(f"Checked location: {location_name}")
        await self.send_msgs([{"cmd": "LocationChecks", "locations": [location_id]}])

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
        difficulty = self.game_interface.get_exhibition_difficulty()

        if stage is None or sport is None or difficulty is None:
            return

        location_name = f"{sport} Ex: Beat {stage} ({difficulty})"
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

    async def handle_locked_tournament_stage_points(self):
        """Locks the points in a tournament match if you don't have the required cup or stage"""

        if not self.in_tournament_match or self.game_interface.match_status() != 0 or not self.game_interface.ready_to_handle():
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

        if required_stage in self.unlocked_stages and required_cup in self.unlocked_cups:
            return

        if required_stage not in self.unlocked_stages and required_cup not in self.unlocked_cups:
            logger.info(f"Blocked points for {sport} {cup} Round {round_number}. Missing {required_stage} & {required_cup}")
        elif required_stage not in self.unlocked_stages:
            logger.info(f"Blocked points for {sport} {cup} Round {round_number}. Missing {required_stage}")
        elif required_cup not in self.unlocked_cups:
            logger.info(f"Blocked points for {sport} {cup}. Missing {required_cup}")

        try:
            self.clear_player_score()
            self.lock_special_meter()
        finally:
            pass

    def clear_player_score(self):
        """Locks the player's score at 0"""

        for address in player_score_addresses:
            if self.game_interface.dolphin_client.read_word(address) != 0:
                self.game_interface.dolphin_client.write_word(address, 0)

    def lock_special_meter(self):
        """Locks the player's special meter at 0"""

        special_meter = self.game_interface.dolphin_client.follow_pointers(self.addresslib.p_special_meter_addr,
                                                                           Offsets.Player.special_meter_offsets)
        value = self.game_interface.dolphin_client.read_float(special_meter)

        if value != 0:
            self.game_interface.dolphin_client.write_float(special_meter, 0)

    # --- Sanity Location Handling ---


    async def send_character_sanity_checks(self):
        """Handles sending checks for Character Sanity"""

        if self.character_sanity == 0:
            return

        if not self.game_interface.ready_to_handle():
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

        if self.send_both_character_sanity and self.character_sanity == 2:
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
                    await self.check_location(f"Play as {character}")
        elif self.game_interface.check_player_amount() == 3:
            for character in [char_1, char_2, char_3]:
                if character != "None":
                    await self.check_location(f"Play as {character}")

    async def send_costume_character_sanity(self, char_1, char_2, char_3, costume_1, costume_2, costume_3):
        """Sends the location for the costume if Character Sanity is enabled"""

        characters_2 = [char_1, char_2]
        costumes_2 = [costume_1, costume_2]
        characters_3 = [char_1, char_2, char_3]
        costumes_3 = [costume_1, costume_2, costume_3]

        if self.game_interface.check_player_amount() == 2:
            for character, costume_byte in zip(characters_2, costumes_2):

                if character in costume_database and costume_byte not in (0, 255) and character != "None":
                    costume_db = costume_database[character]

                    # Fetch the string name
                    costume_name = costume_db.get(costume_byte, costume_db.get(1))

                    if costume_name:
                        await self.check_location(f"Play as {costume_name}")

        elif self.game_interface.check_player_amount() == 3:
            for character, costume_byte in zip(characters_3, costumes_3):

                if character in costume_database and costume_byte not in (0, 255) and character != "None":
                    costume_db = costume_database[character]

                    # Fetch the string name
                    costume_name = costume_db.get(costume_byte, costume_db.get(1))

                    if costume_name:
                        await self.check_location(f"Play as {costume_name}")

    # === Deathlink Stuff ===

    # Sending Deathlink
    async def handle_send_deathlink(self):
        """Gets awaited during in match and sends a deathlink depending on what the deathlink_action is"""

        possible_messages_0 = ["lost the match!", "isn't good enough!", "has a MASSIVE skill issue!",
                             "needs to take a break...", "couldn't sport their mix..."]

        possible_messages_1 = ["got DUNKED on!", "can't handle the heat!",]

        match_status = self.game_interface.dolphin_client.read_byte(self.addresslib.match_status_addr)

        if self.deathlink_enabled:

            # Lose Match Action
            if self.deathlink_action == 0:
                if (match_status == 2 or match_status == 3) and not self.received_death:
                    if not self.has_sent_death and self.slot is not None:
                        message = random.choice(possible_messages_0) # Pick a random message to send
                        await self.send_death(f"{self.player_names[self.slot]} {message}")
                        self.has_sent_death = True
                        self.debug_log("Sent deathlink due to losing the match")

                if match_status == 0:
                    self.has_sent_death = False


            # Every number of Points Action
            elif self.deathlink_action == 1:

                # Dodgeball logic
                if self.game_interface.check_sport() == "Dodgeball":
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
        # Reset our tracker to the new lower score and return False.
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
        self.debug_log("Deathlink Received")
        self.handle_received_deathlink()

    def handle_received_deathlink(self):
        """Gets called when on_deathlink goes off and acts depending on deathlink_consequence
        NOTE: Dodgeball deathlinks get handled differently to everything else since it doesn't have a normal scoring system"""

        if self.deathlink_enabled:
            if self.game_interface.ready_to_handle():
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
                            self.game_interface.dolphin_client.write_byte(addr, 100) # Write 100 for all scores
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

                            offsets = [Offsets.Player.B1.dodge_damage,
                                       Offsets.Player.B2.dodge_damage,
                                       Offsets.Player.B3.dodge_damage,]

                            addr = get_address(PlayerAddresses.dodge_damage)
                            final_addr = self.game_interface.dolphin_client.follow_pointers(addr, offsets[random_char])
                            curr_damage = self.game_interface.dolphin_client.read_word(final_addr)
                            new_damage = curr_damage + self.deathlink_dodge_health_lost
                            self.game_interface.dolphin_client.write_word(final_addr, new_damage)
                            health = 100 - new_damage
                            # Find current the character selected by randint
                            chars = [PlayerAddresses.character_1,
                                     PlayerAddresses.character_2,
                                     PlayerAddresses.character_3,]

                            value = self.game_interface.dolphin_client.read_byte(chars[random_char])
                            character = char_to_id.get(value)

                            logger.info(f"Watch out! It may not look like it, but {character} is on {health} HP!")

    def recover_boss_hp(self):
        """Calculates the amount of HP recovered when sent a deathlink"""

        if self.is_behemoth:
            health_recovered = (self.deathlink_boss_recovered / 100) * self.behemoth_hp
            current_health = self.game_interface.dolphin_client.read_float(self.addresslib.behemoth_hp_addr)
            new_health = current_health + health_recovered
            self.game_interface.dolphin_client.write_float(self.addresslib.behemoth_hp_addr, new_health)
        elif self.is_behemoth_king:
            health_recovered = (self.deathlink_boss_recovered / 100) * self.behemoth_king_hp
            current_health = self.game_interface.dolphin_client.read_float(self.addresslib.behemoth_hp_addr)
            new_health = current_health + health_recovered
            self.game_interface.dolphin_client.write_float(self.addresslib.behemoth_hp_addr, new_health)


    # === Misc stuff idk where to put ===


    async def dolphin_sync_task(self) -> None:
        """The main loop managing the connection to Dolphin and game-state logic routing"""


        while not self.exit_event.is_set():
            try:
                if not self.game_interface.dolphin_client.is_hooked_class():
                    if self.game_session_active:
                        self.reset_game_session_state()
                    await self.game_interface.dolphin_client.attempt_to_hook()

                if self.game_interface.dolphin_client.is_hooked_class():
                    if not self.game_interface.dolphin_client.check_region():
                        if self.game_session_active:
                            self.reset_game_session_state()
                        await asyncio.sleep(1)
                        continue

                    if not self.game_session_active or self.active_game_version != dc.GAME_VERSION:
                        self.reset_game_session_state(game_active=True)

                # Ensure we are connected to the AP Server first
                if not self.server or not self.server.socket or self.server.socket.closed:
                    message = "Waiting for player to connect to Archipelago server..."
                    self.start_process = True
                    if self.last_error_message != message:
                        logger.info(message)
                        self.last_error_message = message
                    await asyncio.sleep(1)
                    continue

                if self.game_interface.dolphin_client.is_hooked_class() and self.start_process and self.slot:
                    unlock_ex_tabs()
                    self.start_process = False

                # Ensure we have received slot data
                if not self.slot:
                    await asyncio.sleep(1)
                    continue

                # Reset error message once connected
                self.last_error_message = None


                connection_state = self.game_interface.get_connection_state()
                self.update_connection_status()

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

    async def stop_stupid_games_played_notifs(self):
        """Stop SOME of the unlock messages from appearing constantly"""

        basket_played = BasketballAddresses.games_played
        dodge_played = DodgeballAddresses.games_played
        volley_played = VolleyballAddresses.games_played
        hockey_played = HockeyAddresses.games_played
        address_list = [basket_played, dodge_played, volley_played, hockey_played]

        for address in address_list:
            value = self.game_interface.dolphin_client.read_word(address)
            if value != 0:
                self.game_interface.dolphin_client.write_word(address, 0)

    async def handle_gecko_codes(self):
        """Handle the gecko code patches for each region"""

        current_module = self.game_interface.dolphin_client.follow_pointers(self.addresslib.current_module_addr,
                                                                            Offsets.Match.current_module_offsets)
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


    # === Where to handle what ===


    async def handle_in_match(self):
        """What functions should be handled during a match"""
        # Cup Goal - Need to wait for AP 0.6.8
        #await self.has_cup_goaled()

        # Deathlink
        await self.handle_send_deathlink()

        # Lock points if you don't have the stage/cup
        await self.handle_locked_tournament_stage_points()

        # Locations
        await self.handle_exhibition_win()
        await self.handle_cup_round_win()
        await self.send_character_sanity_checks()

        # Items
        await self.handle_one_time_items()
        await self.handle_replace_due_to_scoring()
        await self.handle_traps()
        await self.handle_question_mark_panel_items()
        await self.handle_unlocked_abilities()

        if self.game_interface.ready_to_handle():
            self.debug_log("Ready To Handle!")
        else:
            self.debug_log("Not ready to handle...")

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
        await self.handle_replace_due_to_scoring()
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
        
        await asyncio.sleep(0.1)


    async def handle_in_main_menu(self):
        """What functions should be handled in the main menu"""
        #await self.has_cup_goaled()

        await self.handle_received_items()
        await self.check_pending_tournament_location()
        await self.stop_stupid_games_played_notifs()
        await unlock_tournament_tabs_option(self, self.hard_tournament_difficulty, self.unlocked_sports_mix)

        await self.handle_gecko_codes()

        self.has_sent_death = False

        self.forced_item_id = None

        self.in_tournament_match = False
        self.boss_hp_handled = False
        self.is_behemoth = False
        self.is_behemoth_king = False
        self.game_interface.current_tournament = None

        await asyncio.sleep(0.1)
