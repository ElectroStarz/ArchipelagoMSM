from random import randint
from typing import Dict, Optional, List
import Utils
from CommonClient import ClientCommandProcessor, CommonContext, logging, asyncio
import logging
from NetUtils import NetworkItem, ClientStatus
from .MSMInterface import *
from .memory_addresses import *
import traceback

status_messages = {
    ConnectionState.IN_MATCH: "In match",
    ConnectionState.IN_MENU: "In main menu",
    ConnectionState.DISCONNECTED: "Unable to connect to the Dolphin instance, attempting to reconnect...",
    ConnectionState.IN_TOURNAMENT_MAP: "In tournament map",
    ConnectionState.GOALED: "Goaled game!"
}

character_names = [
    "mario", "luigi", "peach", "daisy", "yoshi", "wario", "waluigi",
    "donkey_kong", "diddy_kong", "toad", "bowser", "bowser_jr",
    "moogle", "white_mage", "black_mage", "ninja", "cactuar", "slime"
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
        Utils.async_start(
            self.ctx.update_death_link(self.ctx.deathlink),
            name="Update Deathlink",
        )
        message = (
            f"Deathlink {'enabled' if self.ctx.deathlink else 'disabled'}"
        )
        logger.info(message)

    def _cmd_items_have(self):
        """What items do you have"""
        logger.info(f"{self.ctx.unlocked_stages}")



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

    # Item stuff
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

    def __init__(self, server_address: str, password: str):
        super().__init__(server_address, password)
        self.game_interface = MSMInterface(logger)
        self.command_processor.ctx = self
        self.items_received = []
        self.items_handled = []
        self.locations_handled = []
        self.seed: Optional[str] = None
        self.last_received_index = int

        # Lists for items
        self.unlocked_sports = []
        self.unlocked_normal_cups = []
        self.unlocked_hard_cups = []
        self.unlocked_sports_mix_cups = []
        self.unlocked_sports_crystals = []
        self.unlocked_stages = []
        self.unlocked_characters = []
        self.unlocked_costumes = []
        self.filler_to_give = []
        self.filler_all = []
        self.traps_to_give = []
        self.traps_all = []

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
            self.sports_mix_unlock = self.slot_data["sports_mix_unlock"]


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
        await super().disconnect(allow_auto_reconnect)

    async def has_goaled(self):
        current_stage = self.game_interface.dolphin_client.read_string(MatchAddresses.current_stage)
        address_behemoth_hp = self.game_interface.dolphin_client.follow_pointers(BossAddresses.behemoth_hp,
                                                                                Offsets.BossOffsets.behemoth_hp_offsets)
        behemoth_hp = self.game_interface.dolphin_client.read_float(address_behemoth_hp)
        if self.is_behemoth:
            if current_stage == "s20VO" and behemoth_hp == 0.0:
                if self.goal_condition == 0:
                    await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
        if self.is_behemoth_king:
            if current_stage == "s20VO" and behemoth_hp == 0.0:
                if self.goal_condition == 1:
                    await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])

    async def handle_received_items(self):
        from ..items import item_table
        id_to_name = {data.code: name for name, data in item_table.items()}

        for network_item in self.items_received:
            item_id = network_item.item
            item_name = id_to_name.get(item_id)
            if network_item not in self.items_handled:
                if item_name is None:
                    continue

                if "Sport:" in item_name:
                    self.unlocked_sports.append(item_name)
                elif any(prefix in item_name for prefix in ["Basketball:", "Dodgeball:", "Volleyball:", "Hockey:"]):
                    if "Normal" in item_name:
                        self.unlocked_normal_cups.append(item_name)
                    elif "Hard" in item_name:
                        self.unlocked_hard_cups.append(item_name)
                elif "Sports Mix:" in item_name:
                    self.unlocked_sports_mix_cups.append(item_name)
                elif "Sports Crystal:" in item_name:
                    self.unlocked_sports_crystals.append(item_name)
                elif "Stage:" in item_name:
                    self.unlocked_stages.append(item_name)
                elif "Character:" in item_name:
                    self.unlocked_characters.append(item_name)
                elif "Costume:" in item_name:
                    self.unlocked_costumes.append(item_name)
                elif "1 Time" in item_name:
                    self.filler_to_give.append(item_name)
                    self.filler_all.append(item_name)
                elif "Trap:" in item_name:
                    self.traps_to_give.append(item_name)
                    self.traps_all.append(item_name)
                self.items_handled.append(network_item)

        await self.handle_basketball_unlocked_cups(self.unlocked_normal_cups, self.unlocked_hard_cups)
        await self.handle_dodgeball_unlocked_cups(self.unlocked_normal_cups, self.unlocked_hard_cups)
        await self.handle_volleyball_unlocked_cups(self.unlocked_normal_cups, self.unlocked_hard_cups)
        await self.handle_hockey_unlocked_cups(self.unlocked_normal_cups, self.unlocked_hard_cups)
        await self.handle_sports_mix_unlock(self.unlocked_sports, self.unlocked_sports_crystals)
        await self.handle_unlocked_sports_mix_cups(self.unlocked_sports_mix_cups)
        await self.handle_all_characters(self.unlocked_characters, self.unlocked_costumes)

    # Kinda can't make this yet until there's a way to lock sports
    #async def handle_unlocked_sports(self, unlocked_sports):

    async def handle_all_characters(self, unlocked_characters, unlocked_costumes):
        for char in character_names:
            item_name = f"Character: {char.replace('_', ' ').title()}"

            if char == "Yoshi":
                value = self.yoshi_unlocks_value(unlocked_characters, unlocked_costumes)
            elif char == "Peach":
                value = self.peach_unlocks_value(unlocked_characters, unlocked_costumes)
            elif char == "Toad":
                value = self.toad_unlocks_value(unlocked_characters, unlocked_costumes)
            elif char == "Slime":
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
    def slime_unlocks_value(unlocked_characters, unlocked_costumes):
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

    async def handle_sports_mix_unlock(self, unlocked_sports, unlocked_sports_crystals):
        if self.sports_mix_unlock == 0:
            if "Sport: Sports Mix" in unlocked_sports:
                self.game_interface.dolphin_client.write_byte(SportsMixAddresses.is_sports_mix, 1)
        if self.sports_mix_unlock == 1:
            if ("Sports Crystal: Red" and "Sports Crystal: Green" and "Sports Crystal: Yellow" and
                    "Sports Crystal: Blue") in unlocked_sports_crystals:
                self.game_interface.dolphin_client.write_byte(SportsMixAddresses.is_sports_mix, 1)

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
        if new_coins <= 10:
            self.game_interface.dolphin_client.write_word(OpponentAddresses.Score.coins, new_coins)
        else:
            needed_to_minus = new_coins - 10
            new_coins = new_coins - needed_to_minus
            self.game_interface.dolphin_client.write_word(OpponentAddresses.Score.coins, new_coins)

    async def write_boss_health(self):
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

    async def dolphin_sync_task(self) -> None:
        """
        The main loop managing the connection to Dolphin and game-state logic routing.
        """
        logger.info("Starting Dolphin Connector, attempting to connect to emulator...")
        # Use abort_requested as the standard exit condition for CommonContext
        while not self.exit_event.is_set():
            try:
                # 1. Ensure we are connected to the AP Server first
                if not self.server or not self.server.socket or self.server.socket.closed:
                    message = "Waiting for player to connect to Archipelago server..."
                    if self.last_error_message != message:
                        logger.info(message)
                        self.last_error_message = message
                    await asyncio.sleep(1)
                    continue

                if not self.game_interface.dolphin_client.is_hooked_class():
                    await self.game_interface.dolphin_client.attempt_to_hook()

                # Ensure we have received slot data
                if not self.slot:
                    await asyncio.sleep(1)
                    continue

                # Reset error message once connected
                self.last_error_message = None


                connection_state = self.game_interface.get_connection_state()
                self.update_connection_status(connection_state)

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
                    self.update_connection_status(ConnectionState.DISCONNECTED)
                else:
                    logger.error(f"Sync Task Error:\n{traceback.format_exc()}")
                await asyncio.sleep(3)

    def update_connection_status(self, status: ConnectionState):
        self.connection_state = status

    async def handle_in_match(self):
        await self.handle_received_items()
        await self.handle_traps(self.traps_to_give)

        await asyncio.sleep(0.1)

    async def handle_in_tournament_map(self):
        await self.handle_received_items()

    async def handle_in_main_menu(self):
        await self.handle_received_items()

        await asyncio.sleep(0.1)

    async def update_death_link(self, death_link: bool):
        """Helper function to set Death Link connection tag on/off and update the connection if already connected."""
        old_tags = self.tags.copy()
        if self.deathlink:
            self.tags.add("DeathLink")
        else:
            self.tags -= {"DeathLink"}
        if old_tags != self.tags and self.server and not self.server.socket.closed:
            await self.send_msgs([{"cmd": "ConnectUpdate", "tags": self.tags}])