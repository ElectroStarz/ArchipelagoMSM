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

    def __init__(self, logger: Logger):
        self.logger = logger
        self.dolphin_client = DolphinClient(logger)

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


    def is_in_menu(self) -> bool:
        current_stage = self.dolphin_client.read_string(MatchAddresses.current_stage)
        if current_stage == "s39ba":
            return True
        else:
            return False

    def is_in_match(self) -> bool:
        current_stage = self.dolphin_client.read_string(MatchAddresses.current_stage)
        current_stage_prefix = current_stage[:3]
        if current_stage_prefix in stage_ids:
            return False
        else:
            return True

    def is_in_tournament_map(self) -> bool:
        current_stage = self.dolphin_client.read_string(MatchAddresses.current_stage)
        if "s31" or "s32" or "s33" in current_stage:
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

            # Fallback, likely connected
            return ConnectionState.CONNECTED

        except (DolphinException, RuntimeError):
            return ConnectionState.DISCONNECTED