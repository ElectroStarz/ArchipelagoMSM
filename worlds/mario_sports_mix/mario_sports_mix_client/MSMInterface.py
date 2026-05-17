from enum import Enum
from .dolphin_connection import *
from .memory_addresses_pal import *
from typing import Optional


class ConnectionState(Enum):
    DISCONNECTED = 0
    CONNECTED = 1
    IN_MENU = 2
    IN_TOURNAMENT_MAP = 4
    IN_MATCH = 5
    IN_BOSS = 6
    GOALED = 7

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

    def is_in_boss(self):
        current_stage = self.dolphin_client.read_string(MatchAddresses.current_stage)
        if current_stage == "s20VO":
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

    def ready_to_handle(self):
        match_status = self.dolphin_client.read_byte(MatchAddresses.match_status)
        string_stage = self.dolphin_client.read_string(MatchAddresses.current_stage)
        current_stage = string_stage[0:3]
        timer = self.dolphin_client.read_float(MatchAddresses.time_remaining)
        on_loading_screen = self.dolphin_client.read_word(MatchAddresses.on_loading_screen)
        not_match_prefix = ["s39", "s34", "s21", "s31", "s32", "s33"]
        ready_game = bool

        if match_status == 0 and current_stage not in not_match_prefix:
            if self.check_sport() == "Basketball":
                if timer < 9000:
                    ready_game = True
                else:
                    ready_game = False

            elif self.check_sport() == "Dodgeball":
                if timer < 10800:
                    ready_game = True
                else:
                    ready_game = False

            elif self.check_sport() == "Volleyball":
                if current_stage == "s20":
                    try:
                        self.dolphin_client.follow_pointers(
                            BossAddresses.behemoth_hp,
                            Offsets.Boss.behemoth_hp_offsets
                        )
                        ready_game = True
                    except RuntimeError:
                        ready_game = False
                else:
                    try:
                        # Check if you can follow pointers to the address, if so, then ready
                        self.dolphin_client.follow_pointers(
                            VolleyballAddresses.last_held,
                            Offsets.Volleyball.last_held_offsets
                        )
                        ready_game = True
                    except RuntimeError:
                        ready_game = False
            elif self.check_sport() == "Hockey":
                if timer < 10800:
                    ready_game = True
                else:
                    ready_game = False
        else:
            ready_game = False

        if on_loading_screen == 1:
            loading_screen_active = False
        else:
            loading_screen_active = True


        if ready_game and not loading_screen_active:
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

    def check_sports_mix(self):
        is_sports_mix = self.dolphin_client.read_byte(SportsMixAddresses.is_sports_mix)
        if is_sports_mix == 1:
            return True
        else:
            return False

    def get_exhibition_difficulty(self):
        difficulty = self.dolphin_client.read_byte(MatchAddresses.exhibition_diff)

        return {0: "Easy", 1: "Normal", 2: "Hard", 3: "Expert"}.get(difficulty)

    def get_tournament_difficulty(self, cup: str) -> Optional[str]:
        difficulty = self.dolphin_client.read_byte(MatchAddresses.tournament_diff)

        if cup == "Mushroom Cup":
            return {0: "Normal", 1: "Hard"}.get(difficulty)

        return {1: "Normal", 2: "Hard"}.get(difficulty)

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