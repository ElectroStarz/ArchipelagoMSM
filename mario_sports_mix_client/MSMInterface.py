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
    FEED_PETEY = 7
    HARMONY_HUSTLE = 8
    BOB_OMB_DODGE = 9
    SMASH_SKATE = 10

court_ids = ["s01", "s02", "s03", "s04", "s05", "s06", "s07", "s08", "s09", "s10", "s11", "s12", "s15", "s16", "s17"]

id_to_char = {
    255: "None",
    0: "Mario", 1: "Luigi", 2: "Peach", 3: "Daisy", 4: "Yoshi",
    5: "Wario", 6: "Waluigi", 7: "Donkey Kong", 8: "Diddy Kong", 9: "Toad",
    10: "Bowser", 11: "Bowser Jr", 12: "Moogle", 13: "Cactuar",
    14: "Ninja", 15: "White Mage", 16: "Slime", 17: "Black Mage", 18: "None",
    19: "Mii (Male)", 20: "Mii (Female)",
}

court_names = {
    # Sport Stages
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
    "s15": "Ghoulish Galleon",
    "s16": "Star Ship",
    "s17": "Western Junction",
    "s20": "Behemoth Stage",
    "s39": "Main Menu",

    # Harmony Hustle
    "s40": "Peach's Castle",
    "s41": "DK Dock",
    "s42": "Bowser Jr. Blvd.",

    # Bob-omb Dodge
    "s55": "Mario Stadium",
    "s56": "Ghoulish Galleon",
    "s57": "Western Junction",

    # Feed Petey
    "s70": "Daisy Garden",
    "s71": "DK Dock",
    "s72": "Wario Factory",

    # Smash Skate
    "s85": "Sherbet Sea",
    "s86": "Fire Mountain",
    "s87": "Rowdy Raft",

    # Misc
    "s34": "Opening Cutscene",
    "s21": "Tournament Cutscene",
}

harmony_mapping = {
    0:  "Classic Ocean",
    1:  "Chocobo Rhythm",
    2:  "Mario Athletic",
    3:  "Bloocheep Ocean",
    4:  "Chocobo Pop",
    5:  "Punk Athletic",
    6:  "Punk Ocean",
    7:  "Chocobo Beat",
    8:  "Island Athletic",
    9:  "Mushroom Mix Medley",
    10: "Blossom Mix Medley",
    11: "Star Mix Medley",
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

fp_opp_score_addresses = [
    OpponentAddresses.Score.r1_fp_score,
    OpponentAddresses.Score.r2_fp_score,
    OpponentAddresses.Score.r3_fp_score,
]

bod_opp_damage_pointers = [
    Pointers.Opponent.R1.bod_dodge_damage,
    Pointers.Opponent.R2.bod_dodge_damage,
    Pointers.Opponent.R3.bod_dodge_damage,
]

ss_opp_score_pointers = [
    Pointers.Opponent.R1.ss_score,
    Pointers.Opponent.R2.ss_score,
    Pointers.Opponent.R3.ss_score,
]

class MSMInterface:
    dolphin_client: DolphinClient
    connection_state: str
    logger: Logger
    game_ver: int
    current_tournament: Optional[str] = None

    def __init__(self, logger: Logger):
        self.logger = logger
        self.dolphin_client = DolphinClient(logger)
        self.current_tournament = None
        self.addresslib = AddressLib()

    def is_in_menu(self):
        current_court = self.dolphin_client.read_string(self.addresslib.current_court_addr)
        if current_court == "s39ba":
            return True
        else:
            return False

    def is_in_match(self):
        current_court = self.dolphin_client.read_string(self.addresslib.current_court_addr)
        current_stage_prefix = current_court[:3]

        if current_stage_prefix in court_ids:
            return True
        else:
            return False

    def is_in_boss(self):
        current_stage = self.dolphin_client.read_string(self.addresslib.current_court_addr)

        if current_stage == "s20VO":
            return True
        else:
            return False

    def is_in_tournament_map(self):
        current_stage = self.dolphin_client.read_string(self.addresslib.current_court_addr)
        current_stage_prefix = current_stage[:3]

        if current_stage_prefix in ["s31", "s32", "s33"]:
            return True
        else:
            return False

    def is_in_feed_petey(self):
        current_stage = self.dolphin_client.read_string(self.addresslib.current_court_addr)
        current_stage_prefix = current_stage[:3]

        if current_stage_prefix in ["s70", "s71", "s72"]:
            return True
        else:
            return False

    def is_in_harmony(self):
        current_stage = self.dolphin_client.read_string(self.addresslib.current_court_addr)
        current_stage_prefix = current_stage[:3]

        if current_stage_prefix in ["s40", "s41", "s42"]:
            return True
        else:
            return False

    def is_in_bob_omb(self):
        current_stage = self.dolphin_client.read_string(self.addresslib.current_court_addr)
        current_stage_prefix = current_stage[:3]

        if current_stage_prefix in ["s55", "s56", "s57"]:
            return True
        else:
            return False

    def is_in_smash(self):
        current_stage = self.dolphin_client.read_string(self.addresslib.current_court_addr)
        current_stage_prefix = current_stage[:3]

        if current_stage_prefix in ["s85", "s86", "s87"]:
            return True
        else:
            return False

    def check_team_amount(self):
        value = self.dolphin_client.read_byte(self.addresslib.game_layout_addr)
        
        if value == 0:
            return 3
        elif value == 4:
            return 2
        else:
            return -1

    def get_p_character(self, character: int):
        ls_char = character - 1

        addresses = [PlayerAddresses.character_1, PlayerAddresses.character_2, PlayerAddresses.character_3]

        value = self.dolphin_client.read_byte(get_address(addresses[ls_char]))

        return id_to_char.get(value, "None")

    def get_player_score_addr(self):
        if self.is_in_match():
            current_period = self.dolphin_client.read_byte(self.addresslib.current_period_addr)
            return get_address(player_score_addresses[current_period])
        elif self.is_in_feed_petey():
            return get_address(PlayerAddresses.Score.feed_petey_score)
        elif self.is_in_bob_omb():
            return self.dolphin_client.follow_pointers(get_address(PlayerAddresses.various_shp_pointers),
                                                       Pointers.Player.B1.bod_dodge_damage)
        elif self.is_in_harmony():
            return self.dolphin_client.follow_pointers(get_address(PlayerAddresses.various_shp_pointers),
                                                       Pointers.PartyMode.hh_current_score)
        elif self.is_in_smash():
            return self.dolphin_client.follow_pointers(get_address(PlayerAddresses.various_shp_pointers),
                                                       Pointers.Player.B1.ss_score)
        else: return None

    def get_opponent_score_addr(self, opponent: int):
        ls_opponent = opponent - 1
        if self.is_in_match():
            current_period = self.dolphin_client.read_byte(self.addresslib.current_period_addr)
            return get_address(opponent_score_addresses[current_period])
        elif self.is_in_feed_petey():
            return get_address(fp_opp_score_addresses[ls_opponent])
        elif self.is_in_bob_omb():
            return self.dolphin_client.follow_pointers(get_address(PlayerAddresses.various_shp_pointers),
                                                       bod_opp_damage_pointers[ls_opponent])
        elif self.is_in_harmony():
            return self.dolphin_client.follow_pointers(get_address(PlayerAddresses.various_shp_pointers),
                                                       Pointers.PartyMode.hh_current_score)
        elif self.is_in_smash():
            return self.dolphin_client.follow_pointers(get_address(PlayerAddresses.various_shp_pointers),
                                                       ss_opp_score_pointers[ls_opponent])
        else: return None

    def match_status(self):
        return self.dolphin_client.read_byte(self.addresslib.match_status_addr)

    def get_court(self):
        """Returns the current court ID and name"""

        if not self.is_in_harmony():
            base_id = self.dolphin_client.read_string(self.addresslib.current_court_addr)
            court_id = base_id[:3]
            court_name = court_names.get(court_id)

            return court_id, court_name
        else:

            court_id = self.dolphin_client.read_word(get_address(PartyMode.difficulty))
            court_name = harmony_mapping.get(court_id)

            return court_id, court_name

    def get_mode(self):
        current_sport_value = self.dolphin_client.read_byte(get_address(GlobalTournament.current_sport))
        current_sport = {0: "BA", 1: "VO", 2: "DO", 3: "HO", 5: "SM"}.get(current_sport_value)
        
        if self.is_in_feed_petey():
            return "Feed Petey"
        elif self.is_in_harmony():
            return "Harmony Hustle"
        elif self.is_in_bob_omb():
            return "Bob-omb Dodge"
        elif self.is_in_smash():
            return "Smash Skate"
        elif current_sport == "BA":
            return "Basketball"
        elif current_sport == "DO":
            return "Dodgeball"
        elif current_sport == "VO":
            return "Volleyball"
        elif current_sport == "HO":
            return "Hockey"
        elif current_sport == "SM":
            return "Sports Mix"
        else:
            return None

    def get_tab(self):
        diff = self.dolphin_client.read_word(PartyMode.difficulty)
            
        if self.is_in_feed_petey():
            return {0: "Apple", 1: "Watermelon"}.get(diff)
            
        elif self.is_in_bob_omb():
            return {0: "Bob-Omb", 1: "Cannon"}.get(diff)
            
        elif self.is_in_smash():
            return {0: "Hockey Stick", 1: "Hockey Skate"}.get(diff)
        else:
            return "HH ERROR"

    # For timer: +1800 for every 30 seconds

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

    def is_sports_mix(self):
        is_sports_mix = self.dolphin_client.read_byte(self.addresslib.is_sports_mix_addr)
        if is_sports_mix == 1:
            return True
        else:
            return False

    def get_exhibition_difficulty(self):
        difficulty_int = self.dolphin_client.read_byte(self.addresslib.exhibition_diff_addr)
        name = {0: "Easy", 1: "Normal", 2: "Hard", 3: "Expert"}.get(difficulty_int)

        return difficulty_int, name

    def get_tournament_difficulty(self) -> Optional[str]:
        difficulty = self.dolphin_client.read_byte(self.addresslib.tournament_diff_addr)
        cup = self.get_tournament_cup()

        if cup == "Mushroom":
            return {0: "Normal", 1: "Hard"}.get(difficulty)

        return {1: "Normal", 2: "Hard"}.get(difficulty)

    def get_tournament_cup(self):

        cup = self.dolphin_client.read_byte(get_address(GlobalTournament.current_tournament_cup))

        if cup not in [1, 2, 3]:
            return "Not in Tournament"
        else:
            return {1: "Mushroom", 2: "Flower", 3: "Star"}.get(cup)

    def get_tournament_round(self):
        round = self.dolphin_client.read_byte(get_address(GlobalTournament.current_tournament_round))

        if round not in [1, 2, 3]:
            return "Not in Tournament"
        else:
            return {1: "Round 1", 2: "Round 2", 3: "Round 3"}.get(round)

    def get_tournament_sport(self):
        sport = self.dolphin_client.read_byte(get_address(GlobalTournament.current_tournament_sport_variation))

        if sport not in [0, 1, 2, 3, 5]:
            return "Not in Tournament"
        else:
            return {0: "Basketball", 1: "Volleyball", 2: "Dodgeball", 3: "Hockey", 5: "Sports Mix"}.get(sport)

    def get_player_current_node(self):
        node = self.dolphin_client.read_byte(get_address(GlobalTournament.player_current_node))

        return node
    
    def special_active(self):
        try:
            value = self.dolphin_client.read_pointer(get_address(MatchAddresses.special_active),
                                                     Pointers.Player.special_active_offsets, "word")

            if value == 1:
                return True
            else:
                return False
        except RuntimeError:
            return False


    def get_music_file_name(self, music_name: str):
        # the big evil dictionary of doooooom
        music_to_file = {
            "title_theme": "BGM_MENU_01",
            "exhibition_settings": "BGM_MENU_04",
            "wifi_menu": "BGM_MENU_05",
            "records_menu": "BGM_MENU_06",
            "mario_stadium": "BGM_STAGE_01",
            "mario_stadium_fast": "BGM_STAGE_H01",
            "koopa_troopa_beach": "BGM_STAGE_02",
            "koopa_troopa_beach_fast": "BGM_STAGE_H02",
            "peachs_castle": "BGM_STAGE_03",
            "peachs_castle_fast": "BGM_STAGE_H03",
            "toad_park": "BGM_STAGE_04",
            "toad_park_fast": "BGM_STAGE_H04",
            "dk_dock": "BGM_STAGE_05",
            "dk_dock_fast": "BGM_STAGE_H05",
            "luigis_mansion": "BGM_STAGE_06",
            "luigis_mansion_fast": "BGM_STAGE_H06",
            "daisy_garden": "BGM_STAGE_07",
            "daisy_garden_fast": "BGM_STAGE_H07",
            "wario_factory": "BGM_STAGE_09",
            "wario_factory_fast": "BGM_STAGE_H09",
            "bowser_jr_blvd": "BGM_STAGE_10",
            "bowser_jr_blvd_fast": "BGM_STAGE_H10",
            "bowsers_castle": "BGM_STAGE_11",
            "bowsers_castle_fast": "BGM_STAGE_H11",
            "waluigi_pinball": "BGM_STAGE_12",
            "waluigi_pinball_fast": "BGM_STAGE_H12",
            "ghoulish_galleon": "BGM_STAGE_15",
            "ghoulish_galleon_fast": "BGM_STAGE_H15",
            "star_ship": "BGM_STAGE_16",
            "star_ship_fast": "BGM_STAGE_H16",
            "western_junction": "BGM_STAGE_17",
            "western_junction_fast": "BGM_STAGE_H17",
            "behemoth_stage": "BGM_STAGE_20",
            "behemoth_stage_fast": "BGM_STAGE_H20",
            "behemoth_battle": "BGM_STAGE_20",
            "behemoth_battle_fast": "BGM_STAGE_H20",
            "smash_skate_normal": "BGM_PARTY_01",
            "smash_skate_normal_fast": "BGM_PARTY_H01",
            "feed_petey_normal": "BGM_PARTY_02",
            "feed_petey_bonus_time": "BGM_PARTY_02_ARR",
            "feed_petey_normal_fast": "BGM_PARTY_H02",
            "bob_omb_dodge_normal": "BGM_PARTY_03",
            "bob_omb_dodge_normal_fast": "BGM_PARTY_H03",
            "harmony_hustle_normal": "BGM_PARTY_04",
            "harmony_hustle_normal_fast": "BGM_PARTY_H04",
            "smash_skate_hard": "BGM_PARTY_05",
            "smash_skate_hard_fast": "BGM_PARTY_H05",
            "feed_petey_hard": "BGM_PARTY_06",
            "feed_petey_hard_fast": "BGM_PARTY_H06",
            "bob_omb_dodge_hard": "BGM_PARTY_07",
            "bob_omb_dodge_hard_fast": "BGM_PARTY_H07",
            "tournament_opening": "BGM_TOURNAMENT_00",
            "mushroom_cup": "BGM_TOURNAMENT_01",
            "flower_cup": "BGM_TOURNAMENT_02",
            "star_cup": "BGM_TOURNAMENT_03",
            "tournament_victory": "FANFARE_01_SEmix",
            "win_1": "BGM_WIN_01",
            "lose_1": "BGM_LOSE_01",
            "win_2": "BGM_WIN_02",
            "lose_2": "BGM_LOSE_02",
            "matching": "BGM_MATCHING",
            "results": "BGM_RESULT",
            "get_item": "BGM_GETITEM",
            "starman": "BGM_STAR_01",
            "star_road_complete": "BGM_STAR_02",
            "classic_ocean": "OTOGAME_00_PREVIEW_LP",
            "chocobo_rhythm": "OTOGAME_01_PREVIEW_LP",
            "mario_athletic": "OTOGAME_02_PREVIEW_LP",
            "bloocheep_ocean": "OTOGAME_03_PREVIEW_LP",
            "chocobo_pop": "OTOGAME_04_PREVIEW_LP",
            "chcocobo_pop": "OTOGAME_04_PREVIEW_LP",
            "punk_athletic": "OTOGAME_05_PREVIEW_LP",
            "punk_ocean": "OTOGAME_06_PREVIEW_LP",
            "chocobo_beat": "OTOGAME_07_PREVIEW_LP",
            "island_athletic": "OTOGAME_08_PREVIEW_LP",
            "mushroom_mix_medley": "OTOGAME_09_PREVIEW_LP",
            "flower_mix_medley": "OTOGAME_10_PREVIEW_LP",
            "star_mix_medley": "OTOGAME_11_PREVIEW_LP",
        }

        file_name = music_to_file.get(music_name)

        if file_name is None:
            self.logger.warning(f"No file for {music_name}")
            return None
    
        return file_name + ".brstm"

    def replace_music_file(self, music_to_be_replaced: str, music_to_replace_with: str) -> bool:
        classes = [MusicFiles.MenuSongs, MusicFiles.StageSongs, MusicFiles.PartySongs, MusicFiles.TournamentSongs, MusicFiles.MiscSongs, MusicFiles.HarmonyHustlePreviews]
        address = None

        for cls in classes:
            songs = self.get_songs_from_class(cls)
            if music_to_be_replaced in songs:
                address = get_address(cls.__dict__[music_to_be_replaced])
                break

        original_length = len(self.get_music_file_name(music_to_be_replaced)) 
        new_length = len(self.get_music_file_name(music_to_replace_with))
        new_song = self.get_music_file_name(music_to_replace_with)


        self.logger.info(f"Replacing {music_to_be_replaced} with {music_to_replace_with} at address 0x{address:X}")
        self.dolphin_client.write_string(address, new_song)

        # Clearing in case stale stuff gets in the way
        for _ in range(original_length - new_length - 2):
            self.dolphin_client.write_byte(address + new_length, 0x00)
            new_length += 1
        self.dolphin_client.write_byte(address + new_length, 0x00)
        new_length += 1
        self.dolphin_client.write_byte(address + new_length, 0x00)
        
            
    def get_songs_from_class(self, cls):
        songs = []
        for attr in dir(cls):
            if not attr.startswith("__") and not attr.startswith("base") and not attr.startswith("offset"):
                songs.append(attr)
        return songs

    def get_connection_state(self):
        try:
            if not self.dolphin_client.is_hooked():
                return ConnectionState.DISCONNECTED

            if self.is_in_menu():
                return ConnectionState.IN_MENU

            if self.is_in_tournament_map():
                return ConnectionState.IN_TOURNAMENT_MAP

            if self.is_in_match():
                return ConnectionState.IN_MATCH

            if self.is_in_boss():
                return ConnectionState.IN_BOSS

            if self.is_in_feed_petey():
                return ConnectionState.FEED_PETEY

            if self.is_in_harmony():
                return ConnectionState.HARMONY_HUSTLE

            if self.is_in_bob_omb():
                return ConnectionState.BOB_OMB_DODGE

            if self.is_in_smash():
                return ConnectionState.SMASH_SKATE

            # Fallback, likely connected
            return ConnectionState.CONNECTED

        except (DolphinException, RuntimeError):
            return ConnectionState.DISCONNECTED
