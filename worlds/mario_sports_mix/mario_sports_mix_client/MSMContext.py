import random
from random import randint
from typing import Dict, Optional
import Utils
from CommonClient import ClientCommandProcessor, CommonContext
from NetUtils import ClientStatus
import logging
import traceback

from . import MSMFunctions
from .MSMInterface import *
from ..items import item_table
id_to_name = {data.code: name for name, data in item_table.items()}


status_messages = {
    ConnectionState.IN_MATCH: "In match",
    ConnectionState.IN_MENU: "In main menu",
    ConnectionState.DISCONNECTED: "Unable to connect to the Dolphin instance, attempting to reconnect...",
    ConnectionState.CONNECTED: "Connected to Dolphin!",
    ConnectionState.IN_TOURNAMENT_MAP: "In tournament map",
    ConnectionState.GOALED: "Goaled game!"
}


dol_status_connected = "Dolphin is connected!"
dol_status_lost = "Dolphin connection was lost! Is the emulator running? Is MSM loaded?"
dol_status_no_game = "Dolphin failed to connect! Load Mario Sports Mix (PAL)!"


character_names = [
    "mario", "luigi", "peach", "daisy", "yoshi", "wario", "waluigi",
    "donkey_kong", "diddy_kong", "toad", "bowser", "bowser_jr",
    "moogle", "white_mage", "black_mage", "ninja", "cactuar", "slime"
]

logger = logging.getLogger("Client")

# Check if a function is running
async def track_running_state(func):
    async def wrapper(*args, **kwargs):
        wrapper.is_running = True
        try:
            return func(*args, **kwargs)
        finally:
            wrapper.is_running = False

    wrapper.is_running = False
    return wrapper()

class MSMCommandProcessor(ClientCommandProcessor):
    ctx: "MSMContext"

    def __init__(self, ctx: "MSMContext"):
        super().__init__(ctx)

    def _cmd_status(self):
        """Display the current dolphin connection status."""
        logger.info(f"Connection Status: {status_messages[self.ctx.connection_state]}")

    def _cmd_unlocked_cups(self):
        """Display what cups you have unlocked."""
        if self.ctx.unlocked_normal_cups is not None:
            for cup in self.ctx.unlocked_normal_cups and self.ctx.unlocked_hard_cups and self.ctx.unlocked_sports_mix_cups:
                logger.info(f"Unlocked {cup.replace("Stage:", "")}")
        else:
            logger.info("No unlocked stages")

    def _cmd_unlocked_stages(self):
        """Display what stages you have unlocked."""
        if self.ctx.unlocked_stages is not None:
            for stage in self.ctx.unlocked_stages:
                logger.info(f"Unlocked {stage.replace("Stage:", "")}")
        else:
            logger.info("No unlocked stages")

    def _cmd_unlocked_abilities(self):
        """Display what abilities you have unlocked."""
        if self.ctx.unlocked_abilities is not None:
            for ability in self.ctx.unlocked_abilities:
                logger.info(f"Unlocked {ability.replace("Ability:", "")}")
        else:
            logger.info("No unlocked abilities")

    def _cmd_test(self):
        """Test functions"""
        match_s = self.ctx.game_interface.match_status()
        sport = self.ctx.game_interface.check_sport()
        ex = self.ctx.game_interface.check_ex_difficulty()
        cup = self.ctx.game_interface.check_cup()
        t = self.ctx.game_interface.check_t_difficulty()
        list_s = [match_s, sport, ex, cup, t]
        # for item in list_s:
        #     logger.info(f"{item}")
        logger.info(f"Match status: {match_s}")
        logger.info(f"Sport: {sport}")
        logger.info(f"Exhibition: {ex}")
        logger.info(f"Cup: {cup}")
        logger.info(f"Tournament: {t}")


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
    sports_mix_unlock = Any
    behemoth_hp = float
    behemoth_king_hp = float
    is_behemoth = False
    is_behemoth_king = False
    goal_condition = int

    # Sanity stuff
    special_sanity = False
    court_sanity = Any
    score_sanity = False
    score_sanity_max = int
    score_sanity_points_req = int
    team_sanity = False

    # Item stuff
    # unlocked_sports = []
    # unlocked_normal_cups = []
    # unlocked_hard_cups = []
    # unlocked_sports_mix_cups = []
    # unlocked_sports_crystals = []
    # unlocked_stages = []
    # unlocked_characters = []
    # unlocked_costumes = []
    # unlocked_panel_items = []
    # unlocked_abilities = []
    # filler_to_give = []
    # traps_to_give = []

    def __init__(self, server_address: str, password: str):
        super().__init__(server_address, password)
        self.game_interface = MSMInterface(logger)
        self.command_processor.ctx = self
        self.items_received = []
        self.items_handled = []
        self.locations_handled = []
        self.seed: Optional[str] = None
        self.last_received_index = int
        self.start_process = True
        self.one_time_running = False
        self.item_processed = False

        # Lists for items
        self.unlocked_sports = []
        self.unlocked_normal_cups = []
        self.unlocked_hard_cups = []
        self.unlocked_sports_mix_cups = []
        self.unlocked_sports_crystals = []
        self.unlocked_stages = []
        self.unlocked_characters = []
        self.unlocked_costumes = []
        self.unlocked_panel_items = []
        self.unlocked_abilities = []
        self.filler_to_give = []
        self.traps_to_give = []

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(MSMContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        super().on_package(cmd, args)
        if cmd == "Connected":
            self.slot_data = args["slot_data"]
            self.goal_condition = self.slot_data["goal_condition"]
            self.behemoth_hp = self.slot_data["behemoth_hp"]
            self.behemoth_king_hp = self.slot_data["behemoth_king_hp"]

            self.sports_mix_unlock = self.slot_data["sports_mix_unlock"]

            # Sanity data
            self.special_sanity = self.slot_data["special_sanity"]



            # Sync index with Dolphin if we are currently in-game
            if self.connection_state == ConnectionState.IN_MATCH:
                pass
            else:
                self.last_received_index = -1

        elif cmd == "RoomInfo":
            self.seed = args.get("seed_name", "unknown")


        elif cmd == "ReceivedItems":
            current_index = args["index"]

            for item in args["items"]:

                # Ensure we haven't already processed this specific index
                if current_index >= self.last_received_index:
                    self.items_received.append(item)
                    self.last_received_index = current_index + 1
                    #print(self.items_received)

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

    # === Item Receiving ===

    async def handle_received_items(self):
        prefix = ("Basketball:", "Dodgeball:", "Volleyball:", "Hockey:")

        for network_item in self.items_received:
            item_id = network_item.item
            item_name = id_to_name.get(item_id)
            if network_item not in self.items_handled:
                if item_name is None:
                    continue

                if item_name.startswith("Sport:"):
                    self.unlocked_sports.append(item_name)
                    self.items_handled.append(network_item)
                elif item_name.startswith(prefix):
                    if "Normal" in item_name:
                        self.unlocked_normal_cups.append(item_name)
                        self.items_handled.append(network_item)
                    elif "Hard" in item_name:
                        self.unlocked_hard_cups.append(item_name)
                        self.items_handled.append(network_item)
                elif item_name.startswith("Sports Mix:"):
                    self.unlocked_sports_mix_cups.append(item_name)
                    self.items_handled.append(network_item)
                elif item_name.startswith("Sports Crystal:"):
                    self.unlocked_sports_crystals.append(item_name)
                    self.items_handled.append(network_item)
                elif item_name.startswith("Stage:"):
                    self.unlocked_stages.append(item_name)
                    self.items_handled.append(network_item)
                elif item_name.startswith("Character:"):
                    self.unlocked_characters.append(item_name)
                    self.items_handled.append(network_item)
                elif item_name.startswith("Costume:"):
                    self.unlocked_costumes.append(item_name)
                    self.items_handled.append(network_item)
                elif item_name.startswith("?"):
                    self.unlocked_panel_items.append(item_name)
                    self.items_handled.append(network_item)
                elif item_name.startswith("Ability:"):
                    self.unlocked_abilities.append(item_name)
                    self.items_handled.append(network_item)
                elif item_name.startswith("1"):
                    self.filler_to_give.append(item_name)
                elif item_name.startswith("Trap:"):
                    self.traps_to_give.append(item_name)

        # Cups / Sports Mix
        await self.handle_basketball_unlocked_cups(self.unlocked_normal_cups, self.unlocked_hard_cups)
        await self.handle_dodgeball_unlocked_cups(self.unlocked_normal_cups, self.unlocked_hard_cups)
        await self.handle_volleyball_unlocked_cups(self.unlocked_normal_cups, self.unlocked_hard_cups)
        await self.handle_hockey_unlocked_cups(self.unlocked_normal_cups, self.unlocked_hard_cups)
        await self.handle_sports_mix_unlock(self.unlocked_sports, self.unlocked_sports_crystals)
        await self.handle_unlocked_sports_mix_cups(self.unlocked_sports_mix_cups)

        # Other items
        await self.handle_stage_unlocks(self.unlocked_stages)
        await self.handle_all_characters(self.unlocked_characters, self.unlocked_costumes)

        # Traps + Filler aren't here because they can only be received in game and this function gets awaited during
        # every connection state, if you were to receive a trap or filler in the menu it wouldn't work.

    # Kinda can't make this yet until there's a way to lock sports
    #async def handle_unlocked_sports(self, unlocked_sports):


    # === Character Unlocks ===


    async def handle_all_characters(self, unlocked_characters, unlocked_costumes):
        for char in character_names:
            item_name = f"Character: {char.replace('_', ' ').title()}"

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
                value = 1 if item_name in unlocked_characters else 0


            sports_classes = [
                BasketballAddresses,
                DodgeballAddresses,
                VolleyballAddresses,
                HockeyAddresses
            ]

            for sport in sports_classes:
                try:
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
            if "Costume: Light Blue Yoshi" in unlocked_costumes: value += 24
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
        if "Costume: Green Toad" in unlocked_costumes: value += 24
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


    async def handle_basketball_unlocked_cups(self, unlocked_normal_cups, unlocked_hard_cups):
        # Calculates the memory byte value based on unlocked cups.

        # Normal Cups
        normal_base_value = 0
        # Check for Mushroom Cup
        if "Basketball: Mushroom Cup (Normal)" in unlocked_normal_cups:
            normal_base_value += 1

        # Check for Flower Cup
        if "Basketball: Flower Cup (Normal)" in unlocked_normal_cups:
            normal_base_value += 2

        # Check for Star Cup
        if "Basketball: Star Cup (Normal)" in unlocked_normal_cups:
            normal_base_value += 4

        final_normal = 8 if normal_base_value == 0 else normal_base_value
        self.game_interface.dolphin_client.write_byte(BasketballAddresses.Tournament.normal_cups, final_normal)

        # Hard Cups
        hard_base_value = 0

        # Check for Mushroom Cup
        if "Basketball: Mushroom Cup (Hard)" in unlocked_hard_cups:
            hard_base_value += 1

        # Check for Flower Cup
        if "Basketball: Flower Cup (Hard)" in unlocked_hard_cups:
            hard_base_value += 2

        # Check for Star Cup
        if "Basketball: Star Cup (Hard)" in unlocked_hard_cups:
            hard_base_value += 4

        final_hard = 8 if hard_base_value == 0 else hard_base_value
        dme.write_byte(BasketballAddresses.Tournament.hard_cups, final_hard)

    async def handle_dodgeball_unlocked_cups(self, unlocked_normal_cups, unlocked_hard_cups):
        # Normal Cups
        normal_base_value = 0
        if "Dodgeball: Mushroom Cup (Normal)" in unlocked_normal_cups:
            normal_base_value += 1
        if "Dodgeball: Flower Cup (Normal)" in unlocked_normal_cups:
            normal_base_value += 2
        if "Dodgeball: Star Cup (Normal)" in unlocked_normal_cups:
            normal_base_value += 4

        final_normal = 8 if normal_base_value == 0 else normal_base_value
        self.game_interface.dolphin_client.write_byte(DodgeballAddresses.Tournament.normal_cups, final_normal)

        # Hard Cups
        hard_base_value = 0

        if "Dodgeball: Mushroom Cup (Hard)" in unlocked_hard_cups:
            hard_base_value += 1
        if "Dodgeball: Flower Cup (Hard)" in unlocked_hard_cups:
            hard_base_value += 2
        if "Dodgeball: Star Cup (Hard)" in unlocked_hard_cups:
            hard_base_value += 4

        final_hard = 8 if hard_base_value == 0 else hard_base_value
        dme.write_byte(DodgeballAddresses.Tournament.hard_cups, final_hard)

    async def handle_volleyball_unlocked_cups(self, unlocked_normal_cups, unlocked_hard_cups):
        # Normal Cups
        normal_base_value = 0
        if "Volleyball: Mushroom Cup (Normal)" in unlocked_normal_cups:
            normal_base_value += 1
        if "Volleyball: Flower Cup (Normal)" in unlocked_normal_cups:
            normal_base_value += 2
        if "Volleyball: Star Cup (Normal)" in unlocked_normal_cups:
            normal_base_value += 4

        final_normal = 8 if normal_base_value == 0 else normal_base_value
        self.game_interface.dolphin_client.write_byte(VolleyballAddresses.Tournament.normal_cups, final_normal)

        # Hard Cups
        hard_base_value = 0

        if "Volleyball: Mushroom Cup (Hard)" in unlocked_hard_cups:
            hard_base_value += 1
        if "Volleyball: Flower Cup (Hard)" in unlocked_hard_cups:
            hard_base_value += 2
        if "Volleyball: Star Cup (Hard)" in unlocked_hard_cups:
            hard_base_value += 4

        final_hard = 8 if hard_base_value == 0 else hard_base_value
        dme.write_byte(VolleyballAddresses.Tournament.hard_cups, final_hard)

    async def handle_hockey_unlocked_cups(self, unlocked_normal_cups, unlocked_hard_cups):
        # Normal Cups
        normal_base_value = 0
        if "Hockey: Mushroom Cup (Normal)" in unlocked_normal_cups:
            normal_base_value += 1
        if "Hockey: Flower Cup (Normal)" in unlocked_normal_cups:
            normal_base_value += 2
        if "Hockey: Star Cup (Normal)" in unlocked_normal_cups:
            normal_base_value += 4

        final_normal = 8 if normal_base_value == 0 else normal_base_value
        self.game_interface.dolphin_client.write_byte(HockeyAddresses.Tournament.normal_cups, final_normal)

        # Hard Cups
        hard_base_value = 0

        if "Hockey: Mushroom Cup (Hard)" in unlocked_hard_cups:
            hard_base_value += 1
        if "Hockey: Flower Cup (Hard)" in unlocked_hard_cups:
            hard_base_value += 2
        if "Hockey: Star Cup (Hard)" in unlocked_hard_cups:
            hard_base_value += 4

        final_hard = 8 if hard_base_value == 0 else hard_base_value
        dme.write_byte(HockeyAddresses.Tournament.hard_cups, final_hard)

    async def handle_unlocked_sports_mix_cups(self, unlocked_sports_mix_cups):
        # Calculates the memory byte value based on unlocked cups.

        # Normal Cups
        sm_base_value = 0
        # Check for Mushroom Cup
        if "Sports Mix: Mushroom Cup" in unlocked_sports_mix_cups:
            sm_base_value += 1

        # Check for Flower Cup
        if "Sports Mix: Flower Cup" in unlocked_sports_mix_cups:
            sm_base_value += 2

        # Check for Star Cup
        if "Sports Mix: Star Cup" in unlocked_sports_mix_cups:
            sm_base_value += 4

        final_sm = 8 if sm_base_value == 0 else sm_base_value
        self.game_interface.dolphin_client.write_byte(SportsMixAddresses.cups, final_sm)

    # Sports Mix unlock
    async def handle_sports_mix_unlock(self, unlocked_sports, unlocked_sports_crystals):
        if self.sports_mix_unlock == 0:
            if "Sport: Sports Mix" in unlocked_sports:
                self.game_interface.dolphin_client.write_byte(SportsMixAddresses.sports_mix_unlocked, 11)
        if self.sports_mix_unlock == 1:
            if ("Sports Crystal: Red" and "Sports Crystal: Green" and "Sports Crystal: Yellow" and
                    "Sports Crystal: Blue") in unlocked_sports_crystals:
                self.game_interface.dolphin_client.write_byte(SportsMixAddresses.sports_mix_unlocked, 11)


    # === Exhibition Unlocks ===


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

    STAGE_MAPPING = {
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

    async def handle_stage_unlocks(self, unlocked_stages):
        for address, stages in self.STAGE_MAPPING.items():
            value = 0

            # First Stage
            if stages[0] in unlocked_stages:
                value += 1

            # Second Stage
            if stages[1] in unlocked_stages:
                value += 2

            # Third Stage
            if stages[2] in unlocked_stages:
                value += 4

            final_byte = 8 if value == 0 else value

            self.game_interface.dolphin_client.write_byte(address, final_byte)


    # === Ability Unlocks ===


    async def handle_special_meter_unlock(self, unlocked_abilities):
        if self.game_interface.match_started():

            special_meter = self.game_interface.dolphin_client.follow_pointers(PlayerAddresses.special_meter,
                                                                            Offsets.PlayerOffsets.special_meter_offsets)

            if "Ability: Special Meter" not in unlocked_abilities:
                value = self.game_interface.dolphin_client.read_float(special_meter)
                if value != 0.0:
                    self.game_interface.dolphin_client.write_byte(special_meter, 0.0)
            else:
                pass


    # === Filler + ?-Panel Handling ===


    def has_item(self):
        current_item = self.game_interface.dolphin_client.read_byte(PlayerAddresses.item_held)
        if current_item == 255:
            return False
        else:
            return True


    async def handle_one_time_items(self, filler_to_give):
        if self.game_interface.match_started():

            for filler in filler_to_give:
                if filler == "1 Coin":
                    # Iterate a copy
                    if filler == "1 Coin":
                        current_coins = self.game_interface.dolphin_client.read_word(PlayerAddresses.Score.coins)
                        # Coin count in MSM cannot go above 10
                        if current_coins < 10:
                            new_coins = current_coins + 1
                            self.game_interface.dolphin_client.write_word(PlayerAddresses.Score.coins, new_coins)
                            filler_to_give.remove(filler)
                        else:
                            self.game_interface.dolphin_client.write_word(PlayerAddresses.Score.coins, 10)
                            filler_to_give.remove(filler)

                # Pauses if player currently has an item
                if self.has_item():
                        return

                self.one_time_running = True
                if filler == "1 Green Shell":
                    self.game_interface.dolphin_client.write_word(PlayerAddresses.item_held, 0)
                    logger.info("Sending Green Shell")
                    filler_to_give.remove(filler)
                elif filler == "1 Red Shell":
                    self.game_interface.dolphin_client.write_word(PlayerAddresses.item_held, 1)
                    filler_to_give.remove(filler)
                elif filler == "1 Mini Mushroom":
                    self.game_interface.dolphin_client.write_word(PlayerAddresses.item_held, 2)
                    filler_to_give.remove(filler)
                elif filler == "1 Bob-omb":
                    self.game_interface.dolphin_client.write_word(PlayerAddresses.item_held, 3)
                    filler_to_give.remove(filler)
                elif filler == "1 Super Star":
                    self.game_interface.dolphin_client.write_word(PlayerAddresses.item_held, 4)
                    filler_to_give.remove(filler)
                elif filler == "1 Banana":
                    self.game_interface.dolphin_client.write_word(PlayerAddresses.item_held, 5)
                    filler_to_give.remove(filler)
                self.one_time_running = False

    def has_one_time_items_ran(self):
        if self.one_time_running:
            return True
        else:
            return False

    async def handle_question_mark_panel_items(self, unlocked_panel_items):
        # Check if we currently have an item.
        # If we DON't, reset the flag so we are ready for the next box.
        if not self.has_item():
            self.item_processed = False
            return

        if self.game_interface.match_started() and not self.item_processed:
            if not self.has_item():
                if self.has_one_time_items_ran():
                    pass
                else:
                    logger.info("Question Mark Panel activated! Changing item!")
                    if not unlocked_panel_items:
                        logger.info("No items available! Sucks to be you! >;]")
                        self.game_interface.dolphin_client.write_word(PlayerAddresses.item_held, 255)
                        return

                    random_item = random.choice(unlocked_panel_items)

                    if "Green Shell" in random_item:
                        self.game_interface.dolphin_client.write_word(PlayerAddresses.item_held, 0)
                        logger.info("Item replaced with a Green Shell!")
                    elif "Red Shell" in random_item:
                        self.game_interface.dolphin_client.write_word(PlayerAddresses.item_held, 1)
                        logger.info("Item replaced with a Red Shell!")
                    elif "Mini Mushroom" in random_item:
                        self.game_interface.dolphin_client.write_word(PlayerAddresses.item_held, 2)
                        logger.info("Item replaced with a Mini Mushroom!")
                    elif "Bob-omb" in random_item:
                        self.game_interface.dolphin_client.write_word(PlayerAddresses.item_held, 3)
                        logger.info("Item replaced with a Bob-omb!")
                    elif "Super Star" in random_item:
                        self.game_interface.dolphin_client.write_word(PlayerAddresses.item_held, 4)
                        logger.info("Item replaced with a Super Star!")
                    elif "Banana" in random_item:
                        self.game_interface.dolphin_client.write_word(PlayerAddresses.item_held, 5)
                        logger.info("Item replaced with a Banana!")

                    # Set to true so the loop skips this block next time
                    self.item_processed = True

        await asyncio.sleep(0.1)


    # === Trap Handling ===


    async def handle_traps(self, traps_to_give):
        if self.game_interface.match_status() == "Ongoing":
            for trap in traps_to_give:
                if trap == "Trap: Freeze Character 1":
                    asyncio.create_task(self.run_freeze_trap_1())
                    traps_to_give.remove(trap)
                elif trap == "Trap: Freeze Character 2":
                    asyncio.create_task(self.run_freeze_trap_2())
                    traps_to_give.remove(trap)
                elif trap == "Trap: Freeze Character 3":
                    asyncio.create_task(self.run_freeze_trap_3())
                    traps_to_give.remove(trap)
                elif trap == "Trap: Opponent Coins":
                    asyncio.create_task(self.opponent_coins())
                    traps_to_give.remove(trap)
                elif trap == "Trap: 1/2 Time":
                    current_time = self.game_interface.dolphin_client.read_float(MatchAddresses.time_remaining)
                    self.game_interface.dolphin_client.write_float(MatchAddresses.time_remaining, current_time/2)
                    traps_to_give.remove(trap)

    async def run_freeze_trap_1(self):
        x_pos_1 = self.game_interface.dolphin_client.follow_pointers(PlayerAddresses.Position.pos,
                                                                     Offsets.PlayerOffsets.B1.Position.x_offsets)
        current_x_pos_1 = self.game_interface.dolphin_client.read_float(x_pos_1)
        y_pos_1 = 0.1 # Setting it to 0 causes infinite spin glitch
        z_pos_1 = self.game_interface.dolphin_client.follow_pointers(PlayerAddresses.Position.pos,
                                                                     Offsets.PlayerOffsets.B1.Position.z_offsets)
        current_z_pos_1 = self.game_interface.dolphin_client.read_float(z_pos_1)

        # Set a timer
        end_time = asyncio.get_event_loop().time() + 5.0

        # Loop until the 5 seconds are up - While time is smaller than the end time
        while asyncio.get_event_loop().time() < end_time:
            self.game_interface.dolphin_client.write_float(PlayerAddresses.Position.pos, current_x_pos_1)
            self.game_interface.dolphin_client.write_float(PlayerAddresses.Position.pos, y_pos_1)
            self.game_interface.dolphin_client.write_float(PlayerAddresses.Position.pos, current_z_pos_1)

            await asyncio.sleep(0.01)

    async def run_freeze_trap_2(self):
        x_pos_2 = self.game_interface.dolphin_client.follow_pointers(PlayerAddresses.Position.pos,
                                                                     Offsets.PlayerOffsets.B2.Position.x_offsets)
        current_x_pos_2 = self.game_interface.dolphin_client.read_float(x_pos_2)
        y_pos_2 = 0.1 # Setting it to 0 causes infinite spin glitch
        z_pos_2 = self.game_interface.dolphin_client.follow_pointers(PlayerAddresses.Position.pos,
                                                                     Offsets.PlayerOffsets.B2.Position.z_offsets)
        current_z_pos_2 = self.game_interface.dolphin_client.read_float(z_pos_2)

        # Set a timer
        end_time = asyncio.get_event_loop().time() + 5.0

        # Loop until the 5 seconds are up - While time is smaller than the end time
        while asyncio.get_event_loop().time() < end_time:
            self.game_interface.dolphin_client.write_float(PlayerAddresses.Position.pos, current_x_pos_2)
            self.game_interface.dolphin_client.write_float(PlayerAddresses.Position.pos, y_pos_2)
            self.game_interface.dolphin_client.write_float(PlayerAddresses.Position.pos, current_z_pos_2)

            await asyncio.sleep(0.01)

    async def run_freeze_trap_3(self):
        x_pos_3 = self.game_interface.dolphin_client.follow_pointers(PlayerAddresses.Position.pos,
                                                                     Offsets.PlayerOffsets.B3.Position.x_offsets)
        current_x_pos_3 = self.game_interface.dolphin_client.read_float(x_pos_3)
        y_pos_3 = 0.1 # Setting it to 0 causes infinite spin glitch
        z_pos_3 = self.game_interface.dolphin_client.follow_pointers(PlayerAddresses.Position.pos,
                                                                     Offsets.PlayerOffsets.B3.Position.z_offsets)
        current_z_pos_3 = self.game_interface.dolphin_client.read_float(z_pos_3)

        # Set a timer
        end_time = asyncio.get_event_loop().time() + 5.0

        # Loop until the 5 seconds are up - While time is smaller than the end time
        while asyncio.get_event_loop().time() < end_time:
            self.game_interface.dolphin_client.write_float(PlayerAddresses.Position.pos, current_x_pos_3)
            self.game_interface.dolphin_client.write_float(PlayerAddresses.Position.pos, y_pos_3)
            self.game_interface.dolphin_client.write_float(PlayerAddresses.Position.pos, current_z_pos_3)

            await asyncio.sleep(0.01)

    async def opponent_coins(self):
        current_coins = self.game_interface.dolphin_client.read_word(OpponentAddresses.Score.coins)
        random_int = randint(1,5)
        new_coins = current_coins + random_int
        # Coin count in MSM cannot go above 10
        if new_coins <= 10:
            self.game_interface.dolphin_client.write_word(OpponentAddresses.Score.coins, new_coins)
        else:
            needed_to_minus = new_coins - 10
            new_coins = new_coins - needed_to_minus
            self.game_interface.dolphin_client.write_word(OpponentAddresses.Score.coins, new_coins)


    # === Boss Stuff ===

    async def has_goaled(self):
        if self.is_behemoth:
            address_behemoth_hp = self.game_interface.dolphin_client.follow_pointers(BossAddresses.behemoth_hp,
                                                                                     Offsets.BossOffsets.behemoth_hp_offsets)
            behemoth_hp = self.game_interface.dolphin_client.read_float(address_behemoth_hp)
            if behemoth_hp == 0.0:
                if self.goal_condition == 0:
                    await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
        if self.is_behemoth_king:
            address_behemoth_hp = self.game_interface.dolphin_client.follow_pointers(BossAddresses.behemoth_hp,
                                                                                     Offsets.BossOffsets.behemoth_hp_offsets)
            behemoth_hp = self.game_interface.dolphin_client.read_float(address_behemoth_hp)
            if behemoth_hp == 0.0:
                if self.goal_condition == 1:
                    await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])

    async def write_boss_health(self):
        # Check for Sports Mix
        # 0 = Not Sports Mix, 1 = Is Sports Mix
        is_sports_mix = self.game_interface.dolphin_client.read_byte(SportsMixAddresses.is_sports_mix)

        # s20VO = Behemoth Stage
        current_stage = self.game_interface.dolphin_client.read_string(MatchAddresses.current_stage)

        if is_sports_mix == 0:
            if current_stage == "s20VO":
                behemoth_hp = self.game_interface.dolphin_client.follow_pointers(BossAddresses.behemoth_hp,
                                                                                 Offsets.BossOffsets.behemoth_hp_offsets)
                self.game_interface.dolphin_client.write_float(behemoth_hp, self.behemoth_hp)
                self.is_behemoth_king = False
                self.is_behemoth = True
        # Behemoth King is only accessed through Sports Mix
        elif is_sports_mix == 1:
            if current_stage == "s20VO":
                behemoth_hp = self.game_interface.dolphin_client.follow_pointers(BossAddresses.behemoth_hp,
                                                                                 Offsets.BossOffsets.behemoth_hp_offsets)
                self.game_interface.dolphin_client.write_float(behemoth_hp, self.behemoth_king_hp)
                self.is_behemoth_king = True
                self.is_behemoth = False


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
                        logger.info(message)
                        self.last_error_message = message
                    await asyncio.sleep(1)
                    continue

                if self.game_interface.dolphin_client.is_hooked_class():
                    if self.start_process:
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

    async def handle_in_match(self):
        await self.handle_received_items()
        await self.handle_traps(self.traps_to_give)
        await self.handle_one_time_items(self.filler_to_give)
        await self.handle_question_mark_panel_items(self.unlocked_panel_items)
        await self.handle_special_meter_unlock(self.unlocked_abilities)
        await self.has_goaled()

        await asyncio.sleep(0.1)

    async def handle_in_tournament_map(self):
        await self.handle_received_items()

        await asyncio.sleep(0.1)

    async def handle_in_main_menu(self):
        await self.handle_received_items()
        await self.has_goaled()

        await asyncio.sleep(0.1)