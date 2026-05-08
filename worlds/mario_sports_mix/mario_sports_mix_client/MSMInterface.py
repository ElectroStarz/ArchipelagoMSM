from enum import Enum
from .dolphin_connection import *
from .memory_addresses import *


class ConnectionState(Enum):
    DISCONNECTED = 0
    CONNECTED = 1
    IN_MENU = 2
    IN_TOURNAMENT_MAP = 4
    IN_MATCH = 5
    GOALED = 6

_supported_versions = ["RMKP01"]

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

    def connect_to_dolphin(self):
        try:
            self.dolphin_client.attempt_to_hook()

            current_game_ver = self.dolphin_client.read_string(MatchAddresses.game_code)
            if current_game_ver in _supported_versions:
                self.game_ver = current_game_ver

        except DolphinException:
            print("Unsupported game version detected! Make sure you're using PAL!")

    def disconnect_from_dolphin(self):
        self.dolphin_client.disconnect()
        self.logger.info("Disconnected from Dolphin!")

    def is_in_menu(self):
        current_stage = self.dolphin_client.read_string(MatchAddresses.current_stage)
        if current_stage == "s39ba":
            return True
        else:
            return False

    def is_in_match(self):
        current_stage = self.dolphin_client.read_string(MatchAddresses.current_stage)
        current_stage_prefix = current_stage[:3]
        if current_stage_prefix in stage_ids:
            return True
        else:
            return False

    def is_in_tournament_map(self):
        current_stage = self.dolphin_client.read_string(MatchAddresses.current_stage)
        current_stage_prefix = current_stage[:3]
        if any(prefix in current_stage_prefix for prefix in ["s31", "s32", "s33"]):
            return True
        else:
            return False

    def check_player_amount(self):
        value = self.dolphin_client.read_byte(MatchAddresses.game_layout)
        if value == 0:
            return 3
        elif value == 4:
            return 2
        else:
            return -1

    def match_started(self):
        match_status = self.dolphin_client.read_byte(MatchAddresses.match_status)
        string_stage = self.dolphin_client.read_string(MatchAddresses.current_stage)
        current_stage = string_stage[0:3]
        timer = self.dolphin_client.read_float(MatchAddresses.time_remaining)
        not_match_prefix = ["s39", "s34", "s21", "s31", "s32", "s33"]

        if match_status == 0 and current_stage not in not_match_prefix and timer != 9000:
            return True
        else:
            return False

    def match_status(self):
        match_status = self.dolphin_client.read_byte(MatchAddresses.match_status)
        if match_status == 1:
            return 1 # Won
        elif match_status == 2:
            return 2 # Lost
        elif match_status == 3:
            return 3 # Tied
        else:
            return 0 # Ongoing

    def check_sport(self):
        string_stage = self.dolphin_client.read_string(MatchAddresses.current_stage)
        current_sport = string_stage[3:5]
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

    def check_ex_difficulty(self):
        ex_difficulty = self.dolphin_client.read_byte(MatchAddresses.exhibition_diff)
        if ex_difficulty == 0:
            return "Easy"
        elif ex_difficulty == 1:
            return "Normal"
        elif ex_difficulty == 2:
            return "Hard"
        elif ex_difficulty == 3:
            return "Expert"
        else:
            return None


    def check_cup(self):
        string_stage = self.dolphin_client.read_string(MatchAddresses.current_stage)
        current_stage = string_stage[0:2]
        if ConnectionState.IN_TOURNAMENT_MAP:
            if current_stage == "s31":
                self.current_tournament = "Mushroom Cup"
            elif current_stage == "s32":
                self.current_tournament = "Flower Cup"
            elif current_stage == "s33":
                self.current_tournament = "Star Cup"


    def check_t_difficulty(self):
        tournament_diff = self.dolphin_client.read_byte(MatchAddresses.tournament_diff)
        if self.current_tournament == "Mushroom Cup":
            if tournament_diff == 0:
                return "Normal"
            elif tournament_diff == 1:
                return "Hard"
        else:
            if tournament_diff == 1:
                return "Normal"
            elif tournament_diff == 2:
                return "Hard"
            else:
                return None
        return None



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

            # Fallback, likely connected
            return ConnectionState.CONNECTED

        except (DolphinException, RuntimeError):
            return ConnectionState.DISCONNECTED