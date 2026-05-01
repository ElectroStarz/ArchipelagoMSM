import enum
from .dolphin_connection import *
from .memory_addresses import *


class ConnectionState(enum):
    DISCONNECTED = 0
    CONNECTED = 1
    IN_MENU = 2
    IN_TOURNAMENT_MAP = 4
    IN_MATCH = 5
    GOALED = 6

_supported_versions = ["RMKP01"]

class MSMInterface:
    dolphin_client: DolphinClient
    connection_state: str
    logger: Logger
    game_ver: int

    match_addresses: MatchAddresses
    player_addresses: PlayerAddresses
    opponent_addresses: OpponentAddresses

    basketball_addresses: BasketballAddresses
    dodgeball_addresses: DodgeballAddresses
    volleyball_addresses: VolleyballAddresses
    hockey_addresses: HockeyAddresses

    def __init__(self, logger: Logger):
        self.logger = logger
        self.dolphin_client = DolphinClient(logger)

    def connect_to_dolphin(self):
        try:
            self.dolphin_client.attempt_to_hook()

            current_game = self.dolphin_client.read_string(MatchAddresses.game_code)
            if current_game in _supported_versions:
                self.game_ver = current_game

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
        if "s31" or "s32" or "s33" in current_stage:
            return False
        else:
            return True

    def is_in_tournament_map(self):
        current_stage = self.dolphin_client.read_string(MatchAddresses.current_stage)
        if "s31" or "s32" or "s33" in current_stage:
            return True
        else:
            return False

    def get_connection_state(self):
        try:
            connected = self.dolphin_client.is_hooked()
            if not connected or self.game_ver is None:
                return ConnectionState.DISCONNECTED
            elif self.is_in_menu():
                return ConnectionState.IN_MENU
            elif self.is_in_tournament_map():
                return ConnectionState.IN_TOURNAMENT_MAP
            elif self.is_in_match():
                return ConnectionState.IN_MATCH
            else:
                raise ConnectionError("Failed to connect to server idk what happened.")
        except DolphinException:
            return ConnectionState.DISCONNECTED