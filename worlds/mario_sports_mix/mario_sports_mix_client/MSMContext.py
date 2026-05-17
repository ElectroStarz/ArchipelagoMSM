import asyncio
import logging
import random
import traceback
from collections import deque
from random import randint
from typing import Dict, Set

import Utils
from CommonClient import ClientCommandProcessor, CommonContext
from NetUtils import ClientStatus
from . import MSMFunctions
from .MSMInterface import *
from ..items import item_table
from ..locations import LOCATION_NAME_TO_ID

id_to_name = {data.code: name for name, data in item_table.items()}
CLIENT_VERSION = "0.0.1"


status_messages = {
    ConnectionState.IN_MATCH: "In match",
    ConnectionState.IN_BOSS: "In boss",
    ConnectionState.IN_MENU: "In main menu",
    ConnectionState.DISCONNECTED: "Unable to connect to the Dolphin instance, attempting to reconnect...",
    ConnectionState.CONNECTED: "Connected to Dolphin!",
    ConnectionState.IN_TOURNAMENT_MAP: "In tournament map",
    ConnectionState.GOALED: "Goaled game!"
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

player_score_addresses = [
    PlayerAddresses.Score.score_period_1,
    PlayerAddresses.Score.score_period_2,
    PlayerAddresses.Score.score_period_3,
    PlayerAddresses.Score.score_period_4,
    PlayerAddresses.Score.score_period_5,
]


logger = logging.getLogger("Client")
CONSUMABLE_STORAGE_CATEGORY = "mario_sports_mix_client"
DEBUGGING = False
last_debug_message = None


def debug_log(message: str) -> None:
    global last_debug_message
    if DEBUGGING:
        if message != last_debug_message:
            last_debug_message = message
            logger.info(f"[MSM Debug] {message}")


class MSMCommandProcessor(ClientCommandProcessor):
    ctx: "MSMContext"

    def __init__(self, ctx: "MSMContext"):
        super().__init__(ctx)

    @staticmethod
    def _cmd_debug_mode(*args):
        """Toggle debugging on and off (Default off)"""
        global DEBUGGING

        if not DEBUGGING:
            DEBUGGING = True
            logger.info("Debugging on")
            debug_log("This is what a debug message will look like!")
        else:
            DEBUGGING = False
            logger.info("Debugging off")

    def _cmd_status(self):
        """Display the current dolphin connection status."""
        logger.info(f"Connection Status: {status_messages[self.ctx.connection_state]}")

    def _cmd_unlocked_characters(self):
        """Display what characters you have unlocked."""
        unlocked_characters = self.ctx.unlocked_characters
        final_items = []
        if unlocked_characters:
            for char in unlocked_characters:
                final_items.append(char.replace("Character: ", ""))
            logger.info(f"Unlocked Characters: {final_items}")
        else:
            logger.info("No unlocked characters")

    def _cmd_unlocked_costumes(self):
        """Display what costumes you have unlocked"""
        unlocked_costumes = self.ctx.unlocked_costumes
        final_items = []
        if unlocked_costumes:
            for costume in unlocked_costumes:
                final_items.append(costume.replace("Costume: ", ""))
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
                final_items.append(item.replace("Stage: ", ""))
            logger.info(f"Unlocked Stages: {final_items}")
        else:
            logger.info("No unlocked stages")

    def _cmd_unlocked_abilities(self):
        """Display what abilities you have unlocked."""
        unlocked_abilities = self.ctx.unlocked_abilities
        final_items = []
        if unlocked_abilities:
            for ability in unlocked_abilities:
                final_items.append(ability.replace("Ability: ", ""))
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

                # Now that we have the string, perform the replacement
                final_items.append(item_name.replace("Trap: ", ""))

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
    locations_handled = []
    last_error_message: Optional[str] = None

    slot_data: Dict[str, Utils.Any] = {}
    sports_mix_unlock = int
    behemoth_hp = float
    behemoth_king_hp = float
    is_behemoth = False
    is_behemoth_king = False
    goal_condition = int

    # Sanity stuff
    special_sanity = False
    court_sanity = int
    score_sanity = False
    score_sanity_max = int
    score_sanity_points_req = int
    team_sanity = int

    def __init__(self, server_address: str, password: str):
        super().__init__(server_address, password)
        self.game_interface = MSMInterface(logger)
        self.command_processor.ctx = self
        self.items_received = []
        self.items_handled = []
        self.locations_handled = []
        self.seed: Optional[str] = None

        # Consumables use AP's received-item index as their ID. Keep these as indices, not item names
        # because duplicate filler and trap items are allowed but each copy should only fire once.
        self.queued_consumable_indices: Set[int] = set()
        self.consumed_item_indices: Set[int] = set()
        self.consumed_item_storage_key: Optional[str] = None


        self.start_process = True
        self.one_time_running = False
        self.item_processed = False
        self.awaiting_use = False
        self.forced_item_id = None
        self.boss_hp_handled = False
        self.boss_defeat_handled = False
        self.in_tournament_match = False
        self.last_tournament_location_name: Optional[str] = None
        self.current_item = None
        self.test = False
        self.minus_one = 0xFFFFFFFF


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

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(MSMContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        super().on_package(cmd, args)
        if cmd == "Connected":
            self.slot_data = args["slot_data"]

            # Goal Data
            self.goal_condition = self.slot_data["goal_condition"]
            self.behemoth_hp = self.slot_data["behemoth_hp"]
            self.behemoth_king_hp = self.slot_data["behemoth_king_hp"]

            # Unlock Data
            self.sports_mix_unlock = self.slot_data["sports_mix_unlock"]

            self.load_consumed_item_indices()

            generation_version = self.slot_data.get("version", "0.0.0")

            if CLIENT_VERSION != generation_version:
                logger.error(
                    f"\n=========================================\n"
                    f"VERSION MISMATCH DETECTED!\n"
                    f"Your Client version: {CLIENT_VERSION}\n"
                    f"Seed was generated on version: {generation_version}\n"
                    f"Please update your client or regenerate the seed as things may break!\n"
                    f"========================================="
                )
            else:
                logger.info(f"Version check passed! (v{CLIENT_VERSION})")

        elif cmd == "RoomInfo":
            self.seed = args.get("seed_name", "unknown")
            self.load_consumed_item_indices()

        elif cmd == "ReceivedItems":
            self.load_consumed_item_indices()
            start_index = args["index"]
            debug_log(
                f"ReceivedItems packet start={start_index}, count={len(args['items'])}, "
                f"queued={len(self.queued_consumable_indices)}, consumed={len(self.consumed_item_indices)}"
            )

            for offset, item in enumerate(args["items"]):
                item_index = start_index + offset
                if item_index in self.consumed_item_indices or item_index in self.queued_consumable_indices:
                    debug_log(f"Skipping already queued/consumed item index {item_index}")
                    continue

                item_id = item.item if hasattr(item, "item") else item[0]
                item_name = id_to_name.get(item_id)

                if not item_name:
                    debug_log(f"Skipping unknown item id {item_id} at index {item_index}")
                    continue

                # Add new one-shot item types here if they should wait for an in-match state before firing.
                # The queue stores (received index, name) so reconnects do not add the same item twice.
                if item_name.startswith("1"):
                    self.filler_to_give.append((item_index, item_name))
                    self.queued_consumable_indices.add(item_index)
                    logger.info(f"Queued filler: {item_name}")
                    debug_log(f"Filler queue size is now {len(self.filler_to_give)}")


                elif item_name.startswith("Trap"):
                    self.traps_to_give.append((item_index, item_name))
                    self.queued_consumable_indices.add(item_index)
                    logger.info(f"Queued trap: {item_name}")
                    debug_log(f"Trap queue size is now {len(self.traps_to_give)}")

            Utils.async_start(self.handle_received_items())

    def make_gui(self):
        ui = super().make_gui()
        ui.base_title = "Archipelago Mario Sports Mix Client"
        return ui

    async def disconnect(self, allow_auto_reconnect: bool = False):
        self.game_interface.dolphin_client.disconnect()
        await super().disconnect(allow_auto_reconnect)

    def update_connection_status(self):
        self.connection_state = self.game_interface.get_connection_state()

    def get_consumed_item_storage_key(self) -> Optional[str]:
        if self.seed is None or self.team is None or self.slot is None:
            return None

        # Keep this scoped to the slot. Reusing a save/client on another seed should not inherit old traps.
        return f"{self.seed}_{self.team}_{self.slot}_consumed_items"

    def load_consumed_item_indices(self) -> None:
        storage_key = self.get_consumed_item_storage_key()
        if storage_key is None:
            debug_log("Consumable storage key is not ready yet")
            return
        key: str = storage_key
        if key == self.consumed_item_storage_key:
            return

        if self.consumed_item_storage_key is not None:
            debug_log(f"Switching consumable storage from {self.consumed_item_storage_key} to {key}")
            self.filler_to_give.clear()
            self.traps_to_give.clear()
            self.queued_consumable_indices.clear()
            self.consumed_item_indices.clear()

        # These are items that already fired in a previous client session.
        storage_category: Dict[str, list] = Utils.persistent_load().setdefault(CONSUMABLE_STORAGE_CATEGORY, {})
        self.consumed_item_indices.update(map(int, storage_category.get(key, [])))
        self.queued_consumable_indices.difference_update(self.consumed_item_indices)
        self.consumed_item_storage_key = key
        debug_log(f"Loaded {len(self.consumed_item_indices)} consumed consumable indices from storage")

    def mark_consumable_handled(self, item_index: Optional[int]) -> None:
        if item_index is None:
            return

        self.queued_consumable_indices.discard(item_index)
        if item_index in self.consumed_item_indices:
            debug_log(f"Consumable index {item_index} was already marked handled")
            return

        self.consumed_item_indices.add(item_index)
        debug_log(f"Marked consumable index {item_index} handled")

        storage_key = self.get_consumed_item_storage_key()
        if storage_key is not None:
            # Save after the Dolphin write/trap trigger, not when the item is first queued.
            self.consumed_item_storage_key = storage_key
            Utils.persistent_store(
                CONSUMABLE_STORAGE_CATEGORY,
                storage_key,
                sorted(self.consumed_item_indices),
            )
            debug_log(f"Saved {len(self.consumed_item_indices)} consumed consumable indices")
        else:
            debug_log("Handled consumable in memory only; storage key is not ready")

    def current_item_func(self):
        current_item = self.game_interface.dolphin_client.read_byte(PlayerAddresses.item_held)
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
        prefix = ("Basketball:", "Dodgeball:", "Volleyball:", "Hockey:", "Sports Mix:")

        for network_item in self.items_received:
            item_id = network_item.item
            item_name = id_to_name.get(item_id)
            if network_item not in self.items_handled:
                if item_name is None:
                    continue

                if item_name.startswith("Sport:"):
                    self.unlocked_sports.append(item_name)
                    debug_log(f"Added {item_name} to unlocked_sports")

                elif item_name.startswith(prefix):
                    self.unlocked_cups.append(item_name)
                    debug_log(f"Added {item_name} to unlocked_cups")

                elif item_name.startswith("Sports Crystal:"):
                    self.unlocked_sports_crystals.append(item_name)
                    debug_log(f"Added {item_name} to unlocked_sports_crystals")

                elif item_name.startswith("Stage:"):
                    self.unlocked_stages.append(item_name)
                    debug_log(f"Added {item_name} to unlocked_stages")

                elif item_name.startswith("Character:"):
                    self.unlocked_characters.append(item_name)
                    debug_log(f"Added {item_name} to unlocked_characters")

                elif item_name.startswith("Costume:"):
                    self.unlocked_costumes.append(item_name)
                    debug_log(f"Added {item_name} to unlocked_costumes")

                elif item_name.startswith("?"):
                    self.unlocked_panel_items.append(item_name)
                    debug_log(f"Added {item_name} to unlocked_panel_items")

                elif item_name.startswith("Ability:"):
                    self.unlocked_abilities.append(item_name)
                    debug_log(f"Added {item_name} to unlocked_abilities")

                self.items_handled.append(network_item)


        # Cups / Sports Mix
        await self.handle_cup_unlocks(self.unlocked_cups)
        await self.handle_sports_mix_unlock(self.unlocked_sports, self.unlocked_sports_crystals)

        # Stages
        await self.handle_stage_unlocks(self.unlocked_stages)

        # Characters
        await self.handle_all_characters(self.unlocked_characters, self.unlocked_costumes)

        # Traps + Filler aren't here because they can only be received in game and this function gets awaited during
        # every connection state, if you were to receive a trap or filler in the menu it wouldn't work.

    # Can't make this yet until there's a way to lock sports
    #async def handle_unlocked_sports(self, unlocked_sports):


    # === Character Unlocks ===


    async def handle_all_characters(self, unlocked_characters, unlocked_costumes):
        for char in character_names:
            # Format character name for value
            item_name = f"Character: {char.replace('_', ' ').title()}"

            # Have separate values for characters with costumes, adding values can equal different combinations
            if char == "yoshi":
                value = self.yoshi_unlocks_value(unlocked_characters, unlocked_costumes)
            elif char == "peach":
                value = self.peach_unlocks_value(unlocked_characters, unlocked_costumes)
            elif char == "daisy":
                value = self.daisy_unlocks_value(unlocked_characters, unlocked_costumes)
            elif char == "toad":
                value = self.toad_unlocks_value(unlocked_characters, unlocked_costumes)
            elif char == "ninja":
                value = self.ninja_unlocks_value(unlocked_characters, unlocked_costumes)
            elif char == "white_mage":
                value = self.white_mage_unlocks_value(unlocked_characters, unlocked_costumes)
            elif char == "black_mage":
                value = self.black_mage_unlocks_value(unlocked_characters, unlocked_costumes)
            elif char == "slime":
                value = self.slime_unlocks_value(unlocked_characters, unlocked_costumes)
            else:
                # Else, value is 1 if the item name is in characters, if not it's 0
                value = 1 if item_name in unlocked_characters else 0


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
                    self.game_interface.dolphin_client.write_byte(addr, value)
                except AttributeError:
                    print(f"Warning: {char} not found in {sport.__name__}!")

    @staticmethod
    def yoshi_unlocks_value(unlocked_characters, unlocked_costumes):
        # If they don't have the character item, character is locked
        if "Character: Yoshi" not in unlocked_characters:
            value = 0
            return value
        else:

            value = 1
            if "Costume: Pink Yoshi" in unlocked_costumes: value += 4
            if "Costume: Light Blue Yoshi" in unlocked_costumes: value += 16
            if "Costume: Yellow Yoshi" in unlocked_costumes: value += 64
        return value

    @staticmethod
    def peach_unlocks_value(unlocked_characters, unlocked_costumes):
        # If they don't have the character item, character is locked
        if "Character: Peach" not in unlocked_characters:
            value = 0
            return value

        value = 1
        if "Costume: Tennis-wear Peach" in unlocked_costumes: value += 4
        return value

    @staticmethod
    def daisy_unlocks_value(unlocked_characters, unlocked_costumes):
        # If they don't have the character item, character is locked
        if "Character: Daisy" not in unlocked_characters:
            value = 0
            return value

        value = 1
        if "Costume: Tennis-wear Daisy" in unlocked_costumes: value += 4
        return value

    @staticmethod
    def toad_unlocks_value(unlocked_characters, unlocked_costumes):
        # If they don't have the character item, character is locked
        if "Character: Toad" not in unlocked_characters:
            value = 0
            return value

        value = 1
        if "Costume: Blue Toad" in unlocked_costumes: value += 4
        if "Costume: Green Toad" in unlocked_costumes: value += 16
        if "Costume: Yellow Toad" in unlocked_costumes: value += 64
        return value

    @staticmethod
    def ninja_unlocks_value(unlocked_characters, unlocked_costumes):
        if "Character: Ninja" not in unlocked_characters:
            value = 0
            return value

        value = 1
        if "Costume: Shadow White Ninja" in unlocked_costumes: value += 4
        return value

    @staticmethod
    def white_mage_unlocks_value(unlocked_characters, unlocked_costumes):
        if "Character: White Mage" not in unlocked_characters:
            value = 0
            return value

        value = 1
        if "Costume: Pure White - White Mage" in unlocked_costumes: value += 4
        return value

    @staticmethod
    def black_mage_unlocks_value(unlocked_characters, unlocked_costumes):
        if "Character: Black Mage" not in unlocked_characters:
            value = 0
            return value

        value = 1
        if "Costume: Magic Red Black Mage" in unlocked_costumes: value += 4
        return value

    @staticmethod
    def slime_unlocks_value(unlocked_characters, unlocked_costumes):
        # If they don't have the character item, character is locked
        if "Character: Slime" not in unlocked_characters:
            value = 0
            return value

        value = 1
        if "Costume: She-slime" in unlocked_costumes: value += 4
        if "Costume: Metal Slime" in unlocked_costumes: value += 16
        return value


    # === Cup Unlocks ===


    async def handle_cup_unlocks(self, unlocked_cups):
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

        for address, cups in cup_mapping.items():
            value = 0

            # Mushroom Cup
            # If the Mushroom Cup is in unlocked cups, add 1
            if cups[0] in unlocked_cups:
                value += 1

            # Flower Cup
            # If the Flower Cup is in unlocked cups, add 2
            if cups[1] in unlocked_cups:
                value += 2

            # Star Cup
            # If the Star Cup is in unlocked cups, add 4
            if cups[2] in unlocked_cups:
                value += 4

            # If no cups are unlocked (value is 0), set final_value to 8 which locks all cups, otherwise set
            # final value to value
            final_value = 8 if value == 0 else value

            self.game_interface.dolphin_client.write_byte(address, final_value)


    # === Exhibition Unlocks ===

    async def handle_stage_unlocks(self, unlocked_stages):
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
            b_mushroom: ["Stage: Mario Stadium", "Stage: Koopa Troopa Beach", "Stage: DK Dock"],
            b_flower: ["Stage: Luigi's Mansion", "Stage: Western Junction", "Stage: Daisy Garden"],
            b_star: ["Stage: Bowser Jr. Blvd.", "Stage: Bowser's Castle", "Stage: Star Ship"],
            b_block: ["Stage: Peach's Castle", "Stage: Wario Factory", "Stage: Ghoulish Galleon"],

            # Volleyball
            v_mushroom: ["Stage: Mario Stadium", "Stage: Koopa Troopa Beach", "Stage: Peach's Castle"],
            v_flower: ["Stage: DK Dock", "Stage: Luigi's Mansion", "Stage: Western Junction"],
            v_star: ["Stage: Bowser Jr. Blvd.", "Stage: Bowser's Castle", "Stage: Star Ship"],
            v_block: ["Stage: Wario Factory", "Stage: Waluigi Pinball", "Stage: Ghoulish Galleon"],

            # Dodgeball
            d_mushroom: ["Stage: Mario Stadium", "Stage: Koopa Troopa Beach", "Stage: Peach's Castle"],
            d_flower: ["Stage: DK Dock", "Stage: Toad Park", "Stage: Daisy Garden"],
            d_star: ["Stage: Wario Factory", "Stage: Bowser's Castle", "Stage: Star Ship"],
            d_block: ["Stage: Western Junction", "Stage: Waluigi Pinball", "Stage: Ghoulish Galleon"],

            # Hockey
            h_mushroom: ["Stage: Mario Stadium", "Stage: Toad Park", "Stage: Peach's Castle"],
            h_flower: ["Stage: Western Junction", "Stage: Wario Factory", "Stage: Daisy Garden"],
            h_star: ["Stage: Bowser Jr. Blvd.", "Stage: Waluigi Pinball", "Stage: Star Ship"],
            h_block: ["Stage: Koopa Troopa Beach", "Stage: Ghoulish Galleon", "Stage: Bowser's Castle"],
        }

        for address, stages in stage_mapping.items():
            value = 0

            # First Stage
            # If the first stage is in unlocked stages, add 1
            if stages[0] in unlocked_stages:
                value += 1

            # Second Stage
            # If the second stage is in unlocked stages, add 2
            if stages[1] in unlocked_stages:
                value += 2

            # Third Stage
            # If the third stage is in unlocked stages, add 4
            if stages[2] in unlocked_stages:
                value += 4

            # If no stages are unlocked (value is 0), set final_value to 8 which locks all stages, otherwise set
            # final value to value
            final_value = 8 if value == 0 else value

            self.game_interface.dolphin_client.write_byte(address, final_value)


    # === Sports Mix ===


    async def handle_sports_mix_unlock(self, unlocked_sports, unlocked_sports_crystals):
        if self.sports_mix_unlock == 0:
            if "Sport: Sports Mix" in unlocked_sports:
                self.game_interface.dolphin_client.write_byte(SportsMixAddresses.sports_mix_unlocked, 11)
                debug_log("Sports Mix unlocked by Sports Mix item")

        elif self.sports_mix_unlock == 1:
            if ("Sports Crystal: Red" and "Sports Crystal: Green" and "Sports Crystal: Yellow" and
                    "Sports Crystal: Blue") in unlocked_sports_crystals:
                self.game_interface.dolphin_client.write_byte(SportsMixAddresses.sports_mix_unlocked, 11)
                debug_log("Sports Mix unlocked by Sports Crystals")


    # === Ability Unlocks ===


    async def handle_unlocked_abilities(self):
        await self.handle_special_meter_unlock(self.unlocked_abilities)

    async def handle_special_meter_unlock(self, unlocked_abilities):
        if self.game_interface.ready_to_handle():

            special_meter = self.game_interface.dolphin_client.follow_pointers(PlayerAddresses.special_meter,
                                                                                Offsets.Player.special_meter_offsets)
            # If you don't have the special meter, if the value isn't 0, set it to 0
            if "Ability: Special Meter" not in unlocked_abilities:
                value = self.game_interface.dolphin_client.read_float(special_meter)
                if value != 0.0:
                    self.game_interface.dolphin_client.write_byte(special_meter, 0.0)
                    debug_log("Changed Special Meter to 0.0")
            elif "Ability: Special Meter" in unlocked_abilities:
                pass


    # === Filler + ?-Panel Handling ===


    async def handle_one_time_items(self, filler_to_give):
        # Queue empty? Nothing to do.
        if not filler_to_give:
            return

        # Game not in a valid state? Wait until later.
        if not self.game_interface.ready_to_handle():
            debug_log(f"Waiting to give filler; game not ready. Queue size: {len(filler_to_give)}")
            return

        queued_filler = filler_to_give[0]
        if isinstance(queued_filler, tuple):
            item_index, filler = queued_filler
        else:
            item_index = None
            filler = queued_filler

        # Player already has an item? Don't overwrite it.
        if filler != "1 Coin" and self.current_item_func() != -1:
            debug_log(f"Waiting to give {filler}; player already has an item")
            return

        # Prevent question mark panel replacement while giving item
        self.one_time_running = True
        self.awaiting_use = True

        # Take the oldest queued filler item
        filler_to_give.popleft()
        logger.info(f"Processing from Queue: {filler}")
        debug_log(f"Processing filler index={item_index}, remaining filler queue={len(filler_to_give)}")

        # Coins are handled here because they do not use the item slot.
        if filler == "1 Coin":
            current_coins = self.game_interface.dolphin_client.read_word(PlayerAddresses.Score.coins)

            new_coins = min(current_coins + 1, 10)

            self.game_interface.dolphin_client.write_word(PlayerAddresses.Score.coins, new_coins)

            logger.info(f"Gave 1 Coin ({new_coins}/10)")
            debug_log(f"Coins changed from {current_coins} to {new_coins}")
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

            # FIX: Make absolutely sure we save the INTEGER id, not the string name!
            self.forced_item_id = int(item_id)

            # Give the item
            self.game_interface.dolphin_client.write_word(PlayerAddresses.item_held, self.forced_item_id)

            logger.info(f"Dolphin Write Success: {filler}")
            self.mark_consumable_handled(item_index)
            debug_log(f"Wrote held item id {item_id} for {filler}")

        finally:
            await asyncio.sleep(1)
            self.one_time_running = False

    async def handle_replace_due_to_scoring(self):
        item_data = self.current_item_func()

        if item_data == -1:
            # Slot is empty, stop forcing
            self.awaiting_use = False
            self.forced_item_id = None

        elif self.awaiting_use and item_data != self.forced_item_id:
            # Game tried to overwrite our item, force it back
            self.game_interface.dolphin_client.write_word(PlayerAddresses.item_held, self.forced_item_id)
            debug_log(f"Forced item back to {self.forced_item_id}")
            await asyncio.sleep(1)

    async def handle_question_mark_panel_items(self, unlocked_panel_items):
        item_data = self.current_item_func()
        # If we don't have an item, pause.
        if item_data == -1:
            self.item_processed = False
            return

        # If we are currently forcing an item from a scoring replacement
        # or a one-time item, DO NOT let the ?-panel code claim credit for it.
        if self.awaiting_use and (item_data == self.forced_item_id or self.item_processed):
            return

        # Standard pauses
        if self.one_time_running or not self.game_interface.ready_to_handle() or self.item_processed:
            return

        # Handle Empty List
        if not unlocked_panel_items:
            #
            self.game_interface.dolphin_client.write_word(PlayerAddresses.item_held, self.minus_one)
            debug_log("There are no items available, replaced with -1 (self.minus_one)")
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
        random_item = random.choice(unlocked_panel_items)

        # Extract the base name (e.g., if item is "1 Banana", get "Banana")
        # This searches the keys of our map to find a match
        item_id = next((val for key, val in item_map.items() if key in random_item), None)


        if item_id is not None:
            item_id_int = int(item_id)
            self.game_interface.dolphin_client.write_word(PlayerAddresses.item_held, item_id_int)
            logger.info(f"?-Panel activated! Item replaced with {random_item}!")
            self.item_processed = True
            self.awaiting_use = True
            self.forced_item_id = item_id_int


    # === Trap Handling ===


    async def handle_traps(self, traps_to_give):
        # If no traps in queue, bail
        if not traps_to_give:
            return

        if not self.game_interface.ready_to_handle():
            debug_log(f"Waiting to trigger trap; game not ready. Queue size: {len(traps_to_give)}")
            return

        # Add new traps here. If the trap has an item in items.py but not in this map, it will be skipped once.
        trap_mapping = {
            "Trap: Freeze Character 1": self.run_freeze_trap_1,
            "Trap: Freeze Character 2": self.run_freeze_trap_2,
            "Trap: Freeze Character 3": self.run_freeze_trap_3,
            "Trap: Opponent Coins": self.opponent_coins,
            "Trap: 1/2 Time": self.half_timer,
        }

        queued_trap = traps_to_give.popleft()
        if isinstance(queued_trap, tuple):
            item_index, trap = queued_trap
        else:
            item_index = None
            trap = queued_trap

        logger.info(f"Triggering {trap}")
        debug_log(f"Processing trap index={item_index}, remaining trap queue={len(traps_to_give)}")

        # Handle Function-based traps
        if trap in trap_mapping:
            # If the trap is to freeze character 3, but we're only playing 2-on-2, send trap to either char 1 or 2
            if trap == "Trap: Freeze Character 3" and self.game_interface.check_player_amount() == 2:
                random_int = randint(1,2)
                logger.info(f"2-on-2 detected! Sending trap to character {random_int}")
                redirected_trap = f"Trap: Freeze Character {random_int}"
                asyncio.create_task(trap_mapping[redirected_trap]())
                debug_log(f"Redirected Freeze Character 3 to {redirected_trap}")
                self.mark_consumable_handled(item_index)
            else:
                asyncio.create_task(trap_mapping[trap]())
                debug_log(f"Started trap task for {trap}")
                self.mark_consumable_handled(item_index)
        else:
            logger.warning(f"Unknown trap item: {trap}")
            debug_log(f"Unknown trap {trap} consumed so it does not loop forever")
            self.mark_consumable_handled(item_index)

        # Prevents multiple traps from firing at the exact same millisecond
        await asyncio.sleep(0.5)

    async def run_freeze_trap_1(self):
        if not self.game_interface.ready_to_handle():
            return

        # 1. Get the actual memory addresses for X, Y, and Z
        # We do this ONCE before the loop starts
        addr_x = self.game_interface.dolphin_client.follow_pointers(PlayerAddresses.Position.pos,
                                                                    Offsets.Player.B1.Position.x_offsets)
        addr_y = self.game_interface.dolphin_client.follow_pointers(PlayerAddresses.Position.pos,
                                                                    Offsets.Player.B1.Position.y_offsets)
        addr_z = self.game_interface.dolphin_client.follow_pointers(PlayerAddresses.Position.pos,
                                                                    Offsets.Player.B1.Position.z_offsets)

        # Capture location
        freeze_x = self.game_interface.dolphin_client.read_float(addr_x)
        freeze_y = 0.1  # Setting it to 0 causes infinite spin glitch
        freeze_z = self.game_interface.dolphin_client.read_float(addr_z)

        debug_log(f"Freeze Trap 1 started at ({freeze_x}, {freeze_z})")

        # Set timer
        end_time = asyncio.get_event_loop().time() + 5.0

        # Freeze Loop
        while asyncio.get_event_loop().time() < end_time:
            # Write to THREE DIFFERENT addresses
            self.game_interface.dolphin_client.write_float(addr_x, freeze_x)
            self.game_interface.dolphin_client.write_float(addr_y, freeze_y)
            self.game_interface.dolphin_client.write_float(addr_z, freeze_z)

        debug_log("Freeze Trap 1 finished.")

    async def run_freeze_trap_2(self):
        if not self.game_interface.ready_to_handle():
            return

        addr_x = self.game_interface.dolphin_client.follow_pointers(PlayerAddresses.Position.pos,
                                                                    Offsets.Player.B2.Position.x_offsets)
        addr_y = self.game_interface.dolphin_client.follow_pointers(PlayerAddresses.Position.pos,
                                                                    Offsets.Player.B2.Position.y_offsets)
        addr_z = self.game_interface.dolphin_client.follow_pointers(PlayerAddresses.Position.pos,
                                                                    Offsets.Player.B2.Position.z_offsets)

        # Capture location
        freeze_x = self.game_interface.dolphin_client.read_float(addr_x)
        freeze_y = 0.1  # Setting it to 0 causes infinite spin glitch
        freeze_z = self.game_interface.dolphin_client.read_float(addr_z)

        debug_log(f"Freeze Trap 2 started at ({freeze_x}, {freeze_z})")

        # Set timer
        end_time = asyncio.get_event_loop().time() + 5.0

        # Freeze Loop
        while asyncio.get_event_loop().time() < end_time:
            # Write to THREE DIFFERENT addresses
            self.game_interface.dolphin_client.write_float(addr_x, freeze_x)
            self.game_interface.dolphin_client.write_float(addr_y, freeze_y)
            self.game_interface.dolphin_client.write_float(addr_z, freeze_z)

        debug_log("Freeze Trap 2 finished.")

    async def run_freeze_trap_3(self):
        if not self.game_interface.ready_to_handle():
            return

        addr_x = self.game_interface.dolphin_client.follow_pointers(PlayerAddresses.Position.pos,
                                                                    Offsets.Player.B3.Position.x_offsets)
        addr_y = self.game_interface.dolphin_client.follow_pointers(PlayerAddresses.Position.pos,
                                                                    Offsets.Player.B3.Position.y_offsets)
        addr_z = self.game_interface.dolphin_client.follow_pointers(PlayerAddresses.Position.pos,
                                                                    Offsets.Player.B3.Position.z_offsets)

        # Capture location
        freeze_x = self.game_interface.dolphin_client.read_float(addr_x)
        freeze_y = 0.1  # Setting it to 0 causes infinite spin glitch
        freeze_z = self.game_interface.dolphin_client.read_float(addr_z)

        debug_log(f"Freeze Trap 3 started at ({freeze_x}, {freeze_z})")

        # Set timer
        end_time = asyncio.get_event_loop().time() + 5.0

        # Freeze Loop
        while asyncio.get_event_loop().time() < end_time:
            # Write to THREE DIFFERENT addresses
            self.game_interface.dolphin_client.write_float(addr_x, freeze_x)
            self.game_interface.dolphin_client.write_float(addr_y, freeze_y)
            self.game_interface.dolphin_client.write_float(addr_z, freeze_z)

        debug_log("Freeze Trap 3 finished.")

    async def opponent_coins(self):
        if self.game_interface.ready_to_handle():
            current_coins = self.game_interface.dolphin_client.read_word(OpponentAddresses.Score.coins)
            random_int = randint(1,5)
            new_coins = current_coins + random_int
            # Coin count in MSM cannot go above 10
            final_coins = min(new_coins, 10)
            self.game_interface.dolphin_client.write_word(OpponentAddresses.Score.coins, final_coins)
            debug_log(f"Opponent coins set to {final_coins}")

    async def half_timer(self):
        if self.game_interface.ready_to_handle():
            current_time = self.game_interface.dolphin_client.read_float(MatchAddresses.time_remaining)
            self.game_interface.dolphin_client.write_float(MatchAddresses.time_remaining, current_time / 2)
            debug_log("Timer cut in half")


    # === Boss Stuff ===


    async def has_goaled(self):
        # If we already sent the goal or location check for the boss, stop running
        if self.boss_defeat_handled:
            return

        # Behemoth Handling
        if self.is_behemoth:
            address_behemoth_hp = self.game_interface.dolphin_client.follow_pointers(
                BossAddresses.behemoth_hp, Offsets.Boss.behemoth_hp_offsets
            )

            # Ensure pointer resolution didn't fail/return a bad address
            if address_behemoth_hp:
                behemoth_hp = self.game_interface.dolphin_client.read_float(address_behemoth_hp)

                if behemoth_hp is not None and behemoth_hp <= 0:
                    self.boss_defeat_handled = True  # Lock execution immediately

                    if self.goal_condition == 0:
                        await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                        debug_log("Goal Achieved: Defeated Behemoth!")
                    else:
                        await self.check_location("Defeated Behemoth!")

        # Behemoth King Handling
        if self.is_behemoth_king:
            address_behemoth_hp = self.game_interface.dolphin_client.follow_pointers(
                BossAddresses.behemoth_hp, Offsets.Boss.behemoth_hp_offsets
            )

            if address_behemoth_hp:
                behemoth_hp = self.game_interface.dolphin_client.read_float(address_behemoth_hp)

                if behemoth_hp is not None and behemoth_hp <= 0:
                    self.boss_defeat_handled = True  # Lock execution immediately

                    if self.goal_condition == 1:
                        await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                        debug_log("Goal Achieved: Defeated Behemoth King!")
                    else:
                        await self.check_location("Defeated Behemoth King!")

    async def check_boss_type(self):
        is_sports_mix = self.game_interface.check_sports_mix()
        current_stage = self.game_interface.dolphin_client.read_string(MatchAddresses.current_stage)
        match_status = self.game_interface.dolphin_client.read_byte(MatchAddresses.match_status)

        if current_stage == "s20VO":
            if is_sports_mix:
                self.is_behemoth_king = True
                self.is_behemoth = False
                debug_log("Behemoth King Found")
            else:
                self.is_behemoth_king = False
                self.is_behemoth = True
                debug_log("Behemoth Found")

        if current_stage == "s20VO":
            if match_status == 2:
                self.boss_hp_handled = False

    async def handle_boss_hp(self):
        if not self.boss_hp_handled and self.game_interface.ready_to_handle():
            max_behemoth_hp = self.game_interface.dolphin_client.follow_pointers(BossAddresses.behemoth_hp,
                                                                                 Offsets.Boss.max_hp_offsets)
            behemoth_hp = self.game_interface.dolphin_client.follow_pointers(BossAddresses.behemoth_hp,
                                                                             Offsets.Boss.behemoth_hp_offsets)
            if self.is_behemoth:
                self.game_interface.dolphin_client.write_float(max_behemoth_hp, self.behemoth_hp)
                self.game_interface.dolphin_client.write_float(behemoth_hp, self.behemoth_hp)
                debug_log(f"Behemoth HP set to {self.behemoth_hp}")
                self.boss_hp_handled = True
            elif self.is_behemoth_king:
                self.game_interface.dolphin_client.write_float(max_behemoth_hp, self.behemoth_king_hp)
                self.game_interface.dolphin_client.write_float(behemoth_hp, self.behemoth_king_hp)
                debug_log(f"Behemoth King HP set to {self.behemoth_king_hp}")
                self.boss_hp_handled = True

    async def handle_lock_behemoth_hp(self):
        if not self.in_tournament_match or self.game_interface.match_status() != 0 or not self.game_interface.ready_to_handle():
            return

        required_stage = "Stage: Behemoth Stage"
        if self.is_behemoth:
            boss = "Behemoth"
        elif self.is_behemoth_king:
            boss = "Behemoth King"
        else:
            boss = None

        if required_stage in self.unlocked_stages:
            return

        if boss is None:
            debug_log("Could not find boss, set to None")
            return

        debug_log(f"Locked points for {boss}, you do not have {required_stage}")

        try:
            self.lock_behemoth_hp()
            self.lock_special_meter()
        finally:
            pass

    def lock_behemoth_hp(self):
        behemoth_hp = self.game_interface.dolphin_client.follow_pointers(BossAddresses.behemoth_hp,
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
        location_id = LOCATION_NAME_TO_ID.get(location_name)

        if location_id is None:
            debug_log(f"No AP location found: {location_name}")
            return

        if location_id in self.locations_checked:
            return

        self.locations_checked.add(location_id)
        self.locations_handled.append(location_name)
        debug_log(f"Checked location: {location_name}")
        await self.send_msgs([{"cmd": "LocationChecks", "locations": [location_id]}])

    def get_tournament_cup_and_round(self, sport: str, stage_code: str):
        current_cup = self.game_interface.current_tournament

        if current_cup in tournament_round_stages.get(sport, {}):
            stages = tournament_round_stages[sport][current_cup]
            if stage_code in stages:
                return current_cup, stages.index(stage_code) + 1

            debug_log(f"Stage {stage_code} was not found in current tournament cup {current_cup}")
            return None, None

        for cup, stages in tournament_round_stages.get(sport, {}).items():
            if stage_code in stages:
                return cup, stages.index(stage_code) + 1

        return None, None

    def get_current_cup_location_name(self) -> Optional[str]:
        current_stage = self.game_interface.dolphin_client.read_string(MatchAddresses.current_stage)

        stage_code = current_stage[:3]
        sports_mix_activated = self.game_interface.check_sports_mix()
        sport = self.game_interface.check_sport()


        if stage_code == "s20":
            debug_log(f"Stage {stage_code} is Behemoth Stage, separate function handles that.")
            return None

        if sport is None:
            debug_log(f"Could not build cup location from stage={current_stage}, sport={sport}")
            return None

        cup, round_number = self.get_tournament_cup_and_round(sport, stage_code)

        if cup is None or round_number is None:
            debug_log(f"Could not find tournament cup/round for sport={sport}, stage_code={stage_code}")
            return None

        difficulty = self.game_interface.get_tournament_difficulty(cup)

        if difficulty is None and not sports_mix_activated:
            debug_log(f"Could not find tournament difficulty for cup={cup}")
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
        debug_log(f"Sending pending tournament location: {location_name}")
        await self.check_location(location_name)

    async def handle_exhibition_win(self):
        # Already marked as tournament
        if self.in_tournament_match:
            return

        # If Sports Mix is running, standard Exhibition checks shouldn't fire
        if self.game_interface.check_sports_mix():
            return

        current_stage = self.game_interface.dolphin_client.read_string(MatchAddresses.current_stage)
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
        current_stage = self.game_interface.dolphin_client.read_string(MatchAddresses.current_stage)
        stage_code = current_stage[:3]

        # Check standard bracket maps first
        cup = tournament_map_cups.get(stage_code)
        if cup is not None:
            self.game_interface.current_tournament = cup
            self.in_tournament_match = True
            debug_log(f"Current tournament cup set to {cup} via map screen.")
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
                    debug_log(
                        f"Sports Mix Match Detected! Locking tournament mode. Cup: {possible_cup}, Stage: {stage_code}")
                    return

    async def handle_cup_round_win(self):
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
        if not self.in_tournament_match or self.game_interface.match_status() != 0 or not self.game_interface.ready_to_handle():
            return

        current_stage = self.game_interface.dolphin_client.read_string(MatchAddresses.current_stage)
        stage_code = current_stage[:3]
        stage = stage_names.get(stage_code)
        sports_mix_activated = self.game_interface.check_sports_mix()
        sport = self.game_interface.check_sport()


        if stage is None or sport is None:
            debug_log(f"Could not check tournament stage unlock for stage={current_stage}")
            return

        cup, round_number = self.get_tournament_cup_and_round(sport, stage_code)

        if cup is None or round_number is None:
            debug_log(f"Could not check locked tournament points for sport={sport}, stage_code={stage_code}")
            return

        difficulty = self.game_interface.get_tournament_difficulty(cup)
        required_stage = f"Stage: {stage}"
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
        for address in player_score_addresses:
            if self.game_interface.dolphin_client.read_word(address) != 0:
                self.game_interface.dolphin_client.write_word(address, 0)

    def lock_special_meter(self):
        special_meter = self.game_interface.dolphin_client.follow_pointers(PlayerAddresses.special_meter,
                                                                           Offsets.Player.special_meter_offsets)
        value = self.game_interface.dolphin_client.read_float(special_meter)

        if value != 0.0:
            self.game_interface.dolphin_client.write_float(special_meter, 0.0)


    # === Misc stuff idk where to put ===


    async def dolphin_sync_task(self) -> None:
        """
        The main loop managing the connection to Dolphin and game-state logic routing.
        """

        while not self.exit_event.is_set():
            try:
                if not self.game_interface.dolphin_client.is_hooked_class():
                    await self.game_interface.dolphin_client.attempt_to_hook()

                # Ensure we are connected to the AP Server first
                if not self.server or not self.server.socket or self.server.socket.closed:
                    message = "Waiting for player to connect to Archipelago server..."
                    self.start_process = True
                    if self.last_error_message != message:
                        logger.info("Make sure you have backed up your save file!")
                        logger.info(message)
                        self.last_error_message = message
                    await asyncio.sleep(1)
                    continue

                if self.game_interface.dolphin_client.is_hooked_class() and self.start_process and self.slot:
                    MSMFunctions.unlock_tabs()
                    logger.info("Unlocked tabs!")
                    MSMFunctions.lock_all_cups()
                    logger.info("Locked cups!")
                    MSMFunctions.lock_all_stages()
                    logger.info("Locked stages!")
                    MSMFunctions.lock_all_characters()
                    logger.info("Locked characters!")
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
        # Stop unlock messages from appearing constantly
        basket_played = BasketballAddresses.games_played
        dodge_played = DodgeballAddresses.games_played
        volley_played = VolleyballAddresses.games_played
        hockey_played = HockeyAddresses.games_played
        address_list = [basket_played, dodge_played, volley_played, hockey_played]

        for address in address_list:
            value = self.game_interface.dolphin_client.read_word(address)
            if value != 0:
                self.game_interface.dolphin_client.write_word(address, 0)


    # === Where to handle what ===


    async def handle_in_match(self):
        # Lock points if you don't have the stage/cup
        await self.handle_locked_tournament_stage_points()

        # Locations
        await self.handle_exhibition_win()
        await self.handle_cup_round_win()

        # Items
        await self.handle_one_time_items(self.filler_to_give)
        await self.handle_replace_due_to_scoring()
        await self.handle_traps(self.traps_to_give)
        await self.handle_question_mark_panel_items(self.unlocked_panel_items)
        await self.handle_unlocked_abilities()

        await asyncio.sleep(0.1)

    async def handle_in_boss(self):
        await self.handle_boss_hp()
        await self.check_boss_type()
        await self.handle_lock_behemoth_hp()
        await self.has_goaled()

        # Items
        await self.handle_one_time_items(self.filler_to_give)
        await self.handle_replace_due_to_scoring()
        await self.handle_traps(self.traps_to_give)
        await self.handle_question_mark_panel_items(self.unlocked_panel_items)
        await self.handle_unlocked_abilities()


    async def handle_in_tournament_map(self):
        await self.check_current_cup()
        await self.check_pending_tournament_location()
        await asyncio.sleep(0.1)

    async def handle_in_main_menu(self):
        await self.check_pending_tournament_location()
        self.in_tournament_match = False
        self.boss_hp_handled = False
        self.game_interface.current_tournament = None
        await self.handle_received_items()
        await self.stop_stupid_games_played_notifs()

        await asyncio.sleep(0.1)
