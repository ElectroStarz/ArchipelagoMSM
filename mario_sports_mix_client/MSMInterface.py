from enum import Enum
from .dolphin_connection import *
from typing import Optional
from .memory_addresses_pal import *
from .common_address_library import AddressLib
from .MSMFunctions import get_address

class ConnectionState(Enum):
    DISCONNECTED = 0
    CONNECTED = 1
    IN_MENU = 2
    IN_TOURNAMENT_MAP = 4
    IN_MATCH = 5
    IN_BOSS = 6

stage_ids = ["s01", "s02", "s03", "s04", "s05", "s06", "s07", "s08", "s09", "s10", "s11", "s12", "s15", "s16", "s17"]

class MSMInterface:
    dolphin_client: DolphinClient
    connection_state: str
    logger: Logger
    game_ver: int
    current_tournament = str

    def __init__(self, logger: Logger):
        self.logger = logger
        self.dolphin_client = DolphinClient(logger)
        self.current_tournament = None
        self.addresslib = AddressLib()



    def is_in_menu(self):
        current_stage = self.dolphin_client.read_string(self.addresslib.current_stage_addr)
        if current_stage == "s39ba":
            return True
        else:
            return False

    def is_in_match(self):
        current_stage = self.dolphin_client.read_string(self.addresslib.current_stage_addr)
        current_stage_prefix = current_stage[:3]

        if current_stage_prefix in stage_ids:
            return True
        else:
            return False

    def is_in_boss(self):
        current_stage = self.dolphin_client.read_string(self.addresslib.current_stage_addr)

        if current_stage == "s20VO":
            return True
        else:
            return False

    def is_in_tournament_map(self):
        current_stage = self.dolphin_client.read_string(self.addresslib.current_stage_addr)
        current_stage_prefix = current_stage[:3]
        maps = ["s31", "s32", "s33"]

        if current_stage_prefix in maps:
            return True
        else:
            return False

    def check_player_amount(self):
        value = self.dolphin_client.read_byte(self.addresslib.game_layout_addr)
        
        if value == 0:
            return 3
        elif value == 4:
            return 2
        else:
            return -1


    def match_status(self):
        match_status = self.dolphin_client.read_byte(self.addresslib.match_status_addr)
        if match_status == 1:
            return 1 # Won
        elif match_status == 2:
            return 2 # Lost
        elif match_status == 3:
            return 3 # Tied
        else:
            return 0 # Ongoing

    def check_sport(self):
        string_stage = self.dolphin_client.read_string(self.addresslib.current_stage_addr)
        current_sport = string_stage[-2:]
        if current_sport == "BA":
            return "Basketball"
        elif current_sport == "DO":
            return "Dodgeball"
        elif current_sport == "VO":
            return "Volleyball"
        elif current_sport == "HO":
            return "Hockey"
        else:
            return None

    # For timer -> +1800 for every 30 seconds

    def get_basketball_time(self):
        time = self.dolphin_client.read_byte(self.addresslib.basket_time_addr)

        if time == 0:
            return 5400 # 1:30
        elif time == 1:
            return 7200 # 2:00
        elif time == 2:
            return 9000 # 2:30
        elif time == 3:
            return 10800 # 3:00
        elif time == 4:
            return 12600 # 3:30
        else:
            return 99999

    def get_dodgeball_time(self):
        time = self.dolphin_client.read_byte(self.addresslib.dodge_time_addr)

        if time == 0:
            return 7200 # 2:00
        elif time == 1:
            return 9000 # 2:30
        elif time == 2:
            return 10800 # 3:00
        elif time == 3:
            return 12600 # 3:30
        elif time == 4:
            return 14400 # 4:00
        elif time == 5:
            return "Off"
        else:
            return 99999

    def get_hockey_time(self):
        time = self.dolphin_client.read_byte(self.addresslib.hockey_time_addr)

        if time == 0:
            return 7200  # 2:00
        elif time == 1:
            return 9000  # 2:30
        elif time == 2:
            return 10800  # 3:00
        elif time == 3:
            return 12600  # 3:30
        elif time == 4:
            return 14400  # 4:00
        else:
            return 99999

    def check_sports_mix(self):
        is_sports_mix = self.dolphin_client.read_byte(self.addresslib.is_sports_mix_addr)
        if is_sports_mix == 1:
            return True
        else:
            return False

    def get_exhibition_difficulty(self):
        difficulty_int = self.dolphin_client.read_byte(self.addresslib.exhibition_diff_addr)
        name = {0: "Easy", 1: "Normal", 2: "Hard", 3: "Expert"}.get(difficulty_int)

        return difficulty_int, name

    def get_tournament_difficulty(self, cup: str) -> Optional[str]:
        difficulty = self.dolphin_client.read_byte(self.addresslib.tournament_diff_addr)

        if cup == "Mushroom Cup":
            return {0: "Normal", 1: "Hard"}.get(difficulty)

        return {1: "Normal", 2: "Hard"}.get(difficulty)

    def special_active(self):
        addr = self.dolphin_client.follow_pointers(get_address(MatchAddresses.special_active),
                                                                  Offsets.Player.special_active_offsets)
        value = self.dolphin_client.read_word(addr)

        if value == 1:
            return True
        else:
            return False

    def get_connection_state(self):
        try:
            if not self.dolphin_client.is_hooked_class():
                return ConnectionState.DISCONNECTED

            if self.is_in_menu():
                return ConnectionState.IN_MENU

            if self.is_in_tournament_map():
                return ConnectionState.IN_TOURNAMENT_MAP

            if self.is_in_match():
                return ConnectionState.IN_MATCH

            if self.is_in_boss():
                return ConnectionState.IN_BOSS

            # Fallback, likely connected
            return ConnectionState.CONNECTED

        except (DolphinException, RuntimeError):
            return ConnectionState.DISCONNECTED

