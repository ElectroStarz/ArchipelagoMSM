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

courts_list = ["Mario Stadium", "Koopa Troopa Beach", "Toad Park", "DK Dock", "Peach's Castle", "Daisy Garden",
               "Luigi's Mansion", "Wario Factory", "Bowser Jr. Blvd.", "Bowser's Castle", "Waluigi Pinball",
               "Western Junction", "Ghoulish Galleon", "Star Ship"]

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
    "Basketball: Beat Normal Mushroom Cup Round 1":    LocData(base_id + 1, LocGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Mushroom Cup Round 2":    LocData(base_id + 2, LocGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Mushroom Cup Round 3":    LocData(base_id + 3, LocGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Flower Cup Round 1":      LocData(base_id + 4, LocGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Flower Cup Round 2":      LocData(base_id + 5, LocGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Flower Cup Round 3":      LocData(base_id + 6, LocGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Star Cup Round 1":        LocData(base_id + 7, LocGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Star Cup Round 2":        LocData(base_id + 8, LocGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Beat Normal Star Cup Round 3":        LocData(base_id + 9, LocGroup.BASKETBALL_NORMAL_CUPS, LPT.PRIORITY),

    # Dodgeball
    "Dodgeball: Beat Normal Mushroom Cup Round 1":     LocData(base_id + 10, LocGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Mushroom Cup Round 2":     LocData(base_id + 11, LocGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Mushroom Cup Round 3":     LocData(base_id + 12, LocGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Flower Cup Round 1":       LocData(base_id + 13, LocGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Flower Cup Round 2":       LocData(base_id + 14, LocGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Flower Cup Round 3":       LocData(base_id + 15, LocGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Star Cup Round 1":         LocData(base_id + 16, LocGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Star Cup Round 2":         LocData(base_id + 17, LocGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Beat Normal Star Cup Round 3":         LocData(base_id + 18, LocGroup.DODGEBALL_NORMAL_CUPS, LPT.PRIORITY),

    # Volleyball
    "Volleyball: Beat Normal Mushroom Cup Round 1":    LocData(base_id + 19, LocGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Mushroom Cup Round 2":    LocData(base_id + 20, LocGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Mushroom Cup Round 3":    LocData(base_id + 21, LocGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Flower Cup Round 1":      LocData(base_id + 22, LocGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Flower Cup Round 2":      LocData(base_id + 23, LocGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Flower Cup Round 3":      LocData(base_id + 24, LocGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Star Cup Round 1":        LocData(base_id + 25, LocGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Star Cup Round 2":        LocData(base_id + 26, LocGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Beat Normal Star Cup Round 3":        LocData(base_id + 27, LocGroup.VOLLEYBALL_NORMAL_CUPS, LPT.PRIORITY),

    # Hockey
    "Hockey: Beat Normal Mushroom Cup Round 1":        LocData(base_id + 28, LocGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Mushroom Cup Round 2":        LocData(base_id + 29, LocGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Mushroom Cup Round 3":        LocData(base_id + 30, LocGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Flower Cup Round 1":          LocData(base_id + 31, LocGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Flower Cup Round 2":          LocData(base_id + 32, LocGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Flower Cup Round 3":          LocData(base_id + 33, LocGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Star Cup Round 1":            LocData(base_id + 34, LocGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Star Cup Round 2":            LocData(base_id + 35, LocGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Beat Normal Star Cup Round 3":            LocData(base_id + 36, LocGroup.HOCKEY_NORMAL_CUPS, LPT.PRIORITY),

    # --- Hard ---
    # Basketball
    "Basketball: Beat Hard Mushroom Cup Round 1":      LocData(base_id + 37, LocGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Mushroom Cup Round 2":      LocData(base_id + 38, LocGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Mushroom Cup Round 3":      LocData(base_id + 39, LocGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Flower Cup Round 1":        LocData(base_id + 40, LocGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Flower Cup Round 2":        LocData(base_id + 41, LocGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Flower Cup Round 3":        LocData(base_id + 42, LocGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Star Cup Round 1":          LocData(base_id + 43, LocGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Star Cup Round 2":          LocData(base_id + 44, LocGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Beat Hard Star Cup Round 3":          LocData(base_id + 45, LocGroup.BASKETBALL_HARD_CUPS, LPT.PRIORITY),

    # Dodgeball
    "Dodgeball: Beat Hard Mushroom Cup Round 1":       LocData(base_id + 46, LocGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Mushroom Cup Round 2":       LocData(base_id + 47, LocGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Mushroom Cup Round 3":       LocData(base_id + 48, LocGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Flower Cup Round 1":         LocData(base_id + 49, LocGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Flower Cup Round 2":         LocData(base_id + 50, LocGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Flower Cup Round 3":         LocData(base_id + 51, LocGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Star Cup Round 1":           LocData(base_id + 52, LocGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Star Cup Round 2":           LocData(base_id + 53, LocGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Beat Hard Star Cup Round 3":           LocData(base_id + 54, LocGroup.DODGEBALL_HARD_CUPS, LPT.PRIORITY),

    # Volleyball
    "Volleyball: Beat Hard Mushroom Cup Round 1":      LocData(base_id + 55, LocGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Mushroom Cup Round 2":      LocData(base_id + 56, LocGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Mushroom Cup Round 3":      LocData(base_id + 57, LocGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Flower Cup Round 1":        LocData(base_id + 58, LocGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Flower Cup Round 2":        LocData(base_id + 59, LocGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Flower Cup Round 3":        LocData(base_id + 60, LocGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Star Cup Round 1":          LocData(base_id + 61, LocGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Star Cup Round 2":          LocData(base_id + 62, LocGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Beat Hard Star Cup Round 3":          LocData(base_id + 63, LocGroup.VOLLEYBALL_HARD_CUPS, LPT.PRIORITY),

    # Hockey
    "Hockey: Beat Hard Mushroom Cup Round 1":          LocData(base_id + 64, LocGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Mushroom Cup Round 2":          LocData(base_id + 65, LocGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Mushroom Cup Round 3":          LocData(base_id + 66, LocGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Flower Cup Round 1":            LocData(base_id + 67, LocGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Flower Cup Round 2":            LocData(base_id + 68, LocGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Flower Cup Round 3":            LocData(base_id + 69, LocGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Star Cup Round 1":              LocData(base_id + 70, LocGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Star Cup Round 2":              LocData(base_id + 71, LocGroup.HOCKEY_HARD_CUPS),
    "Hockey: Beat Hard Star Cup Round 3":              LocData(base_id + 72, LocGroup.HOCKEY_HARD_CUPS, LPT.PRIORITY),

}

sports_mix_locations: Dict[str, LocData] = {
    "Sports Mix: Beat Mushroom Cup Round 1":           LocData(base_id + 73, LocGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Mushroom Cup Round 2":           LocData(base_id + 74, LocGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Mushroom Cup Round 3":           LocData(base_id + 75, LocGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Flower Cup Round 1":             LocData(base_id + 76, LocGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Flower Cup Round 2":             LocData(base_id + 77, LocGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Flower Cup Round 3":             LocData(base_id + 78, LocGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Star Cup Round 1":               LocData(base_id + 79, LocGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Star Cup Round 2":               LocData(base_id + 80, LocGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Beat Star Cup Round 3":               LocData(base_id + 81, LocGroup.SPORTS_MIX_CUPS),

}

easy_exhibition_locations: Dict[str, LocData] = {
    # Basketball
    "Basketball Ex: Beat Mario Stadium (Easy)":        LocData(base_id + 200, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Koopa Troopa Beach (Easy)":   LocData(base_id + 201, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat DK Dock (Easy)":              LocData(base_id + 202, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Luigi's Mansion (Easy)":      LocData(base_id + 203, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Western Junction (Easy)":     LocData(base_id + 204, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Daisy Garden (Easy)":         LocData(base_id + 205, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Bowser Jr. Blvd. (Easy)":     LocData(base_id + 206, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Bowser's Castle (Easy)":      LocData(base_id + 207, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Star Ship (Easy)":            LocData(base_id + 208, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Peach's Castle (Easy)":       LocData(base_id + 209, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Wario Factory (Easy)":        LocData(base_id + 210, LocGroup.BASKETBALL_EX_EASY),
    "Basketball Ex: Beat Ghoulish Galleon (Easy)":     LocData(base_id + 211, LocGroup.BASKETBALL_EX_EASY),

    # Dodgeball
    "Dodgeball Ex: Beat Mario Stadium (Easy)":         LocData(base_id + 212, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Koopa Troopa Beach (Easy)":    LocData(base_id + 213, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Peach's Castle (Easy)":        LocData(base_id + 214, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat DK Dock (Easy)":               LocData(base_id + 215, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Toad Park (Easy)":             LocData(base_id + 216, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Daisy Garden (Easy)":          LocData(base_id + 217, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Wario Factory (Easy)":         LocData(base_id + 218, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Bowser's Castle (Easy)":       LocData(base_id + 219, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Star Ship (Easy)":             LocData(base_id + 220, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Western Junction (Easy)":      LocData(base_id + 221, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Waluigi Pinball (Easy)":       LocData(base_id + 222, LocGroup.DODGEBALL_EX_EASY),
    "Dodgeball Ex: Beat Ghoulish Galleon (Easy)":      LocData(base_id + 223, LocGroup.DODGEBALL_EX_EASY),

    # Volleyball
    "Volleyball Ex: Beat Mario Stadium (Easy)":        LocData(base_id + 224, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Koopa Troopa Beach (Easy)":   LocData(base_id + 225, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Peach's Castle (Easy)":       LocData(base_id + 226, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat DK Dock (Easy)":              LocData(base_id + 227, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Luigi's Mansion (Easy)":      LocData(base_id + 228, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Western Junction (Easy)":     LocData(base_id + 229, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Bowser Jr. Blvd. (Easy)":     LocData(base_id + 230, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Bowser's Castle (Easy)":      LocData(base_id + 231, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Star Ship (Easy)":            LocData(base_id + 232, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Wario Factory (Easy)":        LocData(base_id + 233, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Waluigi Pinball (Easy)":      LocData(base_id + 234, LocGroup.VOLLEYBALL_EX_EASY),
    "Volleyball Ex: Beat Ghoulish Galleon (Easy)":     LocData(base_id + 235, LocGroup.VOLLEYBALL_EX_EASY),

    # Hockey
    "Hockey Ex: Beat Mario Stadium (Easy)":            LocData(base_id + 236, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Toad Park (Easy)":                LocData(base_id + 237, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Peach's Castle (Easy)":           LocData(base_id + 238, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Western Junction (Easy)":         LocData(base_id + 239, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Wario Factory (Easy)":            LocData(base_id + 240, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Daisy Garden (Easy)":             LocData(base_id + 241, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Bowser Jr. Blvd. (Easy)":         LocData(base_id + 242, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Waluigi Pinball (Easy)":          LocData(base_id + 243, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Star Ship (Easy)":                LocData(base_id + 244, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Koopa Troopa Beach (Easy)":       LocData(base_id + 245, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Ghoulish Galleon (Easy)":         LocData(base_id + 246, LocGroup.HOCKEY_EX_EASY),
    "Hockey Ex: Beat Bowser's Castle (Easy)":          LocData(base_id + 247, LocGroup.HOCKEY_EX_EASY),
}

normal_exhibition_locations: Dict[str, LocData] = {
    # Basketball
    "Basketball Ex: Beat Mario Stadium (Normal)":      LocData(base_id + 300, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Koopa Troopa Beach (Normal)": LocData(base_id + 301, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat DK Dock (Normal)":            LocData(base_id + 302, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Luigi's Mansion (Normal)":    LocData(base_id + 303, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Western Junction (Normal)":   LocData(base_id + 304, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Daisy Garden (Normal)":       LocData(base_id + 305, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Bowser Jr. Blvd. (Normal)":   LocData(base_id + 306, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Bowser's Castle (Normal)":    LocData(base_id + 307, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Star Ship (Normal)":          LocData(base_id + 308, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Peach's Castle (Normal)":     LocData(base_id + 309, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Wario Factory (Normal)":      LocData(base_id + 310, LocGroup.BASKETBALL_EX_NORMAL),
    "Basketball Ex: Beat Ghoulish Galleon (Normal)":   LocData(base_id + 311, LocGroup.BASKETBALL_EX_NORMAL),

    # Dodgeball
    "Dodgeball Ex: Beat Mario Stadium (Normal)":       LocData(base_id + 312, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Koopa Troopa Beach (Normal)":  LocData(base_id + 313, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Peach's Castle (Normal)":      LocData(base_id + 314, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat DK Dock (Normal)":             LocData(base_id + 315, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Toad Park (Normal)":           LocData(base_id + 316, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Daisy Garden (Normal)":        LocData(base_id + 317, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Wario Factory (Normal)":       LocData(base_id + 318, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Bowser's Castle (Normal)":     LocData(base_id + 319, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Star Ship (Normal)":           LocData(base_id + 320, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Western Junction (Normal)":    LocData(base_id + 321, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Waluigi Pinball (Normal)":     LocData(base_id + 322, LocGroup.DODGEBALL_EX_NORMAL),
    "Dodgeball Ex: Beat Ghoulish Galleon (Normal)":    LocData(base_id + 323, LocGroup.DODGEBALL_EX_NORMAL),

    # Volleyball
    "Volleyball Ex: Beat Mario Stadium (Normal)":      LocData(base_id + 324, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Koopa Troopa Beach (Normal)": LocData(base_id + 325, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Peach's Castle (Normal)":     LocData(base_id + 326, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat DK Dock (Normal)":            LocData(base_id + 327, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Luigi's Mansion (Normal)":    LocData(base_id + 328, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Western Junction (Normal)":   LocData(base_id + 329, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Bowser Jr. Blvd. (Normal)":   LocData(base_id + 330, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Bowser's Castle (Normal)":    LocData(base_id + 331, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Star Ship (Normal)":          LocData(base_id + 332, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Wario Factory (Normal)":      LocData(base_id + 333, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Waluigi Pinball (Normal)":    LocData(base_id + 334, LocGroup.VOLLEYBALL_EX_NORMAL),
    "Volleyball Ex: Beat Ghoulish Galleon (Normal)":   LocData(base_id + 335, LocGroup.VOLLEYBALL_EX_NORMAL),

    # Hockey
    "Hockey Ex: Beat Mario Stadium (Normal)":          LocData(base_id + 336, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Toad Park (Normal)":              LocData(base_id + 337, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Peach's Castle (Normal)":         LocData(base_id + 338, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Western Junction (Normal)":       LocData(base_id + 339, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Wario Factory (Normal)":          LocData(base_id + 340, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Daisy Garden (Normal)":           LocData(base_id + 341, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Bowser Jr. Blvd. (Normal)":       LocData(base_id + 342, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Waluigi Pinball (Normal)":        LocData(base_id + 343, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Star Ship (Normal)":              LocData(base_id + 344, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Koopa Troopa Beach (Normal)":     LocData(base_id + 345, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Ghoulish Galleon (Normal)":       LocData(base_id + 346, LocGroup.HOCKEY_EX_NORMAL),
    "Hockey Ex: Beat Bowser's Castle (Normal)":        LocData(base_id + 347, LocGroup.HOCKEY_EX_NORMAL),
}

hard_exhibition_locations: Dict[str, LocData] = {
    # Basketball
    "Basketball Ex: Beat Mario Stadium (Hard)":        LocData(base_id + 400, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Koopa Troopa Beach (Hard)":   LocData(base_id + 401, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat DK Dock (Hard)":              LocData(base_id + 402, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Luigi's Mansion (Hard)":      LocData(base_id + 403, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Western Junction (Hard)":     LocData(base_id + 404, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Daisy Garden (Hard)":         LocData(base_id + 405, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Bowser Jr. Blvd. (Hard)":     LocData(base_id + 406, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Bowser's Castle (Hard)":      LocData(base_id + 407, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Star Ship (Hard)":            LocData(base_id + 408, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Peach's Castle (Hard)":       LocData(base_id + 409, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Wario Factory (Hard)":        LocData(base_id + 410, LocGroup.BASKETBALL_EX_HARD),
    "Basketball Ex: Beat Ghoulish Galleon (Hard)":     LocData(base_id + 411, LocGroup.BASKETBALL_EX_HARD),

    # Dodgeball
    "Dodgeball Ex: Beat Mario Stadium (Hard)":         LocData(base_id + 412, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Koopa Troopa Beach (Hard)":    LocData(base_id + 413, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Peach's Castle (Hard)":        LocData(base_id + 414, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat DK Dock (Hard)":               LocData(base_id + 415, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Toad Park (Hard)":             LocData(base_id + 416, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Daisy Garden (Hard)":          LocData(base_id + 417, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Wario Factory (Hard)":         LocData(base_id + 418, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Bowser's Castle (Hard)":       LocData(base_id + 419, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Star Ship (Hard)":             LocData(base_id + 420, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Western Junction (Hard)":      LocData(base_id + 421, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Waluigi Pinball (Hard)":       LocData(base_id + 422, LocGroup.DODGEBALL_EX_HARD),
    "Dodgeball Ex: Beat Ghoulish Galleon (Hard)":      LocData(base_id + 423, LocGroup.DODGEBALL_EX_HARD),

    # Volleyball
    "Volleyball Ex: Beat Mario Stadium (Hard)":        LocData(base_id + 424, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Koopa Troopa Beach (Hard)":   LocData(base_id + 425, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Peach's Castle (Hard)":       LocData(base_id + 426, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat DK Dock (Hard)":              LocData(base_id + 427, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Luigi's Mansion (Hard)":      LocData(base_id + 428, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Western Junction (Hard)":     LocData(base_id + 429, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Bowser Jr. Blvd. (Hard)":     LocData(base_id + 430, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Bowser's Castle (Hard)":      LocData(base_id + 431, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Star Ship (Hard)":            LocData(base_id + 432, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Wario Factory (Hard)":        LocData(base_id + 433, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Waluigi Pinball (Hard)":      LocData(base_id + 434, LocGroup.VOLLEYBALL_EX_HARD),
    "Volleyball Ex: Beat Ghoulish Galleon (Hard)":     LocData(base_id + 435, LocGroup.VOLLEYBALL_EX_HARD),

    # Hockey
    "Hockey Ex: Beat Mario Stadium (Hard)":            LocData(base_id + 436, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Toad Park (Hard)":                LocData(base_id + 437, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Peach's Castle (Hard)":           LocData(base_id + 438, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Western Junction (Hard)":         LocData(base_id + 439, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Wario Factory (Hard)":            LocData(base_id + 440, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Daisy Garden (Hard)":             LocData(base_id + 441, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Bowser Jr. Blvd. (Hard)":         LocData(base_id + 442, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Waluigi Pinball (Hard)":          LocData(base_id + 443, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Star Ship (Hard)":                LocData(base_id + 444, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Koopa Troopa Beach (Hard)":       LocData(base_id + 445, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Ghoulish Galleon (Hard)":         LocData(base_id + 446, LocGroup.HOCKEY_EX_HARD),
    "Hockey Ex: Beat Bowser's Castle (Hard)":          LocData(base_id + 447, LocGroup.HOCKEY_EX_HARD),
}

expert_exhibition_locations: Dict[str, LocData] = {
    # Basketball
    "Basketball Ex: Beat Mario Stadium (Expert)":      LocData(base_id + 500, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Koopa Troopa Beach (Expert)": LocData(base_id + 501, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat DK Dock (Expert)":            LocData(base_id + 502, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Luigi's Mansion (Expert)":    LocData(base_id + 503, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Western Junction (Expert)":   LocData(base_id + 504, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Daisy Garden (Expert)":       LocData(base_id + 505, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Bowser Jr. Blvd. (Expert)":   LocData(base_id + 506, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Bowser's Castle (Expert)":    LocData(base_id + 507, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Star Ship (Expert)":          LocData(base_id + 508, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Peach's Castle (Expert)":     LocData(base_id + 509, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Wario Factory (Expert)":      LocData(base_id + 510, LocGroup.BASKETBALL_EX_EXPERT),
    "Basketball Ex: Beat Ghoulish Galleon (Expert)":   LocData(base_id + 511, LocGroup.BASKETBALL_EX_EXPERT),

    # Dodgeball
    "Dodgeball Ex: Beat Mario Stadium (Expert)":       LocData(base_id + 512, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Koopa Troopa Beach (Expert)":  LocData(base_id + 513, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Peach's Castle (Expert)":      LocData(base_id + 514, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat DK Dock (Expert)":             LocData(base_id + 515, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Toad Park (Expert)":           LocData(base_id + 516, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Daisy Garden (Expert)":        LocData(base_id + 517, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Wario Factory (Expert)":       LocData(base_id + 518, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Bowser's Castle (Expert)":     LocData(base_id + 519, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Star Ship (Expert)":           LocData(base_id + 520, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Western Junction (Expert)":    LocData(base_id + 521, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Waluigi Pinball (Expert)":     LocData(base_id + 522, LocGroup.DODGEBALL_EX_EXPERT),
    "Dodgeball Ex: Beat Ghoulish Galleon (Expert)":    LocData(base_id + 523, LocGroup.DODGEBALL_EX_EXPERT),

    # Volleyball
    "Volleyball Ex: Beat Mario Stadium (Expert)":      LocData(base_id + 524, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Koopa Troopa Beach (Expert)": LocData(base_id + 525, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Peach's Castle (Expert)":     LocData(base_id + 526, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat DK Dock (Expert)":            LocData(base_id + 527, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Luigi's Mansion (Expert)":    LocData(base_id + 528, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Western Junction (Expert)":   LocData(base_id + 529, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Bowser Jr. Blvd. (Expert)":   LocData(base_id + 530, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Bowser's Castle (Expert)":    LocData(base_id + 531, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Star Ship (Expert)":          LocData(base_id + 532, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Wario Factory (Expert)":      LocData(base_id + 533, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Waluigi Pinball (Expert)":    LocData(base_id + 534, LocGroup.VOLLEYBALL_EX_EXPERT),
    "Volleyball Ex: Beat Ghoulish Galleon (Expert)":   LocData(base_id + 535, LocGroup.VOLLEYBALL_EX_EXPERT),

    # Hockey
    "Hockey Ex: Beat Mario Stadium (Expert)":          LocData(base_id + 536, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Toad Park (Expert)":              LocData(base_id + 537, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Peach's Castle (Expert)":         LocData(base_id + 538, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Western Junction (Expert)":       LocData(base_id + 539, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Wario Factory (Expert)":          LocData(base_id + 540, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Daisy Garden (Expert)":           LocData(base_id + 541, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Bowser Jr. Blvd. (Expert)":       LocData(base_id + 542, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Waluigi Pinball (Expert)":        LocData(base_id + 543, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Star Ship (Expert)":              LocData(base_id + 544, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Koopa Troopa Beach (Expert)":     LocData(base_id + 545, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Ghoulish Galleon (Expert)":       LocData(base_id + 546, LocGroup.HOCKEY_EX_EXPERT),
    "Hockey Ex: Beat Bowser's Castle (Expert)":        LocData(base_id + 547, LocGroup.HOCKEY_EX_EXPERT),
}

global_exhibition_locations: Dict[str, LocData] = {
    # Easy
    "Exhibition: Beat Mario Stadium (Easy)":           LocData(base_id + 600, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Koopa Troopa Beach (Easy)":      LocData(base_id + 601, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Peach's Castle (Easy)":          LocData(base_id + 602, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat DK Dock (Easy)":                 LocData(base_id + 603, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Toad Park (Easy)":               LocData(base_id + 604, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Luigi's Mansion (Easy)":         LocData(base_id + 605, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Western Junction (Easy)":        LocData(base_id + 606, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Daisy Garden (Easy)":            LocData(base_id + 607, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Wario Factory (Easy)":           LocData(base_id + 608, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Bowser Jr. Blvd. (Easy)":        LocData(base_id + 609, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Bowser's Castle (Easy)":         LocData(base_id + 610, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Waluigi Pinball (Easy)":         LocData(base_id + 611, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Ghoulish Galleon (Easy)":        LocData(base_id + 612, LocGroup.EXHIBITION_EASY),
    "Exhibition: Beat Star Ship (Easy)":               LocData(base_id + 613, LocGroup.EXHIBITION_EASY),

    # Normal
    "Exhibition: Beat Mario Stadium (Normal)":         LocData(base_id + 614, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Koopa Troopa Beach (Normal)":    LocData(base_id + 615, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Peach's Castle (Normal)":        LocData(base_id + 616, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat DK Dock (Normal)":               LocData(base_id + 617, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Toad Park (Normal)":             LocData(base_id + 618, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Luigi's Mansion (Normal)":       LocData(base_id + 619, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Western Junction (Normal)":      LocData(base_id + 620, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Daisy Garden (Normal)":          LocData(base_id + 621, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Wario Factory (Normal)":         LocData(base_id + 622, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Bowser Jr. Blvd. (Normal)":      LocData(base_id + 623, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Bowser's Castle (Normal)":       LocData(base_id + 624, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Waluigi Pinball (Normal)":       LocData(base_id + 625, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Ghoulish Galleon (Normal)":      LocData(base_id + 626, LocGroup.EXHIBITION_NORMAL),
    "Exhibition: Beat Star Ship (Normal)":             LocData(base_id + 627, LocGroup.EXHIBITION_NORMAL),

    # Hard
    "Exhibition: Beat Mario Stadium (Hard)":           LocData(base_id + 628, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Koopa Troopa Beach (Hard)":      LocData(base_id + 629, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Peach's Castle (Hard)":          LocData(base_id + 630, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat DK Dock (Hard)":                 LocData(base_id + 631, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Toad Park (Hard)":               LocData(base_id + 632, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Luigi's Mansion (Hard)":         LocData(base_id + 633, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Western Junction (Hard)":        LocData(base_id + 634, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Daisy Garden (Hard)":            LocData(base_id + 635, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Wario Factory (Hard)":           LocData(base_id + 636, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Bowser Jr. Blvd. (Hard)":        LocData(base_id + 637, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Bowser's Castle (Hard)":         LocData(base_id + 638, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Waluigi Pinball (Hard)":         LocData(base_id + 639, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Ghoulish Galleon (Hard)":        LocData(base_id + 640, LocGroup.EXHIBITION_HARD),
    "Exhibition: Beat Star Ship (Hard)":               LocData(base_id + 641, LocGroup.EXHIBITION_HARD),

    # Expert
    "Exhibition: Beat Mario Stadium (Expert)":         LocData(base_id + 642, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Koopa Troopa Beach (Expert)":    LocData(base_id + 643, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Peach's Castle (Expert)":        LocData(base_id + 644, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat DK Dock (Expert)":               LocData(base_id + 645, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Toad Park (Expert)":             LocData(base_id + 646, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Luigi's Mansion (Expert)":       LocData(base_id + 647, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Western Junction (Expert)":      LocData(base_id + 648, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Daisy Garden (Expert)":          LocData(base_id + 649, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Wario Factory (Expert)":         LocData(base_id + 650, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Bowser Jr. Blvd. (Expert)":      LocData(base_id + 651, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Bowser's Castle (Expert)":       LocData(base_id + 652, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Waluigi Pinball (Expert)":       LocData(base_id + 653, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Ghoulish Galleon (Expert)":      LocData(base_id + 654, LocGroup.EXHIBITION_EXPERT),
    "Exhibition: Beat Star Ship (Expert)":             LocData(base_id + 655, LocGroup.EXHIBITION_EXPERT),
}

# === Party Game Locations ===

feed_petey_locations: Dict[str, LocData] = {
    "Feed Petey: Beat Daisy Garden (Apple)":           LocData(base_id + 800, LocGroup.FEED_PETEY),
    "Feed Petey: Beat Daisy Garden (Watermelon)":      LocData(base_id + 801, LocGroup.FEED_PETEY),
    "Feed Petey: Beat DK Dock (Apple)":                LocData(base_id + 802, LocGroup.FEED_PETEY),
    "Feed Petey: Beat DK Dock (Watermelon)":           LocData(base_id + 803, LocGroup.FEED_PETEY),
    "Feed Petey: Beat Wario Factory (Apple)":          LocData(base_id + 804, LocGroup.FEED_PETEY),
    "Feed Petey: Beat Wario Factory (Watermelon)":     LocData(base_id + 805, LocGroup.FEED_PETEY),
}

harmony_hustle_locations: Dict[str, LocData] = {
    "Harmony Hustle: Beat Classic Ocean":              LocData(base_id + 806, LocGroup.HARMONY_HUSTLE),
    "Harmony Hustle: Beat Chocobo Rhythm":             LocData(base_id + 807, LocGroup.HARMONY_HUSTLE),
    "Harmony Hustle: Beat Mario Athletic":             LocData(base_id + 808, LocGroup.HARMONY_HUSTLE),
    "Harmony Hustle: Beat Mushroom Mix Medley":        LocData(base_id + 809, LocGroup.HARMONY_HUSTLE),

    "Harmony Hustle: Beat Bloocheep Ocean":            LocData(base_id + 810, LocGroup.HARMONY_HUSTLE),
    "Harmony Hustle: Beat Chocobo Pop":                LocData(base_id + 811, LocGroup.HARMONY_HUSTLE),
    "Harmony Hustle: Beat Punk Athletic":              LocData(base_id + 812, LocGroup.HARMONY_HUSTLE),
    "Harmony Hustle: Beat Blossom Mix Medley":         LocData(base_id + 813, LocGroup.HARMONY_HUSTLE),

    "Harmony Hustle: Beat Punk Ocean":                 LocData(base_id + 814, LocGroup.HARMONY_HUSTLE),
    "Harmony Hustle: Beat Chocobo Beat":               LocData(base_id + 815, LocGroup.HARMONY_HUSTLE),
    "Harmony Hustle: Beat Island Athletic":            LocData(base_id + 816, LocGroup.HARMONY_HUSTLE),
    "Harmony Hustle: Beat Star Mix Medley":            LocData(base_id + 817, LocGroup.HARMONY_HUSTLE),
}

bob_omb_dodge_locations: Dict[str, LocData] = {
    "Bob-omb Dodge: Beat Mario Stadium (Bob-omb)":     LocData(base_id + 818, LocGroup.BOB_OMB_DODGE),
    "Bob-omb Dodge: Beat Mario Stadium (Cannon)":      LocData(base_id + 819, LocGroup.BOB_OMB_DODGE),
    "Bob-omb Dodge: Beat Ghoulish Galleon (Bob-omb)":  LocData(base_id + 820, LocGroup.BOB_OMB_DODGE),
    "Bob-omb Dodge: Beat Ghoulish Galleon (Cannon)":   LocData(base_id + 821, LocGroup.BOB_OMB_DODGE),
    "Bob-omb Dodge: Beat Western Junction (Bob-omb)":  LocData(base_id + 822, LocGroup.BOB_OMB_DODGE),
    "Bob-omb Dodge: Beat Western Junction (Cannon)":   LocData(base_id + 823, LocGroup.BOB_OMB_DODGE),
}

smash_skate_locations: Dict[str, LocData] = {
    "Smash Skate: Beat Sherbet Sea (Hockey Stick)":    LocData(base_id + 824, LocGroup.SMASH_SKATE),
    "Smash Skate: Beat Sherbet Sea (Hockey Skate)":    LocData(base_id + 825, LocGroup.SMASH_SKATE),
    "Smash Skate: Beat Rowdy Raft (Hockey Stick)":     LocData(base_id + 826, LocGroup.SMASH_SKATE),
    "Smash Skate: Beat Rowdy Raft (Hockey Skate)":     LocData(base_id + 827, LocGroup.SMASH_SKATE),
    "Smash Skate: Beat Fire Mountain (Hockey Stick)":  LocData(base_id + 828, LocGroup.SMASH_SKATE),
    "Smash Skate: Beat Fire Mountain (Hockey Skate)":  LocData(base_id + 829, LocGroup.SMASH_SKATE),
}

special_sanity_locations: Dict[str, LocData] = {
    "Use Mario's Special":                             LocData(base_id + 5000, LocGroup.SPECIAL_SANITY),
    "Use Luigi's Special":                             LocData(base_id + 5001, LocGroup.SPECIAL_SANITY),
    "Use Peach's Special":                             LocData(base_id + 5002, LocGroup.SPECIAL_SANITY),
    "Use Daisy's Special":                             LocData(base_id + 5003, LocGroup.SPECIAL_SANITY),
    "Use Yoshi's Special":                             LocData(base_id + 5004, LocGroup.SPECIAL_SANITY),
    "Use Wario's Special":                             LocData(base_id + 5005, LocGroup.SPECIAL_SANITY),
    "Use Waluigi's Special":                           LocData(base_id + 5006, LocGroup.SPECIAL_SANITY),
    "Use Donkey Kong's Special":                       LocData(base_id + 5007, LocGroup.SPECIAL_SANITY),
    "Use Diddy Kong's Special":                        LocData(base_id + 5008, LocGroup.SPECIAL_SANITY),
    "Use Toad's Special":                              LocData(base_id + 5009, LocGroup.SPECIAL_SANITY),
    "Use Bowser's Special":                            LocData(base_id + 5010, LocGroup.SPECIAL_SANITY),
    "Use Bowser Jr's Special":                         LocData(base_id + 5011, LocGroup.SPECIAL_SANITY),
    "Use Moogle's Special":                            LocData(base_id + 5012, LocGroup.SPECIAL_SANITY),
    "Use Cactuar's Special":                           LocData(base_id + 5013, LocGroup.SPECIAL_SANITY),
    "Use Ninja's Special":                             LocData(base_id + 5014, LocGroup.SPECIAL_SANITY),
    "Use White Mage's Special":                        LocData(base_id + 5015, LocGroup.SPECIAL_SANITY),
    "Use Slime's Special":                             LocData(base_id + 5016, LocGroup.SPECIAL_SANITY),
    "Use Black Mage's Special":                        LocData(base_id + 5017, LocGroup.SPECIAL_SANITY),
    "Use Mii (Male)'s Special":                        LocData(base_id + 5018, LocGroup.SPECIAL_SANITY),
    "Use Mii (Female)'s Special":                      LocData(base_id + 5019, LocGroup.SPECIAL_SANITY),
}

character_sanity_locations: Dict[str, LocData] = {
    "Win as Mario":                                    LocData(base_id + 6001, LocGroup.CHARACTER_SANITY),
    "Win as Luigi":                                    LocData(base_id + 6002, LocGroup.CHARACTER_SANITY),
    "Win as Peach":                                    LocData(base_id + 6003, LocGroup.CHARACTER_SANITY),
    "Win as Daisy":                                    LocData(base_id + 6004, LocGroup.CHARACTER_SANITY),
    "Win as Yoshi":                                    LocData(base_id + 6005, LocGroup.CHARACTER_SANITY),
    "Win as Wario":                                    LocData(base_id + 6006, LocGroup.CHARACTER_SANITY),
    "Win as Waluigi":                                  LocData(base_id + 6007, LocGroup.CHARACTER_SANITY),
    "Win as Donkey Kong":                              LocData(base_id + 6008, LocGroup.CHARACTER_SANITY),
    "Win as Diddy Kong":                               LocData(base_id + 6009, LocGroup.CHARACTER_SANITY),
    "Win as Toad":                                     LocData(base_id + 6010, LocGroup.CHARACTER_SANITY),
    "Win as Bowser":                                   LocData(base_id + 6011, LocGroup.CHARACTER_SANITY),
    "Win as Bowser Jr":                                LocData(base_id + 6012, LocGroup.CHARACTER_SANITY),
    "Win as Moogle":                                   LocData(base_id + 6013, LocGroup.CHARACTER_SANITY),
    "Win as Cactuar":                                  LocData(base_id + 6014, LocGroup.CHARACTER_SANITY),
    "Win as Ninja":                                    LocData(base_id + 6015, LocGroup.CHARACTER_SANITY),
    "Win as White Mage":                               LocData(base_id + 6016, LocGroup.CHARACTER_SANITY),
    "Win as Slime":                                    LocData(base_id + 6017, LocGroup.CHARACTER_SANITY),
    "Win as Black Mage":                               LocData(base_id + 6018, LocGroup.CHARACTER_SANITY),
    "Win as Mii (Male)":                               LocData(base_id + 6019, LocGroup.CHARACTER_SANITY),
    "Win as Mii (Female)":                             LocData(base_id + 6020, LocGroup.CHARACTER_SANITY),
}

costume_char_sanity_locations: Dict[str, LocData] = {
    "Win as Pink Yoshi":                               LocData(base_id + 6021, LocGroup.COSTUME_SANITY),
    "Win as Light Blue Yoshi":                         LocData(base_id + 6022, LocGroup.COSTUME_SANITY),
    "Win as Yellow Yoshi":                             LocData(base_id + 6023, LocGroup.COSTUME_SANITY),
    "Win as Blue Toad":                                LocData(base_id + 6024, LocGroup.COSTUME_SANITY),
    "Win as Green Toad":                               LocData(base_id + 6025, LocGroup.COSTUME_SANITY),
    "Win as Yellow Toad":                              LocData(base_id + 6026, LocGroup.COSTUME_SANITY),
    "Win as She-Slime":                                LocData(base_id + 6027, LocGroup.COSTUME_SANITY),
    "Win as Metal Slime":                              LocData(base_id + 6028, LocGroup.COSTUME_SANITY),
    "Win as Tennis-wear Peach":                        LocData(base_id + 6029, LocGroup.COSTUME_SANITY),
    "Win as Tennis-wear Daisy":                        LocData(base_id + 6030, LocGroup.COSTUME_SANITY),
    "Win as Shadow White Ninja":                       LocData(base_id + 6031, LocGroup.COSTUME_SANITY),
    "Win as Pure White - White Mage":                  LocData(base_id + 6032, LocGroup.COSTUME_SANITY),
    "Win as Magic Red Black Mage":                     LocData(base_id + 6033, LocGroup.COSTUME_SANITY),
}

court_sanity_locations: Dict[str, LocData] = {
    "Win on Mario Stadium":                            LocData(base_id + 7000, LocGroup.COURT_SANITY),
    "Win on Koopa Troopa Beach":                       LocData(base_id + 7001, LocGroup.COURT_SANITY),
    "Win on Peach's Castle":                           LocData(base_id + 7002, LocGroup.COURT_SANITY),
    "Win on Toad Park":                                LocData(base_id + 7003, LocGroup.COURT_SANITY),
    "Win on DK Dock":                                  LocData(base_id + 7004, LocGroup.COURT_SANITY),
    "Win on Luigi's Mansion":                          LocData(base_id + 7005, LocGroup.COURT_SANITY),
    "Win on Daisy Garden":                             LocData(base_id + 7006, LocGroup.COURT_SANITY),
    "Win on Wario Factory":                            LocData(base_id + 7007, LocGroup.COURT_SANITY),
    "Win on Bowser Jr. Blvd.":                         LocData(base_id + 7008, LocGroup.COURT_SANITY),
    "Win on Bowser's Castle":                          LocData(base_id + 7009, LocGroup.COURT_SANITY),
    "Win on Waluigi Pinball":                          LocData(base_id + 7010, LocGroup.COURT_SANITY),
    "Win on Ghoulish Galleon":                         LocData(base_id + 7011, LocGroup.COURT_SANITY),
    "Win on Star Ship":                                LocData(base_id + 7012, LocGroup.COURT_SANITY),
    "Win on Western Junction":                         LocData(base_id + 7013, LocGroup.COURT_SANITY),

    "Win on Sherbet Sea":                              LocData(base_id + 7014, LocGroup.COURT_SANITY),
    "Win on Fire Mountain":                            LocData(base_id + 7015, LocGroup.COURT_SANITY),
    "Win on Rowdy Raft":                               LocData(base_id + 7016, LocGroup.COURT_SANITY),

    "Win on Classic Ocean":                            LocData(base_id + 7017, LocGroup.COURT_SANITY),
    "Win on Chocobo Rhythm":                           LocData(base_id + 7018, LocGroup.COURT_SANITY),
    "Win on Mario Athletic":                           LocData(base_id + 7019, LocGroup.COURT_SANITY),
    "Win on Bloocheep Ocean":                          LocData(base_id + 7020, LocGroup.COURT_SANITY),
    "Win on Chocobo Pop":                              LocData(base_id + 7021, LocGroup.COURT_SANITY),
    "Win on Punk Athletic":                            LocData(base_id + 7022, LocGroup.COURT_SANITY),
    "Win on Punk Ocean":                               LocData(base_id + 7023, LocGroup.COURT_SANITY),
    "Win on Chocobo Beat":                             LocData(base_id + 7024, LocGroup.COURT_SANITY),
    "Win on Island Athletic":                          LocData(base_id + 7025, LocGroup.COURT_SANITY),
    "Win on Mushroom Mix Medley":                      LocData(base_id + 7026, LocGroup.COURT_SANITY, LPT.PRIORITY),
    "Win on Blossom Mix Medley":                       LocData(base_id + 7027, LocGroup.COURT_SANITY, LPT.PRIORITY),
    "Win on Star Mix Medley":                          LocData(base_id + 7028, LocGroup.COURT_SANITY, LPT.PRIORITY),
}

boss_locations: Dict[str, LocData] = {
    "Defeat Behemoth!":                                LocData(base_id + 20000, LocGroup.BOSS_LOCATIONS, LPT.PRIORITY),
    "Defeat Behemoth King!":                           LocData(base_id + 20001, LocGroup.BOSS_LOCATIONS, LPT.PRIORITY),
}

location_table: Dict[str, LocData] = {
    **cup_round_locations,
    **sports_mix_locations,
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
    sports_mix_flower = world.get_region("Sports Mix: Flower Cup")
    sports_mix_star = world.get_region("Sports Mix: Star Cup")
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
    if world.options.character_sanity.value in (CharacterSanity.option_characters, CharacterSanity.option_characters_and_costumes):
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
        main_menu.add_locations(special_locations, MSMLocation)

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