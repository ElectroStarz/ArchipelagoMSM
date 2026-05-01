from random import randint
from typing import Dict, Optional, List
import Utils
from CommonClient import ClientCommandProcessor, CommonContext, logging, asyncio
import logging
from NetUtils import NetworkItem
from . import dolphin_connection
from .MSMInterface import *
from ..items import ITEM_NAME_TO_ID
import traceback

status_messages = {
    ConnectionState.IN_MATCH: "In match",
    ConnectionState.IN_MENU: "In main menu",
    ConnectionState.DISCONNECTED: "Unable to connect to the Dolphin instance, attempting to reconnect...",
    ConnectionState.IN_TOURNAMENT_MAP: "In tournament map",
    ConnectionState.GOALED: "Goaled game!"
}

character_names = [
    "Mario", "Luigi", "Peach", "Daisy", "Yoshi", "Wario", "Waluigi",
    "Donkey Kong", "Diddy Kong", "Toad", "Bowser", "Bowser Jr.",
    "Moogle", "White Mage", "Black Mage", "Ninja", "Cactuar", "Slime"
]

logger = logging.getLogger("Client")

class MSMCommandProcessor(ClientCommandProcessor):
    ctx: "MSMContext"

    def __init__(self, ctx: "MSMContext"):
        super().__init__(ctx)

    def _cmd_status(self):
        """Display the current dolphin connection status."""
        logger.info(f"Connection status: {status_messages[self.ctx.connection_state]}")

    def _cmd_deathlink(self):
        """Toggle deathlink from client. Overrides default setting."""
        self.ctx.death_link_ = not self.ctx.deathlink
        Utils.async_start(
            self.ctx.update_death_link(self.ctx.deathlink),
            name="Update Deathlink",
        )
        message = (
            f"Deathlink {'enabled' if self.ctx.deathlink else 'disabled'}"
        )
        logger.info(message)





class MSMContext(CommonContext):
    tags = {"AP"}
    game = "Mario Sports Mix"
    game_interface: MSMInterface
    connection_state = ConnectionState.DISCONNECTED
    command_processor = MSMCommandProcessor
    want_slot_data = True
    items_handled = []
    locations_handled = []
    last_error_message: Optional[str] = None
    dolphin_sync_task: Optional[asyncio.Task[Any]] = None

    slot_data: Dict[str, Utils.Any] = {}
    deathlink = False
    deathlink_action = Any
    deathlink_consequence = Any
    behemoth_hp = float
    behemoth_king_hp = float
    is_behemoth = False
    is_behemoth_king = False
    goal_condition = Any

    # Sanity stuff
    special_sanity = False
    court_sanity = Any
    score_sanity = False
    score_sanity_max = int
    score_sanity_points_req = int
    team_sanity = False

    def __init__(self, server_address: str, password: str):
        super().__init__(server_address, password)
        self.game_interface = MSMInterface(logger)
        self.command_processor.ctx = self
        self.items_handled = []
        self.locations_handled = []

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
            self.special_sanity = self.slot_data["special_sanity"]

        elif cmd == "ReceivedItems":
            # handle_recived_items
            pass
        elif cmd == "Bounced":
            print(args)
        elif cmd == "PrintJSON":
            print(args)
        elif cmd == "Retrieved":
            # print("Packed Retrieved with the following argument")
            print(args)
        else:
            print(f"Received package with an unknown command: {cmd}")

    def make_gui(self):
        ui = super().make_gui()
        ui.base_title = "Archipelago Mario Sports Mix Client"
        return ui

    async def disconnect(self, allow_auto_reconnect: bool = False):
        await super().disconnect(allow_auto_reconnect)


    async def has_goaled(self):
        current_stage = self.game_interface.dolphin_client.read_string(MatchAddresses.current_stage)
        behemoth_hp = self.game_interface.dolphin_client.read_float(BossAddresses.behemoth_hp)
        #if self.is_behemoth:
            #if current_stage == "s20VO" and behemoth_hp == 0.0



    async def check_previous_stage(self):
        current_mush_stage_b = self.game_interface.dolphin_client.read_byte(BasketballAddresses.Exhibition.mushroom_cup)
        current_flower_stage_b = self.game_interface.dolphin_client.read_byte(BasketballAddresses.Exhibition.flower_cup)
        current_star_stage_b = self.game_interface.dolphin_client.read_byte(BasketballAddresses.Exhibition.star_cup)
        current_question_stage_b = self.game_interface.dolphin_client.read_byte(BasketballAddresses.Exhibition.question_mark_cup)

        current_mush_stage_d = self.game_interface.dolphin_client.read_byte(DodgeballAddresses.Exhibition.mushroom_cup)
        current_flower_stage_d = self.game_interface.dolphin_client.read_byte(DodgeballAddresses.Exhibition.flower_cup)
        current_star_stage_d = self.game_interface.dolphin_client.read_byte(DodgeballAddresses.Exhibition.star_cup)
        current_question_stage_d = self.game_interface.dolphin_client.read_byte(DodgeballAddresses.Exhibition.question_mark_cup)

        current_mush_stage_v = self.game_interface.dolphin_client.read_byte(VolleyballAddresses.Exhibition.mushroom_cup)
        current_flower_stage_v = self.game_interface.dolphin_client.read_byte(VolleyballAddresses.Exhibition.flower_cup)
        current_star_stage_v = self.game_interface.dolphin_client.read_byte(VolleyballAddresses.Exhibition.star_cup)
        current_question_stage_bv = self.game_interface.dolphin_client.read_byte(VolleyballAddresses.Exhibition.question_mark_cup)

        current_mush_stage_h = self.game_interface.dolphin_client.read_byte(HockeyAddresses.Exhibition.mushroom_cup)
        current_flower_stage_h = self.game_interface.dolphin_client.read_byte(HockeyAddresses.Exhibition.flower_cup)
        current_star_stage_h = self.game_interface.dolphin_client.read_byte(HockeyAddresses.Exhibition.star_cup)
        current_question_stage_h = self.game_interface.dolphin_client.read_byte(HockeyAddresses.Exhibition.question_mark_cup)

    async def handle_received_items(self):
        unlocked_sports = []
        unlocked_normal_cups = []
        unlocked_hard_cups = []
        unlocked_sports_mix_cups = []
        unlocked_sports_crystals = []
        unlocked_stages = []
        unlocked_characters = []
        unlocked_costumes = []
        filler_to_give = []
        filler_all = []
        traps_to_give = []
        traps_all = []
        #unlocked_ex_difficulties = []


        for network_item in self.items_received:
            item_id = network_item.item
            item_name = ITEM_NAME_TO_ID[str(item_id)]
            if network_item not in self.items_handled:
                if item_name is None:
                    continue

                if "Sport:" in item_name:
                    unlocked_sports.append(item_name)
                elif "Basketball:" or "Dodgeball:" or "Volleyball:" or "Hockey:" in item_name:
                    if "Normal" in item_name:
                        unlocked_normal_cups.append(item_name)
                    elif "Hard" in item_name:
                        unlocked_hard_cups.append(item_name)
                elif "Sports Mix:" in item_name:
                    unlocked_sports_mix_cups.append(item_name)
                elif "Sports Crystal:" in item_name:
                    unlocked_sports_crystals.append(item_name)
                elif "Stage:" in item_name:
                    unlocked_stages.append(item_name)
                elif "Character:" in item_name:
                    unlocked_characters.append(item_name)
                elif "Costume:" in item_name:
                    unlocked_costumes.append(item_name)
                elif "1 Time:" in item_name:
                    filler_to_give.append(item_name)
                    filler_all.append(item_name)
                elif "Trap:" in item_name:
                    traps_to_give.append(item_name)
                    traps_all.append(item_name)
                self.items_handled.append(network_item)

        await self.handle_basketball_unlocked_cups(unlocked_normal_cups, unlocked_hard_cups)
        await self.handle_all_characters(unlocked_characters, unlocked_costumes)
        await self.handle_traps(traps_to_give)


    # Kinda can't make this yet until there's a way to lock sports
    #async def handle_unlocked_sports(self, unlocked_sports):

    async def handle_all_characters(self, unlocked_characters, unlocked_costumes):
        for char in character_names:
            # Format the name
            item_name = f"Character: {char}"

            if char == "yoshi":
                value = self.handle_yoshi_unlocks(unlocked_characters, unlocked_costumes)
            elif char == "peach":
                value = self.handle_peach_unlocks(unlocked_characters, unlocked_costumes)
            elif char == "toad":
                value = self.handle_toad_unlocks(unlocked_characters, unlocked_costumes)
            elif char == "slime":
                value = self.handle_slime_unlocks(unlocked_characters, unlocked_costumes)
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
    def handle_yoshi_unlocks(unlocked_characters, unlocked_costumes):
        # If they don't have the character item, character is locked
        if "Character: Yoshi" not in unlocked_characters:
            value = 0
            return value

        value = 1
        if "Costume: Pink Yoshi" in unlocked_costumes: value += 4
        if "Costume: Light Blue Yoshi" in unlocked_costumes: value += 24
        if "Costume: Yellow Yoshi" in unlocked_costumes: value += 64
        return value

    @staticmethod
    def handle_peach_unlocks(unlocked_characters, unlocked_costumes):
        # If they don't have the character item, character is locked
        if "Character: Peach" not in unlocked_characters:
            value = 0
            return value

        value = 1
        if "Costume: Tennis-wear Peach" in unlocked_costumes: value += 4
        return value

    @staticmethod
    def handle_toad_unlocks(unlocked_characters, unlocked_costumes):
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
    def handle_slime_unlocks(unlocked_characters, unlocked_costumes):
        # If they don't have the character item, character is locked
        if "Character: Slime" not in unlocked_characters:
            value = 0
            return value

        value = 1
        if "Costume: She-slime" in unlocked_costumes: value += 4
        if "Costume: Metal Slime" in unlocked_costumes: value += 16
        return value

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
        # Calculates the memory byte value based on unlocked cups.

        # Normal Cups
        normal_base_value = 0
        # Check for Mushroom Cup
        if "Dodgeball: Mushroom Cup (Normal)" in unlocked_normal_cups:
            normal_base_value += 1

        # Check for Flower Cup
        if "Dodgeball: Flower Cup (Normal)" in unlocked_normal_cups:
            normal_base_value += 2

        # Check for Star Cup
        if "Dodgeball: Star Cup (Normal)" in unlocked_normal_cups:
            normal_base_value += 4

        final_normal = 8 if normal_base_value == 0 else normal_base_value
        self.game_interface.dolphin_client.write_byte(DodgeballAddresses.Tournament.normal_cups, final_normal)

        # Hard Cups
        hard_base_value = 0

        # Check for Mushroom Cup
        if "Dodgeball: Mushroom Cup (Hard)" in unlocked_hard_cups:
            hard_base_value += 1

        # Check for Flower Cup
        if "Dodgeball: Flower Cup (Hard)" in unlocked_hard_cups:
            hard_base_value += 2

        # Check for Star Cup
        if "Dodgeball: Star Cup (Hard)" in unlocked_hard_cups:
            hard_base_value += 4

        final_hard = 8 if hard_base_value == 0 else hard_base_value
        dme.write_byte(DodgeballAddresses.Tournament.hard_cups, final_hard)

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

    # Filler handling is in item_manager

    # Trap Handling
    async def handle_traps(self, traps_to_give):
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
        current_x_pos_1 = self.game_interface.dolphin_client.read_float(PlayerAddresses.Position.B1.x_pos)
        y_pos_1 = 0.1 # Setting it to 0 causes infinite spin glitch
        current_z_pos_1 = self.game_interface.dolphin_client.read_float(PlayerAddresses.Position.B1.z_pos)

        # Set a timer
        end_time = asyncio.get_event_loop().time() + 5.0

        # Loop until the 5 seconds are up - While time is smaller than the end time
        while asyncio.get_event_loop().time() < end_time:
            self.game_interface.dolphin_client.write_float(PlayerAddresses.Position.B1.x_pos, current_x_pos_1)
            self.game_interface.dolphin_client.write_float(PlayerAddresses.Position.B1.y_pos, y_pos_1)
            self.game_interface.dolphin_client.write_float(PlayerAddresses.Position.B1.z_pos, current_z_pos_1)

            await asyncio.sleep(0.01)

    async def run_freeze_trap_2(self):
        current_x_pos_2 = self.game_interface.dolphin_client.read_float(PlayerAddresses.Position.B2.x_pos)
        y_pos_2 = 0.1 # Setting it to 0 causes infinite spin glitch
        current_z_pos_2 = self.game_interface.dolphin_client.read_float(PlayerAddresses.Position.B2.z_pos)

        end_time = asyncio.get_event_loop().time() + 5.0

        while asyncio.get_event_loop().time() < end_time:
            self.game_interface.dolphin_client.write_float(PlayerAddresses.Position.B2.x_pos, current_x_pos_2)
            self.game_interface.dolphin_client.write_float(PlayerAddresses.Position.B2.y_pos, y_pos_2)
            self.game_interface.dolphin_client.write_float(PlayerAddresses.Position.B2.z_pos, current_z_pos_2)

            await asyncio.sleep(0.01)

    async def run_freeze_trap_3(self):
        current_x_pos_3 = self.game_interface.dolphin_client.read_float(PlayerAddresses.Position.B3.x_pos)
        y_pos_3 = 0.1 # Setting it to 0 causes infinite spin glitch
        current_z_pos_3 = self.game_interface.dolphin_client.read_float(PlayerAddresses.Position.B3.z_pos)

        end_time = asyncio.get_event_loop().time() + 5.0

        while asyncio.get_event_loop().time() < end_time:
            self.game_interface.dolphin_client.write_float(PlayerAddresses.Position.B3.x_pos, current_x_pos_3)
            self.game_interface.dolphin_client.write_float(PlayerAddresses.Position.B3.y_pos, y_pos_3)
            self.game_interface.dolphin_client.write_float(PlayerAddresses.Position.B3.z_pos, current_z_pos_3)

            await asyncio.sleep(0.01)

    async def opponent_coins(self):
        current_coins = self.game_interface.dolphin_client.read_word(OpponentAddresses.Score.coins)
        random_int = randint(1,5)
        new_coins = current_coins + random_int
        if new_coins <= 10:
            self.game_interface.dolphin_client.write_word(OpponentAddresses.Score.coins, new_coins)
        else:
            needed_to_minus = new_coins - 10
            new_coins = new_coins - needed_to_minus
            self.game_interface.dolphin_client.write_word(OpponentAddresses.Score.coins, new_coins)

    async def write_behemoth_hp(self):
        # Check for Sports Mix
        is_sports_mix = self.game_interface.dolphin_client.read_byte(SportsMixAddresses.is_sports_mix)
        # 0 = Not Sports Mix, 1 = Is Sports Mix
        current_stage = self.game_interface.dolphin_client.read_string(MatchAddresses.current_stage)
        if is_sports_mix == 0:
            if current_stage == "s20VO":
                self.game_interface.dolphin_client.write_float(BossAddresses.behemoth_hp, self.behemoth_hp)
                self.is_behemoth_king = False
                self.is_behemoth = True
        # Behemoth King is only accessed through Sports Mix
        elif is_sports_mix == 1:
            if current_stage == "s20VO":
                self.game_interface.dolphin_client.write_float(BossAddresses.behemoth_hp, self.behemoth_king_hp)
                self.is_behemoth_king = True
                self.is_behemoth = False

    async def dolphin_sync_task_func(self):
        logger.info("Starting Dolphin Connector, attempting to connect to emulator...")

        while not self.exit_event.is_set():
            try:
                if self.server:
                    self.last_error_message = None
                    if not self.slot:
                        await asyncio.sleep(1)
                        continue
                    connection_state = self.game_interface.get_connection_state()
                    self.update_connection_status(connection_state)

                    if connection_state == ConnectionState.IN_MATCH:
                        await self.handle_in_match()
                    elif connection_state == ConnectionState.IN_TOURNAMENT_MAP:
                        await self.handle_in_tournament_map()
                        await asyncio.sleep(0.01)
                    elif connection_state == ConnectionState.IN_MENU:
                        await self.handle_in_main_menu()
                        await asyncio.sleep(0.01)
                    else:
                        await self._handle_game_not_ready()
                        await asyncio.sleep(1)


                else:
                    message = "Waiting for player to connect to server"
                    if self.last_error_message is not message:
                        logger.info("Waiting for player to connect to server")
                        self.last_error_message = message
                    await asyncio.sleep(1)
            except Exception as e:
                if isinstance(e, dolphin_connection.DolphinException):
                    logger.error(str(e))
                else:
                    logger.error(traceback.format_exc())
                await asyncio.sleep(3)
                continue

    def update_connection_status(self, status: ConnectionState):
        self.connection_state = status
        return status

    async def handle_in_match(self):
        await self.handle_received_items()


        await asyncio.sleep(0.1)

    async def handle_in_tournament_map(self):
        pass

    async def handle_in_main_menu(self):
        await self.handle_received_items()

        await asyncio.sleep(0.1)

    async def _handle_game_not_ready(self):
        pass