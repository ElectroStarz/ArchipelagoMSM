from __future__ import annotations
from typing import TYPE_CHECKING, NamedTuple, Optional, List

from BaseClasses import Location
from . import items
from .options import GoalCondition


if TYPE_CHECKING:
    from . import MSMWorld

class MSMLocation(Location):
    game = "Mario Sports Mix"

class LocationData(NamedTuple):
    name: str
    code: Optional[int]
    region: Optional[str]


base_loc_id = 0

def get_locations(world: "MSMWorld") -> List[LocationData]:
    location_table: List[LocationData] = []

    # Normal Cup Difficulty locations
    if "Normal" in world.options.cup_difficulty:
        location_table += [
            # Basketball
            LocationData("Basketball: Beat Normal Mushroom Cup Round 1", base_loc_id + 1, "Basketball: Mushroom Cup (Normal)"),
            LocationData("Basketball: Beat Normal Mushroom Cup Round 2", base_loc_id + 2, "Basketball: Mushroom Cup (Normal)"),
            LocationData("Basketball: Beat Normal Mushroom Cup Round 3", base_loc_id + 3, "Basketball: Mushroom Cup (Normal)"),
            LocationData("Basketball: Beat Normal Flower Cup Round 1", base_loc_id + 4, "Basketball: Flower Cup (Normal)"),
            LocationData("Basketball: Beat Normal Flower Cup Round 2", base_loc_id + 5, "Basketball: Flower Cup (Normal)"),
            LocationData("Basketball: Beat Normal Flower Cup Round 3", base_loc_id + 6, "Basketball: Flower Cup (Normal)"),
            LocationData("Basketball: Beat Normal Star Cup Round 1", base_loc_id + 7, "Basketball: Star Cup (Normal)"),
            LocationData("Basketball: Beat Normal Star Cup Round 2", base_loc_id + 8, "Basketball: Star Cup (Normal)"),
            LocationData("Basketball: Beat Normal Star Cup Round 3", base_loc_id + 9, "Basketball: Star Cup (Normal)"),

            # Dodgeball
            LocationData("Dodgeball: Beat Normal Mushroom Cup Round 1", base_loc_id + 10, "Dodgeball: Mushroom Cup (Normal)"),
            LocationData("Dodgeball: Beat Normal Mushroom Cup Round 2", base_loc_id + 11, "Dodgeball: Mushroom Cup (Normal)"),
            LocationData("Dodgeball: Beat Normal Mushroom Cup Round 3", base_loc_id + 12, "Dodgeball: Mushroom Cup (Normal)"),
            LocationData("Dodgeball: Beat Normal Flower Cup Round 1", base_loc_id + 13, "Dodgeball: Flower Cup (Normal)"),
            LocationData("Dodgeball: Beat Normal Flower Cup Round 2", base_loc_id + 14, "Dodgeball: Flower Cup (Normal)"),
            LocationData("Dodgeball: Beat Normal Flower Cup Round 3", base_loc_id + 15, "Dodgeball: Flower Cup (Normal)"),
            LocationData("Dodgeball: Beat Normal Star Cup Round 1", base_loc_id + 16, "Dodgeball: Star Cup (Normal)"),
            LocationData("Dodgeball: Beat Normal Star Cup Round 2", base_loc_id + 17, "Dodgeball: Star Cup (Normal)"),
            LocationData("Dodgeball: Beat Normal Star Cup Round 3", base_loc_id + 18, "Dodgeball: Star Cup (Normal)"),

            # Volleyball
            LocationData("Volleyball: Beat Normal Mushroom Cup Round 1", base_loc_id + 19, "Volleyball: Mushroom Cup (Normal)"),
            LocationData("Volleyball: Beat Normal Mushroom Cup Round 2", base_loc_id + 20, "Volleyball: Mushroom Cup (Normal)"),
            LocationData("Volleyball: Beat Normal Mushroom Cup Round 3", base_loc_id + 21, "Volleyball: Mushroom Cup (Normal)"),
            LocationData("Volleyball: Beat Normal Flower Cup Round 1", base_loc_id + 22, "Volleyball: Flower Cup (Normal)"),
            LocationData("Volleyball: Beat Normal Flower Cup Round 2", base_loc_id + 23, "Volleyball: Flower Cup (Normal)"),
            LocationData("Volleyball: Beat Normal Flower Cup Round 3", base_loc_id + 24, "Volleyball: Flower Cup (Normal)"),
            LocationData("Volleyball: Beat Normal Star Cup Round 1", base_loc_id + 25, "Volleyball: Star Cup (Normal)"),
            LocationData("Volleyball: Beat Normal Star Cup Round 2", base_loc_id + 26, "Volleyball: Star Cup (Normal)"),
            LocationData("Volleyball: Beat Normal Star Cup Round 3", base_loc_id + 27, "Volleyball: Star Cup (Normal)"),

            # Hockey
            LocationData("Hockey: Beat Normal Mushroom Cup Round 1", base_loc_id + 28, "Hockey: Mushroom Cup (Normal)"),
            LocationData("Hockey: Beat Normal Mushroom Cup Round 2", base_loc_id + 29, "Hockey: Mushroom Cup (Normal)"),
            LocationData("Hockey: Beat Normal Mushroom Cup Round 3", base_loc_id + 30, "Hockey: Mushroom Cup (Normal)"),
            LocationData("Hockey: Beat Normal Flower Cup Round 1", base_loc_id + 31, "Hockey: Flower Cup (Normal)"),
            LocationData("Hockey: Beat Normal Flower Cup Round 2", base_loc_id + 32, "Hockey: Flower Cup (Normal)"),
            LocationData("Hockey: Beat Normal Flower Cup Round 3", base_loc_id + 33, "Hockey: Flower Cup (Normal)"),
            LocationData("Hockey: Beat Normal Star Cup Round 1", base_loc_id + 34, "Hockey: Star Cup (Normal)"),
            LocationData("Hockey: Beat Normal Star Cup Round 2", base_loc_id + 35, "Hockey: Star Cup (Normal)"),
            LocationData("Hockey: Beat Normal Star Cup Round 3", base_loc_id + 36, "Hockey: Star Cup (Normal)"),

        ]

    # Hard Cup Difficulty locations
    if "Hard" in world.options.cup_difficulty:
        location_table += [
            # Basketball
            LocationData("Basketball: Beat Hard Mushroom Cup Round 1", base_loc_id + 100, "Basketball: Mushroom Cup (Hard)"),
            LocationData("Basketball: Beat Hard Mushroom Cup Round 2", base_loc_id + 101, "Basketball: Mushroom Cup (Hard)"),
            LocationData("Basketball: Beat Hard Mushroom Cup Round 3", base_loc_id + 102, "Basketball: Mushroom Cup (Hard)"),
            LocationData("Basketball: Beat Hard Flower Cup Round 1", base_loc_id + 103, "Basketball: Flower Cup (Hard)"),
            LocationData("Basketball: Beat Hard Flower Cup Round 2", base_loc_id + 104, "Basketball: Flower Cup (Hard)"),
            LocationData("Basketball: Beat Hard Flower Cup Round 3", base_loc_id + 105, "Basketball: Flower Cup (Hard)"),
            LocationData("Basketball: Beat Hard Star Cup Round 1", base_loc_id + 106, "Basketball: Star Cup (Hard)"),
            LocationData("Basketball: Beat Hard Star Cup Round 2", base_loc_id + 107, "Basketball: Star Cup (Hard)"),
            LocationData("Basketball: Beat Hard Star Cup Round 3", base_loc_id + 108, "Basketball: Star Cup (Hard)"),

            # Dodgeball
            LocationData("Dodgeball: Beat Hard Mushroom Cup Round 1", base_loc_id + 109, "Dodgeball: Mushroom Cup (Hard)"),
            LocationData("Dodgeball: Beat Hard Mushroom Cup Round 2", base_loc_id + 110, "Dodgeball: Mushroom Cup (Hard)"),
            LocationData("Dodgeball: Beat Hard Mushroom Cup Round 3", base_loc_id + 111, "Dodgeball: Mushroom Cup (Hard)"),
            LocationData("Dodgeball: Beat Hard Flower Cup Round 1", base_loc_id + 112, "Dodgeball: Flower Cup (Hard)"),
            LocationData("Dodgeball: Beat Hard Flower Cup Round 2", base_loc_id + 113, "Dodgeball: Flower Cup (Hard)"),
            LocationData("Dodgeball: Beat Hard Flower Cup Round 3", base_loc_id + 114, "Dodgeball: Flower Cup (Hard)"),
            LocationData("Dodgeball: Beat Hard Star Cup Round 1", base_loc_id + 115, "Dodgeball: Star Cup (Hard)"),
            LocationData("Dodgeball: Beat Hard Star Cup Round 2", base_loc_id + 116, "Dodgeball: Star Cup (Hard)"),
            LocationData("Dodgeball: Beat Hard Star Cup Round 3", base_loc_id + 117, "Dodgeball: Star Cup (Hard)"),

            # Volleyball
            LocationData("Volleyball: Beat Hard Mushroom Cup Round 1", base_loc_id + 118, "Volleyball: Mushroom Cup (Hard)"),
            LocationData("Volleyball: Beat Hard Mushroom Cup Round 2", base_loc_id + 119, "Volleyball: Mushroom Cup (Hard)"),
            LocationData("Volleyball: Beat Hard Mushroom Cup Round 3", base_loc_id + 120, "Volleyball: Mushroom Cup (Hard)"),
            LocationData("Volleyball: Beat Hard Flower Cup Round 1", base_loc_id + 121, "Volleyball: Flower Cup (Hard)"),
            LocationData("Volleyball: Beat Hard Flower Cup Round 2", base_loc_id + 122, "Volleyball: Flower Cup (Hard)"),
            LocationData("Volleyball: Beat Hard Flower Cup Round 3", base_loc_id + 123, "Volleyball: Flower Cup (Hard)"),
            LocationData("Volleyball: Beat Hard Star Cup Round 1", base_loc_id + 124, "Volleyball: Star Cup (Hard)"),
            LocationData("Volleyball: Beat Hard Star Cup Round 2", base_loc_id + 125, "Volleyball: Star Cup (Hard)"),
            LocationData("Volleyball: Beat Hard Star Cup Round 3", base_loc_id + 126, "Volleyball: Star Cup (Hard)"),

            # Hockey
            LocationData("Hockey: Beat Hard Mushroom Cup Round 1", base_loc_id + 127, "Hockey: Mushroom Cup (Hard)"),
            LocationData("Hockey: Beat Hard Mushroom Cup Round 2", base_loc_id + 128, "Hockey: Mushroom Cup (Hard)"),
            LocationData("Hockey: Beat Hard Mushroom Cup Round 3", base_loc_id + 129, "Hockey: Mushroom Cup (Hard)"),
            LocationData("Hockey: Beat Hard Flower Cup Round 1", base_loc_id + 130, "Hockey: Flower Cup (Hard)"),
            LocationData("Hockey: Beat Hard Flower Cup Round 2", base_loc_id + 131, "Hockey: Flower Cup (Hard)"),
            LocationData("Hockey: Beat Hard Flower Cup Round 3", base_loc_id + 132, "Hockey: Flower Cup (Hard)"),
            LocationData("Hockey: Beat Hard Star Cup Round 1", base_loc_id + 133, "Hockey: Star Cup (Hard)"),
            LocationData("Hockey: Beat Hard Star Cup Round 2", base_loc_id + 134, "Hockey: Star Cup (Hard)"),
            LocationData("Hockey: Beat Hard Star Cup Round 3", base_loc_id + 135, "Hockey: Star Cup (Hard)"),

        ]

    # Sports Mix locations
    location_table += [
        LocationData("Sports Mix: Beat Mushroom Cup Round 1", base_loc_id + 150, "Sports Mix: Mushroom Cup"),
        LocationData("Sports Mix: Beat Mushroom Cup Round 2", base_loc_id + 151, "Sports Mix: Mushroom Cup"),
        LocationData("Sports Mix: Beat Mushroom Cup Round 3", base_loc_id + 152, "Sports Mix: Mushroom Cup"),
        LocationData("Sports Mix: Beat Flower Cup Round 1", base_loc_id + 153, "Sports Mix: Flower Cup"),
        LocationData("Sports Mix: Beat Flower Cup Round 2", base_loc_id + 154, "Sports Mix: Flower Cup"),
        LocationData("Sports Mix: Beat Flower Cup Round 3", base_loc_id + 155, "Sports Mix: Flower Cup"),
        LocationData("Sports Mix: Beat Star Cup Round 1", base_loc_id + 156, "Sports Mix: Star Cup"),
        LocationData("Sports Mix: Beat Star Cup Round 2", base_loc_id + 157, "Sports Mix: Star Cup"),
        LocationData("Sports Mix: Beat Star Cup Round 3", base_loc_id + 158, "Sports Mix: Star Cup"),
    ]

    if not world or "Easy" in world.options.exhibition_difficulty:
        location_table += [
            # Basketball
            LocationData("Basketball Ex: Beat Mario Stadium (Easy)", base_loc_id + 140, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Koopa Troopa Beach (Easy)", base_loc_id + 141, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat DK Dock (Easy)", base_loc_id + 142, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Luigi's Mansion (Easy)", base_loc_id + 143, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Western Junction (Easy)", base_loc_id + 144, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Daisy Garden (Easy)", base_loc_id + 145, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Bowser Jr. Blvd. (Easy)", base_loc_id + 146, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Bowser's Castle (Easy)", base_loc_id + 147, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Star Ship (Easy)", base_loc_id + 148, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Peach's Castle (Easy)", base_loc_id + 149, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Wario Factory (Easy)", base_loc_id + 150, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Ghoulish Galleon (Easy)", base_loc_id + 151, "Basketball: Exhibition"),

            # Dodgeball
            LocationData("Dodgeball Ex: Beat Mario Stadium (Easy)", base_loc_id + 200, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Koopa Troopa Beach (Easy)", base_loc_id + 201, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Peach's Castle (Easy)", base_loc_id + 202, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat DK Dock (Easy)", base_loc_id + 203, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Toad Park (Easy)", base_loc_id + 204, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Daisy Garden (Easy)", base_loc_id + 205, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Wario Factory (Easy)", base_loc_id + 206, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Bowser's Castle (Easy)", base_loc_id + 207, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Star Ship (Easy)", base_loc_id + 208, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Western Junction (Easy)", base_loc_id + 209, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Waluigi Pinball (Easy)", base_loc_id + 210, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Ghoulish Galleon (Easy)", base_loc_id + 211, "Dodgeball: Exhibition"),

            # Volleyball
            LocationData("Volleyball Ex: Beat Mario Stadium (Easy)", base_loc_id + 260, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Koopa Troopa Beach (Easy)", base_loc_id + 261, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Peach's Castle (Easy)", base_loc_id + 262, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat DK Dock (Easy)", base_loc_id + 263, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Luigi's Mansion (Easy)", base_loc_id + 264, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Western Junction (Easy)", base_loc_id + 265, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Bowser Jr. Blvd. (Easy)", base_loc_id + 266, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Bowser's Castle (Easy)", base_loc_id + 267, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Star Ship (Easy)", base_loc_id + 268, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Wario Factory (Easy)", base_loc_id + 269, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Waluigi Pinball (Easy)", base_loc_id + 270, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Ghoulish Galleon (Easy)", base_loc_id + 271, "Volleyball: Exhibition"),

            # Hockey
            LocationData("Hockey Ex: Beat Mario Stadium (Easy)", base_loc_id + 320, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Toad Park (Easy)", base_loc_id + 321, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Peach's Castle (Easy)", base_loc_id + 322, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Western Junction (Easy)", base_loc_id + 323, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Wario Factory (Easy)", base_loc_id + 324, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Daisy Garden (Easy)", base_loc_id + 325, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Bowser Jr. Blvd (Easy)", base_loc_id + 326, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Waluigi Pinball (Easy)", base_loc_id + 327, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Star Ship (Easy)", base_loc_id + 328, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Koopa Troopa Beach (Easy)", base_loc_id + 329, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Ghoulish Galleon (Easy)", base_loc_id + 330, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Bowser's Castle (Easy)", base_loc_id + 331, "Hockey: Exhibition"),

        ]

    if not world or "Normal" in world.options.exhibition_difficulty:
        location_table += [
            # Basketball
            LocationData("Basketball Ex: Beat Mario Stadium (Normal)", base_loc_id + 152, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Koopa Troopa Beach (Normal)", base_loc_id + 153, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat DK Dock (Normal)", base_loc_id + 154, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Luigi's Mansion (Normal)", base_loc_id + 155, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Western Junction (Normal)", base_loc_id + 156, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Daisy Garden (Normal)", base_loc_id + 157, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Bowser Jr. Blvd. (Normal)", base_loc_id + 158, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Bowser's Castle (Normal)", base_loc_id + 159, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Star Ship (Normal)", base_loc_id + 160, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Peach's Castle (Normal)", base_loc_id + 161, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Wario Factory (Normal)", base_loc_id + 162, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Ghoulish Galleon (Normal)", base_loc_id + 163, "Basketball: Exhibition"),

            # Dodgeball
            LocationData("Dodgeball Ex: Beat Mario Stadium (Normal)", base_loc_id + 212, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Koopa Troopa Beach (Normal)", base_loc_id + 213, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Peach's Castle (Normal)", base_loc_id + 214, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat DK Dock (Normal)", base_loc_id + 215, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Toad Park (Normal)", base_loc_id + 216, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Daisy Garden (Normal)", base_loc_id + 217, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Wario Factory (Normal)", base_loc_id + 218, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Bowser's Castle (Normal)", base_loc_id + 219, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Star Ship (Normal)", base_loc_id + 220, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Western Junction (Normal)", base_loc_id + 221, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Waluigi Pinball (Normal)", base_loc_id + 222, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Ghoulish Galleon (Normal)", base_loc_id + 223, "Dodgeball: Exhibition"),

            # Volleyball
            LocationData("Volleyball Ex: Beat Mario Stadium (Normal)", base_loc_id + 272, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Koopa Troopa Beach (Normal)", base_loc_id + 273, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Peach's Castle (Normal)", base_loc_id + 274, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat DK Dock (Normal)", base_loc_id + 275, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Luigi's Mansion (Normal)", base_loc_id + 276, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Western Junction (Normal)", base_loc_id + 277, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Bowser Jr. Blvd. (Normal)", base_loc_id + 278, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Bowser's Castle (Normal)", base_loc_id + 279, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Star Ship (Normal)", base_loc_id + 280, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Wario Factory (Normal)", base_loc_id + 281, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Waluigi Pinball (Normal)", base_loc_id + 282, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Ghoulish Galleon (Normal)", base_loc_id + 283, "Volleyball: Exhibition"),

            # Hockey
            LocationData("Hockey Ex: Beat Mario Stadium (Normal)", base_loc_id + 332, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Toad Park (Normal)", base_loc_id + 333, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Peach's Castle (Normal)", base_loc_id + 334, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Western Junction (Normal)", base_loc_id + 335, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Wario Factory (Normal)", base_loc_id + 336, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Daisy Garden (Normal)", base_loc_id + 337, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Bowser Jr. Blvd (Normal)", base_loc_id + 338, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Waluigi Pinball (Normal)", base_loc_id + 339, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Star Ship (Normal)", base_loc_id + 340, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Koopa Troopa Beach (Normal)", base_loc_id + 341, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Ghoulish Galleon (Normal)", base_loc_id + 342, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Bowser's Castle (Normal)", base_loc_id + 343, "Hockey: Exhibition"),
        ]

    if not world or "Hard" in world.options.exhibition_difficulty:
        location_table += [
            # Basketball
            LocationData("Basketball Ex: Beat Mario Stadium (Hard)", base_loc_id + 164, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Koopa Troopa Beach (Hard)", base_loc_id + 165, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat DK Dock (Hard)", base_loc_id + 166, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Luigi's Mansion (Hard)", base_loc_id + 167, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Western Junction (Hard)", base_loc_id + 168, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Daisy Garden (Hard)", base_loc_id + 169, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Bowser Jr. Blvd. (Hard)", base_loc_id + 170, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Bowser's Castle (Hard)", base_loc_id + 171, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Star Ship (Hard)", base_loc_id + 172, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Peach's Castle (Hard)", base_loc_id + 173, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Wario Factory (Hard)", base_loc_id + 174, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Ghoulish Galleon (Hard)", base_loc_id + 175, "Basketball: Exhibition"),

            # Dodgeball
            LocationData("Dodgeball Ex: Beat Mario Stadium (Hard)", base_loc_id + 224, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Koopa Troopa Beach (Hard)", base_loc_id + 225, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Peach's Castle (Hard)", base_loc_id + 226, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat DK Dock (Hard)", base_loc_id + 227, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Toad Park (Hard)", base_loc_id + 228, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Daisy Garden (Hard)", base_loc_id + 229, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Wario Factory (Hard)", base_loc_id + 230, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Bowser's Castle (Hard)", base_loc_id + 231, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Star Ship (Hard)", base_loc_id + 232, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Western Junction (Hard)", base_loc_id + 233, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Waluigi Pinball (Hard)", base_loc_id + 234, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Ghoulish Galleon (Hard)", base_loc_id + 235, "Dodgeball: Exhibition"),

            # Volleyball
            LocationData("Volleyball Ex: Beat Mario Stadium (Hard)", base_loc_id + 284, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Koopa Troopa Beach (Hard)", base_loc_id + 285, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Peach's Castle (Hard)", base_loc_id + 286, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat DK Dock (Hard)", base_loc_id + 287, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Luigi's Mansion (Hard)", base_loc_id + 288, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Western Junction (Hard)", base_loc_id + 289, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Bowser Jr. Blvd. (Hard)", base_loc_id + 290, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Bowser's Castle (Hard)", base_loc_id + 291, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Star Ship (Hard)", base_loc_id + 292, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Wario Factory (Hard)", base_loc_id + 293, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Waluigi Pinball (Hard)", base_loc_id + 294, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Ghoulish Galleon (Hard)", base_loc_id + 295, "Volleyball: Exhibition"),

            # Hockey
            LocationData("Hockey Ex: Beat Mario Stadium (Hard)", base_loc_id + 344, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Toad Park (Hard)", base_loc_id + 345, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Peach's Castle (Hard)", base_loc_id + 346, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Western Junction (Hard)", base_loc_id + 347, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Wario Factory (Hard)", base_loc_id + 348, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Daisy Garden (Hard)", base_loc_id + 349, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Bowser Jr. Blvd (Hard)", base_loc_id + 350, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Waluigi Pinball (Hard)", base_loc_id + 351, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Star Ship (Hard)", base_loc_id + 352, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Koopa Troopa Beach (Hard)", base_loc_id + 353, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Ghoulish Galleon (Hard)", base_loc_id + 354, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Bowser's Castle (Hard)", base_loc_id + 355, "Hockey: Exhibition"),
        ]

    if not world or "Expert" in world.options.exhibition_difficulty:
        location_table += [
            # Basketball
            LocationData("Basketball Ex: Beat Mario Stadium (Expert)", base_loc_id + 176, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Koopa Troopa Beach (Expert)", base_loc_id + 177, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat DK Dock (Expert)", base_loc_id + 178, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Luigi's Mansion (Expert)", base_loc_id + 179, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Western Junction (Expert)", base_loc_id + 180, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Daisy Garden (Expert)", base_loc_id + 181, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Bowser Jr. Blvd. (Expert)", base_loc_id + 182, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Bowser's Castle (Expert)", base_loc_id + 183, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Star Ship (Expert)", base_loc_id + 184, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Peach's Castle (Expert)", base_loc_id + 185, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Wario Factory (Expert)", base_loc_id + 186, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Ghoulish Galleon (Expert)", base_loc_id + 187, "Basketball: Exhibition"),

            # Dodgeball
            LocationData("Dodgeball Ex: Beat Mario Stadium (Expert)", base_loc_id + 236, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Koopa Troopa Beach (Expert)", base_loc_id + 237, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Peach's Castle (Expert)", base_loc_id + 238, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat DK Dock (Expert)", base_loc_id + 239, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Toad Park (Expert)", base_loc_id + 240, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Daisy Garden (Expert)", base_loc_id + 241, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Wario Factory (Expert)", base_loc_id + 242, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Bowser's Castle (Expert)", base_loc_id + 243, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Star Ship (Expert)", base_loc_id + 244, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Western Junction (Expert)", base_loc_id + 245, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Waluigi Pinball (Expert)", base_loc_id + 246, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Ghoulish Galleon (Expert)", base_loc_id + 247, "Dodgeball: Exhibition"),

            # Volleyball
            LocationData("Volleyball Ex: Beat Mario Stadium (Expert)", base_loc_id + 296, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Koopa Troopa Beach (Expert)", base_loc_id + 297, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Peach's Castle (Expert)", base_loc_id + 298, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat DK Dock (Expert)", base_loc_id + 299, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Luigi's Mansion (Expert)", base_loc_id + 300, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Western Junction (Expert)", base_loc_id + 301, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Bowser Jr. Blvd. (Expert)", base_loc_id + 302, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Bowser's Castle (Expert)", base_loc_id + 303, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Star Ship (Expert)", base_loc_id + 304, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Wario Factory (Expert)", base_loc_id + 305, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Waluigi Pinball (Expert)", base_loc_id + 306, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Ghoulish Galleon (Expert)", base_loc_id + 307, "Volleyball: Exhibition"),

            # Hockey
            LocationData("Hockey Ex: Beat Mario Stadium (Expert)", base_loc_id + 356, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Toad Park (Expert)", base_loc_id + 357, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Peach's Castle (Expert)", base_loc_id + 358, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Western Junction (Expert)", base_loc_id + 359, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Wario Factory (Expert)", base_loc_id + 360, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Daisy Garden (Expert)", base_loc_id + 361, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Bowser Jr. Blvd (Expert)", base_loc_id + 362, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Waluigi Pinball (Expert)", base_loc_id + 363, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Star Ship (Expert)", base_loc_id + 364, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Koopa Troopa Beach (Expert)", base_loc_id + 365, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Ghoulish Galleon (Expert)", base_loc_id + 366, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Bowser's Castle (Expert)", base_loc_id + 367, "Hockey: Exhibition"),
        ]

    # Create a location check for Behemoth if the goal is to defeat Behemoth King
    if world.options.goal_condition == GoalCondition.option_defeat_behemoth_king:
        location_table += [
            LocationData("Defeated Behemoth!", base_loc_id + 400, "Behemoth Boss Battle"),
        ]
    return location_table


def create_events(world: "MSMWorld") -> None:
    behemoth_boss = world.get_region("Behemoth Boss Battle")
    behemoth_king_boss = world.get_region("Behemoth King Boss Battle")

    if world.options.goal_condition == GoalCondition.option_defeat_behemoth:
        behemoth_boss.add_event(
            "Defeated Behemoth!", "Victory", location_type=MSMLocation, item_type=items.MSMItem
        )

    if world.options.goal_condition == GoalCondition.option_defeat_behemoth_king:
        behemoth_king_boss.add_event(
            "Defeated Behemoth King!", "Victory", location_type=MSMLocation, item_type=items.MSMItem
        )

