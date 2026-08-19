from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, NamedTuple, Dict

from BaseClasses import Location, LocationProgressType as LPT
from . import items
from .options import *
from .MSMUtils import *

if TYPE_CHECKING:
    from . import MSMWorld

characters = ["Mario", "Luigi", "Peach", "Daisy", "Yoshi", "Wario", "Waluigi", "Donkey Kong",
              "Diddy Kong", "Toad", "Bowser", "Bowser Jr", "Moogle", "Cactuar", "Ninja",
              "White Mage", "Slime", "Black Mage", "Mii (Male)", "Mii (Female)"]

costumes = ["Pink Yoshi", "Light Blue Yoshi", "Yellow Yoshi", "Blue Toad", "Green Toad",
            "Yellow Toad", "She-Slime", "Metal Slime", "Tennis-wear Peach", "Tennis-wear Daisy",
            "Shadow White Ninja", "Pure White - White Mage", "Magic Red Black Mage"]

class MSMLocation(Location):
    game = "Mario Sports Mix"

class LocGroup(str, Enum):
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

    # === Global Exhibitions ===
    EXHIBITION_EASY = "Exhibition Easy"
    EXHIBITION_NORMAL = "Exhibition Normal"
    EXHIBITION_HARD = "Exhibition Hard"
    EXHIBITION_EXPERT = "Exhibition Expert"

    # === Party Mode ===
    FEED_PETEY = "Feed Petey"
    HARMONY_HUSTLE = "Harmony Hustle"
    BOB_OMB_DODGE = "Bob-omb Dodge"
    SMASH_SKATE = "Smash Skate"

    # === Sanity & Misc ===
    SPECIAL_SANITY = "Special Sanity"
    CHARACTER_SANITY = "Character Sanity"
    COSTUME_SANITY = "Costume Sanity"
    COURT_SANITY = "Court Sanity"
    BOSS_LOCATIONS = "Boss Locations"
    WIN_CUPS = "Win Cups"

class LocData(NamedTuple):
    id: int
    group: LocGroup
    location_type: LPT = LPT.DEFAULT


def create_all_locations(world: "MSMWorld") -> None:
    create_regular_locations(world)
    create_events(world)


base_id = 0

cup_round_locations: Dict[str, LocData] = {
    # --- Normal ---
    # Basketball
    "Basketball: Beat Normal Mushroom Cup Round 1": LocData(base_id + 1, LocGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Mushroom Cup Round 2": LocData(base_id + 2, LocGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Mushroom Cup Round 3": LocData(base_id + 3, LocGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Flower Cup Round 1": LocData(base_id + 4, LocGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Flower Cup Round 2": LocData(base_id + 5, LocGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Flower Cup Round 3": LocData(base_id + 6, LocGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Star Cup Round 1": LocData(base_id + 7, LocGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Star Cup Round 2": LocData(base_id + 8, LocGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Star Cup Round 3": LocData(base_id + 9, LocGroup.BASKETBALL_NORMAL_CUPS, LPT.PRIORITY),

    # Dodgeball
    "Dodgeball: Beat Normal Mushroom Cup Round 1": LocData(base_id + 10, LocGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Mushroom Cup Round 2": LocData(base_id + 11, LocGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Mushroom Cup Round 3": LocData(base_id + 12, LocGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Flower Cup Round 1": LocData(base_id + 13, LocGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Flower Cup Round 2": LocData(base_id + 14, LocGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Flower Cup Round 3": LocData(base_id + 15, LocGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Star Cup Round 1": LocData(base_id + 16, LocGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Star Cup Round 2": LocData(base_id + 17, LocGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Star Cup Round 3": LocData(base_id + 18, LocGroup.DODGEBALL_NORMAL_CUPS, LPT.PRIORITY),

    # Volleyball
    "Volleyball: Beat Normal Mushroom Cup Round 1": LocData(base_id + 19, LocGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Mushroom Cup Round 2": LocData(base_id + 20, LocGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Mushroom Cup Round 3": LocData(base_id + 21, LocGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Flower Cup Round 1": LocData(base_id + 22, LocGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Flower Cup Round 2": LocData(base_id + 23, LocGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Flower Cup Round 3": LocData(base_id + 24, LocGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Star Cup Round 1": LocData(base_id + 25, LocGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Star Cup Round 2": LocData(base_id + 26, LocGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Star Cup Round 3": LocData(base_id + 27, LocGroup.VOLLEYBALL_NORMAL_CUPS, LPT.PRIORITY),

    # Hockey
    "Hockey: Beat Normal Mushroom Cup Round 1": LocData(base_id + 28, LocGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Mushroom Cup Round 2": LocData(base_id + 29, LocGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Mushroom Cup Round 3": LocData(base_id + 30, LocGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Flower Cup Round 1": LocData(base_id + 31, LocGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Flower Cup Round 2": LocData(base_id + 32, LocGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Flower Cup Round 3": LocData(base_id + 33, LocGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Star Cup Round 1": LocData(base_id + 34, LocGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Star Cup Round 2": LocData(base_id + 35, LocGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Star Cup Round 3": LocData(base_id + 36, LocGroup.HOCKEY_NORMAL_CUPS, LPT.PRIORITY),

    # --- Hard ---
    # Basketball
    "Basketball: Beat Hard Mushroom Cup Round 1": LocData(base_id + 37, LocGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Mushroom Cup Round 2": LocData(base_id + 38, LocGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Mushroom Cup Round 3": LocData(base_id + 39, LocGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Flower Cup Round 1": LocData(base_id + 40, LocGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Flower Cup Round 2": LocData(base_id + 41, LocGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Flower Cup Round 3": LocData(base_id + 42, LocGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Star Cup Round 1": LocData(base_id + 43, LocGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Star Cup Round 2": LocData(base_id + 44, LocGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Star Cup Round 3": LocData(base_id + 45, LocGroup.BASKETBALL_HARD_CUPS, LPT.PRIORITY),

    # Dodgeball
    "Dodgeball: Beat Hard Mushroom Cup Round 1": LocData(base_id + 46, LocGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Mushroom Cup Round 2": LocData(base_id + 47, LocGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Mushroom Cup Round 3": LocData(base_id + 48, LocGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Flower Cup Round 1": LocData(base_id + 49, LocGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Flower Cup Round 2": LocData(base_id + 50, LocGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Flower Cup Round 3": LocData(base_id + 51, LocGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Star Cup Round 1": LocData(base_id + 52, LocGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Star Cup Round 2": LocData(base_id + 53, LocGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Star Cup Round 3": LocData(base_id + 54, LocGroup.DODGEBALL_HARD_CUPS, LPT.PRIORITY),

    # Volleyball
    "Volleyball: Beat Hard Mushroom Cup Round 1": LocData(base_id + 55, LocGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Mushroom Cup Round 2": LocData(base_id + 56, LocGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Mushroom Cup Round 3": LocData(base_id + 57, LocGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Flower Cup Round 1": LocData(base_id + 58, LocGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Flower Cup Round 2": LocData(base_id + 59, LocGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Flower Cup Round 3": LocData(base_id + 60, LocGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Star Cup Round 1": LocData(base_id + 61, LocGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Star Cup Round 2": LocData(base_id + 62, LocGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Star Cup Round 3": LocData(base_id + 63, LocGroup.VOLLEYBALL_HARD_CUPS, LPT.PRIORITY),

    # Hockey
    "Hockey: Beat Hard Mushroom Cup Round 1": LocData(base_id + 64, LocGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Mushroom Cup Round 2": LocData(base_id + 65, LocGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Mushroom Cup Round 3": LocData(base_id + 66, LocGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Flower Cup Round 1": LocData(base_id + 67, LocGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Flower Cup Round 2": LocData(base_id + 68, LocGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Flower Cup Round 3": LocData(base_id + 69, LocGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Star Cup Round 1": LocData(base_id + 70, LocGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Star Cup Round 2": LocData(base_id + 71, LocGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Star Cup Round 3": LocData(base_id + 72, LocGroup.HOCKEY_HARD_CUPS, LPT.PRIORITY),

}

sports_mix_locations: Dict[str, LocData] = {
    "Sports Mix: Beat Mushroom Cup Round 1": LocData(base_id + 73, LocGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Mushroom Cup Round 2": LocData(base_id + 74, LocGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Mushroom Cup Round 3": LocData(base_id + 75, LocGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Flower Cup Round 1": LocData(base_id + 76, LocGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Flower Cup Round 2": LocData(base_id + 77, LocGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Flower Cup Round 3": LocData(base_id + 78, LocGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Star Cup Round 1": LocData(base_id + 79, LocGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Star Cup Round 2": LocData(base_id + 80, LocGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Star Cup Round 3": LocData(base_id + 81, LocGroup.SPORTS_MIX_CUPS),

}

easy_exhibition_locations: Dict[str, LocData] = {
    # Basketball
    "Basketball Ex: Beat Mario Stadium (Easy)": LocData(base_id + 200, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Koopa Troopa Beach (Easy)": LocData(base_id + 201, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat DK Dock (Easy)": LocData(base_id + 202, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Luigi's Mansion (Easy)": LocData(base_id + 203, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Western Junction (Easy)": LocData(base_id + 204, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Daisy Garden (Easy)": LocData(base_id + 205, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Bowser Jr. Blvd. (Easy)": LocData(base_id + 206, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Bowser's Castle (Easy)": LocData(base_id + 207, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Star Ship (Easy)": LocData(base_id + 208, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Peach's Castle (Easy)": LocData(base_id + 209, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Wario Factory (Easy)": LocData(base_id + 210, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Ghoulish Galleon (Easy)": LocData(base_id + 211, LocGroup.BASKETBALL_EX_EASY),

    # Dodgeball
    "Dodgeball Ex: Beat Mario Stadium (Easy)": LocData(base_id + 212, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Koopa Troopa Beach (Easy)": LocData(base_id + 213, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Peach's Castle (Easy)": LocData(base_id + 214, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat DK Dock (Easy)": LocData(base_id + 215, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Toad Park (Easy)": LocData(base_id + 216, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Daisy Garden (Easy)": LocData(base_id + 217, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Wario Factory (Easy)": LocData(base_id + 218, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Bowser's Castle (Easy)": LocData(base_id + 219, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Star Ship (Easy)": LocData(base_id + 220, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Western Junction (Easy)": LocData(base_id + 221, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Waluigi Pinball (Easy)": LocData(base_id + 222, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Ghoulish Galleon (Easy)": LocData(base_id + 223, LocGroup.DODGEBALL_EX_EASY),

    # Volleyball
    "Volleyball Ex: Beat Mario Stadium (Easy)": LocData(base_id + 224, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Koopa Troopa Beach (Easy)": LocData(base_id + 225, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Peach's Castle (Easy)": LocData(base_id + 226, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat DK Dock (Easy)": LocData(base_id + 227, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Luigi's Mansion (Easy)": LocData(base_id + 228, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Western Junction (Easy)": LocData(base_id + 229, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Bowser Jr. Blvd. (Easy)": LocData(base_id + 230, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Bowser's Castle (Easy)": LocData(base_id + 231, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Star Ship (Easy)": LocData(base_id + 232, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Wario Factory (Easy)": LocData(base_id + 233, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Waluigi Pinball (Easy)": LocData(base_id + 234, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Ghoulish Galleon (Easy)": LocData(base_id + 235, LocGroup.VOLLEYBALL_EX_EASY),

    # Hockey
    "Hockey Ex: Beat Mario Stadium (Easy)": LocData(base_id + 236, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Toad Park (Easy)": LocData(base_id + 237, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Peach's Castle (Easy)": LocData(base_id + 238, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Western Junction (Easy)": LocData(base_id + 239, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Wario Factory (Easy)": LocData(base_id + 240, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Daisy Garden (Easy)": LocData(base_id + 241, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Bowser Jr. Blvd. (Easy)": LocData(base_id + 242, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Waluigi Pinball (Easy)": LocData(base_id + 243, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Star Ship (Easy)": LocData(base_id + 244, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Koopa Troopa Beach (Easy)": LocData(base_id + 245, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Ghoulish Galleon (Easy)": LocData(base_id + 246, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Bowser's Castle (Easy)": LocData(base_id + 247, LocGroup.HOCKEY_EX_EASY),
}

normal_exhibition_locations: Dict[str, LocData] = {
    # Basketball
    "Basketball Ex: Beat Mario Stadium (Normal)": LocData(base_id + 300, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Koopa Troopa Beach (Normal)": LocData(base_id + 301, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat DK Dock (Normal)": LocData(base_id + 302, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Luigi's Mansion (Normal)": LocData(base_id + 303, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Western Junction (Normal)": LocData(base_id + 304, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Daisy Garden (Normal)": LocData(base_id + 305, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Bowser Jr. Blvd. (Normal)": LocData(base_id + 306, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Bowser's Castle (Normal)": LocData(base_id + 307, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Star Ship (Normal)": LocData(base_id + 308, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Peach's Castle (Normal)": LocData(base_id + 309, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Wario Factory (Normal)": LocData(base_id + 310, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Ghoulish Galleon (Normal)": LocData(base_id + 311, LocGroup.BASKETBALL_EX_NORMAL),

    # Dodgeball
    "Dodgeball Ex: Beat Mario Stadium (Normal)": LocData(base_id + 312, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Koopa Troopa Beach (Normal)": LocData(base_id + 313, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Peach's Castle (Normal)": LocData(base_id + 314, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat DK Dock (Normal)": LocData(base_id + 315, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Toad Park (Normal)": LocData(base_id + 316, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Daisy Garden (Normal)": LocData(base_id + 317, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Wario Factory (Normal)": LocData(base_id + 318, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Bowser's Castle (Normal)": LocData(base_id + 319, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Star Ship (Normal)": LocData(base_id + 320, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Western Junction (Normal)": LocData(base_id + 321, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Waluigi Pinball (Normal)": LocData(base_id + 322, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Ghoulish Galleon (Normal)": LocData(base_id + 323, LocGroup.DODGEBALL_EX_NORMAL),

    # Volleyball
    "Volleyball Ex: Beat Mario Stadium (Normal)": LocData(base_id + 324, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Koopa Troopa Beach (Normal)": LocData(base_id + 325, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Peach's Castle (Normal)": LocData(base_id + 326, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat DK Dock (Normal)": LocData(base_id + 327, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Luigi's Mansion (Normal)": LocData(base_id + 328, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Western Junction (Normal)": LocData(base_id + 329, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Bowser Jr. Blvd. (Normal)": LocData(base_id + 330, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Bowser's Castle (Normal)": LocData(base_id + 331, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Star Ship (Normal)": LocData(base_id + 332, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Wario Factory (Normal)": LocData(base_id + 333, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Waluigi Pinball (Normal)": LocData(base_id + 334, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Ghoulish Galleon (Normal)": LocData(base_id + 335, LocGroup.VOLLEYBALL_EX_NORMAL),

    # Hockey
    "Hockey Ex: Beat Mario Stadium (Normal)": LocData(base_id + 336, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Toad Park (Normal)": LocData(base_id + 337, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Peach's Castle (Normal)": LocData(base_id + 338, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Western Junction (Normal)": LocData(base_id + 339, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Wario Factory (Normal)": LocData(base_id + 340, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Daisy Garden (Normal)": LocData(base_id + 341, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Bowser Jr. Blvd. (Normal)": LocData(base_id + 342, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Waluigi Pinball (Normal)": LocData(base_id + 343, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Star Ship (Normal)": LocData(base_id + 344, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Koopa Troopa Beach (Normal)": LocData(base_id + 345, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Ghoulish Galleon (Normal)": LocData(base_id + 346, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Bowser's Castle (Normal)": LocData(base_id + 347, LocGroup.HOCKEY_EX_NORMAL),
}

hard_exhibition_locations: Dict[str, LocData] = {
    # Basketball
    "Basketball Ex: Beat Mario Stadium (Hard)": LocData(base_id + 400, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Koopa Troopa Beach (Hard)": LocData(base_id + 401, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat DK Dock (Hard)": LocData(base_id + 402, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Luigi's Mansion (Hard)": LocData(base_id + 403, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Western Junction (Hard)": LocData(base_id + 404, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Daisy Garden (Hard)": LocData(base_id + 405, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Bowser Jr. Blvd. (Hard)": LocData(base_id + 406, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Bowser's Castle (Hard)": LocData(base_id + 407, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Star Ship (Hard)": LocData(base_id + 408, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Peach's Castle (Hard)": LocData(base_id + 409, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Wario Factory (Hard)": LocData(base_id + 410, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Ghoulish Galleon (Hard)": LocData(base_id + 411, LocGroup.BASKETBALL_EX_HARD),

    # Dodgeball
    "Dodgeball Ex: Beat Mario Stadium (Hard)": LocData(base_id + 412, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Koopa Troopa Beach (Hard)": LocData(base_id + 413, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Peach's Castle (Hard)": LocData(base_id + 414, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat DK Dock (Hard)": LocData(base_id + 415, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Toad Park (Hard)": LocData(base_id + 416, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Daisy Garden (Hard)": LocData(base_id + 417, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Wario Factory (Hard)": LocData(base_id + 418, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Bowser's Castle (Hard)": LocData(base_id + 419, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Star Ship (Hard)": LocData(base_id + 420, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Western Junction (Hard)": LocData(base_id + 421, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Waluigi Pinball (Hard)": LocData(base_id + 422, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Ghoulish Galleon (Hard)": LocData(base_id + 423, LocGroup.DODGEBALL_EX_HARD),

    # Volleyball
    "Volleyball Ex: Beat Mario Stadium (Hard)": LocData(base_id + 424, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Koopa Troopa Beach (Hard)": LocData(base_id + 425, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Peach's Castle (Hard)": LocData(base_id + 426, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat DK Dock (Hard)": LocData(base_id + 427, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Luigi's Mansion (Hard)": LocData(base_id + 428, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Western Junction (Hard)": LocData(base_id + 429, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Bowser Jr. Blvd. (Hard)": LocData(base_id + 430, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Bowser's Castle (Hard)": LocData(base_id + 431, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Star Ship (Hard)": LocData(base_id + 432, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Wario Factory (Hard)": LocData(base_id + 433, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Waluigi Pinball (Hard)": LocData(base_id + 434, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Ghoulish Galleon (Hard)": LocData(base_id + 435, LocGroup.VOLLEYBALL_EX_HARD),

    # Hockey
    "Hockey Ex: Beat Mario Stadium (Hard)": LocData(base_id + 436, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Toad Park (Hard)": LocData(base_id + 437, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Peach's Castle (Hard)": LocData(base_id + 438, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Western Junction (Hard)": LocData(base_id + 439, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Wario Factory (Hard)": LocData(base_id + 440, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Daisy Garden (Hard)": LocData(base_id + 441, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Bowser Jr. Blvd. (Hard)": LocData(base_id + 442, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Waluigi Pinball (Hard)": LocData(base_id + 443, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Star Ship (Hard)": LocData(base_id + 444, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Koopa Troopa Beach (Hard)": LocData(base_id + 445, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Ghoulish Galleon (Hard)": LocData(base_id + 446, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Bowser's Castle (Hard)": LocData(base_id + 447, LocGroup.HOCKEY_EX_HARD),
}

expert_exhibition_locations: Dict[str, LocData] = {
    # Basketball
    "Basketball Ex: Beat Mario Stadium (Expert)": LocData(base_id + 500, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Koopa Troopa Beach (Expert)": LocData(base_id + 501, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat DK Dock (Expert)": LocData(base_id + 502, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Luigi's Mansion (Expert)": LocData(base_id + 503, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Western Junction (Expert)": LocData(base_id + 504, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Daisy Garden (Expert)": LocData(base_id + 505, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Bowser Jr. Blvd. (Expert)": LocData(base_id + 506, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Bowser's Castle (Expert)": LocData(base_id + 507, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Star Ship (Expert)": LocData(base_id + 508, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Peach's Castle (Expert)": LocData(base_id + 509, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Wario Factory (Expert)": LocData(base_id + 510, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Ghoulish Galleon (Expert)": LocData(base_id + 511, LocGroup.BASKETBALL_EX_EXPERT),

    # Dodgeball
    "Dodgeball Ex: Beat Mario Stadium (Expert)": LocData(base_id + 512, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Koopa Troopa Beach (Expert)": LocData(base_id + 513, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Peach's Castle (Expert)": LocData(base_id + 514, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat DK Dock (Expert)": LocData(base_id + 515, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Toad Park (Expert)": LocData(base_id + 516, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Daisy Garden (Expert)": LocData(base_id + 517, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Wario Factory (Expert)": LocData(base_id + 518, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Bowser's Castle (Expert)": LocData(base_id + 519, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Star Ship (Expert)": LocData(base_id + 520, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Western Junction (Expert)": LocData(base_id + 521, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Waluigi Pinball (Expert)": LocData(base_id + 522, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Ghoulish Galleon (Expert)": LocData(base_id + 523, LocGroup.DODGEBALL_EX_EXPERT),

    # Volleyball
    "Volleyball Ex: Beat Mario Stadium (Expert)": LocData(base_id + 524, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Koopa Troopa Beach (Expert)": LocData(base_id + 525, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Peach's Castle (Expert)": LocData(base_id + 526, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat DK Dock (Expert)": LocData(base_id + 527, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Luigi's Mansion (Expert)": LocData(base_id + 528, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Western Junction (Expert)": LocData(base_id + 529, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Bowser Jr. Blvd. (Expert)": LocData(base_id + 530, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Bowser's Castle (Expert)": LocData(base_id + 531, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Star Ship (Expert)": LocData(base_id + 532, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Wario Factory (Expert)": LocData(base_id + 533, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Waluigi Pinball (Expert)": LocData(base_id + 534, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Ghoulish Galleon (Expert)": LocData(base_id + 535, LocGroup.VOLLEYBALL_EX_EXPERT),

    # Hockey
    "Hockey Ex: Beat Mario Stadium (Expert)": LocData(base_id + 536, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Toad Park (Expert)": LocData(base_id + 537, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Peach's Castle (Expert)": LocData(base_id + 538, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Western Junction (Expert)": LocData(base_id + 539, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Wario Factory (Expert)": LocData(base_id + 540, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Daisy Garden (Expert)": LocData(base_id + 541, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Bowser Jr. Blvd. (Expert)": LocData(base_id + 542, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Waluigi Pinball (Expert)": LocData(base_id + 543, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Star Ship (Expert)": LocData(base_id + 544, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Koopa Troopa Beach (Expert)": LocData(base_id + 545, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Ghoulish Galleon (Expert)": LocData(base_id + 546, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Bowser's Castle (Expert)": LocData(base_id + 547, LocGroup.HOCKEY_EX_EXPERT),
}

global_exhibition_locations: Dict[str, LocData] = {
    # Easy
    "Exhibition: Beat Mario Stadium (Easy)": LocData(base_id + 600, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Koopa Troopa Beach (Easy)": LocData(base_id + 601, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Peach's Castle (Easy)": LocData(base_id + 602, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat DK Dock (Easy)": LocData(base_id + 603, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Toad Park (Easy)": LocData(base_id + 604, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Luigi's Mansion (Easy)": LocData(base_id + 605, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Western Junction (Easy)": LocData(base_id + 606, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Daisy Garden (Easy)": LocData(base_id + 607, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Wario Factory (Easy)": LocData(base_id + 608, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Bowser Jr. Blvd. (Easy)": LocData(base_id + 609, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Bowser's Castle (Easy)": LocData(base_id + 610, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Waluigi Pinball (Easy)": LocData(base_id + 611, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Ghoulish Galleon (Easy)": LocData(base_id + 612, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Star Ship (Easy)": LocData(base_id + 613, LocGroup.EXHIBITION_EASY),

    # Normal
    "Exhibition: Beat Mario Stadium (Normal)": LocData(base_id + 614, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Koopa Troopa Beach (Normal)": LocData(base_id + 615, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Peach's Castle (Normal)": LocData(base_id + 616, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat DK Dock (Normal)": LocData(base_id + 617, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Toad Park (Normal)": LocData(base_id + 618, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Luigi's Mansion (Normal)": LocData(base_id + 619, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Western Junction (Normal)": LocData(base_id + 620, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Daisy Garden (Normal)": LocData(base_id + 621, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Wario Factory (Normal)": LocData(base_id + 622, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Bowser Jr. Blvd. (Normal)": LocData(base_id + 623, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Bowser's Castle (Normal)": LocData(base_id + 624, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Waluigi Pinball (Normal)": LocData(base_id + 625, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Ghoulish Galleon (Normal)": LocData(base_id + 626, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Star Ship (Normal)": LocData(base_id + 627, LocGroup.EXHIBITION_NORMAL),

    # Hard
    "Exhibition: Beat Mario Stadium (Hard)": LocData(base_id + 628, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Koopa Troopa Beach (Hard)": LocData(base_id + 629, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Peach's Castle (Hard)": LocData(base_id + 630, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat DK Dock (Hard)": LocData(base_id + 631, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Toad Park (Hard)": LocData(base_id + 632, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Luigi's Mansion (Hard)": LocData(base_id + 633, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Western Junction (Hard)": LocData(base_id + 634, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Daisy Garden (Hard)": LocData(base_id + 635, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Wario Factory (Hard)": LocData(base_id + 636, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Bowser Jr. Blvd. (Hard)": LocData(base_id + 637, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Bowser's Castle (Hard)": LocData(base_id + 638, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Waluigi Pinball (Hard)": LocData(base_id + 639, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Ghoulish Galleon (Hard)": LocData(base_id + 640, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Star Ship (Hard)": LocData(base_id + 641, LocGroup.EXHIBITION_HARD),

    # Expert
    "Exhibition: Beat Mario Stadium (Expert)": LocData(base_id + 642, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Koopa Troopa Beach (Expert)": LocData(base_id + 643, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Peach's Castle (Expert)": LocData(base_id + 644, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat DK Dock (Expert)": LocData(base_id + 645, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Toad Park (Expert)": LocData(base_id + 646, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Luigi's Mansion (Expert)": LocData(base_id + 647, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Western Junction (Expert)": LocData(base_id + 648, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Daisy Garden (Expert)": LocData(base_id + 649, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Wario Factory (Expert)": LocData(base_id + 650, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Bowser Jr. Blvd. (Expert)": LocData(base_id + 651, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Bowser's Castle (Expert)": LocData(base_id + 652, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Waluigi Pinball (Expert)": LocData(base_id + 653, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Ghoulish Galleon (Expert)": LocData(base_id + 654, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Star Ship (Expert)": LocData(base_id + 655, LocGroup.EXHIBITION_EXPERT),
}

# === Party Game Locations ===

feed_petey_locations: Dict[str, LocData] = {
    "Feed Petey: Beat Daisy Garden (Apple)": LocData(base_id + 800, LocGroup.FEED_PETEY),
    "Feed Petey: Beat Daisy Garden (Watermelon)": LocData(base_id + 801, LocGroup.FEED_PETEY),
    "Feed Petey: Beat DK Dock (Apple)": LocData(base_id + 802, LocGroup.FEED_PETEY),
    "Feed Petey: Beat DK Dock (Watermelon)": LocData(base_id + 803, LocGroup.FEED_PETEY),
    "Feed Petey: Beat Wario Factory (Apple)": LocData(base_id + 804, LocGroup.FEED_PETEY),
    "Feed Petey: Beat Wario Factory (Watermelon)": LocData(base_id + 805, LocGroup.FEED_PETEY),
}

harmony_hustle_locations: Dict[str, LocData] = {
    "Harmony Hustle: Beat Classic Ocean": LocData(base_id + 806, LocGroup.HARMONY_HUSTLE),
    "Harmony Hustle: Beat Chocobo Rhythm": LocData(base_id + 807, LocGroup.HARMONY_HUSTLE),
    "Harmony Hustle: Beat Mario Athletic": LocData(base_id + 808, LocGroup.HARMONY_HUSTLE),
    "Harmony Hustle: Beat Mushroom Mix Medley": LocData(base_id + 809, LocGroup.HARMONY_HUSTLE),

    "Harmony Hustle: Beat Bloocheep Ocean": LocData(base_id + 810, LocGroup.HARMONY_HUSTLE),
    "Harmony Hustle: Beat Chocobo Pop": LocData(base_id + 811, LocGroup.HARMONY_HUSTLE),
    "Harmony Hustle: Beat Punk Athletic": LocData(base_id + 812, LocGroup.HARMONY_HUSTLE),
    "Harmony Hustle: Beat Blossom Mix Medley": LocData(base_id + 813, LocGroup.HARMONY_HUSTLE),

    "Harmony Hustle: Beat Punk Ocean": LocData(base_id + 814, LocGroup.HARMONY_HUSTLE),
    "Harmony Hustle: Beat Chocobo Beat": LocData(base_id + 815, LocGroup.HARMONY_HUSTLE),
    "Harmony Hustle: Beat Island Athletic": LocData(base_id + 816, LocGroup.HARMONY_HUSTLE),
    "Harmony Hustle: Beat Star Mix Medley": LocData(base_id + 817, LocGroup.HARMONY_HUSTLE),
}

bob_omb_dodge_locations: Dict[str, LocData] = {
    "Bob-omb Dodge: Beat Mario Stadium (Bob-omb)": LocData(base_id + 818, LocGroup.BOB_OMB_DODGE),
    "Bob-omb Dodge: Beat Mario Stadium (Cannon)": LocData(base_id + 819, LocGroup.BOB_OMB_DODGE),
    "Bob-omb Dodge: Beat Ghoulish Galleon (Bob-omb)": LocData(base_id + 820, LocGroup.BOB_OMB_DODGE),
    "Bob-omb Dodge: Beat Ghoulish Galleon (Cannon)": LocData(base_id + 821, LocGroup.BOB_OMB_DODGE),
    "Bob-omb Dodge: Beat Western Junction (Bob-omb)": LocData(base_id + 822, LocGroup.BOB_OMB_DODGE),
    "Bob-omb Dodge: Beat Western Junction (Cannon)": LocData(base_id + 823, LocGroup.BOB_OMB_DODGE),
}

smash_skate_locations: Dict[str, LocData] = {
    "Smash Skate: Beat Sherbet Sea (Hockey Stick)": LocData(base_id + 824, LocGroup.SMASH_SKATE),
    "Smash Skate: Beat Sherbet Sea (Hockey Skate)": LocData(base_id + 825, LocGroup.SMASH_SKATE),
    "Smash Skate: Beat Rowdy Raft (Hockey Stick)": LocData(base_id + 826, LocGroup.SMASH_SKATE),
    "Smash Skate: Beat Rowdy Raft (Hockey Skate)": LocData(base_id + 827, LocGroup.SMASH_SKATE),
    "Smash Skate: Beat Fire Mountain (Hockey Stick)": LocData(base_id + 828, LocGroup.SMASH_SKATE),
    "Smash Skate: Beat Fire Mountain (Hockey Skate)": LocData(base_id + 829, LocGroup.SMASH_SKATE),
}

special_sanity_locations: Dict[str, LocData] = {
    "Use Mario's Special": LocData(base_id + 5000, LocGroup.SPECIAL_SANITY),
    "Use Luigi's Special": LocData(base_id + 5001, LocGroup.SPECIAL_SANITY),
    "Use Peach's Special": LocData(base_id + 5002, LocGroup.SPECIAL_SANITY),
    "Use Daisy's Special": LocData(base_id + 5003, LocGroup.SPECIAL_SANITY),
    "Use Yoshi's Special": LocData(base_id + 5004, LocGroup.SPECIAL_SANITY),
    "Use Wario's Special": LocData(base_id + 5005, LocGroup.SPECIAL_SANITY),
    "Use Waluigi's Special": LocData(base_id + 5006, LocGroup.SPECIAL_SANITY),
    "Use Donkey Kong's Special": LocData(base_id + 5007, LocGroup.SPECIAL_SANITY),
    "Use Diddy Kong's Special": LocData(base_id + 5008, LocGroup.SPECIAL_SANITY),
    "Use Toad's Special": LocData(base_id + 5009, LocGroup.SPECIAL_SANITY),
    "Use Bowser's Special": LocData(base_id + 5010, LocGroup.SPECIAL_SANITY),
    "Use Bowser Jr's Special": LocData(base_id + 5011, LocGroup.SPECIAL_SANITY),
    "Use Moogle's Special": LocData(base_id + 5012, LocGroup.SPECIAL_SANITY),
    "Use Cactuar's Special": LocData(base_id + 5013, LocGroup.SPECIAL_SANITY),
    "Use Ninja's Special": LocData(base_id + 5014, LocGroup.SPECIAL_SANITY),
    "Use White Mage's Special": LocData(base_id + 5015, LocGroup.SPECIAL_SANITY),
    "Use Slime's Special": LocData(base_id + 5016, LocGroup.SPECIAL_SANITY),
    "Use Black Mage's Special": LocData(base_id + 5017, LocGroup.SPECIAL_SANITY),
    "Use Mii (Male)'s Special": LocData(base_id + 5018, LocGroup.SPECIAL_SANITY),
    "Use Mii (Female)'s Special": LocData(base_id + 5019, LocGroup.SPECIAL_SANITY),
}

character_sanity_locations: Dict[str, LocData] = {
    "Win as Mario": LocData(base_id + 6001, LocGroup.CHARACTER_SANITY),
    "Win as Luigi": LocData(base_id + 6002, LocGroup.CHARACTER_SANITY),
    "Win as Peach": LocData(base_id + 6003, LocGroup.CHARACTER_SANITY),
    "Win as Daisy": LocData(base_id + 6004, LocGroup.CHARACTER_SANITY),
    "Win as Yoshi": LocData(base_id + 6005, LocGroup.CHARACTER_SANITY),
    "Win as Wario": LocData(base_id + 6006, LocGroup.CHARACTER_SANITY),
    "Win as Waluigi": LocData(base_id + 6007, LocGroup.CHARACTER_SANITY),
    "Win as Donkey Kong": LocData(base_id + 6008, LocGroup.CHARACTER_SANITY),
    "Win as Diddy Kong": LocData(base_id + 6009, LocGroup.CHARACTER_SANITY),
    "Win as Toad": LocData(base_id + 6010, LocGroup.CHARACTER_SANITY),
    "Win as Bowser": LocData(base_id + 6011, LocGroup.CHARACTER_SANITY),
    "Win as Bowser Jr": LocData(base_id + 6012, LocGroup.CHARACTER_SANITY),
    "Win as Moogle": LocData(base_id + 6013, LocGroup.CHARACTER_SANITY),
    "Win as Cactuar": LocData(base_id + 6014, LocGroup.CHARACTER_SANITY),
    "Win as Ninja": LocData(base_id + 6015, LocGroup.CHARACTER_SANITY),
    "Win as White Mage": LocData(base_id + 6016, LocGroup.CHARACTER_SANITY),
    "Win as Slime": LocData(base_id + 6017, LocGroup.CHARACTER_SANITY),
    "Win as Black Mage": LocData(base_id + 6018, LocGroup.CHARACTER_SANITY),
    "Win as Mii (Male)": LocData(base_id + 6019, LocGroup.CHARACTER_SANITY),
    "Win as Mii (Female)": LocData(base_id + 6020, LocGroup.CHARACTER_SANITY),
}

costume_char_sanity_locations: Dict[str, LocData] = {
    "Win as Pink Yoshi": LocData(base_id + 6021, LocGroup.COSTUME_SANITY),
    "Win as Light Blue Yoshi": LocData(base_id + 6022, LocGroup.COSTUME_SANITY),
    "Win as Yellow Yoshi": LocData(base_id + 6023, LocGroup.COSTUME_SANITY),
    "Win as Blue Toad": LocData(base_id + 6024, LocGroup.COSTUME_SANITY),
    "Win as Green Toad": LocData(base_id + 6025, LocGroup.COSTUME_SANITY),
    "Win as Yellow Toad": LocData(base_id + 6026, LocGroup.COSTUME_SANITY),
    "Win as She-Slime": LocData(base_id + 6027, LocGroup.COSTUME_SANITY),
    "Win as Metal Slime": LocData(base_id + 6028, LocGroup.COSTUME_SANITY),
    "Win as Tennis-wear Peach": LocData(base_id + 6029, LocGroup.COSTUME_SANITY),
    "Win as Tennis-wear Daisy": LocData(base_id + 6030, LocGroup.COSTUME_SANITY),
    "Win as Shadow White Ninja": LocData(base_id + 6031, LocGroup.COSTUME_SANITY),
    "Win as Pure White - White Mage": LocData(base_id + 6032, LocGroup.COSTUME_SANITY),
    "Win as Magic Red Black Mage": LocData(base_id + 6033, LocGroup.COSTUME_SANITY),
}

court_sanity_locations: Dict[str, LocData] = {
    "Win on Mario Stadium": LocData(base_id + 7000, LocGroup.COURT_SANITY),
    "Win on Koopa Troopa Beach": LocData(base_id + 7001, LocGroup.COURT_SANITY),
    "Win on Peach's Castle": LocData(base_id + 7002, LocGroup.COURT_SANITY),
    "Win on Toad Park": LocData(base_id + 7003, LocGroup.COURT_SANITY),
    "Win on DK Dock": LocData(base_id + 7004, LocGroup.COURT_SANITY),
    "Win on Luigi's Mansion": LocData(base_id + 7005, LocGroup.COURT_SANITY),
    "Win on Daisy Garden": LocData(base_id + 7006, LocGroup.COURT_SANITY),
    "Win on Wario Factory": LocData(base_id + 7007, LocGroup.COURT_SANITY),
    "Win on Bowser Jr. Blvd.": LocData(base_id + 7008, LocGroup.COURT_SANITY),
    "Win on Bowser's Castle": LocData(base_id + 7009, LocGroup.COURT_SANITY),
    "Win on Waluigi Pinball": LocData(base_id + 7010, LocGroup.COURT_SANITY),
    "Win on Ghoulish Galleon": LocData(base_id + 7011, LocGroup.COURT_SANITY),
    "Win on Star Ship": LocData(base_id + 7012, LocGroup.COURT_SANITY),
    "Win on Western Junction": LocData(base_id + 7013, LocGroup.COURT_SANITY),

    "Win on Sherbet Sea": LocData(base_id + 7014, LocGroup.COURT_SANITY),
    "Win on Fire Mountain": LocData(base_id + 7015, LocGroup.COURT_SANITY),
    "Win on Rowdy Raft": LocData(base_id + 7016, LocGroup.COURT_SANITY),

    "Win on Classic Ocean": LocData(base_id + 7017, LocGroup.COURT_SANITY),
    "Win on Chocobo Rhythm": LocData(base_id + 7018, LocGroup.COURT_SANITY),
    "Win on Mario Athletic": LocData(base_id + 7019, LocGroup.COURT_SANITY),
    "Win on Bloocheep Ocean": LocData(base_id + 7020, LocGroup.COURT_SANITY),
    "Win on Chocobo Pop": LocData(base_id + 7021, LocGroup.COURT_SANITY),
    "Win on Punk Athletic": LocData(base_id + 7022, LocGroup.COURT_SANITY),
    "Win on Punk Ocean": LocData(base_id + 7023, LocGroup.COURT_SANITY),
    "Win on Chocobo Beat": LocData(base_id + 7024, LocGroup.COURT_SANITY),
    "Win on Island Athletic": LocData(base_id + 7025, LocGroup.COURT_SANITY),
    "Win on Mushroom Mix Medley": LocData(base_id + 7026, LocGroup.COURT_SANITY, LPT.PRIORITY),
    "Win on Blossom Mix Medley": LocData(base_id + 7027, LocGroup.COURT_SANITY, LPT.PRIORITY),
    "Win on Star Mix Medley": LocData(base_id + 7028, LocGroup.COURT_SANITY, LPT.PRIORITY),
}

boss_locations: Dict[str, LocData] = {
    "Defeat Behemoth!": LocData(base_id + 20000, LocGroup.BOSS_LOCATIONS, LPT.PRIORITY),
    "Defeat Behemoth King!": LocData(base_id + 20001, LocGroup.BOSS_LOCATIONS, LPT.PRIORITY),
}

basketball_alternate_path_normal_locations: Dict[str, LocData] = {
    "Basketball Mushroom Cup Alt Path Normal Node 21": LocData(base_id + 30000, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Node 2B": LocData(base_id + 30001, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Node 31": LocData(base_id + 30002, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Node 28": LocData(base_id + 30003, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Node 38": LocData(base_id + 30004, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Node 3B": LocData(base_id + 30005, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Node 24": LocData(base_id + 30006, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Node 30": LocData(base_id + 30007, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Node 36": LocData(base_id + 30008, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Node 35": LocData(base_id + 30009, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Node 34": LocData(base_id + 30010, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Node 37": LocData(base_id + 30011, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Node 29": LocData(base_id + 30012, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Node 25": LocData(base_id + 30013, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Node 39": LocData(base_id + 30014, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Node 32": LocData(base_id + 30015, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Node 26": LocData(base_id + 30048, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Node 52": LocData(base_id + 30049, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Node 50": LocData(base_id + 30050, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Node 2D": LocData(base_id + 30051, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Node 36": LocData(base_id + 30052, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Node 39": LocData(base_id + 30053, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Node 4E": LocData(base_id + 30054, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Node 3D": LocData(base_id + 30055, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Node 4B": LocData(base_id + 30056, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Node 2A": LocData(base_id + 30057, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Node 32": LocData(base_id + 30058, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Node 55": LocData(base_id + 30059, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Node 57": LocData(base_id + 30060, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Node 44": LocData(base_id + 30061, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Node 43": LocData(base_id + 30062, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Node 46": LocData(base_id + 30063, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Node 47": LocData(base_id + 30064, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Node 49": LocData(base_id + 30065, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Node 3E": LocData(base_id + 30066, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 2E": LocData(base_id + 30105, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 32": LocData(base_id + 30106, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 3E": LocData(base_id + 30107, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 3F": LocData(base_id + 30108, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 27": LocData(base_id + 30109, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 21": LocData(base_id + 30110, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 2A": LocData(base_id + 30111, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 23": LocData(base_id + 30112, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 30": LocData(base_id + 30113, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 38": LocData(base_id + 30114, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 3D": LocData(base_id + 30115, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 41": LocData(base_id + 30116, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 40": LocData(base_id + 30117, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 37": LocData(base_id + 30118, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 36": LocData(base_id + 30119, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 33": LocData(base_id + 30120, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 4A": LocData(base_id + 30121, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 4C": LocData(base_id + 30122, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 49": LocData(base_id + 30123, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 4D": LocData(base_id + 30124, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 43": LocData(base_id + 30125, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 47": LocData(base_id + 30126, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 4B": LocData(base_id + 30127, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 48": LocData(base_id + 30128, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Node 45": LocData(base_id + 30129, LocGroup.BASKETBALL_ALT_NORMAL),
}

basketball_alternate_path_hard_locations: Dict[str, LocData] = {
    "Basketball Mushroom Cup Alt Path Hard Node 21": LocData(base_id + 30016, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Node 2B": LocData(base_id + 30017, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Node 31": LocData(base_id + 30018, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Node 28": LocData(base_id + 30019, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Node 38": LocData(base_id + 30020, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Node 3B": LocData(base_id + 30021, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Node 24": LocData(base_id + 30022, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Node 30": LocData(base_id + 30023, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Node 36": LocData(base_id + 30024, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Node 35": LocData(base_id + 30025, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Node 34": LocData(base_id + 30026, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Node 37": LocData(base_id + 30027, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Node 29": LocData(base_id + 30028, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Node 25": LocData(base_id + 30029, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Node 39": LocData(base_id + 30030, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Node 32": LocData(base_id + 30031, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Node 26": LocData(base_id + 30067, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Node 52": LocData(base_id + 30068, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Node 50": LocData(base_id + 30069, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Node 2D": LocData(base_id + 30070, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Node 36": LocData(base_id + 30071, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Node 39": LocData(base_id + 30072, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Node 4E": LocData(base_id + 30073, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Node 3D": LocData(base_id + 30074, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Node 4B": LocData(base_id + 30075, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Node 2A": LocData(base_id + 30076, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Node 32": LocData(base_id + 30077, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Node 55": LocData(base_id + 30078, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Node 57": LocData(base_id + 30079, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Node 44": LocData(base_id + 30080, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Node 43": LocData(base_id + 30081, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Node 46": LocData(base_id + 30082, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Node 47": LocData(base_id + 30083, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Node 49": LocData(base_id + 30084, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Node 3E": LocData(base_id + 30085, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 2E": LocData(base_id + 30130, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 32": LocData(base_id + 30131, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 3E": LocData(base_id + 30132, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 3F": LocData(base_id + 30133, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 27": LocData(base_id + 30134, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 21": LocData(base_id + 30135, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 2A": LocData(base_id + 30136, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 23": LocData(base_id + 30137, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 30": LocData(base_id + 30138, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 38": LocData(base_id + 30139, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 3D": LocData(base_id + 30140, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 41": LocData(base_id + 30141, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 40": LocData(base_id + 30142, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 37": LocData(base_id + 30143, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 36": LocData(base_id + 30144, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 33": LocData(base_id + 30145, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 4A": LocData(base_id + 30146, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 4C": LocData(base_id + 30147, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 49": LocData(base_id + 30148, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 4D": LocData(base_id + 30149, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 43": LocData(base_id + 30150, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 47": LocData(base_id + 30151, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 4B": LocData(base_id + 30152, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 48": LocData(base_id + 30153, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Node 45": LocData(base_id + 30154, LocGroup.BASKETBALL_ALT_HARD),
}

basketball_alternate_path_global_locations: Dict[str, LocData] = {
    "Basketball Mushroom Cup Alt Path Node 21": LocData(base_id + 30032, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Node 2B": LocData(base_id + 30033, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Node 31": LocData(base_id + 30034, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Node 28": LocData(base_id + 30035, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Node 38": LocData(base_id + 30036, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Node 3B": LocData(base_id + 30037, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Node 24": LocData(base_id + 30038, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Node 30": LocData(base_id + 30039, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Node 36": LocData(base_id + 30040, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Node 35": LocData(base_id + 30041, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Node 34": LocData(base_id + 30042, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Node 37": LocData(base_id + 30043, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Node 29": LocData(base_id + 30044, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Node 25": LocData(base_id + 30045, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Node 39": LocData(base_id + 30046, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Node 32": LocData(base_id + 30047, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Node 26": LocData(base_id + 30086, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Node 52": LocData(base_id + 30087, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Node 50": LocData(base_id + 30088, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Node 2D": LocData(base_id + 30089, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Node 36": LocData(base_id + 30090, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Node 39": LocData(base_id + 30091, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Node 4E": LocData(base_id + 30092, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Node 3D": LocData(base_id + 30093, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Node 4B": LocData(base_id + 30094, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Node 2A": LocData(base_id + 30095, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Node 32": LocData(base_id + 30096, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Node 55": LocData(base_id + 30097, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Node 57": LocData(base_id + 30098, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Node 44": LocData(base_id + 30099, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Node 43": LocData(base_id + 30100, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Node 46": LocData(base_id + 30101, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Node 47": LocData(base_id + 30102, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Node 49": LocData(base_id + 30103, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Node 3E": LocData(base_id + 30104, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 2E": LocData(base_id + 30155, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 32": LocData(base_id + 30156, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 3E": LocData(base_id + 30157, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 3F": LocData(base_id + 30158, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 27": LocData(base_id + 30159, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 21": LocData(base_id + 30160, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 2A": LocData(base_id + 30161, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 23": LocData(base_id + 30162, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 30": LocData(base_id + 30163, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 38": LocData(base_id + 30164, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 3D": LocData(base_id + 30165, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 41": LocData(base_id + 30166, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 40": LocData(base_id + 30167, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 37": LocData(base_id + 30168, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 36": LocData(base_id + 30169, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 33": LocData(base_id + 30170, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 4A": LocData(base_id + 30171, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 4C": LocData(base_id + 30172, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 49": LocData(base_id + 30173, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 4D": LocData(base_id + 30174, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 43": LocData(base_id + 30175, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 47": LocData(base_id + 30176, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 4B": LocData(base_id + 30177, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 48": LocData(base_id + 30178, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Node 45": LocData(base_id + 30179, LocGroup.BASKETBALL_ALT),
}

dodgeball_alternate_path_normal_locations: Dict[str, LocData] = {
    "Dodgeball Mushroom Cup Alt Path Normal Node 21": LocData(base_id + 30180, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Node 2B": LocData(base_id + 30181, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Node 31": LocData(base_id + 30182, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Node 28": LocData(base_id + 30183, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Node 38": LocData(base_id + 30184, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Node 3B": LocData(base_id + 30185, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Node 24": LocData(base_id + 30186, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Node 30": LocData(base_id + 30187, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Node 36": LocData(base_id + 30188, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Node 35": LocData(base_id + 30189, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Node 34": LocData(base_id + 30190, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Node 37": LocData(base_id + 30191, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Node 29": LocData(base_id + 30192, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Node 25": LocData(base_id + 30193, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Node 39": LocData(base_id + 30194, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Node 32": LocData(base_id + 30195, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Node 26": LocData(base_id + 30228, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Node 52": LocData(base_id + 30229, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Node 50": LocData(base_id + 30230, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Node 2D": LocData(base_id + 30231, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Node 36": LocData(base_id + 30232, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Node 39": LocData(base_id + 30233, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Node 4E": LocData(base_id + 30234, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Node 3D": LocData(base_id + 30235, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Node 4B": LocData(base_id + 30236, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Node 2A": LocData(base_id + 30237, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Node 32": LocData(base_id + 30238, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Node 55": LocData(base_id + 30239, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Node 57": LocData(base_id + 30240, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Node 44": LocData(base_id + 30241, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Node 43": LocData(base_id + 30242, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Node 46": LocData(base_id + 30243, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Node 47": LocData(base_id + 30244, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Node 49": LocData(base_id + 30245, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Node 3E": LocData(base_id + 30246, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 2E": LocData(base_id + 30285, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 32": LocData(base_id + 30286, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 3E": LocData(base_id + 30287, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 3F": LocData(base_id + 30288, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 27": LocData(base_id + 30289, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 21": LocData(base_id + 30290, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 2A": LocData(base_id + 30291, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 23": LocData(base_id + 30292, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 30": LocData(base_id + 30293, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 38": LocData(base_id + 30294, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 3D": LocData(base_id + 30295, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 41": LocData(base_id + 30296, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 40": LocData(base_id + 30297, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 37": LocData(base_id + 30298, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 36": LocData(base_id + 30299, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 33": LocData(base_id + 30300, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 4A": LocData(base_id + 30301, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 4C": LocData(base_id + 30302, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 49": LocData(base_id + 30303, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 4D": LocData(base_id + 30304, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 43": LocData(base_id + 30305, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 47": LocData(base_id + 30306, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 4B": LocData(base_id + 30307, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 48": LocData(base_id + 30308, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Node 45": LocData(base_id + 30309, LocGroup.DODGEBALL_ALT_NORMAL),
}

dodgeball_alternate_path_hard_locations: Dict[str, LocData] = {
    "Dodgeball Mushroom Cup Alt Path Hard Node 21": LocData(base_id + 30196, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Node 2B": LocData(base_id + 30197, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Node 31": LocData(base_id + 30198, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Node 28": LocData(base_id + 30199, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Node 38": LocData(base_id + 30200, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Node 3B": LocData(base_id + 30201, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Node 24": LocData(base_id + 30202, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Node 30": LocData(base_id + 30203, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Node 36": LocData(base_id + 30204, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Node 35": LocData(base_id + 30205, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Node 34": LocData(base_id + 30206, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Node 37": LocData(base_id + 30207, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Node 29": LocData(base_id + 30208, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Node 25": LocData(base_id + 30209, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Node 39": LocData(base_id + 30210, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Node 32": LocData(base_id + 30211, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Node 26": LocData(base_id + 30247, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Node 52": LocData(base_id + 30248, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Node 50": LocData(base_id + 30249, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Node 2D": LocData(base_id + 30250, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Node 36": LocData(base_id + 30251, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Node 39": LocData(base_id + 30252, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Node 4E": LocData(base_id + 30253, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Node 3D": LocData(base_id + 30254, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Node 4B": LocData(base_id + 30255, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Node 2A": LocData(base_id + 30256, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Node 32": LocData(base_id + 30257, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Node 55": LocData(base_id + 30258, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Node 57": LocData(base_id + 30259, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Node 44": LocData(base_id + 30260, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Node 43": LocData(base_id + 30261, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Node 46": LocData(base_id + 30262, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Node 47": LocData(base_id + 30263, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Node 49": LocData(base_id + 30264, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Node 3E": LocData(base_id + 30265, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 2E": LocData(base_id + 30310, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 32": LocData(base_id + 30311, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 3E": LocData(base_id + 30312, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 3F": LocData(base_id + 30313, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 27": LocData(base_id + 30314, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 21": LocData(base_id + 30315, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 2A": LocData(base_id + 30316, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 23": LocData(base_id + 30317, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 30": LocData(base_id + 30318, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 38": LocData(base_id + 30319, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 3D": LocData(base_id + 30320, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 41": LocData(base_id + 30321, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 40": LocData(base_id + 30322, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 37": LocData(base_id + 30323, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 36": LocData(base_id + 30324, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 33": LocData(base_id + 30325, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 4A": LocData(base_id + 30326, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 4C": LocData(base_id + 30327, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 49": LocData(base_id + 30328, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 4D": LocData(base_id + 30329, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 43": LocData(base_id + 30330, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 47": LocData(base_id + 30331, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 4B": LocData(base_id + 30332, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 48": LocData(base_id + 30333, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Node 45": LocData(base_id + 30334, LocGroup.DODGEBALL_ALT_HARD),
}

dodgeball_alternate_path_global_locations: Dict[str, LocData] = {
    "Dodgeball Mushroom Cup Alt Path Node 21": LocData(base_id + 30212, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Node 2B": LocData(base_id + 30213, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Node 31": LocData(base_id + 30214, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Node 28": LocData(base_id + 30215, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Node 38": LocData(base_id + 30216, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Node 3B": LocData(base_id + 30217, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Node 24": LocData(base_id + 30218, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Node 30": LocData(base_id + 30219, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Node 36": LocData(base_id + 30220, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Node 35": LocData(base_id + 30221, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Node 34": LocData(base_id + 30222, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Node 37": LocData(base_id + 30223, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Node 29": LocData(base_id + 30224, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Node 25": LocData(base_id + 30225, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Node 39": LocData(base_id + 30226, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Node 32": LocData(base_id + 30227, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Node 26": LocData(base_id + 30266, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Node 52": LocData(base_id + 30267, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Node 50": LocData(base_id + 30268, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Node 2D": LocData(base_id + 30269, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Node 36": LocData(base_id + 30270, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Node 39": LocData(base_id + 30271, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Node 4E": LocData(base_id + 30272, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Node 3D": LocData(base_id + 30273, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Node 4B": LocData(base_id + 30274, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Node 2A": LocData(base_id + 30275, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Node 32": LocData(base_id + 30276, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Node 55": LocData(base_id + 30277, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Node 57": LocData(base_id + 30278, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Node 44": LocData(base_id + 30279, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Node 43": LocData(base_id + 30280, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Node 46": LocData(base_id + 30281, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Node 47": LocData(base_id + 30282, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Node 49": LocData(base_id + 30283, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Node 3E": LocData(base_id + 30284, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 2E": LocData(base_id + 30335, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 32": LocData(base_id + 30336, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 3E": LocData(base_id + 30337, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 3F": LocData(base_id + 30338, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 27": LocData(base_id + 30339, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 21": LocData(base_id + 30340, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 2A": LocData(base_id + 30341, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 23": LocData(base_id + 30342, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 30": LocData(base_id + 30343, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 38": LocData(base_id + 30344, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 3D": LocData(base_id + 30345, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 41": LocData(base_id + 30346, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 40": LocData(base_id + 30347, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 37": LocData(base_id + 30348, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 36": LocData(base_id + 30349, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 33": LocData(base_id + 30350, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 4A": LocData(base_id + 30351, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 4C": LocData(base_id + 30352, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 49": LocData(base_id + 30353, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 4D": LocData(base_id + 30354, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 43": LocData(base_id + 30355, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 47": LocData(base_id + 30356, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 4B": LocData(base_id + 30357, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 48": LocData(base_id + 30358, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Node 45": LocData(base_id + 30359, LocGroup.DODGEBALL_ALT),
}

volleyball_alternate_path_normal_locations: Dict[str, LocData] = {
    "Volleyball Mushroom Cup Alt Path Normal Node 21": LocData(base_id + 30360, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Node 2B": LocData(base_id + 30361, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Node 31": LocData(base_id + 30362, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Node 28": LocData(base_id + 30363, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Node 38": LocData(base_id + 30364, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Node 3B": LocData(base_id + 30365, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Node 24": LocData(base_id + 30366, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Node 30": LocData(base_id + 30367, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Node 36": LocData(base_id + 30368, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Node 35": LocData(base_id + 30369, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Node 34": LocData(base_id + 30370, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Node 37": LocData(base_id + 30371, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Node 29": LocData(base_id + 30372, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Node 25": LocData(base_id + 30373, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Node 39": LocData(base_id + 30374, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Node 32": LocData(base_id + 30375, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Node 26": LocData(base_id + 30408, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Node 52": LocData(base_id + 30409, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Node 50": LocData(base_id + 30410, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Node 2D": LocData(base_id + 30411, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Node 36": LocData(base_id + 30412, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Node 39": LocData(base_id + 30413, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Node 4E": LocData(base_id + 30414, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Node 3D": LocData(base_id + 30415, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Node 4B": LocData(base_id + 30416, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Node 2A": LocData(base_id + 30417, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Node 32": LocData(base_id + 30418, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Node 55": LocData(base_id + 30419, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Node 57": LocData(base_id + 30420, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Node 44": LocData(base_id + 30421, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Node 43": LocData(base_id + 30422, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Node 46": LocData(base_id + 30423, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Node 47": LocData(base_id + 30424, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Node 49": LocData(base_id + 30425, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Node 3E": LocData(base_id + 30426, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 2E": LocData(base_id + 30465, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 32": LocData(base_id + 30466, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 3E": LocData(base_id + 30467, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 3F": LocData(base_id + 30468, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 27": LocData(base_id + 30469, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 21": LocData(base_id + 30470, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 2A": LocData(base_id + 30471, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 23": LocData(base_id + 30472, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 30": LocData(base_id + 30473, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 38": LocData(base_id + 30474, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 3D": LocData(base_id + 30475, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 41": LocData(base_id + 30476, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 40": LocData(base_id + 30477, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 37": LocData(base_id + 30478, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 36": LocData(base_id + 30479, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 33": LocData(base_id + 30480, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 4A": LocData(base_id + 30481, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 4C": LocData(base_id + 30482, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 49": LocData(base_id + 30483, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 4D": LocData(base_id + 30484, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 43": LocData(base_id + 30485, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 47": LocData(base_id + 30486, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 4B": LocData(base_id + 30487, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 48": LocData(base_id + 30488, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Node 45": LocData(base_id + 30489, LocGroup.VOLLEYBALL_ALT_NORMAL),
}

volleyball_alternate_path_hard_locations: Dict[str, LocData] = {
    "Volleyball Mushroom Cup Alt Path Hard Node 21": LocData(base_id + 30376, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Node 2B": LocData(base_id + 30377, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Node 31": LocData(base_id + 30378, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Node 28": LocData(base_id + 30379, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Node 38": LocData(base_id + 30380, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Node 3B": LocData(base_id + 30381, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Node 24": LocData(base_id + 30382, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Node 30": LocData(base_id + 30383, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Node 36": LocData(base_id + 30384, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Node 35": LocData(base_id + 30385, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Node 34": LocData(base_id + 30386, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Node 37": LocData(base_id + 30387, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Node 29": LocData(base_id + 30388, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Node 25": LocData(base_id + 30389, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Node 39": LocData(base_id + 30390, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Node 32": LocData(base_id + 30391, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Node 26": LocData(base_id + 30427, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Node 52": LocData(base_id + 30428, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Node 50": LocData(base_id + 30429, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Node 2D": LocData(base_id + 30430, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Node 36": LocData(base_id + 30431, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Node 39": LocData(base_id + 30432, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Node 4E": LocData(base_id + 30433, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Node 3D": LocData(base_id + 30434, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Node 4B": LocData(base_id + 30435, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Node 2A": LocData(base_id + 30436, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Node 32": LocData(base_id + 30437, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Node 55": LocData(base_id + 30438, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Node 57": LocData(base_id + 30439, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Node 44": LocData(base_id + 30440, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Node 43": LocData(base_id + 30441, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Node 46": LocData(base_id + 30442, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Node 47": LocData(base_id + 30443, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Node 49": LocData(base_id + 30444, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Node 3E": LocData(base_id + 30445, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 2E": LocData(base_id + 30490, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 32": LocData(base_id + 30491, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 3E": LocData(base_id + 30492, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 3F": LocData(base_id + 30493, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 27": LocData(base_id + 30494, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 21": LocData(base_id + 30495, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 2A": LocData(base_id + 30496, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 23": LocData(base_id + 30497, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 30": LocData(base_id + 30498, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 38": LocData(base_id + 30499, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 3D": LocData(base_id + 30500, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 41": LocData(base_id + 30501, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 40": LocData(base_id + 30502, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 37": LocData(base_id + 30503, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 36": LocData(base_id + 30504, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 33": LocData(base_id + 30505, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 4A": LocData(base_id + 30506, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 4C": LocData(base_id + 30507, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 49": LocData(base_id + 30508, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 4D": LocData(base_id + 30509, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 43": LocData(base_id + 30510, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 47": LocData(base_id + 30511, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 4B": LocData(base_id + 30512, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 48": LocData(base_id + 30513, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Node 45": LocData(base_id + 30514, LocGroup.VOLLEYBALL_ALT_HARD),
}

volleyball_alternate_path_global_locations: Dict[str, LocData] = {
    "Volleyball Mushroom Cup Alt Path Node 21": LocData(base_id + 30392, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Node 2B": LocData(base_id + 30393, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Node 31": LocData(base_id + 30394, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Node 28": LocData(base_id + 30395, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Node 38": LocData(base_id + 30396, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Node 3B": LocData(base_id + 30397, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Node 24": LocData(base_id + 30398, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Node 30": LocData(base_id + 30399, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Node 36": LocData(base_id + 30400, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Node 35": LocData(base_id + 30401, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Node 34": LocData(base_id + 30402, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Node 37": LocData(base_id + 30403, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Node 29": LocData(base_id + 30404, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Node 25": LocData(base_id + 30405, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Node 39": LocData(base_id + 30406, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Node 32": LocData(base_id + 30407, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Node 26": LocData(base_id + 30446, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Node 52": LocData(base_id + 30447, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Node 50": LocData(base_id + 30448, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Node 2D": LocData(base_id + 30449, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Node 36": LocData(base_id + 30450, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Node 39": LocData(base_id + 30451, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Node 4E": LocData(base_id + 30452, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Node 3D": LocData(base_id + 30453, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Node 4B": LocData(base_id + 30454, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Node 2A": LocData(base_id + 30455, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Node 32": LocData(base_id + 30456, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Node 55": LocData(base_id + 30457, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Node 57": LocData(base_id + 30458, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Node 44": LocData(base_id + 30459, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Node 43": LocData(base_id + 30460, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Node 46": LocData(base_id + 30461, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Node 47": LocData(base_id + 30462, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Node 49": LocData(base_id + 30463, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Node 3E": LocData(base_id + 30464, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 2E": LocData(base_id + 30515, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 32": LocData(base_id + 30516, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 3E": LocData(base_id + 30517, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 3F": LocData(base_id + 30518, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 27": LocData(base_id + 30519, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 21": LocData(base_id + 30520, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 2A": LocData(base_id + 30521, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 23": LocData(base_id + 30522, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 30": LocData(base_id + 30523, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 38": LocData(base_id + 30524, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 3D": LocData(base_id + 30525, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 41": LocData(base_id + 30526, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 40": LocData(base_id + 30527, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 37": LocData(base_id + 30528, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 36": LocData(base_id + 30529, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 33": LocData(base_id + 30530, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 4A": LocData(base_id + 30531, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 4C": LocData(base_id + 30532, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 49": LocData(base_id + 30533, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 4D": LocData(base_id + 30534, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 43": LocData(base_id + 30535, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 47": LocData(base_id + 30536, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 4B": LocData(base_id + 30537, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 48": LocData(base_id + 30538, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Node 45": LocData(base_id + 30539, LocGroup.VOLLEYBALL_ALT),
}

hockey_alternate_path_normal_locations: Dict[str, LocData] = {
    "Hockey Mushroom Cup Alt Path Normal Node 21": LocData(base_id + 30540, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Node 2B": LocData(base_id + 30541, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Node 31": LocData(base_id + 30542, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Node 28": LocData(base_id + 30543, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Node 38": LocData(base_id + 30544, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Node 3B": LocData(base_id + 30545, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Node 24": LocData(base_id + 30546, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Node 30": LocData(base_id + 30547, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Node 36": LocData(base_id + 30548, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Node 35": LocData(base_id + 30549, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Node 34": LocData(base_id + 30550, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Node 37": LocData(base_id + 30551, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Node 29": LocData(base_id + 30552, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Node 25": LocData(base_id + 30553, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Node 39": LocData(base_id + 30554, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Node 32": LocData(base_id + 30555, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Node 26": LocData(base_id + 30588, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Node 52": LocData(base_id + 30589, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Node 50": LocData(base_id + 30590, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Node 2D": LocData(base_id + 30591, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Node 36": LocData(base_id + 30592, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Node 39": LocData(base_id + 30593, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Node 4E": LocData(base_id + 30594, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Node 3D": LocData(base_id + 30595, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Node 4B": LocData(base_id + 30596, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Node 2A": LocData(base_id + 30597, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Node 32": LocData(base_id + 30598, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Node 55": LocData(base_id + 30599, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Node 57": LocData(base_id + 30600, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Node 44": LocData(base_id + 30601, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Node 43": LocData(base_id + 30602, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Node 46": LocData(base_id + 30603, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Node 47": LocData(base_id + 30604, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Node 49": LocData(base_id + 30605, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Node 3E": LocData(base_id + 30606, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 2E": LocData(base_id + 30645, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 32": LocData(base_id + 30646, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 3E": LocData(base_id + 30647, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 3F": LocData(base_id + 30648, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 27": LocData(base_id + 30649, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 21": LocData(base_id + 30650, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 2A": LocData(base_id + 30651, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 23": LocData(base_id + 30652, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 30": LocData(base_id + 30653, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 38": LocData(base_id + 30654, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 3D": LocData(base_id + 30655, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 41": LocData(base_id + 30656, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 40": LocData(base_id + 30657, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 37": LocData(base_id + 30658, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 36": LocData(base_id + 30659, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 33": LocData(base_id + 30660, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 4A": LocData(base_id + 30661, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 4C": LocData(base_id + 30662, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 49": LocData(base_id + 30663, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 4D": LocData(base_id + 30664, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 43": LocData(base_id + 30665, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 47": LocData(base_id + 30666, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 4B": LocData(base_id + 30667, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 48": LocData(base_id + 30668, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Node 45": LocData(base_id + 30669, LocGroup.HOCKEY_ALT_NORMAL),
}

hockey_alternate_path_hard_locations: Dict[str, LocData] = {
    "Hockey Mushroom Cup Alt Path Hard Node 21": LocData(base_id + 30556, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Node 2B": LocData(base_id + 30557, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Node 31": LocData(base_id + 30558, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Node 28": LocData(base_id + 30559, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Node 38": LocData(base_id + 30560, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Node 3B": LocData(base_id + 30561, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Node 24": LocData(base_id + 30562, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Node 30": LocData(base_id + 30563, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Node 36": LocData(base_id + 30564, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Node 35": LocData(base_id + 30565, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Node 34": LocData(base_id + 30566, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Node 37": LocData(base_id + 30567, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Node 29": LocData(base_id + 30568, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Node 25": LocData(base_id + 30569, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Node 39": LocData(base_id + 30570, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Node 32": LocData(base_id + 30571, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Node 26": LocData(base_id + 30607, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Node 52": LocData(base_id + 30608, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Node 50": LocData(base_id + 30609, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Node 2D": LocData(base_id + 30610, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Node 36": LocData(base_id + 30611, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Node 39": LocData(base_id + 30612, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Node 4E": LocData(base_id + 30613, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Node 3D": LocData(base_id + 30614, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Node 4B": LocData(base_id + 30615, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Node 2A": LocData(base_id + 30616, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Node 32": LocData(base_id + 30617, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Node 55": LocData(base_id + 30618, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Node 57": LocData(base_id + 30619, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Node 44": LocData(base_id + 30620, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Node 43": LocData(base_id + 30621, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Node 46": LocData(base_id + 30622, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Node 47": LocData(base_id + 30623, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Node 49": LocData(base_id + 30624, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Node 3E": LocData(base_id + 30625, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 2E": LocData(base_id + 30670, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 32": LocData(base_id + 30671, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 3E": LocData(base_id + 30672, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 3F": LocData(base_id + 30673, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 27": LocData(base_id + 30674, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 21": LocData(base_id + 30675, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 2A": LocData(base_id + 30676, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 23": LocData(base_id + 30677, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 30": LocData(base_id + 30678, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 38": LocData(base_id + 30679, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 3D": LocData(base_id + 30680, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 41": LocData(base_id + 30681, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 40": LocData(base_id + 30682, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 37": LocData(base_id + 30683, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 36": LocData(base_id + 30684, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 33": LocData(base_id + 30685, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 4A": LocData(base_id + 30686, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 4C": LocData(base_id + 30687, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 49": LocData(base_id + 30688, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 4D": LocData(base_id + 30689, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 43": LocData(base_id + 30690, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 47": LocData(base_id + 30691, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 4B": LocData(base_id + 30692, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 48": LocData(base_id + 30693, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Node 45": LocData(base_id + 30694, LocGroup.HOCKEY_ALT_HARD),
}

hockey_alternate_path_global_locations: Dict[str, LocData] = {
    "Hockey Mushroom Cup Alt Path Node 21": LocData(base_id + 30572, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Node 2B": LocData(base_id + 30573, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Node 31": LocData(base_id + 30574, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Node 28": LocData(base_id + 30575, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Node 38": LocData(base_id + 30576, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Node 3B": LocData(base_id + 30577, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Node 24": LocData(base_id + 30578, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Node 30": LocData(base_id + 30579, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Node 36": LocData(base_id + 30580, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Node 35": LocData(base_id + 30581, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Node 34": LocData(base_id + 30582, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Node 37": LocData(base_id + 30583, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Node 29": LocData(base_id + 30584, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Node 25": LocData(base_id + 30585, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Node 39": LocData(base_id + 30586, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Node 32": LocData(base_id + 30587, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Node 26": LocData(base_id + 30626, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Node 52": LocData(base_id + 30627, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Node 50": LocData(base_id + 30628, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Node 2D": LocData(base_id + 30629, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Node 36": LocData(base_id + 30630, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Node 39": LocData(base_id + 30631, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Node 4E": LocData(base_id + 30632, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Node 3D": LocData(base_id + 30633, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Node 4B": LocData(base_id + 30634, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Node 2A": LocData(base_id + 30635, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Node 32": LocData(base_id + 30636, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Node 55": LocData(base_id + 30637, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Node 57": LocData(base_id + 30638, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Node 44": LocData(base_id + 30639, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Node 43": LocData(base_id + 30640, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Node 46": LocData(base_id + 30641, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Node 47": LocData(base_id + 30642, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Node 49": LocData(base_id + 30643, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Node 3E": LocData(base_id + 30644, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 2E": LocData(base_id + 30695, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 32": LocData(base_id + 30696, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 3E": LocData(base_id + 30697, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 3F": LocData(base_id + 30698, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 27": LocData(base_id + 30699, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 21": LocData(base_id + 30700, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 2A": LocData(base_id + 30701, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 23": LocData(base_id + 30702, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 30": LocData(base_id + 30703, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 38": LocData(base_id + 30704, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 3D": LocData(base_id + 30705, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 41": LocData(base_id + 30706, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 40": LocData(base_id + 30707, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 37": LocData(base_id + 30708, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 36": LocData(base_id + 30709, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 33": LocData(base_id + 30710, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 4A": LocData(base_id + 30711, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 4C": LocData(base_id + 30712, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 49": LocData(base_id + 30713, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 4D": LocData(base_id + 30714, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 43": LocData(base_id + 30715, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 47": LocData(base_id + 30716, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 4B": LocData(base_id + 30717, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 48": LocData(base_id + 30718, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Node 45": LocData(base_id + 30719, LocGroup.HOCKEY_ALT),
}

sports_mix_alternate_path_locations: Dict[str, LocData] = {
    "Sports Mix Mushroom Cup Alt Path Node 21": LocData(base_id + 30720, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Node 2B": LocData(base_id + 30721, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Node 31": LocData(base_id + 30722, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Node 28": LocData(base_id + 30723, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Node 38": LocData(base_id + 30724, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Node 3B": LocData(base_id + 30725, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Node 24": LocData(base_id + 30726, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Node 30": LocData(base_id + 30727, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Node 36": LocData(base_id + 30728, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Node 35": LocData(base_id + 30729, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Node 34": LocData(base_id + 30730, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Node 37": LocData(base_id + 30731, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Node 29": LocData(base_id + 30732, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Node 25": LocData(base_id + 30733, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Node 39": LocData(base_id + 30734, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Node 32": LocData(base_id + 30735, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Node 26": LocData(base_id + 30736, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Node 52": LocData(base_id + 30737, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Node 50": LocData(base_id + 30738, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Node 2D": LocData(base_id + 30739, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Node 36": LocData(base_id + 30740, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Node 39": LocData(base_id + 30741, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Node 4E": LocData(base_id + 30742, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Node 3D": LocData(base_id + 30743, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Node 4B": LocData(base_id + 30744, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Node 2A": LocData(base_id + 30745, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Node 32": LocData(base_id + 30746, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Node 55": LocData(base_id + 30747, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Node 57": LocData(base_id + 30748, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Node 44": LocData(base_id + 30749, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Node 43": LocData(base_id + 30750, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Node 46": LocData(base_id + 30751, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Node 47": LocData(base_id + 30752, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Node 49": LocData(base_id + 30753, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Node 3E": LocData(base_id + 30754, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 2E": LocData(base_id + 30755, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 32": LocData(base_id + 30756, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 3E": LocData(base_id + 30757, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 3F": LocData(base_id + 30758, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 27": LocData(base_id + 30759, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 21": LocData(base_id + 30760, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 2A": LocData(base_id + 30761, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 23": LocData(base_id + 30762, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 30": LocData(base_id + 30763, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 38": LocData(base_id + 30764, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 3D": LocData(base_id + 30765, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 41": LocData(base_id + 30766, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 40": LocData(base_id + 30767, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 37": LocData(base_id + 30768, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 36": LocData(base_id + 30769, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 33": LocData(base_id + 30770, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 4A": LocData(base_id + 30771, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 4C": LocData(base_id + 30772, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 49": LocData(base_id + 30773, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 4D": LocData(base_id + 30774, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 43": LocData(base_id + 30775, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 47": LocData(base_id + 30776, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 4B": LocData(base_id + 30777, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 48": LocData(base_id + 30778, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Node 45": LocData(base_id + 30779, LocGroup.SPORTS_MIX_ALT),
}

global_alternate_path_normal_locations: Dict[str, LocData] = {
    "Mushroom Cup Alt Path Normal Node 21": LocData(base_id + 30780, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Node 2B": LocData(base_id + 30781, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Node 31": LocData(base_id + 30782, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Node 28": LocData(base_id + 30783, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Node 38": LocData(base_id + 30784, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Node 3B": LocData(base_id + 30785, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Node 24": LocData(base_id + 30786, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Node 30": LocData(base_id + 30787, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Node 36": LocData(base_id + 30788, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Node 35": LocData(base_id + 30789, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Node 34": LocData(base_id + 30790, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Node 37": LocData(base_id + 30791, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Node 29": LocData(base_id + 30792, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Node 25": LocData(base_id + 30793, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Node 39": LocData(base_id + 30794, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Node 32": LocData(base_id + 30795, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Node 26": LocData(base_id + 30828, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Node 52": LocData(base_id + 30829, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Node 50": LocData(base_id + 30830, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Node 2D": LocData(base_id + 30831, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Node 36": LocData(base_id + 30832, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Node 39": LocData(base_id + 30833, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Node 4E": LocData(base_id + 30834, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Node 3D": LocData(base_id + 30835, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Node 4B": LocData(base_id + 30836, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Node 2A": LocData(base_id + 30837, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Node 32": LocData(base_id + 30838, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Node 55": LocData(base_id + 30839, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Node 57": LocData(base_id + 30840, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Node 44": LocData(base_id + 30841, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Node 43": LocData(base_id + 30842, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Node 46": LocData(base_id + 30843, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Node 47": LocData(base_id + 30844, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Node 49": LocData(base_id + 30845, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Node 3E": LocData(base_id + 30846, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 2E": LocData(base_id + 30885, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 32": LocData(base_id + 30886, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 3E": LocData(base_id + 30887, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 3F": LocData(base_id + 30888, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 27": LocData(base_id + 30889, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 21": LocData(base_id + 30890, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 2A": LocData(base_id + 30891, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 23": LocData(base_id + 30892, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 30": LocData(base_id + 30893, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 38": LocData(base_id + 30894, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 3D": LocData(base_id + 30895, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 41": LocData(base_id + 30896, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 40": LocData(base_id + 30897, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 37": LocData(base_id + 30898, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 36": LocData(base_id + 30899, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 33": LocData(base_id + 30900, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 4A": LocData(base_id + 30901, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 4C": LocData(base_id + 30902, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 49": LocData(base_id + 30903, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 4D": LocData(base_id + 30904, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 43": LocData(base_id + 30905, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 47": LocData(base_id + 30906, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 4B": LocData(base_id + 30907, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 48": LocData(base_id + 30908, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Node 45": LocData(base_id + 30909, LocGroup.ALT_NORMAL),
}

global_alternate_path_hard_locations: Dict[str, LocData] = {
    "Mushroom Cup Alt Path Hard Node 21": LocData(base_id + 30796, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Node 2B": LocData(base_id + 30797, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Node 31": LocData(base_id + 30798, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Node 28": LocData(base_id + 30799, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Node 38": LocData(base_id + 30800, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Node 3B": LocData(base_id + 30801, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Node 24": LocData(base_id + 30802, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Node 30": LocData(base_id + 30803, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Node 36": LocData(base_id + 30804, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Node 35": LocData(base_id + 30805, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Node 34": LocData(base_id + 30806, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Node 37": LocData(base_id + 30807, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Node 29": LocData(base_id + 30808, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Node 25": LocData(base_id + 30809, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Node 39": LocData(base_id + 30810, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Node 32": LocData(base_id + 30811, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Node 26": LocData(base_id + 30847, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Node 52": LocData(base_id + 30848, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Node 50": LocData(base_id + 30849, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Node 2D": LocData(base_id + 30850, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Node 36": LocData(base_id + 30851, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Node 39": LocData(base_id + 30852, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Node 4E": LocData(base_id + 30853, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Node 3D": LocData(base_id + 30854, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Node 4B": LocData(base_id + 30855, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Node 2A": LocData(base_id + 30856, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Node 32": LocData(base_id + 30857, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Node 55": LocData(base_id + 30858, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Node 57": LocData(base_id + 30859, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Node 44": LocData(base_id + 30860, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Node 43": LocData(base_id + 30861, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Node 46": LocData(base_id + 30862, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Node 47": LocData(base_id + 30863, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Node 49": LocData(base_id + 30864, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Node 3E": LocData(base_id + 30865, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 2E": LocData(base_id + 30910, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 32": LocData(base_id + 30911, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 3E": LocData(base_id + 30912, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 3F": LocData(base_id + 30913, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 27": LocData(base_id + 30914, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 21": LocData(base_id + 30915, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 2A": LocData(base_id + 30916, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 23": LocData(base_id + 30917, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 30": LocData(base_id + 30918, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 38": LocData(base_id + 30919, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 3D": LocData(base_id + 30920, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 41": LocData(base_id + 30921, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 40": LocData(base_id + 30922, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 37": LocData(base_id + 30923, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 36": LocData(base_id + 30924, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 33": LocData(base_id + 30925, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 4A": LocData(base_id + 30926, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 4C": LocData(base_id + 30927, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 49": LocData(base_id + 30928, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 4D": LocData(base_id + 30929, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 43": LocData(base_id + 30930, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 47": LocData(base_id + 30931, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 4B": LocData(base_id + 30932, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 48": LocData(base_id + 30933, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Node 45": LocData(base_id + 30934, LocGroup.ALT_HARD),
}

global_alternate_path_global_locations: Dict[str, LocData] = {
    "Mushroom Cup Alt Path Node 21": LocData(base_id + 30812, LocGroup.ALT),
    "Mushroom Cup Alt Path Node 2B": LocData(base_id + 30813, LocGroup.ALT),
    "Mushroom Cup Alt Path Node 31": LocData(base_id + 30814, LocGroup.ALT),
    "Mushroom Cup Alt Path Node 28": LocData(base_id + 30815, LocGroup.ALT),
    "Mushroom Cup Alt Path Node 38": LocData(base_id + 30816, LocGroup.ALT),
    "Mushroom Cup Alt Path Node 3B": LocData(base_id + 30817, LocGroup.ALT),
    "Mushroom Cup Alt Path Node 24": LocData(base_id + 30818, LocGroup.ALT),
    "Mushroom Cup Alt Path Node 30": LocData(base_id + 30819, LocGroup.ALT),
    "Mushroom Cup Alt Path Node 36": LocData(base_id + 30820, LocGroup.ALT),
    "Mushroom Cup Alt Path Node 35": LocData(base_id + 30821, LocGroup.ALT),
    "Mushroom Cup Alt Path Node 34": LocData(base_id + 30822, LocGroup.ALT),
    "Mushroom Cup Alt Path Node 37": LocData(base_id + 30823, LocGroup.ALT),
    "Mushroom Cup Alt Path Node 29": LocData(base_id + 30824, LocGroup.ALT),
    "Mushroom Cup Alt Path Node 25": LocData(base_id + 30825, LocGroup.ALT),
    "Mushroom Cup Alt Path Node 39": LocData(base_id + 30826, LocGroup.ALT),
    "Mushroom Cup Alt Path Node 32": LocData(base_id + 30827, LocGroup.ALT),
    "Flower Cup Alt Path Node 26": LocData(base_id + 30866, LocGroup.ALT),
    "Flower Cup Alt Path Node 52": LocData(base_id + 30867, LocGroup.ALT),
    "Flower Cup Alt Path Node 50": LocData(base_id + 30868, LocGroup.ALT),
    "Flower Cup Alt Path Node 2D": LocData(base_id + 30869, LocGroup.ALT),
    "Flower Cup Alt Path Node 36": LocData(base_id + 30870, LocGroup.ALT),
    "Flower Cup Alt Path Node 39": LocData(base_id + 30871, LocGroup.ALT),
    "Flower Cup Alt Path Node 4E": LocData(base_id + 30872, LocGroup.ALT),
    "Flower Cup Alt Path Node 3D": LocData(base_id + 30873, LocGroup.ALT),
    "Flower Cup Alt Path Node 4B": LocData(base_id + 30874, LocGroup.ALT),
    "Flower Cup Alt Path Node 2A": LocData(base_id + 30875, LocGroup.ALT),
    "Flower Cup Alt Path Node 32": LocData(base_id + 30876, LocGroup.ALT),
    "Flower Cup Alt Path Node 55": LocData(base_id + 30877, LocGroup.ALT),
    "Flower Cup Alt Path Node 57": LocData(base_id + 30878, LocGroup.ALT),
    "Flower Cup Alt Path Node 44": LocData(base_id + 30879, LocGroup.ALT),
    "Flower Cup Alt Path Node 43": LocData(base_id + 30880, LocGroup.ALT),
    "Flower Cup Alt Path Node 46": LocData(base_id + 30881, LocGroup.ALT),
    "Flower Cup Alt Path Node 47": LocData(base_id + 30882, LocGroup.ALT),
    "Flower Cup Alt Path Node 49": LocData(base_id + 30883, LocGroup.ALT),
    "Flower Cup Alt Path Node 3E": LocData(base_id + 30884, LocGroup.ALT),
    "Star Cup Alt Path Node 2E": LocData(base_id + 30935, LocGroup.ALT),
    "Star Cup Alt Path Node 32": LocData(base_id + 30936, LocGroup.ALT),
    "Star Cup Alt Path Node 3E": LocData(base_id + 30937, LocGroup.ALT),
    "Star Cup Alt Path Node 3F": LocData(base_id + 30938, LocGroup.ALT),
    "Star Cup Alt Path Node 27": LocData(base_id + 30939, LocGroup.ALT),
    "Star Cup Alt Path Node 21": LocData(base_id + 30940, LocGroup.ALT),
    "Star Cup Alt Path Node 2A": LocData(base_id + 30941, LocGroup.ALT),
    "Star Cup Alt Path Node 23": LocData(base_id + 30942, LocGroup.ALT),
    "Star Cup Alt Path Node 30": LocData(base_id + 30943, LocGroup.ALT),
    "Star Cup Alt Path Node 38": LocData(base_id + 30944, LocGroup.ALT),
    "Star Cup Alt Path Node 3D": LocData(base_id + 30945, LocGroup.ALT),
    "Star Cup Alt Path Node 41": LocData(base_id + 30946, LocGroup.ALT),
    "Star Cup Alt Path Node 40": LocData(base_id + 30947, LocGroup.ALT),
    "Star Cup Alt Path Node 37": LocData(base_id + 30948, LocGroup.ALT),
    "Star Cup Alt Path Node 36": LocData(base_id + 30949, LocGroup.ALT),
    "Star Cup Alt Path Node 33": LocData(base_id + 30950, LocGroup.ALT),
    "Star Cup Alt Path Node 4A": LocData(base_id + 30951, LocGroup.ALT),
    "Star Cup Alt Path Node 4C": LocData(base_id + 30952, LocGroup.ALT),
    "Star Cup Alt Path Node 49": LocData(base_id + 30953, LocGroup.ALT),
    "Star Cup Alt Path Node 4D": LocData(base_id + 30954, LocGroup.ALT),
    "Star Cup Alt Path Node 43": LocData(base_id + 30955, LocGroup.ALT),
    "Star Cup Alt Path Node 47": LocData(base_id + 30956, LocGroup.ALT),
    "Star Cup Alt Path Node 4B": LocData(base_id + 30957, LocGroup.ALT),
    "Star Cup Alt Path Node 48": LocData(base_id + 30958, LocGroup.ALT),
    "Star Cup Alt Path Node 45": LocData(base_id + 30959, LocGroup.ALT),
}

basketball_alternate_path_normal_locations: Dict[str, LocData] = {
    "Basketball Mushroom Cup Alt Path Normal East of Red Toad House":                LocData(base_id + 30000, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal By Lake":                LocData(base_id + 30001, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Lake Platform":                LocData(base_id + 30002, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal South of Lake":                LocData(base_id + 30003, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Red Toad House":                LocData(base_id + 30004, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal By Castle Flowers":                LocData(base_id + 30005, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Lower Field":                LocData(base_id + 30006, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Below the Curve":                LocData(base_id + 30007, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Lower Curve":                LocData(base_id + 30008, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Middle Curve":                LocData(base_id + 30009, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Upper Curve":                LocData(base_id + 30010, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Top of the Mountain":                LocData(base_id + 30011, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Upper Field":                LocData(base_id + 30012, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Near Green Toad House":                LocData(base_id + 30013, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal By Logs":                LocData(base_id + 30014, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Mushroom Cup Alt Path Normal Hidden Finale":                LocData(base_id + 30015, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Left-Center Bridge":         LocData(base_id + 30048, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Flower Lake Island":         LocData(base_id + 30049, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Leftmost Bridge":         LocData(base_id + 30050, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Left Shoreline":         LocData(base_id + 30051, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Bottom-Left Island House":         LocData(base_id + 30052, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Bottom-Left Island Cannon":         LocData(base_id + 30053, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Bottom-Right Island":         LocData(base_id + 30054, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Middle-Left Islands":         LocData(base_id + 30055, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Top-Left Island":         LocData(base_id + 30056, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Waterwheel":         LocData(base_id + 30057, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Right Shoreline":         LocData(base_id + 30058, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Below Rightmost Bridge":         LocData(base_id + 30059, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Above Rightmost Bridge":         LocData(base_id + 30060, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Middle-Right Island Field":         LocData(base_id + 30061, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Middle-Right Island Cannon":         LocData(base_id + 30062, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Top-Right Island Tower":         LocData(base_id + 30063, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Top-Right Island Bottom Field":         LocData(base_id + 30064, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Top-Right Island Right Field":         LocData(base_id + 30065, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Flower Cup Alt Path Normal Hidden Finale":         LocData(base_id + 30066, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Tower C3":           LocData(base_id + 30105, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Tower B1":           LocData(base_id + 30106, LocGroup.BASKETBALL_ALT_NORMAL),
    # "Basketball Star Cup Alt Path Normal Node 3E":           LocData(base_id + 30107, LocGroup.BASKETBALL_ALT_NORMAL),
    # "Basketball Star Cup Alt Path Normal Node 3F":           LocData(base_id + 30108, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Tower D2":           LocData(base_id + 30109, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Tower E1":           LocData(base_id + 30110, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Tower D7":           LocData(base_id + 30111, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Tower E6":           LocData(base_id + 30112, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Tower C6":           LocData(base_id + 30113, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Tower B7":           LocData(base_id + 30114, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Tower A7":           LocData(base_id + 30115, LocGroup.BASKETBALL_ALT_NORMAL),
    # "Basketball Star Cup Alt Path Normal Node 41":           LocData(base_id + 30116, LocGroup.BASKETBALL_ALT_NORMAL),
    # "Basketball Star Cup Alt Path Normal Node 40":           LocData(base_id + 30117, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Tower B6":           LocData(base_id + 30118, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Tower B5":           LocData(base_id + 30119, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Tower B2":           LocData(base_id + 30120, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Star Road (Left) Intro":           LocData(base_id + 30121, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Star Road (Left) Bonus":           LocData(base_id + 30122, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Star Road (Right) Intro":           LocData(base_id + 30123, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Star Road (Right) Bonus":           LocData(base_id + 30124, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Star Road Bottom-Left of Star":           LocData(base_id + 30125, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Star Road Top-Left of Star":           LocData(base_id + 30126, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Star Road Top-Center of Star":           LocData(base_id + 30127, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Star Road Top-Right of Star":           LocData(base_id + 30128, LocGroup.BASKETBALL_ALT_NORMAL),
    "Basketball Star Cup Alt Path Normal Star Road Bottom-Right of Star":           LocData(base_id + 30129, LocGroup.BASKETBALL_ALT_NORMAL),
}

basketball_alternate_path_hard_locations: Dict[str, LocData] = {
    "Basketball Mushroom Cup Alt Path Hard East of Red Toad House":                  LocData(base_id + 30016, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard By Lake":                  LocData(base_id + 30017, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Lake Platform":                  LocData(base_id + 30018, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard South of Lake":                  LocData(base_id + 30019, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Red Toad House":                  LocData(base_id + 30020, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard By Castle Flowers":                  LocData(base_id + 30021, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Lower Field":                  LocData(base_id + 30022, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Below the Curve":                  LocData(base_id + 30023, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Lower Curve":                  LocData(base_id + 30024, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Middle Curve":                  LocData(base_id + 30025, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Upper Curve":                  LocData(base_id + 30026, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Top of the Mountain":                  LocData(base_id + 30027, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Upper Field":                  LocData(base_id + 30028, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Near Green Toad House":                  LocData(base_id + 30029, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard By Logs":                  LocData(base_id + 30030, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Mushroom Cup Alt Path Hard Hidden Finale":                  LocData(base_id + 30031, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Left-Center Bridge":           LocData(base_id + 30067, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Flower Lake Island":           LocData(base_id + 30068, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Leftmost Bridge":           LocData(base_id + 30069, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Left Shoreline":           LocData(base_id + 30070, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Bottom-Left Island House":           LocData(base_id + 30071, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Bottom-Left Island Cannon":           LocData(base_id + 30072, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Bottom-Right Island":           LocData(base_id + 30073, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Middle-Left Islands":           LocData(base_id + 30074, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Top-Left Island":           LocData(base_id + 30075, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Waterwheel":           LocData(base_id + 30076, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Right Shoreline":           LocData(base_id + 30077, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Below Rightmost Bridge":           LocData(base_id + 30078, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Above Rightmost Bridge":           LocData(base_id + 30079, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Middle-Right Island Field":           LocData(base_id + 30080, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Middle-Right Island Cannon":           LocData(base_id + 30081, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Top-Right Island Tower":           LocData(base_id + 30082, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Top-Right Island Bottom Field":           LocData(base_id + 30083, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Top-Right Island Right Field":           LocData(base_id + 30084, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Flower Cup Alt Path Hard Hidden Finale":           LocData(base_id + 30085, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Tower C3":             LocData(base_id + 30130, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Tower B1":             LocData(base_id + 30131, LocGroup.BASKETBALL_ALT_HARD),
    # "Basketball Star Cup Alt Path Hard Node 3E":             LocData(base_id + 30132, LocGroup.BASKETBALL_ALT_HARD),
    # "Basketball Star Cup Alt Path Hard Node 3F":             LocData(base_id + 30133, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Tower D2":             LocData(base_id + 30134, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Tower E1":             LocData(base_id + 30135, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Tower D7":             LocData(base_id + 30136, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Tower E6":             LocData(base_id + 30137, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Tower C6":             LocData(base_id + 30138, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Tower B7":             LocData(base_id + 30139, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Tower A7":             LocData(base_id + 30140, LocGroup.BASKETBALL_ALT_HARD),
    # "Basketball Star Cup Alt Path Hard Node 41":             LocData(base_id + 30141, LocGroup.BASKETBALL_ALT_HARD),
    # "Basketball Star Cup Alt Path Hard Node 40":             LocData(base_id + 30142, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Tower B6":             LocData(base_id + 30143, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Tower B5":             LocData(base_id + 30144, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Tower B2":             LocData(base_id + 30145, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Star Road (Left) Intro":             LocData(base_id + 30146, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Star Road (Left) Bonus":             LocData(base_id + 30147, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Star Road (Right) Intro":             LocData(base_id + 30148, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Star Road (Right) Bonus":             LocData(base_id + 30149, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Star Road Bottom-Left of Star":             LocData(base_id + 30150, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Star Road Top-Left of Star":             LocData(base_id + 30151, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Star Road Top-Center of Star":             LocData(base_id + 30152, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Star Road Top-Right of Star":             LocData(base_id + 30153, LocGroup.BASKETBALL_ALT_HARD),
    "Basketball Star Cup Alt Path Hard Star Road Bottom-Right of Star":             LocData(base_id + 30154, LocGroup.BASKETBALL_ALT_HARD),
}

basketball_alternate_path_global_locations: Dict[str, LocData] = {
    "Basketball Mushroom Cup Alt Path East of Red Toad House":                       LocData(base_id + 30032, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path By Lake":                       LocData(base_id + 30033, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Lake Platform":                       LocData(base_id + 30034, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path South of Lake":                       LocData(base_id + 30035, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Red Toad House":                       LocData(base_id + 30036, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path By Castle Flowers":                       LocData(base_id + 30037, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Lower Field":                       LocData(base_id + 30038, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Below the Curve":                       LocData(base_id + 30039, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Lower Curve":                       LocData(base_id + 30040, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Middle Curve":                       LocData(base_id + 30041, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Upper Curve":                       LocData(base_id + 30042, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Top of the Mountain":                       LocData(base_id + 30043, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Upper Field":                       LocData(base_id + 30044, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Near Green Toad House":                       LocData(base_id + 30045, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path By Logs":                       LocData(base_id + 30046, LocGroup.BASKETBALL_ALT),
    "Basketball Mushroom Cup Alt Path Hidden Finale":                       LocData(base_id + 30047, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Left-Center Bridge":                LocData(base_id + 30086, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Flower Lake Island":                LocData(base_id + 30087, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Leftmost Bridge":                LocData(base_id + 30088, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Left Shoreline":                LocData(base_id + 30089, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Bottom-Left Island House":                LocData(base_id + 30090, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Bottom-Left Island Cannon":                LocData(base_id + 30091, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Bottom-Right Island":                LocData(base_id + 30092, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Middle-Left Islands":                LocData(base_id + 30093, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Top-Left Island":                LocData(base_id + 30094, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Waterwheel":                LocData(base_id + 30095, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Right Shoreline":                LocData(base_id + 30096, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Below Rightmost Bridge":                LocData(base_id + 30097, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Above Rightmost Bridge":                LocData(base_id + 30098, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Middle-Right Island Field":                LocData(base_id + 30099, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Middle-Right Island Cannon":                LocData(base_id + 30100, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Top-Right Island Tower":                LocData(base_id + 30101, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Top-Right Island Bottom Field":                LocData(base_id + 30102, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Top-Right Island Right Field":                LocData(base_id + 30103, LocGroup.BASKETBALL_ALT),
    "Basketball Flower Cup Alt Path Hidden Finale":                LocData(base_id + 30104, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Tower C3":                  LocData(base_id + 30155, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Tower B1":                  LocData(base_id + 30156, LocGroup.BASKETBALL_ALT),
    # "Basketball Star Cup Alt Path Node 3E":                  LocData(base_id + 30157, LocGroup.BASKETBALL_ALT),
    # "Basketball Star Cup Alt Path Node 3F":                  LocData(base_id + 30158, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Tower D2":                  LocData(base_id + 30159, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Tower E1":                  LocData(base_id + 30160, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Tower D7":                  LocData(base_id + 30161, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Tower E6":                  LocData(base_id + 30162, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Tower C6":                  LocData(base_id + 30163, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Tower B7":                  LocData(base_id + 30164, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Tower A7":                  LocData(base_id + 30165, LocGroup.BASKETBALL_ALT),
    # "Basketball Star Cup Alt Path Node 41":                  LocData(base_id + 30166, LocGroup.BASKETBALL_ALT),
    # "Basketball Star Cup Alt Path Node 40":                  LocData(base_id + 30167, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Tower B6":                  LocData(base_id + 30168, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Tower B5":                  LocData(base_id + 30169, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Tower B2":                  LocData(base_id + 30170, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Star Road (Left) Intro":                  LocData(base_id + 30171, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Star Road (Left) Bonus":                  LocData(base_id + 30172, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Star Road (Right) Intro":                  LocData(base_id + 30173, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Star Road (Right) Bonus":                  LocData(base_id + 30174, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Star Road Bottom-Left of Star":                  LocData(base_id + 30175, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Star Road Top-Left of Star":                  LocData(base_id + 30176, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Star Road Top-Center of Star":                  LocData(base_id + 30177, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Star Road Top-Right of Star":                  LocData(base_id + 30178, LocGroup.BASKETBALL_ALT),
    "Basketball Star Cup Alt Path Star Road Bottom-Right of Star":                  LocData(base_id + 30179, LocGroup.BASKETBALL_ALT),
}


dodgeball_alternate_path_normal_locations: Dict[str, LocData] = {
    "Dodgeball Mushroom Cup Alt Path Normal East of Red Toad House":                LocData(base_id + 30180, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal By Lake":                LocData(base_id + 30181, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Lake Platform":                LocData(base_id + 30182, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal South of Lake":                LocData(base_id + 30183, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Red Toad House":                LocData(base_id + 30184, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal By Castle Flowers":                LocData(base_id + 30185, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Lower Field":                LocData(base_id + 30186, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Below the Curve":                LocData(base_id + 30187, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Lower Curve":                LocData(base_id + 30188, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Middle Curve":                LocData(base_id + 30189, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Upper Curve":                LocData(base_id + 30190, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Top of the Mountain":                LocData(base_id + 30191, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Upper Field":                LocData(base_id + 30192, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Near Green Toad House":                LocData(base_id + 30193, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal By Logs":                LocData(base_id + 30194, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Mushroom Cup Alt Path Normal Hidden Finale":                LocData(base_id + 30195, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Left-Center Bridge":         LocData(base_id + 30228, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Flower Lake Island":         LocData(base_id + 30229, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Leftmost Bridge":         LocData(base_id + 30230, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Left Shoreline":         LocData(base_id + 30231, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Bottom-Left Island House":         LocData(base_id + 30232, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Bottom-Left Island Cannon":         LocData(base_id + 30233, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Bottom-Right Island":         LocData(base_id + 30234, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Middle-Left Islands":         LocData(base_id + 30235, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Top-Left Island":         LocData(base_id + 30236, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Waterwheel":         LocData(base_id + 30237, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Right Shoreline":         LocData(base_id + 30238, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Below Rightmost Bridge":         LocData(base_id + 30239, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Above Rightmost Bridge":         LocData(base_id + 30240, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Middle-Right Island Field":         LocData(base_id + 30241, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Middle-Right Island Cannon":         LocData(base_id + 30242, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Top-Right Island Tower":         LocData(base_id + 30243, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Top-Right Island Bottom Field":         LocData(base_id + 30244, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Top-Right Island Right Field":         LocData(base_id + 30245, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Flower Cup Alt Path Normal Hidden Finale":         LocData(base_id + 30246, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Tower C3":           LocData(base_id + 30285, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Tower B1":           LocData(base_id + 30286, LocGroup.DODGEBALL_ALT_NORMAL),
    # "Dodgeball Star Cup Alt Path Normal Node 3E":           LocData(base_id + 30287, LocGroup.DODGEBALL_ALT_NORMAL),
    # "Dodgeball Star Cup Alt Path Normal Node 3F":           LocData(base_id + 30288, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Tower D2":           LocData(base_id + 30289, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Tower E1":           LocData(base_id + 30290, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Tower D7":           LocData(base_id + 30291, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Tower E6":           LocData(base_id + 30292, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Tower C6":           LocData(base_id + 30293, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Tower B7":           LocData(base_id + 30294, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Tower A7":           LocData(base_id + 30295, LocGroup.DODGEBALL_ALT_NORMAL),
    # "Dodgeball Star Cup Alt Path Normal Node 41":           LocData(base_id + 30296, LocGroup.DODGEBALL_ALT_NORMAL),
    # "Dodgeball Star Cup Alt Path Normal Node 40":           LocData(base_id + 30297, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Tower B6":           LocData(base_id + 30298, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Tower B5":           LocData(base_id + 30299, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Tower B2":           LocData(base_id + 30300, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Star Road (Left) Intro":           LocData(base_id + 30301, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Star Road (Left) Bonus":           LocData(base_id + 30302, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Star Road (Right) Intro":           LocData(base_id + 30303, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Star Road (Right) Bonus":           LocData(base_id + 30304, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Star Road Bottom-Left of Star":           LocData(base_id + 30305, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Star Road Top-Left of Star":           LocData(base_id + 30306, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Star Road Top-Center of Star":           LocData(base_id + 30307, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Star Road Top-Right of Star":           LocData(base_id + 30308, LocGroup.DODGEBALL_ALT_NORMAL),
    "Dodgeball Star Cup Alt Path Normal Star Road Bottom-Right of Star":           LocData(base_id + 30309, LocGroup.DODGEBALL_ALT_NORMAL),
}

dodgeball_alternate_path_hard_locations: Dict[str, LocData] = {
    "Dodgeball Mushroom Cup Alt Path Hard East of Red Toad House":                  LocData(base_id + 30196, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard By Lake":                  LocData(base_id + 30197, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Lake Platform":                  LocData(base_id + 30198, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard South of Lake":                  LocData(base_id + 30199, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Red Toad House":                  LocData(base_id + 30200, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard By Castle Flowers":                  LocData(base_id + 30201, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Lower Field":                  LocData(base_id + 30202, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Below the Curve":                  LocData(base_id + 30203, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Lower Curve":                  LocData(base_id + 30204, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Middle Curve":                  LocData(base_id + 30205, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Upper Curve":                  LocData(base_id + 30206, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Top of the Mountain":                  LocData(base_id + 30207, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Upper Field":                  LocData(base_id + 30208, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Near Green Toad House":                  LocData(base_id + 30209, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard By Logs":                  LocData(base_id + 30210, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Mushroom Cup Alt Path Hard Hidden Finale":                  LocData(base_id + 30211, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Left-Center Bridge":           LocData(base_id + 30247, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Flower Lake Island":           LocData(base_id + 30248, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Leftmost Bridge":           LocData(base_id + 30249, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Left Shoreline":           LocData(base_id + 30250, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Bottom-Left Island House":           LocData(base_id + 30251, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Bottom-Left Island Cannon":           LocData(base_id + 30252, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Bottom-Right Island":           LocData(base_id + 30253, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Middle-Left Islands":           LocData(base_id + 30254, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Top-Left Island":           LocData(base_id + 30255, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Waterwheel":           LocData(base_id + 30256, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Right Shoreline":           LocData(base_id + 30257, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Below Rightmost Bridge":           LocData(base_id + 30258, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Above Rightmost Bridge":           LocData(base_id + 30259, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Middle-Right Island Field":           LocData(base_id + 30260, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Middle-Right Island Cannon":           LocData(base_id + 30261, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Top-Right Island Tower":           LocData(base_id + 30262, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Top-Right Island Bottom Field":           LocData(base_id + 30263, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Top-Right Island Right Field":           LocData(base_id + 30264, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Flower Cup Alt Path Hard Hidden Finale":           LocData(base_id + 30265, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Tower C3":             LocData(base_id + 30310, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Tower B1":             LocData(base_id + 30311, LocGroup.DODGEBALL_ALT_HARD),
    # "Dodgeball Star Cup Alt Path Hard Node 3E":             LocData(base_id + 30312, LocGroup.DODGEBALL_ALT_HARD),
    # "Dodgeball Star Cup Alt Path Hard Node 3F":             LocData(base_id + 30313, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Tower D2":             LocData(base_id + 30314, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Tower E1":             LocData(base_id + 30315, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Tower D7":             LocData(base_id + 30316, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Tower E6":             LocData(base_id + 30317, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Tower C6":             LocData(base_id + 30318, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Tower B7":             LocData(base_id + 30319, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Tower A7":             LocData(base_id + 30320, LocGroup.DODGEBALL_ALT_HARD),
    # "Dodgeball Star Cup Alt Path Hard Node 41":             LocData(base_id + 30321, LocGroup.DODGEBALL_ALT_HARD),
    # "Dodgeball Star Cup Alt Path Hard Node 40":             LocData(base_id + 30322, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Tower B6":             LocData(base_id + 30323, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Tower B5":             LocData(base_id + 30324, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Tower B2":             LocData(base_id + 30325, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Star Road (Left) Intro":             LocData(base_id + 30326, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Star Road (Left) Bonus":             LocData(base_id + 30327, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Star Road (Right) Intro":             LocData(base_id + 30328, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Star Road (Right) Bonus":             LocData(base_id + 30329, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Star Road Bottom-Left of Star":             LocData(base_id + 30330, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Star Road Top-Left of Star":             LocData(base_id + 30331, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Star Road Top-Center of Star":             LocData(base_id + 30332, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Star Road Top-Right of Star":             LocData(base_id + 30333, LocGroup.DODGEBALL_ALT_HARD),
    "Dodgeball Star Cup Alt Path Hard Star Road Bottom-Right of Star":             LocData(base_id + 30334, LocGroup.DODGEBALL_ALT_HARD),
}

dodgeball_alternate_path_global_locations: Dict[str, LocData] = {
    "Dodgeball Mushroom Cup Alt Path East of Red Toad House":                       LocData(base_id + 30212, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path By Lake":                       LocData(base_id + 30213, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Lake Platform":                       LocData(base_id + 30214, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path South of Lake":                       LocData(base_id + 30215, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Red Toad House":                       LocData(base_id + 30216, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path By Castle Flowers":                       LocData(base_id + 30217, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Lower Field":                       LocData(base_id + 30218, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Below the Curve":                       LocData(base_id + 30219, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Lower Curve":                       LocData(base_id + 30220, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Middle Curve":                       LocData(base_id + 30221, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Upper Curve":                       LocData(base_id + 30222, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Top of the Mountain":                       LocData(base_id + 30223, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Upper Field":                       LocData(base_id + 30224, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Near Green Toad House":                       LocData(base_id + 30225, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path By Logs":                       LocData(base_id + 30226, LocGroup.DODGEBALL_ALT),
    "Dodgeball Mushroom Cup Alt Path Hidden Finale":                       LocData(base_id + 30227, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Left-Center Bridge":                LocData(base_id + 30266, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Flower Lake Island":                LocData(base_id + 30267, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Leftmost Bridge":                LocData(base_id + 30268, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Left Shoreline":                LocData(base_id + 30269, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Bottom-Left Island House":                LocData(base_id + 30270, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Bottom-Left Island Cannon":                LocData(base_id + 30271, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Bottom-Right Island":                LocData(base_id + 30272, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Middle-Left Islands":                LocData(base_id + 30273, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Top-Left Island":                LocData(base_id + 30274, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Waterwheel":                LocData(base_id + 30275, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Right Shoreline":                LocData(base_id + 30276, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Below Rightmost Bridge":                LocData(base_id + 30277, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Above Rightmost Bridge":                LocData(base_id + 30278, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Middle-Right Island Field":                LocData(base_id + 30279, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Middle-Right Island Cannon":                LocData(base_id + 30280, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Top-Right Island Tower":                LocData(base_id + 30281, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Top-Right Island Bottom Field":                LocData(base_id + 30282, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Top-Right Island Right Field":                LocData(base_id + 30283, LocGroup.DODGEBALL_ALT),
    "Dodgeball Flower Cup Alt Path Hidden Finale":                LocData(base_id + 30284, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Tower C3":                  LocData(base_id + 30335, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Tower B1":                  LocData(base_id + 30336, LocGroup.DODGEBALL_ALT),
    # "Dodgeball Star Cup Alt Path Node 3E":                  LocData(base_id + 30337, LocGroup.DODGEBALL_ALT),
    # "Dodgeball Star Cup Alt Path Node 3F":                  LocData(base_id + 30338, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Tower D2":                  LocData(base_id + 30339, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Tower E1":                  LocData(base_id + 30340, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Tower D7":                  LocData(base_id + 30341, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Tower E6":                  LocData(base_id + 30342, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Tower C6":                  LocData(base_id + 30343, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Tower B7":                  LocData(base_id + 30344, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Tower A7":                  LocData(base_id + 30345, LocGroup.DODGEBALL_ALT),
    # "Dodgeball Star Cup Alt Path Node 41":                  LocData(base_id + 30346, LocGroup.DODGEBALL_ALT),
    # "Dodgeball Star Cup Alt Path Node 40":                  LocData(base_id + 30347, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Tower B6":                  LocData(base_id + 30348, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Tower B5":                  LocData(base_id + 30349, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Tower B2":                  LocData(base_id + 30350, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Star Road (Left) Intro":                  LocData(base_id + 30351, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Star Road (Left) Bonus":                  LocData(base_id + 30352, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Star Road (Right) Intro":                  LocData(base_id + 30353, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Star Road (Right) Bonus":                  LocData(base_id + 30354, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Star Road Bottom-Left of Star":                  LocData(base_id + 30355, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Star Road Top-Left of Star":                  LocData(base_id + 30356, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Star Road Top-Center of Star":                  LocData(base_id + 30357, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Star Road Top-Right of Star":                  LocData(base_id + 30358, LocGroup.DODGEBALL_ALT),
    "Dodgeball Star Cup Alt Path Star Road Bottom-Right of Star":                  LocData(base_id + 30359, LocGroup.DODGEBALL_ALT),
}


volleyball_alternate_path_normal_locations: Dict[str, LocData] = {
    "Volleyball Mushroom Cup Alt Path Normal East of Red Toad House":                LocData(base_id + 30360, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal By Lake":                LocData(base_id + 30361, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Lake Platform":                LocData(base_id + 30362, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal South of Lake":                LocData(base_id + 30363, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Red Toad House":                LocData(base_id + 30364, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal By Castle Flowers":                LocData(base_id + 30365, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Lower Field":                LocData(base_id + 30366, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Below the Curve":                LocData(base_id + 30367, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Lower Curve":                LocData(base_id + 30368, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Middle Curve":                LocData(base_id + 30369, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Upper Curve":                LocData(base_id + 30370, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Top of the Mountain":                LocData(base_id + 30371, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Upper Field":                LocData(base_id + 30372, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Near Green Toad House":                LocData(base_id + 30373, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal By Logs":                LocData(base_id + 30374, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Mushroom Cup Alt Path Normal Hidden Finale":                LocData(base_id + 30375, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Left-Center Bridge":         LocData(base_id + 30408, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Flower Lake Island":         LocData(base_id + 30409, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Leftmost Bridge":         LocData(base_id + 30410, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Left Shoreline":         LocData(base_id + 30411, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Bottom-Left Island House":         LocData(base_id + 30412, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Bottom-Left Island Cannon":         LocData(base_id + 30413, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Bottom-Right Island":         LocData(base_id + 30414, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Middle-Left Islands":         LocData(base_id + 30415, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Top-Left Island":         LocData(base_id + 30416, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Waterwheel":         LocData(base_id + 30417, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Right Shoreline":         LocData(base_id + 30418, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Below Rightmost Bridge":         LocData(base_id + 30419, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Above Rightmost Bridge":         LocData(base_id + 30420, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Middle-Right Island Field":         LocData(base_id + 30421, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Middle-Right Island Cannon":         LocData(base_id + 30422, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Top-Right Island Tower":         LocData(base_id + 30423, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Top-Right Island Bottom Field":         LocData(base_id + 30424, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Top-Right Island Right Field":         LocData(base_id + 30425, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Flower Cup Alt Path Normal Hidden Finale":         LocData(base_id + 30426, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Tower C3":           LocData(base_id + 30465, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Tower B1":           LocData(base_id + 30466, LocGroup.VOLLEYBALL_ALT_NORMAL),
    # "Volleyball Star Cup Alt Path Normal Node 3E":           LocData(base_id + 30467, LocGroup.VOLLEYBALL_ALT_NORMAL),
    # "Volleyball Star Cup Alt Path Normal Node 3F":           LocData(base_id + 30468, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Tower D2":           LocData(base_id + 30469, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Tower E1":           LocData(base_id + 30470, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Tower D7":           LocData(base_id + 30471, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Tower E6":           LocData(base_id + 30472, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Tower C6":           LocData(base_id + 30473, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Tower B7":           LocData(base_id + 30474, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Tower A7":           LocData(base_id + 30475, LocGroup.VOLLEYBALL_ALT_NORMAL),
    # "Volleyball Star Cup Alt Path Normal Node 41":           LocData(base_id + 30476, LocGroup.VOLLEYBALL_ALT_NORMAL),
    # "Volleyball Star Cup Alt Path Normal Node 40":           LocData(base_id + 30477, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Tower B6":           LocData(base_id + 30478, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Tower B5":           LocData(base_id + 30479, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Tower B2":           LocData(base_id + 30480, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Star Road (Left) Intro":           LocData(base_id + 30481, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Star Road (Left) Bonus":           LocData(base_id + 30482, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Star Road (Right) Intro":           LocData(base_id + 30483, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Star Road (Right) Bonus":           LocData(base_id + 30484, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Star Road Bottom-Left of Star":           LocData(base_id + 30485, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Star Road Top-Left of Star":           LocData(base_id + 30486, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Star Road Top-Center of Star":           LocData(base_id + 30487, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Star Road Top-Right of Star":           LocData(base_id + 30488, LocGroup.VOLLEYBALL_ALT_NORMAL),
    "Volleyball Star Cup Alt Path Normal Star Road Bottom-Right of Star":           LocData(base_id + 30489, LocGroup.VOLLEYBALL_ALT_NORMAL),
}

volleyball_alternate_path_hard_locations: Dict[str, LocData] = {
    "Volleyball Mushroom Cup Alt Path Hard East of Red Toad House":                  LocData(base_id + 30376, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard By Lake":                  LocData(base_id + 30377, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Lake Platform":                  LocData(base_id + 30378, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard South of Lake":                  LocData(base_id + 30379, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Red Toad House":                  LocData(base_id + 30380, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard By Castle Flowers":                  LocData(base_id + 30381, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Lower Field":                  LocData(base_id + 30382, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Below the Curve":                  LocData(base_id + 30383, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Lower Curve":                  LocData(base_id + 30384, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Middle Curve":                  LocData(base_id + 30385, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Upper Curve":                  LocData(base_id + 30386, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Top of the Mountain":                  LocData(base_id + 30387, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Upper Field":                  LocData(base_id + 30388, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Near Green Toad House":                  LocData(base_id + 30389, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard By Logs":                  LocData(base_id + 30390, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Mushroom Cup Alt Path Hard Hidden Finale":                  LocData(base_id + 30391, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Left-Center Bridge":           LocData(base_id + 30427, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Flower Lake Island":           LocData(base_id + 30428, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Leftmost Bridge":           LocData(base_id + 30429, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Left Shoreline":           LocData(base_id + 30430, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Bottom-Left Island House":           LocData(base_id + 30431, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Bottom-Left Island Cannon":           LocData(base_id + 30432, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Bottom-Right Island":           LocData(base_id + 30433, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Middle-Left Islands":           LocData(base_id + 30434, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Top-Left Island":           LocData(base_id + 30435, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Waterwheel":           LocData(base_id + 30436, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Right Shoreline":           LocData(base_id + 30437, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Below Rightmost Bridge":           LocData(base_id + 30438, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Above Rightmost Bridge":           LocData(base_id + 30439, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Middle-Right Island Field":           LocData(base_id + 30440, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Middle-Right Island Cannon":           LocData(base_id + 30441, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Top-Right Island Tower":           LocData(base_id + 30442, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Top-Right Island Bottom Field":           LocData(base_id + 30443, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Top-Right Island Right Field":           LocData(base_id + 30444, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Flower Cup Alt Path Hard Hidden Finale":           LocData(base_id + 30445, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Tower C3":             LocData(base_id + 30490, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Tower B1":             LocData(base_id + 30491, LocGroup.VOLLEYBALL_ALT_HARD),
    # "Volleyball Star Cup Alt Path Hard Node 3E":             LocData(base_id + 30492, LocGroup.VOLLEYBALL_ALT_HARD),
    # "Volleyball Star Cup Alt Path Hard Node 3F":             LocData(base_id + 30493, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Tower D2":             LocData(base_id + 30494, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Tower E1":             LocData(base_id + 30495, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Tower D7":             LocData(base_id + 30496, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Tower E6":             LocData(base_id + 30497, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Tower C6":             LocData(base_id + 30498, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Tower B7":             LocData(base_id + 30499, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Tower A7":             LocData(base_id + 30500, LocGroup.VOLLEYBALL_ALT_HARD),
    # "Volleyball Star Cup Alt Path Hard Node 41":             LocData(base_id + 30501, LocGroup.VOLLEYBALL_ALT_HARD),
    # "Volleyball Star Cup Alt Path Hard Node 40":             LocData(base_id + 30502, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Tower B6":             LocData(base_id + 30503, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Tower B5":             LocData(base_id + 30504, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Tower B2":             LocData(base_id + 30505, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Star Road (Left) Intro":             LocData(base_id + 30506, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Star Road (Left) Bonus":             LocData(base_id + 30507, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Star Road (Right) Intro":             LocData(base_id + 30508, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Star Road (Right) Bonus":             LocData(base_id + 30509, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Star Road Bottom-Left of Star":             LocData(base_id + 30510, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Star Road Top-Left of Star":             LocData(base_id + 30511, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Star Road Top-Center of Star":             LocData(base_id + 30512, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Star Road Top-Right of Star":             LocData(base_id + 30513, LocGroup.VOLLEYBALL_ALT_HARD),
    "Volleyball Star Cup Alt Path Hard Star Road Bottom-Right of Star":             LocData(base_id + 30514, LocGroup.VOLLEYBALL_ALT_HARD),
}

volleyball_alternate_path_global_locations: Dict[str, LocData] = {
    "Volleyball Mushroom Cup Alt Path East of Red Toad House":                       LocData(base_id + 30392, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path By Lake":                       LocData(base_id + 30393, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Lake Platform":                       LocData(base_id + 30394, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path South of Lake":                       LocData(base_id + 30395, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Red Toad House":                       LocData(base_id + 30396, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path By Castle Flowers":                       LocData(base_id + 30397, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Lower Field":                       LocData(base_id + 30398, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Below the Curve":                       LocData(base_id + 30399, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Lower Curve":                       LocData(base_id + 30400, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Middle Curve":                       LocData(base_id + 30401, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Upper Curve":                       LocData(base_id + 30402, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Top of the Mountain":                       LocData(base_id + 30403, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Upper Field":                       LocData(base_id + 30404, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Near Green Toad House":                       LocData(base_id + 30405, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path By Logs":                       LocData(base_id + 30406, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Mushroom Cup Alt Path Hidden Finale":                       LocData(base_id + 30407, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Left-Center Bridge":                LocData(base_id + 30446, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Flower Lake Island":                LocData(base_id + 30447, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Leftmost Bridge":                LocData(base_id + 30448, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Left Shoreline":                LocData(base_id + 30449, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Bottom-Left Island House":                LocData(base_id + 30450, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Bottom-Left Island Cannon":                LocData(base_id + 30451, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Bottom-Right Island":                LocData(base_id + 30452, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Middle-Left Islands":                LocData(base_id + 30453, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Top-Left Island":                LocData(base_id + 30454, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Waterwheel":                LocData(base_id + 30455, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Right Shoreline":                LocData(base_id + 30456, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Below Rightmost Bridge":                LocData(base_id + 30457, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Above Rightmost Bridge":                LocData(base_id + 30458, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Middle-Right Island Field":                LocData(base_id + 30459, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Middle-Right Island Cannon":                LocData(base_id + 30460, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Top-Right Island Tower":                LocData(base_id + 30461, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Top-Right Island Bottom Field":                LocData(base_id + 30462, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Top-Right Island Right Field":                LocData(base_id + 30463, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Flower Cup Alt Path Hidden Finale":                LocData(base_id + 30464, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Tower C3":                  LocData(base_id + 30515, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Tower B1":                  LocData(base_id + 30516, LocGroup.VOLLEYBALL_ALT),
    # "Volleyball Star Cup Alt Path Node 3E":                  LocData(base_id + 30517, LocGroup.VOLLEYBALL_ALT),
    # "Volleyball Star Cup Alt Path Node 3F":                  LocData(base_id + 30518, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Tower D2":                  LocData(base_id + 30519, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Tower E1":                  LocData(base_id + 30520, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Tower D7":                  LocData(base_id + 30521, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Tower E6":                  LocData(base_id + 30522, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Tower C6":                  LocData(base_id + 30523, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Tower B7":                  LocData(base_id + 30524, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Tower A7":                  LocData(base_id + 30525, LocGroup.VOLLEYBALL_ALT),
    # "Volleyball Star Cup Alt Path Node 41":                  LocData(base_id + 30526, LocGroup.VOLLEYBALL_ALT),
    # "Volleyball Star Cup Alt Path Node 40":                  LocData(base_id + 30527, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Tower B6":                  LocData(base_id + 30528, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Tower B5":                  LocData(base_id + 30529, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Tower B2":                  LocData(base_id + 30530, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Star Road (Left) Intro":                  LocData(base_id + 30531, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Star Road (Left) Bonus":                  LocData(base_id + 30532, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Star Road (Right) Intro":                  LocData(base_id + 30533, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Star Road (Right) Bonus":                  LocData(base_id + 30534, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Star Road Bottom-Left of Star":                  LocData(base_id + 30535, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Star Road Top-Left of Star":                  LocData(base_id + 30536, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Star Road Top-Center of Star":                  LocData(base_id + 30537, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Star Road Top-Right of Star":                  LocData(base_id + 30538, LocGroup.VOLLEYBALL_ALT),
    "Volleyball Star Cup Alt Path Star Road Bottom-Right of Star":                  LocData(base_id + 30539, LocGroup.VOLLEYBALL_ALT),
}


hockey_alternate_path_normal_locations: Dict[str, LocData] = {
    "Hockey Mushroom Cup Alt Path Normal East of Red Toad House":                LocData(base_id + 30540, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal By Lake":                LocData(base_id + 30541, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Lake Platform":                LocData(base_id + 30542, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal South of Lake":                LocData(base_id + 30543, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Red Toad House":                LocData(base_id + 30544, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal By Castle Flowers":                LocData(base_id + 30545, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Lower Field":                LocData(base_id + 30546, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Below the Curve":                LocData(base_id + 30547, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Lower Curve":                LocData(base_id + 30548, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Middle Curve":                LocData(base_id + 30549, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Upper Curve":                LocData(base_id + 30550, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Top of the Mountain":                LocData(base_id + 30551, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Upper Field":                LocData(base_id + 30552, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Near Green Toad House":                LocData(base_id + 30553, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal By Logs":                LocData(base_id + 30554, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Mushroom Cup Alt Path Normal Hidden Finale":                LocData(base_id + 30555, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Left-Center Bridge":         LocData(base_id + 30588, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Flower Lake Island":         LocData(base_id + 30589, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Leftmost Bridge":         LocData(base_id + 30590, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Left Shoreline":         LocData(base_id + 30591, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Bottom-Left Island House":         LocData(base_id + 30592, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Bottom-Left Island Cannon":         LocData(base_id + 30593, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Bottom-Right Island":         LocData(base_id + 30594, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Middle-Left Islands":         LocData(base_id + 30595, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Top-Left Island":         LocData(base_id + 30596, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Waterwheel":         LocData(base_id + 30597, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Right Shoreline":         LocData(base_id + 30598, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Below Rightmost Bridge":         LocData(base_id + 30599, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Above Rightmost Bridge":         LocData(base_id + 30600, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Middle-Right Island Field":         LocData(base_id + 30601, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Middle-Right Island Cannon":         LocData(base_id + 30602, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Top-Right Island Tower":         LocData(base_id + 30603, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Top-Right Island Bottom Field":         LocData(base_id + 30604, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Top-Right Island Right Field":         LocData(base_id + 30605, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Flower Cup Alt Path Normal Hidden Finale":         LocData(base_id + 30606, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Tower C3":           LocData(base_id + 30645, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Tower B1":           LocData(base_id + 30646, LocGroup.HOCKEY_ALT_NORMAL),
    # "Hockey Star Cup Alt Path Normal Node 3E":           LocData(base_id + 30647, LocGroup.HOCKEY_ALT_NORMAL),
    # "Hockey Star Cup Alt Path Normal Node 3F":           LocData(base_id + 30648, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Tower D2":           LocData(base_id + 30649, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Tower E1":           LocData(base_id + 30650, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Tower D7":           LocData(base_id + 30651, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Tower E6":           LocData(base_id + 30652, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Tower C6":           LocData(base_id + 30653, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Tower B7":           LocData(base_id + 30654, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Tower A7":           LocData(base_id + 30655, LocGroup.HOCKEY_ALT_NORMAL),
    # "Hockey Star Cup Alt Path Normal Node 41":           LocData(base_id + 30656, LocGroup.HOCKEY_ALT_NORMAL),
    # "Hockey Star Cup Alt Path Normal Node 40":           LocData(base_id + 30657, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Tower B6":           LocData(base_id + 30658, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Tower B5":           LocData(base_id + 30659, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Tower B2":           LocData(base_id + 30660, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Star Road (Left) Intro":           LocData(base_id + 30661, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Star Road (Left) Bonus":           LocData(base_id + 30662, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Star Road (Right) Intro":           LocData(base_id + 30663, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Star Road (Right) Bonus":           LocData(base_id + 30664, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Star Road Bottom-Left of Star":           LocData(base_id + 30665, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Star Road Top-Left of Star":           LocData(base_id + 30666, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Star Road Top-Center of Star":           LocData(base_id + 30667, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Star Road Top-Right of Star":           LocData(base_id + 30668, LocGroup.HOCKEY_ALT_NORMAL),
    "Hockey Star Cup Alt Path Normal Star Road Bottom-Right of Star":           LocData(base_id + 30669, LocGroup.HOCKEY_ALT_NORMAL),
}

hockey_alternate_path_hard_locations: Dict[str, LocData] = {
    "Hockey Mushroom Cup Alt Path Hard East of Red Toad House":                  LocData(base_id + 30556, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard By Lake":                  LocData(base_id + 30557, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Lake Platform":                  LocData(base_id + 30558, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard South of Lake":                  LocData(base_id + 30559, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Red Toad House":                  LocData(base_id + 30560, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard By Castle Flowers":                  LocData(base_id + 30561, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Lower Field":                  LocData(base_id + 30562, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Below the Curve":                  LocData(base_id + 30563, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Lower Curve":                  LocData(base_id + 30564, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Middle Curve":                  LocData(base_id + 30565, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Upper Curve":                  LocData(base_id + 30566, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Top of the Mountain":                  LocData(base_id + 30567, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Upper Field":                  LocData(base_id + 30568, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Near Green Toad House":                  LocData(base_id + 30569, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard By Logs":                  LocData(base_id + 30570, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Mushroom Cup Alt Path Hard Hidden Finale":                  LocData(base_id + 30571, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Left-Center Bridge":           LocData(base_id + 30607, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Flower Lake Island":           LocData(base_id + 30608, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Leftmost Bridge":           LocData(base_id + 30609, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Left Shoreline":           LocData(base_id + 30610, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Bottom-Left Island House":           LocData(base_id + 30611, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Bottom-Left Island Cannon":           LocData(base_id + 30612, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Bottom-Right Island":           LocData(base_id + 30613, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Middle-Left Islands":           LocData(base_id + 30614, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Top-Left Island":           LocData(base_id + 30615, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Waterwheel":           LocData(base_id + 30616, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Right Shoreline":           LocData(base_id + 30617, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Below Rightmost Bridge":           LocData(base_id + 30618, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Above Rightmost Bridge":           LocData(base_id + 30619, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Middle-Right Island Field":           LocData(base_id + 30620, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Middle-Right Island Cannon":           LocData(base_id + 30621, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Top-Right Island Tower":           LocData(base_id + 30622, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Top-Right Island Bottom Field":           LocData(base_id + 30623, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Top-Right Island Right Field":           LocData(base_id + 30624, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Flower Cup Alt Path Hard Hidden Finale":           LocData(base_id + 30625, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Tower C3":             LocData(base_id + 30670, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Tower B1":             LocData(base_id + 30671, LocGroup.HOCKEY_ALT_HARD),
    # "Hockey Star Cup Alt Path Hard Node 3E":             LocData(base_id + 30672, LocGroup.HOCKEY_ALT_HARD),
    # "Hockey Star Cup Alt Path Hard Node 3F":             LocData(base_id + 30673, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Tower D2":             LocData(base_id + 30674, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Tower E1":             LocData(base_id + 30675, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Tower D7":             LocData(base_id + 30676, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Tower E6":             LocData(base_id + 30677, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Tower C6":             LocData(base_id + 30678, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Tower B7":             LocData(base_id + 30679, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Tower A7":             LocData(base_id + 30680, LocGroup.HOCKEY_ALT_HARD),
    # "Hockey Star Cup Alt Path Hard Node 41":             LocData(base_id + 30681, LocGroup.HOCKEY_ALT_HARD),
    # "Hockey Star Cup Alt Path Hard Node 40":             LocData(base_id + 30682, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Tower B6":             LocData(base_id + 30683, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Tower B5":             LocData(base_id + 30684, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Tower B2":             LocData(base_id + 30685, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Star Road (Left) Intro":             LocData(base_id + 30686, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Star Road (Left) Bonus":             LocData(base_id + 30687, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Star Road (Right) Intro":             LocData(base_id + 30688, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Star Road (Right) Bonus":             LocData(base_id + 30689, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Star Road Bottom-Left of Star":             LocData(base_id + 30690, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Star Road Top-Left of Star":             LocData(base_id + 30691, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Star Road Top-Center of Star":             LocData(base_id + 30692, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Star Road Top-Right of Star":             LocData(base_id + 30693, LocGroup.HOCKEY_ALT_HARD),
    "Hockey Star Cup Alt Path Hard Star Road Bottom-Right of Star":             LocData(base_id + 30694, LocGroup.HOCKEY_ALT_HARD),
}

hockey_alternate_path_global_locations: Dict[str, LocData] = {
    "Hockey Mushroom Cup Alt Path East of Red Toad House":                       LocData(base_id + 30572, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path By Lake":                       LocData(base_id + 30573, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Lake Platform":                       LocData(base_id + 30574, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path South of Lake":                       LocData(base_id + 30575, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Red Toad House":                       LocData(base_id + 30576, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path By Castle Flowers":                       LocData(base_id + 30577, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Lower Field":                       LocData(base_id + 30578, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Below the Curve":                       LocData(base_id + 30579, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Lower Curve":                       LocData(base_id + 30580, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Middle Curve":                       LocData(base_id + 30581, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Upper Curve":                       LocData(base_id + 30582, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Top of the Mountain":                       LocData(base_id + 30583, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Upper Field":                       LocData(base_id + 30584, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Near Green Toad House":                       LocData(base_id + 30585, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path By Logs":                       LocData(base_id + 30586, LocGroup.HOCKEY_ALT),
    "Hockey Mushroom Cup Alt Path Hidden Finale":                       LocData(base_id + 30587, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Left-Center Bridge":                LocData(base_id + 30626, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Flower Lake Island":                LocData(base_id + 30627, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Leftmost Bridge":                LocData(base_id + 30628, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Left Shoreline":                LocData(base_id + 30629, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Bottom-Left Island House":                LocData(base_id + 30630, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Bottom-Left Island Cannon":                LocData(base_id + 30631, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Bottom-Right Island":                LocData(base_id + 30632, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Middle-Left Islands":                LocData(base_id + 30633, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Top-Left Island":                LocData(base_id + 30634, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Waterwheel":                LocData(base_id + 30635, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Right Shoreline":                LocData(base_id + 30636, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Below Rightmost Bridge":                LocData(base_id + 30637, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Above Rightmost Bridge":                LocData(base_id + 30638, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Middle-Right Island Field":                LocData(base_id + 30639, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Middle-Right Island Cannon":                LocData(base_id + 30640, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Top-Right Island Tower":                LocData(base_id + 30641, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Top-Right Island Bottom Field":                LocData(base_id + 30642, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Top-Right Island Right Field":                LocData(base_id + 30643, LocGroup.HOCKEY_ALT),
    "Hockey Flower Cup Alt Path Hidden Finale":                LocData(base_id + 30644, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Tower C3":                  LocData(base_id + 30695, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Tower B1":                  LocData(base_id + 30696, LocGroup.HOCKEY_ALT),
    # "Hockey Star Cup Alt Path Node 3E":                  LocData(base_id + 30697, LocGroup.HOCKEY_ALT),
    # "Hockey Star Cup Alt Path Node 3F":                  LocData(base_id + 30698, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Tower D2":                  LocData(base_id + 30699, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Tower E1":                  LocData(base_id + 30700, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Tower D7":                  LocData(base_id + 30701, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Tower E6":                  LocData(base_id + 30702, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Tower C6":                  LocData(base_id + 30703, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Tower B7":                  LocData(base_id + 30704, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Tower A7":                  LocData(base_id + 30705, LocGroup.HOCKEY_ALT),
    # "Hockey Star Cup Alt Path Node 41":                  LocData(base_id + 30706, LocGroup.HOCKEY_ALT),
    # "Hockey Star Cup Alt Path Node 40":                  LocData(base_id + 30707, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Tower B6":                  LocData(base_id + 30708, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Tower B5":                  LocData(base_id + 30709, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Tower B2":                  LocData(base_id + 30710, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Star Road (Left) Intro":                  LocData(base_id + 30711, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Star Road (Left) Bonus":                  LocData(base_id + 30712, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Star Road (Right) Intro":                  LocData(base_id + 30713, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Star Road (Right) Bonus":                  LocData(base_id + 30714, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Star Road Bottom-Left of Star":                  LocData(base_id + 30715, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Star Road Top-Left of Star":                  LocData(base_id + 30716, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Star Road Top-Center of Star":                  LocData(base_id + 30717, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Star Road Top-Right of Star":                  LocData(base_id + 30718, LocGroup.HOCKEY_ALT),
    "Hockey Star Cup Alt Path Star Road Bottom-Right of Star":                  LocData(base_id + 30719, LocGroup.HOCKEY_ALT),
}

sports_mix_alternate_path_locations: Dict[str, LocData] = {
    "Sports Mix Mushroom Cup Alt Path East of Red Toad House":                LocData(base_id + 30720, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path By Lake":                LocData(base_id + 30721, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Lake Platform":                LocData(base_id + 30722, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path South of Lake":                LocData(base_id + 30723, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Red Toad House":                LocData(base_id + 30724, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path By Castle Flowers":                LocData(base_id + 30725, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Lower Field":                LocData(base_id + 30726, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Below the Curve":                LocData(base_id + 30727, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Lower Curve":                LocData(base_id + 30728, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Middle Curve":                LocData(base_id + 30729, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Upper Curve":                LocData(base_id + 30730, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Top of the Mountain":                LocData(base_id + 30731, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Upper Field":                LocData(base_id + 30732, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Near Green Toad House":                LocData(base_id + 30733, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path By Logs":                LocData(base_id + 30734, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Mushroom Cup Alt Path Hidden Finale":                LocData(base_id + 30735, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Left-Center Bridge":         LocData(base_id + 30736, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Flower Lake Island":         LocData(base_id + 30737, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Leftmost Bridge":         LocData(base_id + 30738, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Left Shoreline":         LocData(base_id + 30739, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Bottom-Left Island House":         LocData(base_id + 30740, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Bottom-Left Island Cannon":         LocData(base_id + 30741, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Bottom-Right Island":         LocData(base_id + 30742, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Middle-Left Islands":         LocData(base_id + 30743, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Top-Left Island":         LocData(base_id + 30744, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Waterwheel":         LocData(base_id + 30745, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Right Shoreline":         LocData(base_id + 30746, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Below Rightmost Bridge":         LocData(base_id + 30747, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Above Rightmost Bridge":         LocData(base_id + 30748, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Middle-Right Island Field":         LocData(base_id + 30749, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Middle-Right Island Cannon":         LocData(base_id + 30750, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Top-Right Island Tower":         LocData(base_id + 30751, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Top-Right Island Bottom Field":         LocData(base_id + 30752, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Top-Right Island Right Field":         LocData(base_id + 30753, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Flower Cup Alt Path Hidden Finale":         LocData(base_id + 30754, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Tower C3":           LocData(base_id + 30755, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Tower B1":           LocData(base_id + 30756, LocGroup.SPORTS_MIX_ALT),
    # "Sports Mix Star Cup Alt Path Node 3E":           LocData(base_id + 30757, LocGroup.SPORTS_MIX_ALT),
    # "Sports Mix Star Cup Alt Path Node 3F":           LocData(base_id + 30758, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Tower D2":           LocData(base_id + 30759, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Tower E1":           LocData(base_id + 30760, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Tower D7":           LocData(base_id + 30761, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Tower E6":           LocData(base_id + 30762, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Tower C6":           LocData(base_id + 30763, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Tower B7":           LocData(base_id + 30764, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Tower A7":           LocData(base_id + 30765, LocGroup.SPORTS_MIX_ALT),
    # "Sports Mix Star Cup Alt Path Node 41":           LocData(base_id + 30766, LocGroup.SPORTS_MIX_ALT),
    # "Sports Mix Star Cup Alt Path Node 40":           LocData(base_id + 30767, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Tower B6":           LocData(base_id + 30768, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Tower B5":           LocData(base_id + 30769, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Tower B2":           LocData(base_id + 30770, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Star Road (Left) Intro":           LocData(base_id + 30771, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Star Road (Left) Bonus":           LocData(base_id + 30772, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Star Road (Right) Intro":           LocData(base_id + 30773, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Star Road (Right) Bonus":           LocData(base_id + 30774, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Star Road Bottom-Left of Star":           LocData(base_id + 30775, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Star Road Top-Left of Star":           LocData(base_id + 30776, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Star Road Top-Center of Star":           LocData(base_id + 30777, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Star Road Top-Right of Star":           LocData(base_id + 30778, LocGroup.SPORTS_MIX_ALT),
    "Sports Mix Star Cup Alt Path Star Road Bottom-Right of Star":           LocData(base_id + 30779, LocGroup.SPORTS_MIX_ALT),
}

global_alternate_path_normal_locations: Dict[str, LocData] = {
    "Mushroom Cup Alt Path Normal East of Red Toad House":                LocData(base_id + 30780, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal By Lake":                LocData(base_id + 30781, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Lake Platform":                LocData(base_id + 30782, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal South of Lake":                LocData(base_id + 30783, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Red Toad House":                LocData(base_id + 30784, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal By Castle Flowers":                LocData(base_id + 30785, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Lower Field":                LocData(base_id + 30786, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Below the Curve":                LocData(base_id + 30787, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Lower Curve":                LocData(base_id + 30788, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Middle Curve":                LocData(base_id + 30789, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Upper Curve":                LocData(base_id + 30790, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Top of the Mountain":                LocData(base_id + 30791, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Upper Field":                LocData(base_id + 30792, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Near Green Toad House":                LocData(base_id + 30793, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal By Logs":                LocData(base_id + 30794, LocGroup.ALT_NORMAL),
    "Mushroom Cup Alt Path Normal Hidden Finale":                LocData(base_id + 30795, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Left-Center Bridge":         LocData(base_id + 30828, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Flower Lake Island":         LocData(base_id + 30829, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Leftmost Bridge":         LocData(base_id + 30830, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Left Shoreline":         LocData(base_id + 30831, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Bottom-Left Island House":         LocData(base_id + 30832, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Bottom-Left Island Cannon":         LocData(base_id + 30833, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Bottom-Right Island":         LocData(base_id + 30834, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Middle-Left Islands":         LocData(base_id + 30835, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Top-Left Island":         LocData(base_id + 30836, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Waterwheel":         LocData(base_id + 30837, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Right Shoreline":         LocData(base_id + 30838, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Below Rightmost Bridge":         LocData(base_id + 30839, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Above Rightmost Bridge":         LocData(base_id + 30840, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Middle-Right Island Field":         LocData(base_id + 30841, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Middle-Right Island Cannon":         LocData(base_id + 30842, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Top-Right Island Tower":         LocData(base_id + 30843, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Top-Right Island Bottom Field":         LocData(base_id + 30844, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Top-Right Island Right Field":         LocData(base_id + 30845, LocGroup.ALT_NORMAL),
    "Flower Cup Alt Path Normal Hidden Finale":         LocData(base_id + 30846, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Tower C3":           LocData(base_id + 30885, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Tower B1":           LocData(base_id + 30886, LocGroup.ALT_NORMAL),
    # "Star Cup Alt Path Normal Node 3E":           LocData(base_id + 30887, LocGroup.ALT_NORMAL),
    # "Star Cup Alt Path Normal Node 3F":           LocData(base_id + 30888, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Tower D2":           LocData(base_id + 30889, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Tower E1":           LocData(base_id + 30890, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Tower D7":           LocData(base_id + 30891, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Tower E6":           LocData(base_id + 30892, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Tower C6":           LocData(base_id + 30893, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Tower B7":           LocData(base_id + 30894, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Tower A7":           LocData(base_id + 30895, LocGroup.ALT_NORMAL),
    # "Star Cup Alt Path Normal Node 41":           LocData(base_id + 30896, LocGroup.ALT_NORMAL),
    # "Star Cup Alt Path Normal Node 40":           LocData(base_id + 30897, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Tower B6":           LocData(base_id + 30898, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Tower B5":           LocData(base_id + 30899, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Tower B2":           LocData(base_id + 30900, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Star Road (Left) Intro":           LocData(base_id + 30901, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Star Road (Left) Bonus":           LocData(base_id + 30902, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Star Road (Right) Intro":           LocData(base_id + 30903, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Star Road (Right) Bonus":           LocData(base_id + 30904, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Star Road Bottom-Left of Star":           LocData(base_id + 30905, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Star Road Top-Left of Star":           LocData(base_id + 30906, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Star Road Top-Center of Star":           LocData(base_id + 30907, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Star Road Top-Right of Star":           LocData(base_id + 30908, LocGroup.ALT_NORMAL),
    "Star Cup Alt Path Normal Star Road Bottom-Right of Star":           LocData(base_id + 30909, LocGroup.ALT_NORMAL),
}

global_alternate_path_hard_locations: Dict[str, LocData] = {
    "Mushroom Cup Alt Path Hard East of Red Toad House":                  LocData(base_id + 30796, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard By Lake":                  LocData(base_id + 30797, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Lake Platform":                  LocData(base_id + 30798, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard South of Lake":                  LocData(base_id + 30799, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Red Toad House":                  LocData(base_id + 30800, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard By Castle Flowers":                  LocData(base_id + 30801, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Lower Field":                  LocData(base_id + 30802, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Below the Curve":                  LocData(base_id + 30803, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Lower Curve":                  LocData(base_id + 30804, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Middle Curve":                  LocData(base_id + 30805, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Upper Curve":                  LocData(base_id + 30806, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Top of the Mountain":                  LocData(base_id + 30807, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Upper Field":                  LocData(base_id + 30808, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Near Green Toad House":                  LocData(base_id + 30809, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard By Logs":                  LocData(base_id + 30810, LocGroup.ALT_HARD),
    "Mushroom Cup Alt Path Hard Hidden Finale":                  LocData(base_id + 30811, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Left-Center Bridge":           LocData(base_id + 30847, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Flower Lake Island":           LocData(base_id + 30848, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Leftmost Bridge":           LocData(base_id + 30849, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Left Shoreline":           LocData(base_id + 30850, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Bottom-Left Island House":           LocData(base_id + 30851, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Bottom-Left Island Cannon":           LocData(base_id + 30852, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Bottom-Right Island":           LocData(base_id + 30853, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Middle-Left Islands":           LocData(base_id + 30854, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Top-Left Island":           LocData(base_id + 30855, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Waterwheel":           LocData(base_id + 30856, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Right Shoreline":           LocData(base_id + 30857, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Below Rightmost Bridge":           LocData(base_id + 30858, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Above Rightmost Bridge":           LocData(base_id + 30859, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Middle-Right Island Field":           LocData(base_id + 30860, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Middle-Right Island Cannon":           LocData(base_id + 30861, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Top-Right Island Tower":           LocData(base_id + 30862, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Top-Right Island Bottom Field":           LocData(base_id + 30863, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Top-Right Island Right Field":           LocData(base_id + 30864, LocGroup.ALT_HARD),
    "Flower Cup Alt Path Hard Hidden Finale":           LocData(base_id + 30865, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Tower C3":             LocData(base_id + 30910, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Tower B1":             LocData(base_id + 30911, LocGroup.ALT_HARD),
    # "Star Cup Alt Path Hard Node 3E":             LocData(base_id + 30912, LocGroup.ALT_HARD),
    # "Star Cup Alt Path Hard Node 3F":             LocData(base_id + 30913, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Tower D2":             LocData(base_id + 30914, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Tower E1":             LocData(base_id + 30915, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Tower D7":             LocData(base_id + 30916, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Tower E6":             LocData(base_id + 30917, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Tower C6":             LocData(base_id + 30918, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Tower B7":             LocData(base_id + 30919, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Tower A7":             LocData(base_id + 30920, LocGroup.ALT_HARD),
    # "Star Cup Alt Path Hard Node 41":             LocData(base_id + 30921, LocGroup.ALT_HARD),
    # "Star Cup Alt Path Hard Node 40":             LocData(base_id + 30922, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Tower B6":             LocData(base_id + 30923, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Tower B5":             LocData(base_id + 30924, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Tower B2":             LocData(base_id + 30925, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Star Road (Left) Intro":             LocData(base_id + 30926, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Star Road (Left) Bonus":             LocData(base_id + 30927, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Star Road (Right) Intro":             LocData(base_id + 30928, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Star Road (Right) Bonus":             LocData(base_id + 30929, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Star Road Bottom-Left of Star":             LocData(base_id + 30930, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Star Road Top-Left of Star":             LocData(base_id + 30931, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Star Road Top-Center of Star":             LocData(base_id + 30932, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Star Road Top-Right of Star":             LocData(base_id + 30933, LocGroup.ALT_HARD),
    "Star Cup Alt Path Hard Star Road Bottom-Right of Star":             LocData(base_id + 30934, LocGroup.ALT_HARD),
}

global_alternate_path_global_locations: Dict[str, LocData] = {
    "Mushroom Cup Alt Path East of Red Toad House":                       LocData(base_id + 30812, LocGroup.ALT),
    "Mushroom Cup Alt Path By Lake":                       LocData(base_id + 30813, LocGroup.ALT),
    "Mushroom Cup Alt Path Lake Platform":                       LocData(base_id + 30814, LocGroup.ALT),
    "Mushroom Cup Alt Path South of Lake":                       LocData(base_id + 30815, LocGroup.ALT),
    "Mushroom Cup Alt Path Red Toad House":                       LocData(base_id + 30816, LocGroup.ALT),
    "Mushroom Cup Alt Path By Castle Flowers":                       LocData(base_id + 30817, LocGroup.ALT),
    "Mushroom Cup Alt Path Lower Field":                       LocData(base_id + 30818, LocGroup.ALT),
    "Mushroom Cup Alt Path Below the Curve":                       LocData(base_id + 30819, LocGroup.ALT),
    "Mushroom Cup Alt Path Lower Curve":                       LocData(base_id + 30820, LocGroup.ALT),
    "Mushroom Cup Alt Path Middle Curve":                       LocData(base_id + 30821, LocGroup.ALT),
    "Mushroom Cup Alt Path Upper Curve":                       LocData(base_id + 30822, LocGroup.ALT),
    "Mushroom Cup Alt Path Top of the Mountain":                       LocData(base_id + 30823, LocGroup.ALT),
    "Mushroom Cup Alt Path Upper Field":                       LocData(base_id + 30824, LocGroup.ALT),
    "Mushroom Cup Alt Path Near Green Toad House":                       LocData(base_id + 30825, LocGroup.ALT),
    "Mushroom Cup Alt Path By Logs":                       LocData(base_id + 30826, LocGroup.ALT),
    "Mushroom Cup Alt Path Hidden Finale":                       LocData(base_id + 30827, LocGroup.ALT),
    "Flower Cup Alt Path Left-Center Bridge":                LocData(base_id + 30866, LocGroup.ALT),
    "Flower Cup Alt Path Flower Lake Island":                LocData(base_id + 30867, LocGroup.ALT),
    "Flower Cup Alt Path Leftmost Bridge":                LocData(base_id + 30868, LocGroup.ALT),
    "Flower Cup Alt Path Left Shoreline":                LocData(base_id + 30869, LocGroup.ALT),
    "Flower Cup Alt Path Bottom-Left Island House":                LocData(base_id + 30870, LocGroup.ALT),
    "Flower Cup Alt Path Bottom-Left Island Cannon":                LocData(base_id + 30871, LocGroup.ALT),
    "Flower Cup Alt Path Bottom-Right Island":                LocData(base_id + 30872, LocGroup.ALT),
    "Flower Cup Alt Path Middle-Left Islands":                LocData(base_id + 30873, LocGroup.ALT),
    "Flower Cup Alt Path Top-Left Island":                LocData(base_id + 30874, LocGroup.ALT),
    "Flower Cup Alt Path Waterwheel":                LocData(base_id + 30875, LocGroup.ALT),
    "Flower Cup Alt Path Right Shoreline":                LocData(base_id + 30876, LocGroup.ALT),
    "Flower Cup Alt Path Below Rightmost Bridge":                LocData(base_id + 30877, LocGroup.ALT),
    "Flower Cup Alt Path Above Rightmost Bridge":                LocData(base_id + 30878, LocGroup.ALT),
    "Flower Cup Alt Path Middle-Right Island Field":                LocData(base_id + 30879, LocGroup.ALT),
    "Flower Cup Alt Path Middle-Right Island Cannon":                LocData(base_id + 30880, LocGroup.ALT),
    "Flower Cup Alt Path Top-Right Island Tower":                LocData(base_id + 30881, LocGroup.ALT),
    "Flower Cup Alt Path Top-Right Island Bottom Field":                LocData(base_id + 30882, LocGroup.ALT),
    "Flower Cup Alt Path Top-Right Island Right Field":                LocData(base_id + 30883, LocGroup.ALT),
    "Flower Cup Alt Path Hidden Finale":                LocData(base_id + 30884, LocGroup.ALT),
    "Star Cup Alt Path Tower C3":                  LocData(base_id + 30935, LocGroup.ALT),
    "Star Cup Alt Path Tower B1":                  LocData(base_id + 30936, LocGroup.ALT),
    # "Star Cup Alt Path Node 3E":                  LocData(base_id + 30937, LocGroup.ALT),
    # "Star Cup Alt Path Node 3F":                  LocData(base_id + 30938, LocGroup.ALT),
    "Star Cup Alt Path Tower D2":                  LocData(base_id + 30939, LocGroup.ALT),
    "Star Cup Alt Path Tower E1":                  LocData(base_id + 30940, LocGroup.ALT),
    "Star Cup Alt Path Tower D7":                  LocData(base_id + 30941, LocGroup.ALT),
    "Star Cup Alt Path Tower E6":                  LocData(base_id + 30942, LocGroup.ALT),
    "Star Cup Alt Path Tower C6":                  LocData(base_id + 30943, LocGroup.ALT),
    "Star Cup Alt Path Tower B7":                  LocData(base_id + 30944, LocGroup.ALT),
    "Star Cup Alt Path Tower A7":                  LocData(base_id + 30945, LocGroup.ALT),
    # "Star Cup Alt Path Node 41":                  LocData(base_id + 30946, LocGroup.ALT),
    # "Star Cup Alt Path Node 40":                  LocData(base_id + 30947, LocGroup.ALT),
    "Star Cup Alt Path Tower B6":                  LocData(base_id + 30948, LocGroup.ALT),
    "Star Cup Alt Path Tower B5":                  LocData(base_id + 30949, LocGroup.ALT),
    "Star Cup Alt Path Tower B2":                  LocData(base_id + 30950, LocGroup.ALT),
    "Star Cup Alt Path Star Road (Left) Intro":                  LocData(base_id + 30951, LocGroup.ALT),
    "Star Cup Alt Path Star Road (Left) Bonus":                  LocData(base_id + 30952, LocGroup.ALT),
    "Star Cup Alt Path Star Road (Right) Intro":                  LocData(base_id + 30953, LocGroup.ALT),
    "Star Cup Alt Path Star Road (Right) Bonus":                  LocData(base_id + 30954, LocGroup.ALT),
    "Star Cup Alt Path Star Road Bottom-Left of Star":                  LocData(base_id + 30955, LocGroup.ALT),
    "Star Cup Alt Path Star Road Top-Left of Star":                  LocData(base_id + 30956, LocGroup.ALT),
    "Star Cup Alt Path Star Road Top-Center of Star":                  LocData(base_id + 30957, LocGroup.ALT),
    "Star Cup Alt Path Star Road Top-Right of Star":                  LocData(base_id + 30958, LocGroup.ALT),
    "Star Cup Alt Path Star Road Bottom-Right of Star":                  LocData(base_id + 30959, LocGroup.ALT),
}


location_table: Dict[str, LocData] = {
    **cup_round_locations,
    **sports_mix_locations,
    **basketball_alternate_path_normal_locations,
    **basketball_alternate_path_hard_locations,
    **basketball_alternate_path_global_locations,
    **dodgeball_alternate_path_normal_locations,
    **dodgeball_alternate_path_hard_locations,
    **dodgeball_alternate_path_global_locations,
    **volleyball_alternate_path_normal_locations,
    **volleyball_alternate_path_hard_locations,
    **volleyball_alternate_path_global_locations,
    **hockey_alternate_path_normal_locations,
    **hockey_alternate_path_hard_locations,
    **hockey_alternate_path_global_locations,
    **sports_mix_alternate_path_locations,
    **global_alternate_path_normal_locations,
    **global_alternate_path_hard_locations,
    **global_alternate_path_global_locations,
    **easy_exhibition_locations,
    **normal_exhibition_locations,
    **hard_exhibition_locations,
    **expert_exhibition_locations,
    **global_exhibition_locations,
    **feed_petey_locations,
    **harmony_hustle_locations,
    **bob_omb_dodge_locations,
    **smash_skate_locations,
    **special_sanity_locations,
    **character_sanity_locations,
    **costume_char_sanity_locations,
    **court_sanity_locations,
    **boss_locations,
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
    b_mushroom_alt_n = world.get_region("Basketball: Mushroom Cup Alt Paths (Normal)")
    b_flower_alt_n = world.get_region("Basketball: Flower Cup Alt Paths (Normal)")
    b_star_alt_n = world.get_region("Basketball: Star Cup Alt Paths (Normal)")
    b_mushroom_cup_h = world.get_region("Basketball: Mushroom Cup (Hard)")
    b_flower_cup_h = world.get_region("Basketball: Flower Cup (Hard)")
    b_star_cup_h = world.get_region("Basketball: Star Cup (Hard)")
    b_mushroom_alt_h = world.get_region("Basketball: Mushroom Cup Alt Paths (Hard)")
    b_flower_alt_h = world.get_region("Basketball: Flower Cup Alt Paths (Hard)")
    b_star_alt_h = world.get_region("Basketball: Star Cup Alt Paths (Hard)")
    b_mushroom_alt_g = world.get_region("Basketball: Mushroom Cup Alt Paths (Global)")
    b_flower_alt_g = world.get_region("Basketball: Flower Cup Alt Paths (Global)")
    b_star_alt_g = world.get_region("Basketball: Star Cup Alt Paths (Global)")

    # Dodgeball
    d_exhibition = world.get_region("Dodgeball: Exhibition")
    d_mushroom_cup_n = world.get_region("Dodgeball: Mushroom Cup (Normal)")
    d_flower_cup_n = world.get_region("Dodgeball: Flower Cup (Normal)")
    d_star_cup_n = world.get_region("Dodgeball: Star Cup (Normal)")
    d_mushroom_alt_n = world.get_region("Dodgeball: Mushroom Cup Alt Paths (Normal)")
    d_flower_alt_n = world.get_region("Dodgeball: Flower Cup Alt Paths (Normal)")
    d_star_alt_n = world.get_region("Dodgeball: Star Cup Alt Paths (Normal)")
    d_mushroom_cup_h = world.get_region("Dodgeball: Mushroom Cup (Hard)")
    d_flower_cup_h = world.get_region("Dodgeball: Flower Cup (Hard)")
    d_star_cup_h = world.get_region("Dodgeball: Star Cup (Hard)")
    d_mushroom_alt_h = world.get_region("Dodgeball: Mushroom Cup Alt Paths (Hard)")
    d_flower_alt_h = world.get_region("Dodgeball: Flower Cup Alt Paths (Hard)")
    d_star_alt_h = world.get_region("Dodgeball: Star Cup Alt Paths (Hard)")
    d_mushroom_alt_g = world.get_region("Dodgeball: Mushroom Cup Alt Paths (Global)")
    d_flower_alt_g = world.get_region("Dodgeball: Flower Cup Alt Paths (Global)")
    d_star_alt_g = world.get_region("Dodgeball: Star Cup Alt Paths (Global)")

    # Volleyball
    v_exhibition = world.get_region("Volleyball: Exhibition")
    v_mushroom_cup_n = world.get_region("Volleyball: Mushroom Cup (Normal)")
    v_flower_cup_n = world.get_region("Volleyball: Flower Cup (Normal)")
    v_star_cup_n = world.get_region("Volleyball: Star Cup (Normal)")
    v_mushroom_alt_n = world.get_region("Volleyball: Mushroom Cup Alt Paths (Normal)")
    v_flower_alt_n = world.get_region("Volleyball: Flower Cup Alt Paths (Normal)")
    v_star_alt_n = world.get_region("Volleyball: Star Cup Alt Paths (Normal)")
    v_mushroom_cup_h = world.get_region("Volleyball: Mushroom Cup (Hard)")
    v_flower_cup_h = world.get_region("Volleyball: Flower Cup (Hard)")
    v_star_cup_h = world.get_region("Volleyball: Star Cup (Hard)")
    v_mushroom_alt_h = world.get_region("Volleyball: Mushroom Cup Alt Paths (Hard)")
    v_flower_alt_h = world.get_region("Volleyball: Flower Cup Alt Paths (Hard)")
    v_star_alt_h = world.get_region("Volleyball: Star Cup Alt Paths (Hard)")
    v_mushroom_alt_g = world.get_region("Volleyball: Mushroom Cup Alt Paths (Global)")
    v_flower_alt_g = world.get_region("Volleyball: Flower Cup Alt Paths (Global)")
    v_star_alt_g = world.get_region("Volleyball: Star Cup Alt Paths (Global)")

    # Hockey
    h_exhibition = world.get_region("Hockey: Exhibition")
    h_mushroom_cup_n = world.get_region("Hockey: Mushroom Cup (Normal)")
    h_flower_cup_n = world.get_region("Hockey: Flower Cup (Normal)")
    h_star_cup_n = world.get_region("Hockey: Star Cup (Normal)")
    h_mushroom_alt_n = world.get_region("Hockey: Mushroom Cup Alt Paths (Normal)")
    h_flower_alt_n = world.get_region("Hockey: Flower Cup Alt Paths (Normal)")
    h_star_alt_n = world.get_region("Hockey: Star Cup Alt Paths (Normal)")
    h_mushroom_cup_h = world.get_region("Hockey: Mushroom Cup (Hard)")
    h_flower_cup_h = world.get_region("Hockey: Flower Cup (Hard)")
    h_star_cup_h = world.get_region("Hockey: Star Cup (Hard)")
    h_mushroom_alt_h = world.get_region("Hockey: Mushroom Cup Alt Paths (Hard)")
    h_flower_alt_h = world.get_region("Hockey: Flower Cup Alt Paths (Hard)")
    h_star_alt_h = world.get_region("Hockey: Star Cup Alt Paths (Hard)")
    h_mushroom_alt_g = world.get_region("Hockey: Mushroom Cup Alt Paths (Global)")
    h_flower_alt_g = world.get_region("Hockey: Flower Cup Alt Paths (Global)")
    h_star_alt_g = world.get_region("Hockey: Star Cup Alt Paths (Global)")

    # Sports Mix
    sports_mix_mushroom = world.get_region("Sports Mix: Mushroom Cup")
    sports_mix_flower = world.get_region("Sports Mix: Flower Cup")
    sports_mix_star = world.get_region("Sports Mix: Star Cup")
    sports_mix_mushroom_alt = world.get_region("Sports Mix: Mushroom Cup Alt Paths")
    sports_mix_flower_alt = world.get_region("Sports Mix: Flower Cup Alt Paths")
    sports_mix_star_alt = world.get_region("Sports Mix: Star Cup Alt Paths")

    # Global Sports
    g_mushroom_alt_n = world.get_region("Global: Mushroom Cup Alt Paths (Normal)")
    g_flower_alt_n = world.get_region("Global: Flower Cup Alt Paths (Normal)")
    g_star_alt_n = world.get_region("Global: Star Cup Alt Paths (Normal)")
    g_mushroom_alt_h = world.get_region("Global: Mushroom Cup Alt Paths (Hard)")
    g_flower_alt_h = world.get_region("Global: Flower Cup Alt Paths (Hard)")
    g_star_alt_h = world.get_region("Global: Star Cup Alt Paths (Hard)")
    g_mushroom_alt_g = world.get_region("Global: Mushroom Cup Alt Paths (Global)")
    g_flower_alt_g = world.get_region("Global: Flower Cup Alt Paths (Global)")
    g_star_alt_g = world.get_region("Global: Star Cup Alt Paths (Global)")

    # Party Modes
    feed_petey = world.get_region("Feed Petey")
    harmony_hustle = world.get_region("Harmony Hustle")
    bob_omb_dodge = world.get_region("Bob-omb Dodge")
    smash_skate = world.get_region("Smash Skate")

    # === Tournament Locations ===

    cup_regions = {
        "Normal": {
            "Basketball": {
                "Mushroom": b_mushroom_cup_n,
                "Flower": b_flower_cup_n,
                "Star": b_star_cup_n,
            },
            "Dodgeball": {
                "Mushroom": d_mushroom_cup_n,
                "Flower": d_flower_cup_n,
                "Star": d_star_cup_n,
            },
            "Volleyball": {
                "Mushroom": v_mushroom_cup_n,
                "Flower": v_flower_cup_n,
                "Star": v_star_cup_n,
            },
            "Hockey": {
                "Mushroom": h_mushroom_cup_n,
                "Flower": h_flower_cup_n,
                "Star": h_star_cup_n,
            },
        },

        "Hard": {
            "Basketball": {
                "Mushroom": b_mushroom_cup_h,
                "Flower": b_flower_cup_h,
                "Star": b_star_cup_h,
            },
            "Dodgeball": {
                "Mushroom": d_mushroom_cup_h,
                "Flower": d_flower_cup_h,
                "Star": d_star_cup_h,
            },
            "Volleyball": {
                "Mushroom": v_mushroom_cup_h,
                "Flower": v_flower_cup_h,
                "Star": v_star_cup_h,
            },
            "Hockey": {
                "Mushroom": h_mushroom_cup_h,
                "Flower": h_flower_cup_h,
                "Star": h_star_cup_h,
            },
        }
    }

    alt_path_regions = {
        "Normal": {
        "Basketball": {
            "Mushroom": b_mushroom_alt_n,
            "Flower": b_flower_alt_n,
            "Star": b_star_alt_n,
        },
        "Dodgeball": {
            "Mushroom": d_mushroom_alt_n,
            "Flower": d_flower_alt_n,
            "Star": d_star_alt_n,
        },
        "Volleyball": {
            "Mushroom": v_mushroom_alt_n,
            "Flower": v_flower_alt_n,
            "Star": v_star_alt_n,
        },
        "Hockey": {
            "Mushroom": h_mushroom_alt_n,
            "Flower": h_flower_alt_n,
            "Star": h_star_alt_n,
        },
        "Global": {
            "Mushroom": g_mushroom_alt_n,
            "Flower": g_flower_alt_n,
            "Star": g_star_alt_n,
        }
    },

        "Hard": {
            "Basketball": {
                "Mushroom": b_mushroom_alt_h,
                "Flower": b_flower_alt_h,
                "Star": b_star_alt_h,
            },
            "Dodgeball": {
                "Mushroom": d_mushroom_alt_h,
                "Flower": d_flower_alt_h,
                "Star": d_star_alt_h,
            },
            "Volleyball": {
                "Mushroom": v_mushroom_alt_h,
                "Flower": v_flower_alt_h,
                "Star": v_star_alt_h,
            },
            "Hockey": {
                "Mushroom": h_mushroom_alt_h,
                "Flower": h_flower_alt_h,
                "Star": h_star_alt_h,
            },
            "Global": {
                "Mushroom": g_mushroom_alt_h,
                "Flower": g_flower_alt_h,
                "Star": g_star_alt_h,
            }
        },

        "Global": {
            "Basketball": {
                "Mushroom": b_mushroom_alt_g,
                "Flower": b_flower_alt_g,
                "Star": b_star_alt_g,
            },
            "Dodgeball": {
                "Mushroom": d_mushroom_alt_g,
                "Flower": d_flower_alt_g,
                "Star": d_star_alt_g,
            },
            "Volleyball": {
                "Mushroom": v_mushroom_alt_g,
                "Flower": v_flower_alt_g,
                "Star": v_star_alt_g,
            },
            "Hockey": {
                "Mushroom": h_mushroom_alt_g,
                "Flower": h_flower_alt_g,
                "Star": h_star_alt_g,
            },
            "Global": {
                "Mushroom": g_mushroom_alt_g,
                "Flower": g_flower_alt_g,
                "Star": g_star_alt_g,
            }
        }
    }

    alt_path_tables = {
        "Basketball": {
            "Normal": basketball_alternate_path_normal_locations,
            "Hard": basketball_alternate_path_hard_locations,
            "Global": basketball_alternate_path_global_locations,
        },
        "Dodgeball": {
            "Normal": dodgeball_alternate_path_normal_locations,
            "Hard": dodgeball_alternate_path_hard_locations,
            "Global": dodgeball_alternate_path_global_locations,
        },
        "Volleyball": {
            "Normal": volleyball_alternate_path_normal_locations,
            "Hard": volleyball_alternate_path_hard_locations,
            "Global": volleyball_alternate_path_global_locations,
        },
        "Hockey": {
            "Normal": hockey_alternate_path_normal_locations,
            "Hard": hockey_alternate_path_hard_locations,
            "Global": hockey_alternate_path_global_locations,
        },
        "Global": {
            "Normal": global_alternate_path_normal_locations,
            "Hard": global_alternate_path_hard_locations,
            "Global": global_alternate_path_global_locations,
        },
    }

    if world.options.include_tournaments.value:
        for difficulty, sports in cup_regions.items():
            if difficulty == "Hard" and not world.options.hard_tournament_difficulty.value:
                continue

            for sport, cups in sports.items():
                if sport not in world.options.enabled_sports.value:
                    continue

                for cup, region in cups.items():
                    locations = get_location_names_with_ids([
                        f"{sport}: Beat {difficulty} {cup} Cup Round {i}"
                        for i in range(1, 4)
                    ])

                    region.add_locations(locations, MSMLocation)

        sports_mix_regions = {
            "Mushroom": sports_mix_mushroom,
            "Flower": sports_mix_flower,
            "Star": sports_mix_star,
        }

        if "Sports Mix" in world.options.enabled_sports.value:
            for cup, region in sports_mix_regions.items():
                locations = get_location_names_with_ids([
                    f"Sports Mix: Beat {cup} Cup Round {i}"
                    for i in range(1, 4)
                ])

                region.add_locations(locations, MSMLocation)

        if world.options.include_alt_paths.value:
            alt_path_type = world.options.alt_path_type.value

            sports_mix_alt_regions = {
                "Mushroom": sports_mix_mushroom_alt,
                "Flower": sports_mix_flower_alt,
                "Star": sports_mix_star_alt,
            }

            if alt_path_type == 0:
                for difficulty, sports in alt_path_regions.items():
                    if difficulty == "Global" or (
                            difficulty == "Hard" and not world.options.hard_tournament_difficulty.value):
                        continue

                    for sport, cups in sports.items():
                        if sport == "Global" or (sport not in world.options.enabled_sports.value):
                            continue

                        for cup, region in cups.items():
                            location_names = [
                                name for name in alt_path_tables[sport][difficulty]
                                if cup.casefold() in name.casefold()
                            ]

                            locations = get_location_names_with_ids(location_names)
                            region.add_locations(locations, MSMLocation)

                if "Sports Mix" in world.options.enabled_sports.value:
                    for cup, region in sports_mix_alt_regions.items():
                        location_names = [
                            name for name in sports_mix_alternate_path_locations
                            if cup.casefold() in name.casefold()
                        ]
                        locations = get_location_names_with_ids(location_names)
                        region.add_locations(locations, MSMLocation)

            elif alt_path_type == 1:
                for sport, cups in alt_path_regions["Global"].items():
                    if sport == "Global" or (sport not in world.options.enabled_sports.value):
                        continue

                    for cup, region in cups.items():
                        location_names = [
                            name for name in alt_path_tables[sport]["Global"]
                            if cup.casefold() in name.casefold()
                        ]

                        locations = get_location_names_with_ids(location_names)
                        region.add_locations(locations, MSMLocation)

            elif alt_path_type == 2 or alt_path_type == 4:
                for difficulty, sports in alt_path_regions.items():

                    if difficulty == "Global" or (
                            difficulty == "Hard" and not world.options.hard_tournament_difficulty.value):
                        continue

                    for cup, region in sports["Global"].items():
                        location_names = [
                            name for name in alt_path_tables["Global"][difficulty]
                            if cup.casefold() in name.casefold()
                        ]

                        locations = get_location_names_with_ids(location_names)
                        region.add_locations(locations, MSMLocation)

            elif alt_path_type == 3 or alt_path_type == 5:
                for cup, region in alt_path_regions["Global"]["Global"].items():
                    location_names = [
                        name for name in alt_path_tables["Global"]["Global"]
                        if cup.casefold() in name.casefold()
                    ]

                    locations = get_location_names_with_ids(location_names)
                    region.add_locations(locations, MSMLocation)

        if world.options.include_alt_paths.value:
            alt_path_type = world.options.alt_path_type.value

            sports_mix_alt_regions = {
                "Mushroom": sports_mix_mushroom_alt,
                "Flower": sports_mix_flower_alt,
                "Star": sports_mix_star_alt,
            }

            if alt_path_type == 0:
                for difficulty, sports in alt_path_regions.items():
                    if difficulty == "Global" or (difficulty == "Hard" and not world.options.hard_tournament_difficulty.value):
                        continue
                
                    for sport, cups in sports.items():
                        if sport == "Global" or (sport not in world.options.enabled_sports.value):
                            continue
                
                        for cup, region in cups.items():
                                        
                            location_names = [
                                name for name in alt_path_tables[sport][difficulty]
                                if f"{cup.casefold()} cup" in name.casefold()
                            ]

                            locations = get_location_names_with_ids(location_names)
                            region.add_locations(locations, MSMLocation)

                if "Sports Mix" in world.options.enabled_sports.value:
                    for cup, region in sports_mix_alt_regions.items():
                        location_names = [
                            name for name in sports_mix_alternate_path_locations
                            if f"{cup.casefold()} cup" in name.casefold()
                        ]
                        locations = get_location_names_with_ids(location_names)
                        region.add_locations(locations, MSMLocation)

            elif alt_path_type == 1:
                for sport, cups in alt_path_regions["Global"].items():
                    if sport == "Global" or (sport not in world.options.enabled_sports.value):
                        continue
                                    
                    for cup, region in cups.items():
                                                        
                        location_names = [
                            name for name in alt_path_tables[sport]["Global"]
                            if f"{cup.casefold()} cup" in name.casefold()
                        ]
                    
                        locations = get_location_names_with_ids(location_names)
                        region.add_locations(locations, MSMLocation)

            elif alt_path_type == 2 or alt_path_type == 4:
                for difficulty, sports in alt_path_regions.items():

                    if difficulty == "Global" or (difficulty == "Hard" and not world.options.hard_tournament_difficulty.value):
                        continue

                    for cup, region in sports["Global"].items():

                        location_names = [
                            name for name in alt_path_tables["Global"][difficulty]
                            if f"{cup.casefold()} cup" in name.casefold()
                        ]

                        locations = get_location_names_with_ids(location_names)
                        region.add_locations(locations, MSMLocation)
            
            elif alt_path_type == 3 or alt_path_type == 5:
                for cup, region in alt_path_regions["Global"]["Global"].items():

                    location_names = [
                        name for name in alt_path_tables["Global"]["Global"]
                        if f"{cup.casefold()} cup" in name.casefold()
                    ]

                    locations = get_location_names_with_ids(location_names)
                    region.add_locations(locations, MSMLocation)
                        



    # === Exhibition Locations for each difficulty ===

    exhibition_courts = {
        "Basketball": [
            "Mario Stadium",
            "Koopa Troopa Beach",
            "DK Dock",
            "Luigi's Mansion",
            "Western Junction",
            "Daisy Garden",
            "Bowser Jr. Blvd.",
            "Bowser's Castle",
            "Star Ship",
            "Peach's Castle",
            "Wario Factory",
            "Ghoulish Galleon"
        ],
        "Dodgeball": [
            "Mario Stadium",
            "Koopa Troopa Beach",
            "Peach's Castle",
            "DK Dock",
            "Toad Park",
            "Daisy Garden",
            "Wario Factory",
            "Bowser's Castle",
            "Star Ship",
            "Western Junction",
            "Waluigi Pinball",
            "Ghoulish Galleon"
        ],
        "Volleyball": [
            "Mario Stadium",
            "Koopa Troopa Beach",
            "Peach's Castle",
            "DK Dock",
            "Luigi's Mansion",
            "Western Junction",
            "Bowser Jr. Blvd.",
            "Bowser's Castle",
            "Star Ship",
            "Wario Factory",
            "Waluigi Pinball",
            "Ghoulish Galleon"
        ],
        "Hockey": [
            "Mario Stadium",
            "Toad Park",
            "Peach's Castle",
            "Western Junction",
            "Wario Factory",
            "Daisy Garden",
            "Bowser Jr. Blvd.",
            "Waluigi Pinball",
            "Star Ship",
            "Koopa Troopa Beach",
            "Ghoulish Galleon",
            "Bowser's Castle"
        ]
    }

    regions = {
        "Basketball": b_exhibition,
        "Dodgeball": d_exhibition,
        "Volleyball": v_exhibition,
        "Hockey": h_exhibition,
    }

    if world.options.include_exhibition.value:
        for difficulty in world.options.exhibition_difficulties.value:

            if world.options.exhibition_type == ExhibitionType.option_all_sports:
                # Each sport has its own distinct set of "{sport} Ex: ..." locations,
                # so these must be created and added once per enabled sport.
                for sport, courts in exhibition_courts.items():
                    if sport not in world.options.enabled_sports.value:
                        continue

                    locations = get_location_names_with_ids([
                        f"{sport} Ex: Beat {court} ({difficulty})"
                        for court in courts
                    ])

                    regions[sport].add_locations(locations, MSMLocation)

            else:
                # Universal exhibitions are only playable when at least one main
                # sport is enabled. Do not create unreachable global exhibition
                # checks for configurations such as Party Palooza + enabled_sports: [].
                enabled_main_sports = {
                    sport for sport in world.options.enabled_sports.value
                    if sport in exhibition_courts
                }
                if not enabled_main_sports:
                    continue

                locations = get_location_names_with_ids([
                    f"Exhibition: Beat {court} ({difficulty})"
                    for court in courts_list
                ])

                world.get_region("Exhibition").add_locations(locations, MSMLocation)

    # === Party Mode Locations ===

    party_mode_to_locations = {
        "Feed Petey": feed_petey_locations,
        "Harmony Hustle": harmony_hustle_locations,
        "Bob-omb Dodge": bob_omb_dodge_locations,
        "Smash Skate": smash_skate_locations,
    }

    party_mode_to_region = {
        "Feed Petey": feed_petey,
        "Harmony Hustle": harmony_hustle,
        "Bob-omb Dodge": bob_omb_dodge,
        "Smash Skate": smash_skate,
    }

    if world.options.party_mode:
        for mode in world.options.party_mode.value:
            locations = party_mode_to_locations[mode]
            region = party_mode_to_region[mode]

            for location in locations:
                region.add_locations(get_location_names_with_ids([location]), MSMLocation)

    # === Sanity Locations ===

    # Character Sanity Locations
    if world.options.character_sanity.value in (CharacterSanity.option_characters,
                                                CharacterSanity.option_characters_and_costumes):
        character_locations = get_location_names_with_ids([location for location in character_sanity_locations])
        main_menu.add_locations(character_locations)

    if world.options.character_sanity.value == CharacterSanity.option_characters_and_costumes:
        costume_locations = get_location_names_with_ids([location for location in costume_char_sanity_locations])
        main_menu.add_locations(costume_locations)

    # Court Sanity Locations
    if world.options.court_sanity.value:
        locations = {}

        tournament_courts = {
            "Basketball": {
                "Mario Stadium", "Koopa Troopa Beach", "DK Dock",
                "Luigi's Mansion", "Western Junction", "Daisy Garden",
                "Bowser Jr. Blvd.", "Bowser's Castle", "Star Ship",
            },
            "Dodgeball": {
                "Mario Stadium", "Koopa Troopa Beach", "Peach's Castle",
                "DK Dock", "Toad Park", "Daisy Garden",
                "Wario Factory", "Bowser's Castle", "Star Ship",
            },
            "Volleyball": {
                "Mario Stadium", "Koopa Troopa Beach", "Peach's Castle",
                "DK Dock", "Luigi's Mansion", "Western Junction",
                "Bowser Jr. Blvd.", "Bowser's Castle", "Star Ship",
            },
            "Hockey": {
                "Mario Stadium", "Toad Park", "Peach's Castle",
                "Western Junction", "Wario Factory", "Daisy Garden",
                "Bowser Jr. Blvd.", "Waluigi Pinball", "Star Ship",
            },
        }

        party_mode_courts = {
            "Feed Petey": {"Daisy Garden", "DK Dock", "Wario Factory"},
            "Harmony Hustle": {"Peach's Castle", "DK Dock", "Bowser Jr. Blvd."},
            "Bob-omb Dodge": {"Mario Stadium", "Ghoulish Galleon", "Western Junction"},
            "Smash Skate": {"Sherbet Sea", "Rowdy Raft", "Fire Mountain"},
        }

        playable_courts = set()
        enabled_main_sports = {
            sport for sport in world.options.enabled_sports.value
            if sport in exhibition_courts
        }

        # Only create Court Sanity checks for courts that are playable in the
        # generated configuration. Tournament-only seeds must not inherit the
        # larger exhibition court lists.
        if world.options.include_tournaments.value:
            for sport in enabled_main_sports:
                playable_courts.update(tournament_courts[sport])

        # An exhibition option with no selected difficulties creates no matches,
        # so it must not create otherwise-unreachable Court Sanity checks.
        if (world.options.include_exhibition.value and
                world.options.exhibition_difficulties.value and
                enabled_main_sports):
            if world.options.exhibition_type.value == ExhibitionType.option_all_sports:
                for sport in enabled_main_sports:
                    playable_courts.update(exhibition_courts[sport])
            else:
                playable_courts.update(courts_list)

        for mode in world.options.party_mode.value:
            playable_courts.update(party_mode_courts.get(mode, set()))

        for court in playable_courts:
            location_name = f"Win on {court}"
            locations.update(get_location_names_with_ids([location_name]))

        main_menu.add_locations(locations, MSMLocation)

    # Special Sanity
    if world.options.special_sanity.value:
        special_locations = get_location_names_with_ids([location for location in special_sanity_locations])
        main_menu.add_locations(special_locations)

def create_events(world: "MSMWorld") -> None:
    behemoth_boss = world.get_region("Behemoth Boss Battle")
    behemoth_king_boss = world.get_region("Behemoth King Boss Battle")
    main_menu = world.get_region("Main Menu")

    if world.options.goal_condition.value == GoalCondition.option_defeat_behemoth:
        behemoth_boss.add_event("Defeat Behemoth!", "Victory!", location_type=MSMLocation,
                                item_type=items.MSMItem)

        if world.options.boss_locations.value == BossLocations.option_defeat_behemoth_king:
            behemoth_king_location = get_location_names_with_ids(["Defeat Behemoth King!"])
            behemoth_boss.add_locations(behemoth_king_location, MSMLocation)

    elif world.options.goal_condition.value == GoalCondition.option_defeat_behemoth_king:
        behemoth_king_boss.add_event("Defeat Behemoth King!", "Victory!", location_type=MSMLocation,
                                     item_type=items.MSMItem)

        if world.options.boss_locations.value == BossLocations.option_defeat_behemoth:
            behemoth_location = get_location_names_with_ids(["Defeat Behemoth!"])
            behemoth_boss.add_locations(behemoth_location, MSMLocation)

    elif world.options.goal_condition.value == GoalCondition.option_win_cups:
        win_cup_value = world.options.win_cups_amount.value
        menu = world.get_region("Main Menu")
        menu.add_event(f"Win {win_cup_value} Cups!", "Victory!", location_type=MSMLocation,
                       item_type=items.MSMItem)

        if world.options.boss_locations.value in (BossLocations.option_defeat_behemoth, BossLocations.option_both):
            behemoth_locations = get_location_names_with_ids(["Defeat Behemoth!"])
            behemoth_boss.add_locations(behemoth_locations, MSMLocation)

        if world.options.boss_locations.value in (BossLocations.option_defeat_behemoth_king, BossLocations.option_both):
            behemoth_king_locations = get_location_names_with_ids(["Defeat Behemoth King!"])
            behemoth_king_boss.add_locations(behemoth_king_locations, MSMLocation)

    elif world.options.goal_condition.value == GoalCondition.option_exhibition_tour:
        amount = find_num_exhibition_locs(
            world.options.enabled_sports.value,
            world.options.exhibition_type.value,
            world.options.exhibition_difficulties.value,
        )

        main_menu.add_event(f"Win {amount} Exhibition Matches!", "Victory!", location_type=MSMLocation,
                            item_type=items.MSMItem)

        if world.options.boss_locations.value in (BossLocations.option_defeat_behemoth, BossLocations.option_both):
            behemoth_locations = get_location_names_with_ids(["Defeat Behemoth!"])
            behemoth_boss.add_locations(behemoth_locations, MSMLocation)

        if world.options.boss_locations.value in (BossLocations.option_defeat_behemoth_king, BossLocations.option_both):
            behemoth_king_locations = get_location_names_with_ids(["Defeat Behemoth King!"])
            behemoth_king_boss.add_locations(behemoth_king_locations, MSMLocation)

    elif world.options.goal_condition.value == GoalCondition.option_party_palooza:
        main_menu.add_event(f"Win Party Mode!", "Victory!", location_type=MSMLocation,
                            item_type=items.MSMItem)

        if world.options.boss_locations.value in (BossLocations.option_defeat_behemoth, BossLocations.option_both):
            behemoth_locations = get_location_names_with_ids(["Defeat Behemoth!"])
            behemoth_boss.add_locations(behemoth_locations, MSMLocation)

        if world.options.boss_locations.value in (BossLocations.option_defeat_behemoth_king, BossLocations.option_both):
            behemoth_king_locations = get_location_names_with_ids(["Defeat Behemoth King!"])
            behemoth_king_boss.add_locations(behemoth_king_locations, MSMLocation)
