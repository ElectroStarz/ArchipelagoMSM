from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, NamedTuple, Dict

from BaseClasses import Location
from . import items
from .options import GoalCondition, BeMean, HardTournamentDifficulty, CharacterSanity

if TYPE_CHECKING:
    from . import MSMWorld

class MSMLocation(Location):
    game = "Mario Sports Mix"


class LocationGroup(str, Enum):
    # === Cup Groups ===
    BASKETBALL_NORMAL_CUPS = "Basketball Normal Cups"
    BASKETBALL_HARD_CUPS = "Basketball Hard Cups"

    DODGEBALL_NORMAL_CUPS = "Dodgeball Normal Cups"
    DODGEBALL_HARD_CUPS = "Dodgeball Hard Cups"

    VOLLEYBALL_NORMAL_CUPS = "Volleyball Normal Cups"
    VOLLEYBALL_HARD_CUPS = "Volleyball Hard Cups"

    HOCKEY_NORMAL_CUPS = "Hockey Normal Cups"
    HOCKEY_HARD_CUPS = "Hockey Hard Cups"

    SPORTS_MIX_CUPS = "Sports Mix Cups"

    # === Basketball Exhibitions ===
    BASKETBALL_EX_EASY = "Basketball Exhibition Easy"
    BASKETBALL_EX_NORMAL = "Basketball Exhibition Normal"
    BASKETBALL_EX_HARD = "Basketball Exhibition Hard"
    BASKETBALL_EX_EXPERT = "Basketball Exhibition Expert"

    # === Dodgeball Exhibitions ===
    DODGEBALL_EX_EASY = "Dodgeball Exhibition Easy"
    DODGEBALL_EX_NORMAL = "Dodgeball Exhibition Normal"
    DODGEBALL_EX_HARD = "Dodgeball Exhibition Hard"
    DODGEBALL_EX_EXPERT = "Dodgeball Exhibition Expert"

    # === Volleyball Exhibitions ===
    VOLLEYBALL_EX_EASY = "Volleyball Exhibition Easy"
    VOLLEYBALL_EX_NORMAL = "Volleyball Exhibition Normal"
    VOLLEYBALL_EX_HARD = "Volleyball Exhibition Hard"
    VOLLEYBALL_EX_EXPERT = "Volleyball Exhibition Expert"

    # === Hockey Exhibitions ===
    HOCKEY_EX_EASY = "Hockey Exhibition Easy"
    HOCKEY_EX_NORMAL = "Hockey Exhibition Normal"
    HOCKEY_EX_HARD = "Hockey Exhibition Hard"
    HOCKEY_EX_EXPERT = "Hockey Exhibition Expert"

    # === Sanity & Misc ===
    SPECIAL_SANITY = "Special Sanity"
    CHARACTER_SANITY = "Character Sanity"
    COSTUME_SANITY = "Costume Sanity"
    BOSS_LOCATIONS = "Boss Locations"

class LocationData(NamedTuple):
    id: int
    group: LocationGroup



def create_all_locations(world: "MSMWorld") -> None:
    create_regular_locations(world)
    create_events(world)


base_loc_id = 0


location_table: Dict[str, LocationData] = {

    # === Beating Cup Round Locations ===
    # === Normal ===
    # Basketball
    "Basketball: Beat Normal Mushroom Cup Round 1": LocationData(base_loc_id + 1, LocationGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Mushroom Cup Round 2": LocationData(base_loc_id + 2, LocationGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Mushroom Cup Round 3": LocationData(base_loc_id + 3, LocationGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Flower Cup Round 1": LocationData(base_loc_id + 4, LocationGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Flower Cup Round 2": LocationData(base_loc_id + 5, LocationGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Flower Cup Round 3": LocationData(base_loc_id + 6, LocationGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Star Cup Round 1": LocationData(base_loc_id + 7, LocationGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Star Cup Round 2": LocationData(base_loc_id + 8, LocationGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Star Cup Round 3": LocationData(base_loc_id + 9, LocationGroup.BASKETBALL_NORMAL_CUPS),

    # Dodgeball
    "Dodgeball: Beat Normal Mushroom Cup Round 1": LocationData(base_loc_id + 10, LocationGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Mushroom Cup Round 2": LocationData(base_loc_id + 11, LocationGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Mushroom Cup Round 3": LocationData(base_loc_id + 12, LocationGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Flower Cup Round 1": LocationData(base_loc_id + 13, LocationGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Flower Cup Round 2": LocationData(base_loc_id + 14, LocationGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Flower Cup Round 3": LocationData(base_loc_id + 15, LocationGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Star Cup Round 1": LocationData(base_loc_id + 16, LocationGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Star Cup Round 2": LocationData(base_loc_id + 17, LocationGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Star Cup Round 3": LocationData(base_loc_id + 18, LocationGroup.DODGEBALL_NORMAL_CUPS),

    # Volleyball
    "Volleyball: Beat Normal Mushroom Cup Round 1": LocationData(base_loc_id + 19,
                                                                 LocationGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Mushroom Cup Round 2": LocationData(base_loc_id + 20,
                                                                 LocationGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Mushroom Cup Round 3": LocationData(base_loc_id + 21,
                                                                 LocationGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Flower Cup Round 1": LocationData(base_loc_id + 22, LocationGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Flower Cup Round 2": LocationData(base_loc_id + 23, LocationGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Flower Cup Round 3": LocationData(base_loc_id + 24, LocationGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Star Cup Round 1": LocationData(base_loc_id + 25, LocationGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Star Cup Round 2": LocationData(base_loc_id + 26, LocationGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Star Cup Round 3": LocationData(base_loc_id + 27, LocationGroup.VOLLEYBALL_NORMAL_CUPS),

    # Hockey
    "Hockey: Beat Normal Mushroom Cup Round 1": LocationData(base_loc_id + 28, LocationGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Mushroom Cup Round 2": LocationData(base_loc_id + 29, LocationGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Mushroom Cup Round 3": LocationData(base_loc_id + 30, LocationGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Flower Cup Round 1": LocationData(base_loc_id + 31, LocationGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Flower Cup Round 2": LocationData(base_loc_id + 32, LocationGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Flower Cup Round 3": LocationData(base_loc_id + 33, LocationGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Star Cup Round 1": LocationData(base_loc_id + 34, LocationGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Star Cup Round 2": LocationData(base_loc_id + 35, LocationGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Star Cup Round 3": LocationData(base_loc_id + 36, LocationGroup.HOCKEY_NORMAL_CUPS),

    # === Hard ===
    # Basketball
    "Basketball: Beat Hard Mushroom Cup Round 1": LocationData(base_loc_id + 37, LocationGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Mushroom Cup Round 2": LocationData(base_loc_id + 38, LocationGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Mushroom Cup Round 3": LocationData(base_loc_id + 39, LocationGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Flower Cup Round 1": LocationData(base_loc_id + 40, LocationGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Flower Cup Round 2": LocationData(base_loc_id + 41, LocationGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Flower Cup Round 3": LocationData(base_loc_id + 42, LocationGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Star Cup Round 1": LocationData(base_loc_id + 43, LocationGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Star Cup Round 2": LocationData(base_loc_id + 44, LocationGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Star Cup Round 3": LocationData(base_loc_id + 45, LocationGroup.BASKETBALL_HARD_CUPS),

    # Dodgeball
    "Dodgeball: Beat Hard Mushroom Cup Round 1": LocationData(base_loc_id + 46, LocationGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Mushroom Cup Round 2": LocationData(base_loc_id + 47, LocationGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Mushroom Cup Round 3": LocationData(base_loc_id + 48, LocationGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Flower Cup Round 1": LocationData(base_loc_id + 49, LocationGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Flower Cup Round 2": LocationData(base_loc_id + 50, LocationGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Flower Cup Round 3": LocationData(base_loc_id + 51, LocationGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Star Cup Round 1": LocationData(base_loc_id + 52, LocationGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Star Cup Round 2": LocationData(base_loc_id + 53, LocationGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Star Cup Round 3": LocationData(base_loc_id + 54, LocationGroup.DODGEBALL_HARD_CUPS),

    # Volleyball
    "Volleyball: Beat Hard Mushroom Cup Round 1": LocationData(base_loc_id + 55, LocationGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Mushroom Cup Round 2": LocationData(base_loc_id + 56, LocationGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Mushroom Cup Round 3": LocationData(base_loc_id + 57, LocationGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Flower Cup Round 1": LocationData(base_loc_id + 58, LocationGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Flower Cup Round 2": LocationData(base_loc_id + 59, LocationGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Flower Cup Round 3": LocationData(base_loc_id + 60, LocationGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Star Cup Round 1": LocationData(base_loc_id + 61, LocationGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Star Cup Round 2": LocationData(base_loc_id + 62, LocationGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Star Cup Round 3": LocationData(base_loc_id + 63, LocationGroup.VOLLEYBALL_HARD_CUPS),

    # Hockey
    "Hockey: Beat Hard Mushroom Cup Round 1": LocationData(base_loc_id + 64, LocationGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Mushroom Cup Round 2": LocationData(base_loc_id + 65, LocationGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Mushroom Cup Round 3": LocationData(base_loc_id + 66, LocationGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Flower Cup Round 1": LocationData(base_loc_id + 67, LocationGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Flower Cup Round 2": LocationData(base_loc_id + 68, LocationGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Flower Cup Round 3": LocationData(base_loc_id + 69, LocationGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Star Cup Round 1": LocationData(base_loc_id + 70, LocationGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Star Cup Round 2": LocationData(base_loc_id + 71, LocationGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Star Cup Round 3": LocationData(base_loc_id + 72, LocationGroup.HOCKEY_HARD_CUPS),

    # === Sports Mix Locations ===
    "Sports Mix: Beat Mushroom Cup Round 1": LocationData(base_loc_id + 73, LocationGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Mushroom Cup Round 2": LocationData(base_loc_id + 74, LocationGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Mushroom Cup Round 3": LocationData(base_loc_id + 75, LocationGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Flower Cup Round 1": LocationData(base_loc_id + 76, LocationGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Flower Cup Round 2": LocationData(base_loc_id + 77, LocationGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Flower Cup Round 3": LocationData(base_loc_id + 78, LocationGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Star Cup Round 1": LocationData(base_loc_id + 79, LocationGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Star Cup Round 2": LocationData(base_loc_id + 80, LocationGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Star Cup Round 3": LocationData(base_loc_id + 81, LocationGroup.SPORTS_MIX_CUPS),

    # === Easy Exhibition Locations ===
    # Basketball
    "Basketball Ex: Beat Mario Stadium (Easy)": LocationData(base_loc_id + 200, LocationGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Koopa Troopa Beach (Easy)": LocationData(base_loc_id + 201, LocationGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat DK Dock (Easy)": LocationData(base_loc_id + 202, LocationGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Luigi's Mansion (Easy)": LocationData(base_loc_id + 203, LocationGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Western Junction (Easy)": LocationData(base_loc_id + 204, LocationGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Daisy Garden (Easy)": LocationData(base_loc_id + 205, LocationGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Bowser Jr. Blvd. (Easy)": LocationData(base_loc_id + 206, LocationGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Bowser's Castle (Easy)": LocationData(base_loc_id + 207, LocationGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Star Ship (Easy)": LocationData(base_loc_id + 208, LocationGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Peach's Castle (Easy)": LocationData(base_loc_id + 209, LocationGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Wario Factory (Easy)": LocationData(base_loc_id + 210, LocationGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Ghoulish Galleon (Easy)": LocationData(base_loc_id + 211, LocationGroup.BASKETBALL_EX_EASY),

    # Dodgeball
    "Dodgeball Ex: Beat Mario Stadium (Easy)": LocationData(base_loc_id + 212, LocationGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Koopa Troopa Beach (Easy)": LocationData(base_loc_id + 213, LocationGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Peach's Castle (Easy)": LocationData(base_loc_id + 214, LocationGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat DK Dock (Easy)": LocationData(base_loc_id + 215, LocationGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Toad Park (Easy)": LocationData(base_loc_id + 216, LocationGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Daisy Garden (Easy)": LocationData(base_loc_id + 217, LocationGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Wario Factory (Easy)": LocationData(base_loc_id + 218, LocationGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Bowser's Castle (Easy)": LocationData(base_loc_id + 219, LocationGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Star Ship (Easy)": LocationData(base_loc_id + 220, LocationGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Western Junction (Easy)": LocationData(base_loc_id + 221, LocationGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Waluigi Pinball (Easy)": LocationData(base_loc_id + 222, LocationGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Ghoulish Galleon (Easy)": LocationData(base_loc_id + 223, LocationGroup.DODGEBALL_EX_EASY),

    # Volleyball
    "Volleyball Ex: Beat Mario Stadium (Easy)": LocationData(base_loc_id + 224, LocationGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Koopa Troopa Beach (Easy)": LocationData(base_loc_id + 225, LocationGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Peach's Castle (Easy)": LocationData(base_loc_id + 226, LocationGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat DK Dock (Easy)": LocationData(base_loc_id + 227, LocationGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Luigi's Mansion (Easy)": LocationData(base_loc_id + 228, LocationGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Western Junction (Easy)": LocationData(base_loc_id + 229, LocationGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Bowser Jr. Blvd. (Easy)": LocationData(base_loc_id + 230, LocationGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Bowser's Castle (Easy)": LocationData(base_loc_id + 231, LocationGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Star Ship (Easy)": LocationData(base_loc_id + 232, LocationGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Wario Factory (Easy)": LocationData(base_loc_id + 233, LocationGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Waluigi Pinball (Easy)": LocationData(base_loc_id + 234, LocationGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Ghoulish Galleon (Easy)": LocationData(base_loc_id + 235, LocationGroup.VOLLEYBALL_EX_EASY),

    # Hockey
    "Hockey Ex: Beat Mario Stadium (Easy)": LocationData(base_loc_id + 236, LocationGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Toad Park (Easy)": LocationData(base_loc_id + 237, LocationGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Peach's Castle (Easy)": LocationData(base_loc_id + 238, LocationGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Western Junction (Easy)": LocationData(base_loc_id + 239, LocationGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Wario Factory (Easy)": LocationData(base_loc_id + 240, LocationGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Daisy Garden (Easy)": LocationData(base_loc_id + 241, LocationGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Bowser Jr. Blvd. (Easy)": LocationData(base_loc_id + 242, LocationGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Waluigi Pinball (Easy)": LocationData(base_loc_id + 243, LocationGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Star Ship (Easy)": LocationData(base_loc_id + 244, LocationGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Koopa Troopa Beach (Easy)": LocationData(base_loc_id + 245, LocationGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Ghoulish Galleon (Easy)": LocationData(base_loc_id + 246, LocationGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Bowser's Castle (Easy)": LocationData(base_loc_id + 247, LocationGroup.HOCKEY_EX_EASY),

    # === Normal Exhibition Locations ===
    # Basketball
    "Basketball Ex: Beat Mario Stadium (Normal)": LocationData(base_loc_id + 300, LocationGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Koopa Troopa Beach (Normal)": LocationData(base_loc_id + 301,
                                                                    LocationGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat DK Dock (Normal)": LocationData(base_loc_id + 302, LocationGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Luigi's Mansion (Normal)": LocationData(base_loc_id + 303, LocationGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Western Junction (Normal)": LocationData(base_loc_id + 304,
                                                                  LocationGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Daisy Garden (Normal)": LocationData(base_loc_id + 305, LocationGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Bowser Jr. Blvd. (Normal)": LocationData(base_loc_id + 306,
                                                                  LocationGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Bowser's Castle (Normal)": LocationData(base_loc_id + 307, LocationGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Star Ship (Normal)": LocationData(base_loc_id + 308, LocationGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Peach's Castle (Normal)": LocationData(base_loc_id + 309, LocationGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Wario Factory (Normal)": LocationData(base_loc_id + 310, LocationGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Ghoulish Galleon (Normal)": LocationData(base_loc_id + 311,
                                                                  LocationGroup.BASKETBALL_EX_NORMAL),

    # Dodgeball
    "Dodgeball Ex: Beat Mario Stadium (Normal)": LocationData(base_loc_id + 312, LocationGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Koopa Troopa Beach (Normal)": LocationData(base_loc_id + 313,
                                                                   LocationGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Peach's Castle (Normal)": LocationData(base_loc_id + 314, LocationGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat DK Dock (Normal)": LocationData(base_loc_id + 315, LocationGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Toad Park (Normal)": LocationData(base_loc_id + 316, LocationGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Daisy Garden (Normal)": LocationData(base_loc_id + 317, LocationGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Wario Factory (Normal)": LocationData(base_loc_id + 318, LocationGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Bowser's Castle (Normal)": LocationData(base_loc_id + 319, LocationGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Star Ship (Normal)": LocationData(base_loc_id + 320, LocationGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Western Junction (Normal)": LocationData(base_loc_id + 321, LocationGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Waluigi Pinball (Normal)": LocationData(base_loc_id + 322, LocationGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Ghoulish Galleon (Normal)": LocationData(base_loc_id + 323, LocationGroup.DODGEBALL_EX_NORMAL),

    # Volleyball
    "Volleyball Ex: Beat Mario Stadium (Normal)": LocationData(base_loc_id + 324, LocationGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Koopa Troopa Beach (Normal)": LocationData(base_loc_id + 325,
                                                                    LocationGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Peach's Castle (Normal)": LocationData(base_loc_id + 326, LocationGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat DK Dock (Normal)": LocationData(base_loc_id + 327, LocationGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Luigi's Mansion (Normal)": LocationData(base_loc_id + 328, LocationGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Western Junction (Normal)": LocationData(base_loc_id + 329,
                                                                  LocationGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Bowser Jr. Blvd. (Normal)": LocationData(base_loc_id + 330,
                                                                  LocationGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Bowser's Castle (Normal)": LocationData(base_loc_id + 331, LocationGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Star Ship (Normal)": LocationData(base_loc_id + 332, LocationGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Wario Factory (Normal)": LocationData(base_loc_id + 333, LocationGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Waluigi Pinball (Normal)": LocationData(base_loc_id + 334, LocationGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Ghoulish Galleon (Normal)": LocationData(base_loc_id + 335,
                                                                  LocationGroup.VOLLEYBALL_EX_NORMAL),

    # Hockey
    "Hockey Ex: Beat Mario Stadium (Normal)": LocationData(base_loc_id + 336, LocationGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Toad Park (Normal)": LocationData(base_loc_id + 337, LocationGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Peach's Castle (Normal)": LocationData(base_loc_id + 338, LocationGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Western Junction (Normal)": LocationData(base_loc_id + 339, LocationGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Wario Factory (Normal)": LocationData(base_loc_id + 340, LocationGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Daisy Garden (Normal)": LocationData(base_loc_id + 341, LocationGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Bowser Jr. Blvd. (Normal)": LocationData(base_loc_id + 342, LocationGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Waluigi Pinball (Normal)": LocationData(base_loc_id + 343, LocationGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Star Ship (Normal)": LocationData(base_loc_id + 344, LocationGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Koopa Troopa Beach (Normal)": LocationData(base_loc_id + 345, LocationGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Ghoulish Galleon (Normal)": LocationData(base_loc_id + 346, LocationGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Bowser's Castle (Normal)": LocationData(base_loc_id + 347, LocationGroup.HOCKEY_EX_NORMAL),

    # === Hard Exhibition Locations ===
    # Basketball
    "Basketball Ex: Beat Mario Stadium (Hard)": LocationData(base_loc_id + 400, LocationGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Koopa Troopa Beach (Hard)": LocationData(base_loc_id + 401, LocationGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat DK Dock (Hard)": LocationData(base_loc_id + 402, LocationGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Luigi's Mansion (Hard)": LocationData(base_loc_id + 403, LocationGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Western Junction (Hard)": LocationData(base_loc_id + 404, LocationGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Daisy Garden (Hard)": LocationData(base_loc_id + 405, LocationGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Bowser Jr. Blvd. (Hard)": LocationData(base_loc_id + 406, LocationGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Bowser's Castle (Hard)": LocationData(base_loc_id + 407, LocationGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Star Ship (Hard)": LocationData(base_loc_id + 408, LocationGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Peach's Castle (Hard)": LocationData(base_loc_id + 409, LocationGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Wario Factory (Hard)": LocationData(base_loc_id + 410, LocationGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Ghoulish Galleon (Hard)": LocationData(base_loc_id + 411, LocationGroup.BASKETBALL_EX_HARD),

    # Dodgeball
    "Dodgeball Ex: Beat Mario Stadium (Hard)": LocationData(base_loc_id + 412, LocationGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Koopa Troopa Beach (Hard)": LocationData(base_loc_id + 413, LocationGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Peach's Castle (Hard)": LocationData(base_loc_id + 414, LocationGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat DK Dock (Hard)": LocationData(base_loc_id + 415, LocationGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Toad Park (Hard)": LocationData(base_loc_id + 416, LocationGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Daisy Garden (Hard)": LocationData(base_loc_id + 417, LocationGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Wario Factory (Hard)": LocationData(base_loc_id + 418, LocationGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Bowser's Castle (Hard)": LocationData(base_loc_id + 419, LocationGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Star Ship (Hard)": LocationData(base_loc_id + 420, LocationGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Western Junction (Hard)": LocationData(base_loc_id + 421, LocationGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Waluigi Pinball (Hard)": LocationData(base_loc_id + 422, LocationGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Ghoulish Galleon (Hard)": LocationData(base_loc_id + 423, LocationGroup.DODGEBALL_EX_HARD),

    # Volleyball
    "Volleyball Ex: Beat Mario Stadium (Hard)": LocationData(base_loc_id + 424, LocationGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Koopa Troopa Beach (Hard)": LocationData(base_loc_id + 425, LocationGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Peach's Castle (Hard)": LocationData(base_loc_id + 426, LocationGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat DK Dock (Hard)": LocationData(base_loc_id + 427, LocationGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Luigi's Mansion (Hard)": LocationData(base_loc_id + 428, LocationGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Western Junction (Hard)": LocationData(base_loc_id + 429, LocationGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Bowser Jr. Blvd. (Hard)": LocationData(base_loc_id + 430, LocationGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Bowser's Castle (Hard)": LocationData(base_loc_id + 431, LocationGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Star Ship (Hard)": LocationData(base_loc_id + 432, LocationGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Wario Factory (Hard)": LocationData(base_loc_id + 433, LocationGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Waluigi Pinball (Hard)": LocationData(base_loc_id + 434, LocationGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Ghoulish Galleon (Hard)": LocationData(base_loc_id + 435, LocationGroup.VOLLEYBALL_EX_HARD),

    # Hockey
    "Hockey Ex: Beat Mario Stadium (Hard)": LocationData(base_loc_id + 436, LocationGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Toad Park (Hard)": LocationData(base_loc_id + 437, LocationGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Peach's Castle (Hard)": LocationData(base_loc_id + 438, LocationGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Western Junction (Hard)": LocationData(base_loc_id + 439, LocationGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Wario Factory (Hard)": LocationData(base_loc_id + 440, LocationGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Daisy Garden (Hard)": LocationData(base_loc_id + 441, LocationGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Bowser Jr. Blvd. (Hard)": LocationData(base_loc_id + 442, LocationGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Waluigi Pinball (Hard)": LocationData(base_loc_id + 443, LocationGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Star Ship (Hard)": LocationData(base_loc_id + 444, LocationGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Koopa Troopa Beach (Hard)": LocationData(base_loc_id + 445, LocationGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Ghoulish Galleon (Hard)": LocationData(base_loc_id + 446, LocationGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Bowser's Castle (Hard)": LocationData(base_loc_id + 447, LocationGroup.HOCKEY_EX_HARD),

    # === Expert Exhibition Locations ===
    # Basketball
    "Basketball Ex: Beat Mario Stadium (Expert)": LocationData(base_loc_id + 500, LocationGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Koopa Troopa Beach (Expert)": LocationData(base_loc_id + 501,
                                                                    LocationGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat DK Dock (Expert)": LocationData(base_loc_id + 502, LocationGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Luigi's Mansion (Expert)": LocationData(base_loc_id + 503, LocationGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Western Junction (Expert)": LocationData(base_loc_id + 504,
                                                                  LocationGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Daisy Garden (Expert)": LocationData(base_loc_id + 505, LocationGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Bowser Jr. Blvd. (Expert)": LocationData(base_loc_id + 506,
                                                                  LocationGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Bowser's Castle (Expert)": LocationData(base_loc_id + 507, LocationGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Star Ship (Expert)": LocationData(base_loc_id + 508, LocationGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Peach's Castle (Expert)": LocationData(base_loc_id + 509, LocationGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Wario Factory (Expert)": LocationData(base_loc_id + 510, LocationGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Ghoulish Galleon (Expert)": LocationData(base_loc_id + 511,
                                                                  LocationGroup.BASKETBALL_EX_EXPERT),

    # Dodgeball
    "Dodgeball Ex: Beat Mario Stadium (Expert)": LocationData(base_loc_id + 512, LocationGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Koopa Troopa Beach (Expert)": LocationData(base_loc_id + 513,
                                                                   LocationGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Peach's Castle (Expert)": LocationData(base_loc_id + 514, LocationGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat DK Dock (Expert)": LocationData(base_loc_id + 515, LocationGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Toad Park (Expert)": LocationData(base_loc_id + 516, LocationGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Daisy Garden (Expert)": LocationData(base_loc_id + 517, LocationGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Wario Factory (Expert)": LocationData(base_loc_id + 518, LocationGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Bowser's Castle (Expert)": LocationData(base_loc_id + 519, LocationGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Star Ship (Expert)": LocationData(base_loc_id + 520, LocationGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Western Junction (Expert)": LocationData(base_loc_id + 521, LocationGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Waluigi Pinball (Expert)": LocationData(base_loc_id + 522, LocationGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Ghoulish Galleon (Expert)": LocationData(base_loc_id + 523, LocationGroup.DODGEBALL_EX_EXPERT),

    # Volleyball
    "Volleyball Ex: Beat Mario Stadium (Expert)": LocationData(base_loc_id + 524, LocationGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Koopa Troopa Beach (Expert)": LocationData(base_loc_id + 525,
                                                                    LocationGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Peach's Castle (Expert)": LocationData(base_loc_id + 526, LocationGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat DK Dock (Expert)": LocationData(base_loc_id + 527, LocationGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Luigi's Mansion (Expert)": LocationData(base_loc_id + 528, LocationGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Western Junction (Expert)": LocationData(base_loc_id + 529,
                                                                  LocationGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Bowser Jr. Blvd. (Expert)": LocationData(base_loc_id + 530,
                                                                  LocationGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Bowser's Castle (Expert)": LocationData(base_loc_id + 531, LocationGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Star Ship (Expert)": LocationData(base_loc_id + 532, LocationGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Wario Factory (Expert)": LocationData(base_loc_id + 533, LocationGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Waluigi Pinball (Expert)": LocationData(base_loc_id + 534, LocationGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Ghoulish Galleon (Expert)": LocationData(base_loc_id + 535,
                                                                  LocationGroup.VOLLEYBALL_EX_EXPERT),

    # Hockey
    "Hockey Ex: Beat Mario Stadium (Expert)": LocationData(base_loc_id + 536, LocationGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Toad Park (Expert)": LocationData(base_loc_id + 537, LocationGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Peach's Castle (Expert)": LocationData(base_loc_id + 538, LocationGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Western Junction (Expert)": LocationData(base_loc_id + 539, LocationGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Wario Factory (Expert)": LocationData(base_loc_id + 540, LocationGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Daisy Garden (Expert)": LocationData(base_loc_id + 541, LocationGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Bowser Jr. Blvd. (Expert)": LocationData(base_loc_id + 542, LocationGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Waluigi Pinball (Expert)": LocationData(base_loc_id + 543, LocationGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Star Ship (Expert)": LocationData(base_loc_id + 544, LocationGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Koopa Troopa Beach (Expert)": LocationData(base_loc_id + 545, LocationGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Ghoulish Galleon (Expert)": LocationData(base_loc_id + 546, LocationGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Bowser's Castle (Expert)": LocationData(base_loc_id + 547, LocationGroup.HOCKEY_EX_EXPERT),

    # === Special Sanity Locations ===
    "Use Mario's Special!": LocationData(base_loc_id + 560, LocationGroup.SPECIAL_SANITY),
    "Use Luigi's Special!": LocationData(base_loc_id + 561, LocationGroup.SPECIAL_SANITY),
    "Use Peach's Special!": LocationData(base_loc_id + 562, LocationGroup.SPECIAL_SANITY),
    "Use Daisy's Special!": LocationData(base_loc_id + 563, LocationGroup.SPECIAL_SANITY),
    "Use Yoshi's Special!": LocationData(base_loc_id + 564, LocationGroup.SPECIAL_SANITY),
    "Use Wario's Special!": LocationData(base_loc_id + 565, LocationGroup.SPECIAL_SANITY),
    "Use Waluigi's Special!": LocationData(base_loc_id + 566, LocationGroup.SPECIAL_SANITY),
    "Use Donkey Kong's Special!": LocationData(base_loc_id + 567, LocationGroup.SPECIAL_SANITY),
    "Use Diddy Kong's Special!": LocationData(base_loc_id + 568, LocationGroup.SPECIAL_SANITY),
    "Use Toad's Special!": LocationData(base_loc_id + 569, LocationGroup.SPECIAL_SANITY),
    "Use Bowser's Special!": LocationData(base_loc_id + 570, LocationGroup.SPECIAL_SANITY),
    "Use Bowser Jr's Special!": LocationData(base_loc_id + 571, LocationGroup.SPECIAL_SANITY),
    "Use Moogle's Special!": LocationData(base_loc_id + 572, LocationGroup.SPECIAL_SANITY),
    "Use Cactuar's Special!": LocationData(base_loc_id + 573, LocationGroup.SPECIAL_SANITY),
    "Use Ninja's Special!": LocationData(base_loc_id + 574, LocationGroup.SPECIAL_SANITY),
    "Use White Mage's Special!": LocationData(base_loc_id + 575, LocationGroup.SPECIAL_SANITY),
    "Use Slime's Special!": LocationData(base_loc_id + 576, LocationGroup.SPECIAL_SANITY),
    "Use Black Mage's Special!": LocationData(base_loc_id + 577, LocationGroup.SPECIAL_SANITY),

    # === Character Sanity Locations ===
    "Play as Mario": LocationData(base_loc_id + 1001, LocationGroup.CHARACTER_SANITY),
    "Play as Luigi": LocationData(base_loc_id + 1002, LocationGroup.CHARACTER_SANITY),
    "Play as Peach": LocationData(base_loc_id + 1003, LocationGroup.CHARACTER_SANITY),
    "Play as Daisy": LocationData(base_loc_id + 1004, LocationGroup.CHARACTER_SANITY),
    "Play as Yoshi": LocationData(base_loc_id + 1005, LocationGroup.CHARACTER_SANITY),
    "Play as Wario": LocationData(base_loc_id + 1006, LocationGroup.CHARACTER_SANITY),
    "Play as Waluigi": LocationData(base_loc_id + 1007, LocationGroup.CHARACTER_SANITY),
    "Play as Donkey Kong": LocationData(base_loc_id + 1008, LocationGroup.CHARACTER_SANITY),
    "Play as Diddy Kong": LocationData(base_loc_id + 1009, LocationGroup.CHARACTER_SANITY),
    "Play as Toad": LocationData(base_loc_id + 1010, LocationGroup.CHARACTER_SANITY),
    "Play as Bowser": LocationData(base_loc_id + 1011, LocationGroup.CHARACTER_SANITY),
    "Play as Bowser Jr": LocationData(base_loc_id + 1012, LocationGroup.CHARACTER_SANITY),
    "Play as Moogle": LocationData(base_loc_id + 1013, LocationGroup.CHARACTER_SANITY),
    "Play as Cactuar": LocationData(base_loc_id + 1014, LocationGroup.CHARACTER_SANITY),
    "Play as Ninja": LocationData(base_loc_id + 1015, LocationGroup.CHARACTER_SANITY),
    "Play as White Mage": LocationData(base_loc_id + 1016, LocationGroup.CHARACTER_SANITY),
    "Play as Slime": LocationData(base_loc_id + 1017, LocationGroup.CHARACTER_SANITY),
    "Play as Black Mage": LocationData(base_loc_id + 1018, LocationGroup.CHARACTER_SANITY),
    "Play as Mii (Male)": LocationData(base_loc_id + 1019, LocationGroup.CHARACTER_SANITY),
    "Play as Mii (Female)": LocationData(base_loc_id + 1020, LocationGroup.CHARACTER_SANITY),

    # === Costumes ===
    "Play as Pink Yoshi": LocationData(base_loc_id + 1021, LocationGroup.COSTUME_SANITY),
    "Play as Light Blue Yoshi": LocationData(base_loc_id + 1022, LocationGroup.COSTUME_SANITY),
    "Play as Yellow Yoshi": LocationData(base_loc_id + 1023, LocationGroup.COSTUME_SANITY),
    "Play as Blue Toad": LocationData(base_loc_id + 1024, LocationGroup.COSTUME_SANITY),
    "Play as Green Toad": LocationData(base_loc_id + 1025, LocationGroup.COSTUME_SANITY),
    "Play as Yellow Toad": LocationData(base_loc_id + 1026, LocationGroup.COSTUME_SANITY),
    "Play as She-Slime": LocationData(base_loc_id + 1027, LocationGroup.COSTUME_SANITY),
    "Play as Metal Slime": LocationData(base_loc_id + 1028, LocationGroup.COSTUME_SANITY),
    "Play as Tennis-wear Peach": LocationData(base_loc_id + 1029, LocationGroup.COSTUME_SANITY),
    "Play as Tennis-wear Daisy": LocationData(base_loc_id + 1030, LocationGroup.COSTUME_SANITY),
    "Play as Shadow White Ninja": LocationData(base_loc_id + 1031, LocationGroup.COSTUME_SANITY),
    "Play as Pure White - White Mage": LocationData(base_loc_id + 1032, LocationGroup.COSTUME_SANITY),
    "Play as Magic Red Black Mage": LocationData(base_loc_id + 1033, LocationGroup.COSTUME_SANITY),

    # === Boss Locations ===
    "Defeat Behemoth!": LocationData(base_loc_id + 2000, LocationGroup.BOSS_LOCATIONS),
    "Defeat Behemoth King!": LocationData(base_loc_id + 2001, LocationGroup.BOSS_LOCATIONS),
}

LOCATION_NAME_TO_ID = {location_name: data.id for location_name, data in location_table.items()}

auto_location_groups = {}

# Loop through every single location
for loc_name, loc_data in location_table.items():

    # Grab the string name of the group from the Enum
    # (e.g., "Basketball Exhibition Easy")
    group_name = loc_data.group.value

    # If this group isn't in our dictionary yet, create an empty set for it
    if group_name not in auto_location_groups:
        auto_location_groups[group_name] = set()

    # Add the location's name into that group's set
    auto_location_groups[group_name].add(loc_name)


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: location_table[location_name].id for location_name in location_names}


def create_regular_locations(world: MSMWorld) -> None:
    main_menu = world.get_region("Main Menu")
    # Basketball
    b_exhibition = world.get_region("Basketball: Exhibition")
    b_mushroom_cup_n = world.get_region("Basketball: Mushroom Cup (Normal)")
    b_flower_cup_n = world.get_region("Basketball: Flower Cup (Normal)")
    b_star_cup_n = world.get_region("Basketball: Star Cup (Normal)")
    b_mushroom_cup_h = world.get_region("Basketball: Mushroom Cup (Hard)")
    b_flower_cup_h = world.get_region("Basketball: Flower Cup (Hard)")
    b_star_cup_h = world.get_region("Basketball: Star Cup (Hard)")
    # Dodgeball
    d_exhibition = world.get_region("Dodgeball: Exhibition")
    d_mushroom_cup_n = world.get_region("Dodgeball: Mushroom Cup (Normal)")
    d_flower_cup_n = world.get_region("Dodgeball: Flower Cup (Normal)")
    d_star_cup_n = world.get_region("Dodgeball: Star Cup (Normal)")
    d_mushroom_cup_h = world.get_region("Dodgeball: Mushroom Cup (Hard)")
    d_flower_cup_h = world.get_region("Dodgeball: Flower Cup (Hard)")
    d_star_cup_h = world.get_region("Dodgeball: Star Cup (Hard)")
    # Volleyball
    v_exhibition = world.get_region("Volleyball: Exhibition")
    v_mushroom_cup_n = world.get_region("Volleyball: Mushroom Cup (Normal)")
    v_flower_cup_n = world.get_region("Volleyball: Flower Cup (Normal)")
    v_star_cup_n = world.get_region("Volleyball: Star Cup (Normal)")
    v_mushroom_cup_h = world.get_region("Volleyball: Mushroom Cup (Hard)")
    v_flower_cup_h = world.get_region("Volleyball: Flower Cup (Hard)")
    v_star_cup_h = world.get_region("Volleyball: Star Cup (Hard)")
    # Hockey
    h_exhibition = world.get_region("Hockey: Exhibition")
    h_mushroom_cup_n = world.get_region("Hockey: Mushroom Cup (Normal)")
    h_flower_cup_n = world.get_region("Hockey: Flower Cup (Normal)")
    h_star_cup_n = world.get_region("Hockey: Star Cup (Normal)")
    h_mushroom_cup_h = world.get_region("Hockey: Mushroom Cup (Hard)")
    h_flower_cup_h = world.get_region("Hockey: Flower Cup (Hard)")
    h_star_cup_h = world.get_region("Hockey: Star Cup (Hard)")
    # Sports Mix
    sports_mix_mushroom = world.get_region("Sports Mix: Mushroom Cup")
    sm_mushroom_locations = get_location_names_with_ids(["Sports Mix: Beat Mushroom Cup Round 1",
    "Sports Mix: Beat Mushroom Cup Round 2", "Sports Mix: Beat Mushroom Cup Round 3"])
    sports_mix_mushroom.add_locations(sm_mushroom_locations, MSMLocation)
    sports_mix_flower = world.get_region("Sports Mix: Flower Cup")
    sm_flower_locations = get_location_names_with_ids(["Sports Mix: Beat Flower Cup Round 1",
    "Sports Mix: Beat Flower Cup Round 2", "Sports Mix: Beat Flower Cup Round 3"])
    sports_mix_flower.add_locations(sm_flower_locations, MSMLocation)
    sports_mix_star = world.get_region("Sports Mix: Star Cup")
    sm_star_locations = get_location_names_with_ids(["Sports Mix: Beat Star Cup Round 1",
    "Sports Mix: Beat Star Cup Round 2", "Sports Mix: Beat Star Cup Round 3"])
    sports_mix_star.add_locations(sm_star_locations, MSMLocation)


    # === Exhibition Locations for each difficulty ===

    # Normal Difficulty
    # Basketball
    b_mushroom_n_locations = get_location_names_with_ids(["Basketball: Beat Normal Mushroom Cup Round 1",
    "Basketball: Beat Normal Mushroom Cup Round 2", "Basketball: Beat Normal Mushroom Cup Round 3"])
    b_flower_n_locations = get_location_names_with_ids(["Basketball: Beat Normal Flower Cup Round 1",
    "Basketball: Beat Normal Flower Cup Round 2", "Basketball: Beat Normal Flower Cup Round 3"])
    b_star_n_locations = get_location_names_with_ids(["Basketball: Beat Normal Star Cup Round 1",
    "Basketball: Beat Normal Star Cup Round 2", "Basketball: Beat Normal Star Cup Round 3"])

    b_mushroom_cup_n.add_locations(b_mushroom_n_locations, MSMLocation)
    b_flower_cup_n.add_locations(b_flower_n_locations, MSMLocation)
    b_star_cup_n.add_locations(b_star_n_locations, MSMLocation)

    # Dodgeball
    d_mushroom_n_locations = get_location_names_with_ids(["Dodgeball: Beat Normal Mushroom Cup Round 1",
    "Dodgeball: Beat Normal Mushroom Cup Round 2", "Dodgeball: Beat Normal Mushroom Cup Round 3"])
    d_flower_n_locations = get_location_names_with_ids(["Dodgeball: Beat Normal Flower Cup Round 1",
    "Dodgeball: Beat Normal Flower Cup Round 2", "Dodgeball: Beat Normal Flower Cup Round 3"])
    d_star_n_locations = get_location_names_with_ids(["Dodgeball: Beat Normal Star Cup Round 1",
    "Dodgeball: Beat Normal Star Cup Round 2", "Dodgeball: Beat Normal Star Cup Round 3"])

    d_mushroom_cup_n.add_locations(d_mushroom_n_locations, MSMLocation)
    d_flower_cup_n.add_locations(d_flower_n_locations, MSMLocation)
    d_star_cup_n.add_locations(d_star_n_locations, MSMLocation)

    # Volleyball
    v_mushroom_n_locations = get_location_names_with_ids(["Volleyball: Beat Normal Mushroom Cup Round 1",
    "Volleyball: Beat Normal Mushroom Cup Round 2", "Volleyball: Beat Normal Mushroom Cup Round 3"])
    v_flower_n_locations = get_location_names_with_ids(["Volleyball: Beat Normal Flower Cup Round 1",
    "Volleyball: Beat Normal Flower Cup Round 2", "Volleyball: Beat Normal Flower Cup Round 3"])
    v_star_n_locations = get_location_names_with_ids(["Volleyball: Beat Normal Star Cup Round 1",
    "Volleyball: Beat Normal Star Cup Round 2", "Volleyball: Beat Normal Star Cup Round 3"])

    v_mushroom_cup_n.add_locations(v_mushroom_n_locations, MSMLocation)
    v_flower_cup_n.add_locations(v_flower_n_locations, MSMLocation)
    v_star_cup_n.add_locations(v_star_n_locations, MSMLocation)

    # Hockey
    h_mushroom_n_locations = get_location_names_with_ids(["Hockey: Beat Normal Mushroom Cup Round 1",
    "Hockey: Beat Normal Mushroom Cup Round 2", "Hockey: Beat Normal Mushroom Cup Round 3"])
    h_flower_n_locations = get_location_names_with_ids(["Hockey: Beat Normal Flower Cup Round 1",
    "Hockey: Beat Normal Flower Cup Round 2", "Hockey: Beat Normal Flower Cup Round 3"])
    h_star_n_locations = get_location_names_with_ids(["Hockey: Beat Normal Star Cup Round 1",
    "Hockey: Beat Normal Star Cup Round 2", "Hockey: Beat Normal Star Cup Round 3"])

    h_mushroom_cup_n.add_locations(h_mushroom_n_locations, MSMLocation)
    h_flower_cup_n.add_locations(h_flower_n_locations, MSMLocation)
    h_star_cup_n.add_locations(h_star_n_locations, MSMLocation)

    # Hard Difficulty
    if world.options.hard_tournament_difficulty == HardTournamentDifficulty.option_true:
        # Basketball
        b_mushroom_h_locations = get_location_names_with_ids(["Basketball: Beat Hard Mushroom Cup Round 1",
    "Basketball: Beat Hard Mushroom Cup Round 2", "Basketball: Beat Hard Mushroom Cup Round 3"])
        b_flower_h_locations = get_location_names_with_ids(["Basketball: Beat Hard Flower Cup Round 1",
    "Basketball: Beat Hard Flower Cup Round 2", "Basketball: Beat Hard Flower Cup Round 3"])
        b_star_h_locations = get_location_names_with_ids(["Basketball: Beat Hard Star Cup Round 1",
    "Basketball: Beat Hard Star Cup Round 2", "Basketball: Beat Hard Star Cup Round 3"])

        b_mushroom_cup_h.add_locations(b_mushroom_h_locations, MSMLocation)
        b_flower_cup_h.add_locations(b_flower_h_locations, MSMLocation)
        b_star_cup_h.add_locations(b_star_h_locations, MSMLocation)

        # Dodgeball
        d_mushroom_h_locations = get_location_names_with_ids(["Dodgeball: Beat Hard Mushroom Cup Round 1",
    "Dodgeball: Beat Hard Mushroom Cup Round 2", "Dodgeball: Beat Hard Mushroom Cup Round 3"])
        d_flower_h_locations = get_location_names_with_ids(["Dodgeball: Beat Hard Flower Cup Round 1",
    "Dodgeball: Beat Hard Flower Cup Round 2", "Dodgeball: Beat Hard Flower Cup Round 3"])
        d_star_h_locations = get_location_names_with_ids(["Dodgeball: Beat Hard Star Cup Round 1",
    "Dodgeball: Beat Hard Star Cup Round 2", "Dodgeball: Beat Hard Star Cup Round 3"])

        d_mushroom_cup_h.add_locations(d_mushroom_h_locations, MSMLocation)
        d_flower_cup_h.add_locations(d_flower_h_locations, MSMLocation)
        d_star_cup_h.add_locations(d_star_h_locations, MSMLocation)

        # Volleyball
        v_mushroom_h_locations = get_location_names_with_ids(["Volleyball: Beat Hard Mushroom Cup Round 1",
    "Volleyball: Beat Hard Mushroom Cup Round 2", "Volleyball: Beat Hard Mushroom Cup Round 3"])
        v_flower_h_locations = get_location_names_with_ids(["Volleyball: Beat Hard Flower Cup Round 1",
    "Volleyball: Beat Hard Flower Cup Round 2", "Volleyball: Beat Hard Flower Cup Round 3"])
        v_star_h_locations = get_location_names_with_ids(["Volleyball: Beat Hard Star Cup Round 1",
    "Volleyball: Beat Hard Star Cup Round 2", "Volleyball: Beat Hard Star Cup Round 3"])

        v_mushroom_cup_h.add_locations(v_mushroom_h_locations, MSMLocation)
        v_flower_cup_h.add_locations(v_flower_h_locations, MSMLocation)
        v_star_cup_h.add_locations(v_star_h_locations, MSMLocation)

        # Hockey
        h_mushroom_h_locations = get_location_names_with_ids(["Hockey: Beat Hard Mushroom Cup Round 1",
    "Hockey: Beat Hard Mushroom Cup Round 2", "Hockey: Beat Hard Mushroom Cup Round 3"])
        h_flower_h_locations = get_location_names_with_ids(["Hockey: Beat Hard Flower Cup Round 1",
    "Hockey: Beat Hard Flower Cup Round 2", "Hockey: Beat Hard Flower Cup Round 3"])
        h_star_h_locations = get_location_names_with_ids(["Hockey: Beat Hard Star Cup Round 1",
    "Hockey: Beat Hard Star Cup Round 2", "Hockey: Beat Hard Star Cup Round 3"])

        h_mushroom_cup_h.add_locations(h_mushroom_h_locations, MSMLocation)
        h_flower_cup_h.add_locations(h_flower_h_locations, MSMLocation)
        h_star_cup_h.add_locations(h_star_h_locations, MSMLocation)

    # === Exhibition Locations for each difficulty ===

    # Easy Difficulty
    if "Easy" in world.options.exhibition_difficulty:
        b_exhibition_locations_e = get_location_names_with_ids([
        "Basketball Ex: Beat Mario Stadium (Easy)",
        "Basketball Ex: Beat Koopa Troopa Beach (Easy)",
        "Basketball Ex: Beat DK Dock (Easy)",
        "Basketball Ex: Beat Luigi's Mansion (Easy)",
        "Basketball Ex: Beat Western Junction (Easy)",
        "Basketball Ex: Beat Daisy Garden (Easy)",
        "Basketball Ex: Beat Bowser Jr. Blvd. (Easy)",
        "Basketball Ex: Beat Bowser's Castle (Easy)",
        "Basketball Ex: Beat Star Ship (Easy)",
        "Basketball Ex: Beat Peach's Castle (Easy)",
        "Basketball Ex: Beat Wario Factory (Easy)",
        "Basketball Ex: Beat Ghoulish Galleon (Easy)"])
        d_exhibition_locations_e = get_location_names_with_ids([
        "Dodgeball Ex: Beat Mario Stadium (Easy)",
        "Dodgeball Ex: Beat Koopa Troopa Beach (Easy)",
        "Dodgeball Ex: Beat Peach's Castle (Easy)",
        "Dodgeball Ex: Beat DK Dock (Easy)",
        "Dodgeball Ex: Beat Toad Park (Easy)",
        "Dodgeball Ex: Beat Daisy Garden (Easy)",
        "Dodgeball Ex: Beat Wario Factory (Easy)",
        "Dodgeball Ex: Beat Bowser's Castle (Easy)",
        "Dodgeball Ex: Beat Star Ship (Easy)",
        "Dodgeball Ex: Beat Western Junction (Easy)",
        "Dodgeball Ex: Beat Waluigi Pinball (Easy)",
        "Dodgeball Ex: Beat Ghoulish Galleon (Easy)"])
        v_exhibition_locations_e = get_location_names_with_ids([
        "Volleyball Ex: Beat Mario Stadium (Easy)",
        "Volleyball Ex: Beat Koopa Troopa Beach (Easy)",
        "Volleyball Ex: Beat Peach's Castle (Easy)",
        "Volleyball Ex: Beat DK Dock (Easy)",
        "Volleyball Ex: Beat Luigi's Mansion (Easy)",
        "Volleyball Ex: Beat Western Junction (Easy)",
        "Volleyball Ex: Beat Bowser Jr. Blvd. (Easy)",
        "Volleyball Ex: Beat Bowser's Castle (Easy)",
        "Volleyball Ex: Beat Star Ship (Easy)",
        "Volleyball Ex: Beat Wario Factory (Easy)",
        "Volleyball Ex: Beat Waluigi Pinball (Easy)",
        "Volleyball Ex: Beat Ghoulish Galleon (Easy)"])
        h_exhibition_locations_e = get_location_names_with_ids([
        "Hockey Ex: Beat Mario Stadium (Easy)",
        "Hockey Ex: Beat Toad Park (Easy)",
        "Hockey Ex: Beat Peach's Castle (Easy)",
        "Hockey Ex: Beat Western Junction (Easy)",
        "Hockey Ex: Beat Wario Factory (Easy)",
        "Hockey Ex: Beat Daisy Garden (Easy)",
        "Hockey Ex: Beat Bowser Jr. Blvd. (Easy)",
        "Hockey Ex: Beat Waluigi Pinball (Easy)",
        "Hockey Ex: Beat Star Ship (Easy)",
        "Hockey Ex: Beat Koopa Troopa Beach (Easy)",
        "Hockey Ex: Beat Ghoulish Galleon (Easy)",
        "Hockey Ex: Beat Bowser's Castle (Easy)"])

        b_exhibition.add_locations(b_exhibition_locations_e)
        d_exhibition.add_locations(d_exhibition_locations_e)
        v_exhibition.add_locations(v_exhibition_locations_e)
        h_exhibition.add_locations(h_exhibition_locations_e)

    # Normal Difficulty
    if "Normal" in world.options.exhibition_difficulty:
        b_exhibition_locations_n = get_location_names_with_ids([
        "Basketball Ex: Beat Mario Stadium (Normal)",
        "Basketball Ex: Beat Koopa Troopa Beach (Normal)",
        "Basketball Ex: Beat DK Dock (Normal)",
        "Basketball Ex: Beat Luigi's Mansion (Normal)",
        "Basketball Ex: Beat Western Junction (Normal)",
        "Basketball Ex: Beat Daisy Garden (Normal)",
        "Basketball Ex: Beat Bowser Jr. Blvd. (Normal)",
        "Basketball Ex: Beat Bowser's Castle (Normal)",
        "Basketball Ex: Beat Star Ship (Normal)",
        "Basketball Ex: Beat Peach's Castle (Normal)",
        "Basketball Ex: Beat Wario Factory (Normal)",
        "Basketball Ex: Beat Ghoulish Galleon (Normal)"])
        d_exhibition_locations_n = get_location_names_with_ids([
        "Dodgeball Ex: Beat Mario Stadium (Normal)",
        "Dodgeball Ex: Beat Koopa Troopa Beach (Normal)",
        "Dodgeball Ex: Beat Peach's Castle (Normal)",
        "Dodgeball Ex: Beat DK Dock (Normal)",
        "Dodgeball Ex: Beat Toad Park (Normal)",
        "Dodgeball Ex: Beat Daisy Garden (Normal)",
        "Dodgeball Ex: Beat Wario Factory (Normal)",
        "Dodgeball Ex: Beat Bowser's Castle (Normal)",
        "Dodgeball Ex: Beat Star Ship (Normal)",
        "Dodgeball Ex: Beat Western Junction (Normal)",
        "Dodgeball Ex: Beat Waluigi Pinball (Normal)",
        "Dodgeball Ex: Beat Ghoulish Galleon (Normal)"])
        v_exhibition_locations_n = get_location_names_with_ids([
        "Volleyball Ex: Beat Mario Stadium (Normal)",
        "Volleyball Ex: Beat Koopa Troopa Beach (Normal)",
        "Volleyball Ex: Beat Peach's Castle (Normal)",
        "Volleyball Ex: Beat DK Dock (Normal)",
        "Volleyball Ex: Beat Luigi's Mansion (Normal)",
        "Volleyball Ex: Beat Western Junction (Normal)",
        "Volleyball Ex: Beat Bowser Jr. Blvd. (Normal)",
        "Volleyball Ex: Beat Bowser's Castle (Normal)",
        "Volleyball Ex: Beat Star Ship (Normal)",
        "Volleyball Ex: Beat Wario Factory (Normal)",
        "Volleyball Ex: Beat Waluigi Pinball (Normal)",
        "Volleyball Ex: Beat Ghoulish Galleon (Normal)"])
        h_exhibition_locations_n = get_location_names_with_ids([
        "Hockey Ex: Beat Mario Stadium (Normal)",
        "Hockey Ex: Beat Toad Park (Normal)",
        "Hockey Ex: Beat Peach's Castle (Normal)",
        "Hockey Ex: Beat Western Junction (Normal)",
        "Hockey Ex: Beat Wario Factory (Normal)",
        "Hockey Ex: Beat Daisy Garden (Normal)",
        "Hockey Ex: Beat Bowser Jr. Blvd. (Normal)",
        "Hockey Ex: Beat Waluigi Pinball (Normal)",
        "Hockey Ex: Beat Star Ship (Normal)",
        "Hockey Ex: Beat Koopa Troopa Beach (Normal)",
        "Hockey Ex: Beat Ghoulish Galleon (Normal)",
        "Hockey Ex: Beat Bowser's Castle (Normal)"])

        b_exhibition.add_locations(b_exhibition_locations_n)
        d_exhibition.add_locations(d_exhibition_locations_n)
        v_exhibition.add_locations(v_exhibition_locations_n)
        h_exhibition.add_locations(h_exhibition_locations_n)

    # Hard Difficulty
    if "Hard" in world.options.exhibition_difficulty:
        b_exhibition_locations_h = get_location_names_with_ids([
        "Basketball Ex: Beat Mario Stadium (Hard)",
        "Basketball Ex: Beat Koopa Troopa Beach (Hard)",
        "Basketball Ex: Beat DK Dock (Hard)",
        "Basketball Ex: Beat Luigi's Mansion (Hard)",
        "Basketball Ex: Beat Western Junction (Hard)",
        "Basketball Ex: Beat Daisy Garden (Hard)",
        "Basketball Ex: Beat Bowser Jr. Blvd. (Hard)",
        "Basketball Ex: Beat Bowser's Castle (Hard)",
        "Basketball Ex: Beat Star Ship (Hard)",
        "Basketball Ex: Beat Peach's Castle (Hard)",
        "Basketball Ex: Beat Wario Factory (Hard)",
        "Basketball Ex: Beat Ghoulish Galleon (Hard)"])
        v_exhibition_locations_h = get_location_names_with_ids([
        "Volleyball Ex: Beat Mario Stadium (Hard)",
        "Volleyball Ex: Beat Koopa Troopa Beach (Hard)",
        "Volleyball Ex: Beat Peach's Castle (Hard)",
        "Volleyball Ex: Beat DK Dock (Hard)",
        "Volleyball Ex: Beat Luigi's Mansion (Hard)",
        "Volleyball Ex: Beat Western Junction (Hard)",
        "Volleyball Ex: Beat Bowser Jr. Blvd. (Hard)",
        "Volleyball Ex: Beat Bowser's Castle (Hard)",
        "Volleyball Ex: Beat Star Ship (Hard)",
        "Volleyball Ex: Beat Wario Factory (Hard)",
        "Volleyball Ex: Beat Waluigi Pinball (Hard)",
        "Volleyball Ex: Beat Ghoulish Galleon (Hard)"])
        d_exhibition_locations_h = get_location_names_with_ids([
        "Dodgeball Ex: Beat Mario Stadium (Hard)",
        "Dodgeball Ex: Beat Koopa Troopa Beach (Hard)",
        "Dodgeball Ex: Beat Peach's Castle (Hard)",
        "Dodgeball Ex: Beat DK Dock (Hard)",
        "Dodgeball Ex: Beat Toad Park (Hard)",
        "Dodgeball Ex: Beat Daisy Garden (Hard)",
        "Dodgeball Ex: Beat Wario Factory (Hard)",
        "Dodgeball Ex: Beat Bowser's Castle (Hard)",
        "Dodgeball Ex: Beat Star Ship (Hard)",
        "Dodgeball Ex: Beat Western Junction (Hard)",
        "Dodgeball Ex: Beat Waluigi Pinball (Hard)",
        "Dodgeball Ex: Beat Ghoulish Galleon (Hard)"])
        h_exhibition_locations_h = get_location_names_with_ids([
        "Hockey Ex: Beat Mario Stadium (Hard)",
        "Hockey Ex: Beat Toad Park (Hard)",
        "Hockey Ex: Beat Peach's Castle (Hard)",
        "Hockey Ex: Beat Western Junction (Hard)",
        "Hockey Ex: Beat Wario Factory (Hard)",
        "Hockey Ex: Beat Daisy Garden (Hard)",
        "Hockey Ex: Beat Bowser Jr. Blvd. (Hard)",
        "Hockey Ex: Beat Waluigi Pinball (Hard)",
        "Hockey Ex: Beat Star Ship (Hard)",
        "Hockey Ex: Beat Koopa Troopa Beach (Hard)",
        "Hockey Ex: Beat Ghoulish Galleon (Hard)",
        "Hockey Ex: Beat Bowser's Castle (Hard)"])

        b_exhibition.add_locations(b_exhibition_locations_h)
        d_exhibition.add_locations(d_exhibition_locations_h)
        v_exhibition.add_locations(v_exhibition_locations_h)
        h_exhibition.add_locations(h_exhibition_locations_h)

    # Expert Difficulty
    if "Expert" in world.options.exhibition_difficulty:
        b_exhibition_locations_ex = get_location_names_with_ids([
        "Basketball Ex: Beat Mario Stadium (Expert)",
        "Basketball Ex: Beat Koopa Troopa Beach (Expert)",
        "Basketball Ex: Beat DK Dock (Expert)",
        "Basketball Ex: Beat Luigi's Mansion (Expert)",
        "Basketball Ex: Beat Western Junction (Expert)",
        "Basketball Ex: Beat Daisy Garden (Expert)",
        "Basketball Ex: Beat Bowser Jr. Blvd. (Expert)",
        "Basketball Ex: Beat Bowser's Castle (Expert)",
        "Basketball Ex: Beat Star Ship (Expert)",
        "Basketball Ex: Beat Peach's Castle (Expert)",
        "Basketball Ex: Beat Wario Factory (Expert)",
        "Basketball Ex: Beat Ghoulish Galleon (Expert)"])
        d_exhibition_locations_ex = get_location_names_with_ids([
        "Dodgeball Ex: Beat Mario Stadium (Expert)",
        "Dodgeball Ex: Beat Koopa Troopa Beach (Expert)",
        "Dodgeball Ex: Beat Peach's Castle (Expert)",
        "Dodgeball Ex: Beat DK Dock (Expert)",
        "Dodgeball Ex: Beat Toad Park (Expert)",
        "Dodgeball Ex: Beat Daisy Garden (Expert)",
        "Dodgeball Ex: Beat Wario Factory (Expert)",
        "Dodgeball Ex: Beat Bowser's Castle (Expert)",
        "Dodgeball Ex: Beat Star Ship (Expert)",
        "Dodgeball Ex: Beat Western Junction (Expert)",
        "Dodgeball Ex: Beat Waluigi Pinball (Expert)",
        "Dodgeball Ex: Beat Ghoulish Galleon (Expert)"])
        v_exhibition_locations_ex = get_location_names_with_ids([
        "Volleyball Ex: Beat Mario Stadium (Expert)",
        "Volleyball Ex: Beat Koopa Troopa Beach (Expert)",
        "Volleyball Ex: Beat Peach's Castle (Expert)",
        "Volleyball Ex: Beat DK Dock (Expert)",
        "Volleyball Ex: Beat Luigi's Mansion (Expert)",
        "Volleyball Ex: Beat Western Junction (Expert)",
        "Volleyball Ex: Beat Bowser Jr. Blvd. (Expert)",
        "Volleyball Ex: Beat Bowser's Castle (Expert)",
        "Volleyball Ex: Beat Star Ship (Expert)",
        "Volleyball Ex: Beat Wario Factory (Expert)",
        "Volleyball Ex: Beat Waluigi Pinball (Expert)",
        "Volleyball Ex: Beat Ghoulish Galleon (Expert)"])
        h_exhibition_locations_ex = get_location_names_with_ids([
        "Hockey Ex: Beat Mario Stadium (Expert)",
        "Hockey Ex: Beat Toad Park (Expert)",
        "Hockey Ex: Beat Peach's Castle (Expert)",
        "Hockey Ex: Beat Western Junction (Expert)",
        "Hockey Ex: Beat Wario Factory (Expert)",
        "Hockey Ex: Beat Daisy Garden (Expert)",
        "Hockey Ex: Beat Bowser Jr. Blvd. (Expert)",
        "Hockey Ex: Beat Waluigi Pinball (Expert)",
        "Hockey Ex: Beat Star Ship (Expert)",
        "Hockey Ex: Beat Koopa Troopa Beach (Expert)",
        "Hockey Ex: Beat Ghoulish Galleon (Expert)",
        "Hockey Ex: Beat Bowser's Castle (Expert)"])

        b_exhibition.add_locations(b_exhibition_locations_ex)
        d_exhibition.add_locations(d_exhibition_locations_ex)
        v_exhibition.add_locations(v_exhibition_locations_ex)
        h_exhibition.add_locations(h_exhibition_locations_ex)

    # Character Sanity Locations
    if (world.options.character_sanity == CharacterSanity.option_characters or
        world.options.character_sanity == CharacterSanity.option_characters_and_costumes):
        character_locations = get_location_names_with_ids(["Play as Mario", "Play as Luigi", "Play as Peach",
        "Play as Daisy", "Play as Yoshi", "Play as Wario", "Play as Waluigi", "Play as Donkey Kong",
        "Play as Diddy Kong", "Play as Toad", "Play as Bowser", "Play as Bowser Jr", "Play as Moogle",
        "Play as Cactuar", "Play as Ninja", "Play as White Mage", "Play as Slime", "Play as Black Mage",
        "Play as Mii (Male)", "Play as Mii (Female)"])
        main_menu.add_locations(character_locations)

    if (world.options.character_sanity == CharacterSanity.option_costumes or
        world.options.character_sanity == CharacterSanity.option_characters_and_costumes):
        costume_locations = get_location_names_with_ids(["Play as Pink Yoshi", "Play as Light Blue Yoshi",
        "Play as Yellow Yoshi", "Play as Blue Toad", "Play as Green Toad", "Play as Yellow Toad", "Play as She-Slime",
        "Play as Metal Slime", "Play as Tennis-wear Peach", "Play as Tennis-wear Daisy", "Play as Shadow White Ninja",
        "Play as Pure White - White Mage", "Play as Magic Red Black Mage"])
        main_menu.add_locations(costume_locations)


def create_events(world: "MSMWorld") -> None:
    if world.options.goal_condition == GoalCondition.option_defeat_behemoth:
        behemoth_boss = world.get_region("Behemoth Boss Battle")
        behemoth_boss.add_event(
            "Defeat Behemoth!", "Victory!", location_type=MSMLocation, item_type=items.MSMItem
        )
        if world.options.be_mean == BeMean.option_defeat_behemoth_king:
            behemoth_king_location = get_location_names_with_ids(["Defeat Behemoth King!"])
            behemoth_boss = world.get_region("Behemoth King Boss Battle")
            behemoth_boss.add_locations(behemoth_king_location, MSMLocation)

    if world.options.goal_condition == GoalCondition.option_defeat_behemoth_king:
        behemoth_king_boss = world.get_region("Behemoth King Boss Battle")
        behemoth_king_boss.add_event(
            "Defeat Behemoth King!", "Victory!", location_type=MSMLocation,
            item_type=items.MSMItem)
        if world.options.be_mean == BeMean.option_defeat_behemoth:
            behemoth_location = get_location_names_with_ids(["Defeat Behemoth!"])
            behemoth_boss = world.get_region("Behemoth Boss Battle")
            behemoth_boss.add_locations(behemoth_location, MSMLocation)

    if world.options.goal_condition == GoalCondition.option_win_cups:
        win_cup_value = world.options.win_cups_amount.value
        menu = world.get_region("Main Menu")
        menu.add_event(f"Win {win_cup_value} Cups", "Victory!", location_type=MSMLocation,
                       item_type=items.MSMItem)

        if world.options.be_mean == BeMean.option_defeat_behemoth:
            behemoth_locations = get_location_names_with_ids(["Defeat Behemoth!"])
            behemoth_boss = world.get_region("Behemoth Boss Battle")
            behemoth_boss.add_locations(behemoth_locations, MSMLocation)

        elif world.options.be_mean == BeMean.option_defeat_behemoth_king:
            behemoth_king_locations = get_location_names_with_ids(["Defeat Behemoth King!"])
            behemoth_king = world.get_region("Behemoth King Boss Battle")
            behemoth_king.add_locations(behemoth_king_locations, MSMLocation)

        elif world.options.be_mean == BeMean.option_both:
            behemoth_locations = get_location_names_with_ids(["Defeat Behemoth!"])
            behemoth_boss = world.get_region("Behemoth Boss Battle")
            behemoth_boss.add_locations(behemoth_locations, MSMLocation)

            behemoth_king_locations = get_location_names_with_ids(["Defeat Behemoth King!"])
            behemoth_king = world.get_region("Behemoth King Boss Battle")
            behemoth_king.add_locations(behemoth_king_locations, MSMLocation)