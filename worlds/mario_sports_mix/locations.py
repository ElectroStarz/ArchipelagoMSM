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

def create_all_locations(world: "MSMWorld") -> None:
    get_locations(world)
    create_events(world)


base_loc_id = 0

def get_locations(world: Optional["MSMWorld"]) -> List[LocationData]:
    location_table: List[LocationData] = []

    if not world or "Normal" in world.options.cup_difficulty:
        location_table += [
            # Basketball
            LocationData("Basketball: Beat Normal Mushroom Cup Round 1", base_loc_id + 0, "Basketball: Mushroom Cup (Normal)"),
            LocationData("Basketball: Beat Normal Mushroom Cup Round 2", base_loc_id + 1, "Basketball: Mushroom Cup (Normal)"),
            LocationData("Basketball: Beat Normal Mushroom Cup Round 3", base_loc_id + 2, "Basketball: Mushroom Cup (Normal)"),
            LocationData("Basketball: Win Normal Mushroom Cup", base_loc_id + 3, "Basketball: Mushroom Cup (Normal)"),
            LocationData("Basketball: Beat Normal Flower Cup Round 1", base_loc_id + 4, "Basketball: Flower Cup (Normal)"),
            LocationData("Basketball: Beat Normal Flower Cup Round 2", base_loc_id + 5, "Basketball: Flower Cup (Normal)"),
            LocationData("Basketball: Beat Normal Flower Cup Round 3", base_loc_id + 6, "Basketball: Flower Cup (Normal)"),
            LocationData("Basketball: Win Normal Flower Cup", base_loc_id + 7, "Basketball: Flower Cup (Normal)"),
            LocationData("Basketball: Beat Normal Star Cup Round 1", base_loc_id + 8, "Basketball: Star Cup (Normal)"),
            LocationData("Basketball: Beat Normal Star Cup Round 2", base_loc_id + 9, "Basketball: Star Cup (Normal)"),
            LocationData("Basketball: Beat Normal Star Cup Round 3", base_loc_id + 10, "Basketball: Star Cup (Normal)"),
            LocationData("Basketball: Win Normal Star Cup", base_loc_id + 11, "Basketball: Star Cup (Normal)"),

            # Dodgeball
            LocationData("Dodgeball: Beat Normal Mushroom Cup Round 1", base_loc_id + 12, "Dodgeball: Mushroom Cup (Normal)"),
            LocationData("Dodgeball: Beat Normal Mushroom Cup Round 2", base_loc_id + 13, "Dodgeball: Mushroom Cup (Normal)"),
            LocationData("Dodgeball: Beat Normal Mushroom Cup Round 3", base_loc_id + 14, "Dodgeball: Mushroom Cup (Normal)"),
            LocationData("Dodgeball: Win Normal Mushroom Cup", base_loc_id + 15, "Dodgeball: Mushroom Cup (Normal)"),
            LocationData("Dodgeball: Beat Normal Flower Cup Round 1", base_loc_id + 16, "Dodgeball: Flower Cup (Normal)"),
            LocationData("Dodgeball: Beat Normal Flower Cup Round 2", base_loc_id + 17, "Dodgeball: Flower Cup (Normal)"),
            LocationData("Dodgeball: Beat Normal Flower Cup Round 3", base_loc_id + 18, "Dodgeball: Flower Cup (Normal)"),
            LocationData("Dodgeball: Win Normal Flower Cup", base_loc_id + 19, "Dodgeball: Flower Cup (Normal)"),
            LocationData("Dodgeball: Beat Normal Star Cup Round 1", base_loc_id + 20, "Dodgeball: Star Cup (Normal)"),
            LocationData("Dodgeball: Beat Normal Star Cup Round 2", base_loc_id + 21, "Dodgeball: Star Cup (Normal)"),
            LocationData("Dodgeball: Beat Normal Star Cup Round 3", base_loc_id + 22, "Dodgeball: Star Cup (Normal)"),
            LocationData("Dodgeball: Win Normal Star Cup", base_loc_id + 23, "Dodgeball: Star Cup (Normal)"),

            # Volleyball
            LocationData("Volleyball: Beat Normal Mushroom Cup Round 1", base_loc_id + 24, "Volleyball: Mushroom Cup (Normal)"),
            LocationData("Volleyball: Beat Normal Mushroom Cup Round 2", base_loc_id + 25, "Volleyball: Mushroom Cup (Normal)"),
            LocationData("Volleyball: Beat Normal Mushroom Cup Round 3", base_loc_id + 26, "Volleyball: Mushroom Cup (Normal)"),
            LocationData("Volleyball: Win Normal Mushroom Cup", base_loc_id + 27, "Volleyball: Mushroom Cup (Normal)"),
            LocationData("Volleyball: Beat Normal Flower Cup Round 1", base_loc_id + 28, "Volleyball: Flower Cup (Normal)"),
            LocationData("Volleyball: Beat Normal Flower Cup Round 2", base_loc_id + 29, "Volleyball: Flower Cup (Normal)"),
            LocationData("Volleyball: Beat Normal Flower Cup Round 3", base_loc_id + 30, "Volleyball: Flower Cup (Normal)"),
            LocationData("Volleyball: Win Normal Flower Cup", base_loc_id + 31, "Volleyball: Flower Cup (Normal)"),
            LocationData("Volleyball: Beat Normal Star Cup Round 1", base_loc_id + 32, "Volleyball: Star Cup (Normal)"),
            LocationData("Volleyball: Beat Normal Star Cup Round 2", base_loc_id + 33, "Volleyball: Star Cup (Normal)"),
            LocationData("Volleyball: Beat Normal Star Cup Round 3", base_loc_id + 34, "Volleyball: Star Cup (Normal)"),
            LocationData("Volleyball: Win Normal Star Cup", base_loc_id + 35, "Volleyball: Star Cup (Normal)"),

            # Hockey
            LocationData("Hockey: Beat Normal Mushroom Cup Round 1", base_loc_id + 36, "Hockey: Mushroom Cup (Normal)"),
            LocationData("Hockey: Beat Normal Mushroom Cup Round 2", base_loc_id + 37, "Hockey: Mushroom Cup (Normal)"),
            LocationData("Hockey: Beat Normal Mushroom Cup Round 3", base_loc_id + 38, "Hockey: Mushroom Cup (Normal)"),
            LocationData("Hockey: Win Normal Mushroom Cup", base_loc_id + 39, "Hockey: Mushroom Cup (Normal)"),
            LocationData("Hockey: Beat Normal Flower Cup Round 1", base_loc_id + 40, "Hockey: Flower Cup (Normal)"),
            LocationData("Hockey: Beat Normal Flower Cup Round 2", base_loc_id + 41, "Hockey: Flower Cup (Normal)"),
            LocationData("Hockey: Beat Normal Flower Cup Round 3", base_loc_id + 42, "Hockey: Flower Cup (Normal)"),
            LocationData("Hockey: Win Normal Flower Cup", base_loc_id + 43, "Hockey: Flower Cup (Normal)"),
            LocationData("Hockey: Beat Normal Star Cup Round 1", base_loc_id + 44, "Hockey: Star Cup (Normal)"),
            LocationData("Hockey: Beat Normal Star Cup Round 2", base_loc_id + 45, "Hockey: Star Cup (Normal)"),
            LocationData("Hockey: Beat Normal Star Cup Round 3", base_loc_id + 46, "Hockey: Star Cup (Normal)"),
            LocationData("Hockey: Win Normal Star Cup", base_loc_id + 47, "Hockey: Star Cup (Normal)"),
        ]

    if not world or "Hard" in world.options.cup_difficulty:
        location_table += [
            # Basketball
            LocationData("Basketball: Beat Hard Mushroom Cup Round 1", base_loc_id + 48, "Basketball: Mushroom Cup (Hard)"),
            LocationData("Basketball: Beat Hard Mushroom Cup Round 2", base_loc_id + 49, "Basketball: Mushroom Cup (Hard)"),
            LocationData("Basketball: Beat Hard Mushroom Cup Round 3", base_loc_id + 50, "Basketball: Mushroom Cup (Hard)"),
            LocationData("Basketball: Win Hard Mushroom Cup", base_loc_id + 51, "Basketball: Mushroom Cup (Hard)"),
            LocationData("Basketball: Beat Hard Flower Cup Round 1", base_loc_id + 52, "Basketball: Flower Cup (Hard)"),
            LocationData("Basketball: Beat Hard Flower Cup Round 2", base_loc_id + 53, "Basketball: Flower Cup (Hard)"),
            LocationData("Basketball: Beat Hard Flower Cup Round 3", base_loc_id + 54, "Basketball: Flower Cup (Hard)"),
            LocationData("Basketball: Win Hard Flower Cup", base_loc_id + 55, "Basketball: Flower Cup (Hard)"),
            LocationData("Basketball: Beat Hard Star Cup Round 1", base_loc_id + 56, "Basketball: Star Cup (Hard)"),
            LocationData("Basketball: Beat Hard Star Cup Round 2", base_loc_id + 57, "Basketball: Star Cup (Hard)"),
            LocationData("Basketball: Beat Hard Star Cup Round 3", base_loc_id + 58, "Basketball: Star Cup (Hard)"),
            LocationData("Basketball: Win Hard Star Cup", base_loc_id + 59, "Basketball: Star Cup (Hard)"),

            # Dodgeball
            LocationData("Dodgeball: Beat Hard Mushroom Cup Round 1", base_loc_id + 60, "Dodgeball: Mushroom Cup (Hard)"),
            LocationData("Dodgeball: Beat Hard Mushroom Cup Round 2", base_loc_id + 61, "Dodgeball: Mushroom Cup (Hard)"),
            LocationData("Dodgeball: Beat Hard Mushroom Cup Round 3", base_loc_id + 62, "Dodgeball: Mushroom Cup (Hard)"),
            LocationData("Dodgeball: Win Hard Mushroom Cup", base_loc_id + 63, "Dodgeball: Mushroom Cup (Hard)"),
            LocationData("Dodgeball: Beat Hard Flower Cup Round 1", base_loc_id + 64, "Dodgeball: Flower Cup (Hard)"),
            LocationData("Dodgeball: Beat Hard Flower Cup Round 2", base_loc_id + 65, "Dodgeball: Flower Cup (Hard)"),
            LocationData("Dodgeball: Beat Hard Flower Cup Round 3", base_loc_id + 66, "Dodgeball: Flower Cup (Hard)"),
            LocationData("Dodgeball: Win Hard Flower Cup", base_loc_id + 67, "Dodgeball: Flower Cup (Hard)"),
            LocationData("Dodgeball: Beat Hard Star Cup Round 1", base_loc_id + 68, "Dodgeball: Star Cup (Hard)"),
            LocationData("Dodgeball: Beat Hard Star Cup Round 2", base_loc_id + 69, "Dodgeball: Star Cup (Hard)"),
            LocationData("Dodgeball: Beat Hard Star Cup Round 3", base_loc_id + 70, "Dodgeball: Star Cup (Hard)"),
            LocationData("Dodgeball: Win Hard Star Cup", base_loc_id + 71, "Dodgeball: Star Cup (Hard)"),

            # Volleyball
            LocationData("Volleyball: Beat Hard Mushroom Cup Round 1", base_loc_id + 72, "Volleyball: Mushroom Cup (Hard)"),
            LocationData("Volleyball: Beat Hard Mushroom Cup Round 2", base_loc_id + 73, "Volleyball: Mushroom Cup (Hard)"),
            LocationData("Volleyball: Beat Hard Mushroom Cup Round 3", base_loc_id + 74, "Volleyball: Mushroom Cup (Hard)"),
            LocationData("Volleyball: Win Hard Mushroom Cup", base_loc_id + 75, "Volleyball: Mushroom Cup (Hard)"),
            LocationData("Volleyball: Beat Hard Flower Cup Round 1", base_loc_id + 76, "Volleyball: Flower Cup (Hard)"),
            LocationData("Volleyball: Beat Hard Flower Cup Round 2", base_loc_id + 77, "Volleyball: Flower Cup (Hard)"),
            LocationData("Volleyball: Beat Hard Flower Cup Round 3", base_loc_id + 78, "Volleyball: Flower Cup (Hard)"),
            LocationData("Volleyball: Win Hard Flower Cup", base_loc_id + 79, "Volleyball: Flower Cup (Hard)"),
            LocationData("Volleyball: Beat Hard Star Cup Round 1", base_loc_id + 80, "Volleyball: Star Cup (Hard)"),
            LocationData("Volleyball: Beat Hard Star Cup Round 2", base_loc_id + 81, "Volleyball: Star Cup (Hard)"),
            LocationData("Volleyball: Beat Hard Star Cup Round 3", base_loc_id + 82, "Volleyball: Star Cup (Hard)"),
            LocationData("Volleyball: Win Hard Star Cup", base_loc_id + 83, "Volleyball: Star Cup (Hard)"),

            # Hockey
            LocationData("Hockey: Beat Hard Mushroom Cup Round 1", base_loc_id + 84, "Hockey: Mushroom Cup (Hard)"),
            LocationData("Hockey: Beat Hard Mushroom Cup Round 2", base_loc_id + 85, "Hockey: Mushroom Cup (Hard)"),
            LocationData("Hockey: Beat Hard Mushroom Cup Round 3", base_loc_id + 86, "Hockey: Mushroom Cup (Hard)"),
            LocationData("Hockey: Win Hard Mushroom Cup", base_loc_id + 87, "Hockey: Mushroom Cup (Hard)"),
            LocationData("Hockey: Beat Hard Flower Cup Round 1", base_loc_id + 88, "Hockey: Flower Cup (Hard)"),
            LocationData("Hockey: Beat Hard Flower Cup Round 2", base_loc_id + 89, "Hockey: Flower Cup (Hard)"),
            LocationData("Hockey: Beat Hard Flower Cup Round 3", base_loc_id + 90, "Hockey: Flower Cup (Hard)"),
            LocationData("Hockey: Win Hard Flower Cup", base_loc_id + 91, "Hockey: Flower Cup (Hard)"),
            LocationData("Hockey: Beat Hard Star Cup Round 1", base_loc_id + 92, "Hockey: Star Cup (Hard)"),
            LocationData("Hockey: Beat Hard Star Cup Round 2", base_loc_id + 93, "Hockey: Star Cup (Hard)"),
            LocationData("Hockey: Beat Hard Star Cup Round 3", base_loc_id + 94, "Hockey: Star Cup (Hard)"),
            LocationData("Hockey: Win Hard Star Cup", base_loc_id + 95, "Hockey: Star Cup (Hard)"),
        ]

    # Sports Mix locations
    location_table += [
        LocationData("Sports Mix: Beat Mushroom Cup Round 1", base_loc_id + 96, "Sports Mix: Mushroom Cup"),
        LocationData("Sports Mix: Beat Mushroom Cup Round 2", base_loc_id + 97, "Sports Mix: Mushroom Cup"),
        LocationData("Sports Mix: Beat Mushroom Cup Round 3", base_loc_id + 98, "Sports Mix: Mushroom Cup"),
        LocationData("Sports Mix: Win Mushroom Cup", base_loc_id + 99, "Sports Mix: Mushroom Cup"),
        LocationData("Sports Mix: Beat Flower Cup Round 1", base_loc_id + 100, "Sports Mix: Flower Cup"),
        LocationData("Sports Mix: Beat Flower Cup Round 2", base_loc_id + 101, "Sports Mix: Flower Cup"),
        LocationData("Sports Mix: Beat Flower Cup Round 3", base_loc_id + 102, "Sports Mix: Flower Cup"),
        LocationData("Sports Mix: Win Flower Cup", base_loc_id + 103, "Sports Mix: Flower Cup"),
        LocationData("Sports Mix: Beat Star Cup Round 1", base_loc_id + 104, "Sports Mix: Star Cup"),
        LocationData("Sports Mix: Beat Star Cup Round 2", base_loc_id + 105, "Sports Mix: Star Cup"),
        LocationData("Sports Mix: Beat Star Cup Round 3", base_loc_id + 106, "Sports Mix: Star Cup"),
        LocationData("Sports Mix: Win Star Cup", base_loc_id + 107, "Sports Mix: Star Cup"),
    ]

    if not world or "Easy" in world.options.exhibition_difficulty:
        location_table += [
            # Basketball
            LocationData("Basketball Ex: Beat Mario Stadium (Easy)", base_loc_id + 200, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Koopa Troopa Beach (Easy)", base_loc_id + 201, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat DK Dock (Easy)", base_loc_id + 202, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Luigi's Mansion (Easy)", base_loc_id + 203, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Western Junction (Easy)", base_loc_id + 204, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Daisy Garden (Easy)", base_loc_id + 205, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Bowser Jr. Blvd. (Easy)", base_loc_id + 206, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Bowser's Castle (Easy)", base_loc_id + 207, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Star Ship (Easy)", base_loc_id + 208, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Peach's Castle (Easy)", base_loc_id + 209, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Wario Factory (Easy)", base_loc_id + 210, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Ghoulish Galleon (Easy)", base_loc_id + 211, "Basketball: Exhibition"),

            # Dodgeball
            LocationData("Dodgeball Ex: Beat Mario Stadium (Easy)", base_loc_id + 212, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Koopa Troopa Beach (Easy)", base_loc_id + 213, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Peach's Castle (Easy)", base_loc_id + 214, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat DK Dock (Easy)", base_loc_id + 215, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Toad Park (Easy)", base_loc_id + 216, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Daisy Garden (Easy)", base_loc_id + 217, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Wario Factory (Easy)", base_loc_id + 218, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Bowser's Castle (Easy)", base_loc_id + 219, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Star Ship (Easy)", base_loc_id + 220, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Western Junction (Easy)", base_loc_id + 221, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Waluigi Pinball (Easy)", base_loc_id + 222, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Ghoulish Galleon (Easy)", base_loc_id + 223, "Dodgeball: Exhibition"),

            # Volleyball
            LocationData("Volleyball Ex: Beat Mario Stadium (Easy)", base_loc_id + 224, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Koopa Troopa Beach (Easy)", base_loc_id + 225, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Peach's Castle (Easy)", base_loc_id + 226, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat DK Dock (Easy)", base_loc_id + 227, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Luigi's Mansion (Easy)", base_loc_id + 228, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Western Junction (Easy)", base_loc_id + 229, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Bowser Jr. Blvd. (Easy)", base_loc_id + 230, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Bowser's Castle (Easy)", base_loc_id + 231, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Star Ship (Easy)", base_loc_id + 232, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Wario Factory (Easy)", base_loc_id + 233, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Waluigi Pinball (Easy)", base_loc_id + 234, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Ghoulish Galleon (Easy)", base_loc_id + 235, "Volleyball: Exhibition"),

            # Hockey
            LocationData("Hockey Ex: Beat Mario Stadium (Easy)", base_loc_id + 236, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Toad Park (Easy)", base_loc_id + 237, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Peach's Castle (Easy)", base_loc_id + 238, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Western Junction (Easy)", base_loc_id + 239, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Wario Factory (Easy)", base_loc_id + 240, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Daisy Garden (Easy)", base_loc_id + 241, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Bowser Jr. Blvd (Easy)", base_loc_id + 242, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Waluigi Pinball (Easy)", base_loc_id + 243, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Star Ship (Easy)", base_loc_id + 244, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Koopa Troopa Beach (Easy)", base_loc_id + 245, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Ghoulish Galleon (Easy)", base_loc_id + 246, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Bowser's Castle (Easy)", base_loc_id + 247, "Hockey: Exhibition"),

        ]

    if not world or "Normal" in world.options.exhibition_difficulty:
        location_table += [
            # Basketball
            LocationData("Basketball Ex: Beat Mario Stadium (Normal)", base_loc_id + 300, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Koopa Troopa Beach (Normal)", base_loc_id + 301, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat DK Dock (Normal)", base_loc_id + 302, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Luigi's Mansion (Normal)", base_loc_id + 303, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Western Junction (Normal)", base_loc_id + 304, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Daisy Garden (Normal)", base_loc_id + 305, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Bowser Jr. Blvd. (Normal)", base_loc_id + 306, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Bowser's Castle (Normal)", base_loc_id + 307, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Star Ship (Normal)", base_loc_id + 308, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Peach's Castle (Normal)", base_loc_id + 309, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Wario Factory (Normal)", base_loc_id + 310, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Ghoulish Galleon (Normal)", base_loc_id + 311, "Basketball: Exhibition"),

            # Dodgeball
            LocationData("Dodgeball Ex: Beat Mario Stadium (Normal)", base_loc_id + 312, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Koopa Troopa Beach (Normal)", base_loc_id + 313, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Peach's Castle (Normal)", base_loc_id + 314, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat DK Dock (Normal)", base_loc_id + 315, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Toad Park (Normal)", base_loc_id + 316, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Daisy Garden (Normal)", base_loc_id + 317, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Wario Factory (Normal)", base_loc_id + 318, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Bowser's Castle (Normal)", base_loc_id + 319, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Star Ship (Normal)", base_loc_id + 320, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Western Junction (Normal)", base_loc_id + 321, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Waluigi Pinball (Normal)", base_loc_id + 322, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Ghoulish Galleon (Normal)", base_loc_id + 323, "Dodgeball: Exhibition"),

            # Volleyball
            LocationData("Volleyball Ex: Beat Mario Stadium (Normal)", base_loc_id + 324, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Koopa Troopa Beach (Normal)", base_loc_id + 325, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Peach's Castle (Normal)", base_loc_id + 326, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat DK Dock (Normal)", base_loc_id + 327, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Luigi's Mansion (Normal)", base_loc_id + 328, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Western Junction (Normal)", base_loc_id + 329, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Bowser Jr. Blvd. (Normal)", base_loc_id + 330, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Bowser's Castle (Normal)", base_loc_id + 331, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Star Ship (Normal)", base_loc_id + 332, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Wario Factory (Normal)", base_loc_id + 333, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Waluigi Pinball (Normal)", base_loc_id + 334, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Ghoulish Galleon (Normal)", base_loc_id + 335, "Volleyball: Exhibition"),

            # Hockey
            LocationData("Hockey Ex: Beat Mario Stadium (Normal)", base_loc_id + 336, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Toad Park (Normal)", base_loc_id + 337, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Peach's Castle (Normal)", base_loc_id + 338, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Western Junction (Normal)", base_loc_id + 339, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Wario Factory (Normal)", base_loc_id + 340, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Daisy Garden (Normal)", base_loc_id + 341, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Bowser Jr. Blvd (Normal)", base_loc_id + 342, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Waluigi Pinball (Normal)", base_loc_id + 343, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Star Ship (Normal)", base_loc_id + 344, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Koopa Troopa Beach (Normal)", base_loc_id + 345, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Ghoulish Galleon (Normal)", base_loc_id + 346, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Bowser's Castle (Normal)", base_loc_id + 347, "Hockey: Exhibition"),
        ]

    if not world or "Hard" in world.options.exhibition_difficulty:
        location_table += [
            # Basketball
            LocationData("Basketball Ex: Beat Mario Stadium (Hard)", base_loc_id + 400, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Koopa Troopa Beach (Hard)", base_loc_id + 401, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat DK Dock (Hard)", base_loc_id + 402, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Luigi's Mansion (Hard)", base_loc_id + 403, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Western Junction (Hard)", base_loc_id + 404, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Daisy Garden (Hard)", base_loc_id + 405, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Bowser Jr. Blvd. (Hard)", base_loc_id + 406, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Bowser's Castle (Hard)", base_loc_id + 407, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Star Ship (Hard)", base_loc_id + 408, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Peach's Castle (Hard)", base_loc_id + 409, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Wario Factory (Hard)", base_loc_id + 410, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Ghoulish Galleon (Hard)", base_loc_id + 411, "Basketball: Exhibition"),

            # Dodgeball
            LocationData("Dodgeball Ex: Beat Mario Stadium (Hard)", base_loc_id + 412, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Koopa Troopa Beach (Hard)", base_loc_id + 413, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Peach's Castle (Hard)", base_loc_id + 414, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat DK Dock (Hard)", base_loc_id + 415, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Toad Park (Hard)", base_loc_id + 416, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Daisy Garden (Hard)", base_loc_id + 417, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Wario Factory (Hard)", base_loc_id + 418, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Bowser's Castle (Hard)", base_loc_id + 419, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Star Ship (Hard)", base_loc_id + 420, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Western Junction (Hard)", base_loc_id + 421, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Waluigi Pinball (Hard)", base_loc_id + 422, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Ghoulish Galleon (Hard)", base_loc_id + 423, "Dodgeball: Exhibition"),

            # Volleyball
            LocationData("Volleyball Ex: Beat Mario Stadium (Hard)", base_loc_id + 424, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Koopa Troopa Beach (Hard)", base_loc_id + 425, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Peach's Castle (Hard)", base_loc_id + 426, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat DK Dock (Hard)", base_loc_id + 427, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Luigi's Mansion (Hard)", base_loc_id + 428, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Western Junction (Hard)", base_loc_id + 429, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Bowser Jr. Blvd. (Hard)", base_loc_id + 430, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Bowser's Castle (Hard)", base_loc_id + 431, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Star Ship (Hard)", base_loc_id + 432, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Wario Factory (Hard)", base_loc_id + 433, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Waluigi Pinball (Hard)", base_loc_id + 434, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Ghoulish Galleon (Hard)", base_loc_id + 435, "Volleyball: Exhibition"),

            # Hockey
            LocationData("Hockey Ex: Beat Mario Stadium (Hard)", base_loc_id + 436, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Toad Park (Hard)", base_loc_id + 437, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Peach's Castle (Hard)", base_loc_id + 438, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Western Junction (Hard)", base_loc_id + 439, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Wario Factory (Hard)", base_loc_id + 440, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Daisy Garden (Hard)", base_loc_id + 441, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Bowser Jr. Blvd (Hard)", base_loc_id + 442, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Waluigi Pinball (Hard)", base_loc_id + 443, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Star Ship (Hard)", base_loc_id + 444, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Koopa Troopa Beach (Hard)", base_loc_id + 445, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Ghoulish Galleon (Hard)", base_loc_id + 446, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Bowser's Castle (Hard)", base_loc_id + 447, "Hockey: Exhibition"),
        ]

    if not world or "Expert" in world.options.exhibition_difficulty:
        location_table += [
            # Basketball
            LocationData("Basketball Ex: Beat Mario Stadium (Expert)", base_loc_id + 500, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Koopa Troopa Beach (Expert)", base_loc_id + 501, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat DK Dock (Expert)", base_loc_id + 502, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Luigi's Mansion (Expert)", base_loc_id + 503, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Western Junction (Expert)", base_loc_id + 504, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Daisy Garden (Expert)", base_loc_id + 505, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Bowser Jr. Blvd. (Expert)", base_loc_id + 506, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Bowser's Castle (Expert)", base_loc_id + 507, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Star Ship (Expert)", base_loc_id + 508, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Peach's Castle (Expert)", base_loc_id + 509, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Wario Factory (Expert)", base_loc_id + 510, "Basketball: Exhibition"),
            LocationData("Basketball Ex: Beat Ghoulish Galleon (Expert)", base_loc_id + 511, "Basketball: Exhibition"),

            # Dodgeball
            LocationData("Dodgeball Ex: Beat Mario Stadium (Expert)", base_loc_id + 512, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Koopa Troopa Beach (Expert)", base_loc_id + 513, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Peach's Castle (Expert)", base_loc_id + 514, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat DK Dock (Expert)", base_loc_id + 515, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Toad Park (Expert)", base_loc_id + 516, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Daisy Garden (Expert)", base_loc_id + 517, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Wario Factory (Expert)", base_loc_id + 518, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Bowser's Castle (Expert)", base_loc_id + 519, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Star Ship (Expert)", base_loc_id + 520, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Western Junction (Expert)", base_loc_id + 521, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Waluigi Pinball (Expert)", base_loc_id + 522, "Dodgeball: Exhibition"),
            LocationData("Dodgeball Ex: Beat Ghoulish Galleon (Expert)", base_loc_id + 523, "Dodgeball: Exhibition"),

            # Volleyball
            LocationData("Volleyball Ex: Beat Mario Stadium (Expert)", base_loc_id + 524, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Koopa Troopa Beach (Expert)", base_loc_id + 525, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Peach's Castle (Expert)", base_loc_id + 526, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat DK Dock (Expert)", base_loc_id + 527, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Luigi's Mansion (Expert)", base_loc_id + 528, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Western Junction (Expert)", base_loc_id + 529, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Bowser Jr. Blvd. (Expert)", base_loc_id + 530, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Bowser's Castle (Expert)", base_loc_id + 531, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Star Ship (Expert)", base_loc_id + 532, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Wario Factory (Expert)", base_loc_id + 533, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Waluigi Pinball (Expert)", base_loc_id + 534, "Volleyball: Exhibition"),
            LocationData("Volleyball Ex: Beat Ghoulish Galleon (Expert)", base_loc_id + 535, "Volleyball: Exhibition"),

            # Hockey
            LocationData("Hockey Ex: Beat Mario Stadium (Expert)", base_loc_id + 536, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Toad Park (Expert)", base_loc_id + 537, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Peach's Castle (Expert)", base_loc_id + 538, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Western Junction (Expert)", base_loc_id + 539, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Wario Factory (Expert)", base_loc_id + 540, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Daisy Garden (Expert)", base_loc_id + 541, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Bowser Jr. Blvd (Expert)", base_loc_id + 542, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Waluigi Pinball (Expert)", base_loc_id + 543, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Star Ship (Expert)", base_loc_id + 544, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Koopa Troopa Beach (Expert)", base_loc_id + 545, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Ghoulish Galleon (Expert)", base_loc_id + 546, "Hockey: Exhibition"),
            LocationData("Hockey Ex: Beat Bowser's Castle (Expert)", base_loc_id + 547, "Hockey: Exhibition"),
        ]

    if not world or world.options.special_sanity == True:
        location_table +=[
            LocationData("Use Mario's Special!", base_loc_id + 560, "Main Menu"),
            LocationData("Use Luigi's Special!", base_loc_id + 561, "Main Menu"),
            LocationData("Use Peach's Special!", base_loc_id + 562, "Main Menu"),
            LocationData("Use Daisy's Special!", base_loc_id + 563, "Main Menu"),
            LocationData("Use Yoshi's Special!", base_loc_id + 564, "Main Menu"),
            LocationData("Use Wario's Special!", base_loc_id + 565, "Main Menu"),
            LocationData("Use Waluigi's Special!", base_loc_id + 566, "Main Menu"),
            LocationData("Use Donkey Kong's Special!", base_loc_id + 567, "Main Menu"),
            LocationData("Use Diddy Kong's Special!", base_loc_id + 568, "Main Menu"),
            LocationData("Use Toad's Special!", base_loc_id + 569, "Main Menu"),
            LocationData("Use Bowser's Special!", base_loc_id + 570, "Main Menu"),
            LocationData("Use Bowser Jr's Special!", base_loc_id + 571, "Main Menu"),
            LocationData("Use Moogle's Special!", base_loc_id + 572, "Main Menu"),
            LocationData("Use Cactuar's Special!", base_loc_id + 573, "Main Menu"),
            LocationData("Use Ninja's Special!", base_loc_id + 574, "Main Menu"),
            LocationData("Use White Mage's Special!", base_loc_id + 575, "Main Menu"),
            LocationData("Use Slime's Special!", base_loc_id + 576, "Main Menu"),
            LocationData("Use Black Mage's Special!", base_loc_id + 577, "Main Menu"),
        ]

    # Create a location check for Behemoth if the goal is to defeat Behemoth King
    if not world or world.options.goal_condition == GoalCondition.option_defeat_behemoth_king:
        location_table += [
            LocationData("Defeated Behemoth!", base_loc_id + 600, "Behemoth Boss Battle"),
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

