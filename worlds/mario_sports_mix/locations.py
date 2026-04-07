from __future__ import annotations
from typing import TYPE_CHECKING, NamedTuple, Optional, List

from BaseClasses import Location
from . import items
from .options import GoalCondition


if TYPE_CHECKING:
    from .world import MSMWorld

class MSMLocation(Location):
    game = "Mario Sports Mix"

class LocationData(NamedTuple):
    name: str
    code: Optional[int]
    region: Optional[str]


base_loc_id = 0


def get_locations(world: MSMWorld) -> List[LocationData]:
    location_table: List[LocationData] = []

    if not world or "Basketball" in world.options.enabled_sports:
        if "Normal" in world.options.cup_difficulty:
            location_table += [
                LocationData("Basketball: Beat Normal Mushroom Cup Round 1", base_loc_id + 1, "Basketball: Mushroom Cup (Normal)"),
                LocationData("Basketball: Beat Normal Mushroom Cup Round 2", base_loc_id + 2, "Basketball: Mushroom Cup (Normal)"),
                LocationData("Basketball: Beat Normal Mushroom Cup Round 3", base_loc_id + 3, "Basketball: Mushroom Cup (Normal)"),
                LocationData("Basketball: Beat Normal Flower Cup Round 1", base_loc_id + 4, "Basketball: Flower Cup (Normal)"),
                LocationData("Basketball: Beat Normal Flower Cup Round 2", base_loc_id + 5, "Basketball: Flower Cup (Normal)"),
                LocationData("Basketball: Beat Normal Flower Cup Round 3", base_loc_id + 6, "Basketball: Flower Cup (Normal)"),
                LocationData("Basketball: Beat Normal Star Cup Round 1", base_loc_id + 7, "Basketball: Star Cup (Normal)"),
                LocationData("Basketball: Beat Normal Star Cup Round 2", base_loc_id + 8, "Basketball: Star Cup (Normal)"),
                LocationData("Basketball: Beat Normal Star Cup Round 3", base_loc_id + 9, "Basketball: Star Cup (Normal)"),
            ]

    if not world or "Basketball" in world.options.enabled_sports:
        if "Hard" in world.options.cup_difficulty:
            location_table += [
                LocationData("Basketball: Beat Hard Mushroom Cup Round 1", base_loc_id + 10, "Basketball: Mushroom Cup (Hard)"),
                LocationData("Basketball: Beat Hard Mushroom Cup Round 2", base_loc_id + 11, "Basketball: Mushroom Cup (Hard)"),
                LocationData("Basketball: Beat Hard Mushroom Cup Round 3", base_loc_id + 12, "Basketball: Mushroom Cup (Hard)"),
                LocationData("Basketball: Beat Hard Flower Cup Round 1", base_loc_id + 13, "Basketball: Flower Cup (Hard)"),
                LocationData("Basketball: Beat Hard Flower Cup Round 2", base_loc_id + 14, "Basketball: Flower Cup (Hard)"),
                LocationData("Basketball: Beat Hard Flower Cup Round 3", base_loc_id + 15, "Basketball: Flower Cup (Hard)"),
                LocationData("Basketball: Beat Hard Star Cup Round 1", base_loc_id + 16, "Basketball: Star Cup (Hard)"),
                LocationData("Basketball: Beat Hard Star Cup Round 2", base_loc_id + 17, "Basketball: Star Cup (Hard)"),
                LocationData("Basketball: Beat Hard Star Cup Round 3", base_loc_id + 18, "Basketball: Star Cup (Hard)"),
            ]

    if not world or "Dodgeball" in world.options.enabled_sports:
        if "Normal" in world.options.cup_difficulty:
            location_table +=[
                LocationData("Dodgeball: Beat Normal Mushroom Cup Round 1", base_loc_id + 10, "Dodgeball: Mushroom Cup (Normal)"),
                LocationData("Dodgeball: Beat Normal Mushroom Cup Round 2", base_loc_id + 11, "Dodgeball: Mushroom Cup (Normal)"),
                LocationData("Dodgeball: Beat Normal Mushroom Cup Round 3", base_loc_id + 12, "Dodgeball: Mushroom Cup (Normal)"),
                LocationData("Dodgeball: Beat Normal Flower Cup Round 1", base_loc_id + 13, "Dodgeball: Flower Cup (Normal)"),
                LocationData("Dodgeball: Beat Normal Flower Cup Round 2", base_loc_id + 14, "Dodgeball: Flower Cup (Normal)"),
                LocationData("Dodgeball: Beat Normal Flower Cup Round 3", base_loc_id + 15, "Dodgeball: Flower Cup (Normal)"),
                LocationData("Dodgeball: Beat Normal Star Cup Round 1", base_loc_id + 16, "Dodgeball: Star Cup (Normal)"),
                LocationData("Dodgeball: Beat Normal Star Cup Round 2", base_loc_id + 17, "Dodgeball: Star Cup (Normal)"),
                LocationData("Dodgeball: Beat Normal Star Cup Round 3", base_loc_id + 18, "Dodgeball: Star Cup (Normal)")
            ]

    if not world or "Dodgeball" in world.options.enabled_sports:
        if "Hard" in world.options.cup_difficulty:
            location_table += [
                LocationData("Dodgeball: Beat Hard Mushroom Cup Round 1", base_loc_id + 38, "Dodgeball: Mushroom Cup (Hard)"),
                LocationData("Dodgeball: Beat Hard Mushroom Cup Round 2", base_loc_id + 39, "Dodgeball: Mushroom Cup (Hard)"),
                LocationData("Dodgeball: Beat Hard Mushroom Cup Round 3", base_loc_id + 40, "Dodgeball: Mushroom Cup (Hard)"),
                LocationData("Dodgeball: Beat Hard Flower Cup Round 1", base_loc_id + 41, "Dodgeball: Flower Cup (Hard)"),
                LocationData("Dodgeball: Beat Hard Flower Cup Round 2", base_loc_id + 42, "Dodgeball: Flower Cup (Hard)"),
                LocationData("Dodgeball: Beat Hard Flower Cup Round 3", base_loc_id + 43, "Dodgeball: Flower Cup (Hard)"),
                LocationData("Dodgeball: Beat Hard Star Cup Round 1", base_loc_id + 44, "Dodgeball: Star Cup (Hard)"),
                LocationData("Dodgeball: Beat Hard Star Cup Round 2", base_loc_id + 45, "Dodgeball: Star Cup (Hard)"),
                LocationData("Dodgeball: Beat Hard Star Cup Round 3", base_loc_id + 46, "Dodgeball: Star Cup (Hard)"),
            ]


        if not world or "Volleyball" in world.options.enabled_sports:
            if "Normal" in world.options.cup_difficulty:
                location_table += [
                    LocationData("Volleyball: Beat Normal Mushroom Cup Round 1", base_loc_id + 60, "Volleyball: Mushroom Cup (Normal)"),
                    LocationData("Volleyball: Beat Normal Mushroom Cup Round 2", base_loc_id + 61, "Volleyball: Mushroom Cup (Normal)"),
                    LocationData("Volleyball: Beat Normal Mushroom Cup Round 3", base_loc_id + 62, "Volleyball: Mushroom Cup (Normal)"),
                    LocationData("Volleyball: Beat Normal Flower Cup Round 1", base_loc_id + 63, "Volleyball: Flower Cup (Normal)"),
                    LocationData("Volleyball: Beat Normal Flower Cup Round 2", base_loc_id + 64, "Volleyball: Flower Cup (Normal)"),
                    LocationData("Volleyball: Beat Normal Flower Cup Round 3", base_loc_id + 65, "Volleyball: Flower Cup (Normal)"),
                    LocationData("Volleyball: Beat Normal Star Cup Round 1", base_loc_id + 66, "Volleyball: Star Cup (Normal)"),
                    LocationData("Volleyball: Beat Normal Star Cup Round 2", base_loc_id + 67, "Volleyball: Star Cup (Normal)"),
                    LocationData("Volleyball: Beat Normal Star Cup Round 3", base_loc_id + 68, "Volleyball: Star Cup (Normal)"),
                ]

        if not world or "Volleyball" in world.options.enabled_sports:
            if "Hard" in world.options.cup_difficulty:
                location_table += [
                    LocationData("Volleyball: Beat Hard Mushroom Cup Round 1", base_loc_id + 69, "Volleyball: Mushroom Cup (Hard)"),
                    LocationData("Volleyball: Beat Hard Mushroom Cup Round 2", base_loc_id + 70, "Volleyball: Mushroom Cup (Hard)"),
                    LocationData("Volleyball: Beat Hard Mushroom Cup Round 3", base_loc_id + 71, "Volleyball: Mushroom Cup (Hard)"),
                    LocationData("Volleyball: Beat Hard Flower Cup Round 1", base_loc_id + 72, "Volleyball: Flower Cup (Hard)"),
                    LocationData("Volleyball: Beat Hard Flower Cup Round 2", base_loc_id + 73, "Volleyball: Flower Cup (Hard)"),
                    LocationData("Volleyball: Beat Hard Flower Cup Round 3", base_loc_id + 74, "Volleyball: Flower Cup (Hard)"),
                    LocationData("Volleyball: Beat Hard Star Cup Round 1", base_loc_id + 75, "Volleyball: Star Cup (Hard)"),
                    LocationData("Volleyball: Beat Hard Star Cup Round 2", base_loc_id + 76, "Volleyball: Star Cup (Hard)"),
                    LocationData("Volleyball: Beat Hard Star Cup Round 3", base_loc_id + 77, "Volleyball: Star Cup (Hard)"),
                ]

        if not world or "Hockey" in world.options.enabled_sports:
            if "Normal" in world.options.cup_difficulty:
                location_table += [
                    LocationData("Hockey: Beat Normal Mushroom Cup Round 1", base_loc_id + 90, "Hockey: Mushroom Cup (Normal)"),
                    LocationData("Hockey: Beat Normal Mushroom Cup Round 2", base_loc_id + 91, "Hockey: Mushroom Cup (Normal)"),
                    LocationData("Hockey: Beat Normal Mushroom Cup Round 3", base_loc_id + 92, "Hockey: Mushroom Cup (Normal)"),
                    LocationData("Hockey: Beat Normal Flower Cup Round 1", base_loc_id + 93, "Hockey: Flower Cup (Normal)"),
                    LocationData("Hockey: Beat Normal Flower Cup Round 2", base_loc_id + 94, "Hockey: Flower Cup (Normal)"),
                    LocationData("Hockey: Beat Normal Flower Cup Round 3", base_loc_id + 95, "Hockey: Flower Cup (Normal)"),
                    LocationData("Hockey: Beat Normal Star Cup Round 1", base_loc_id + 96, "Hockey: Star Cup (Normal)"),
                    LocationData("Hockey: Beat Normal Star Cup Round 2", base_loc_id + 97, "Hockey: Star Cup (Normal)"),
                    LocationData("Hockey: Beat Normal Star Cup Round 3", base_loc_id + 98, "Hockey: Star Cup (Normal)"),
                ]

        if not world or "Hockey" in world.options.enabled_sports:
            if "Hard" in world.options.cup_difficulty:
                location_table += [
                    LocationData("Hockey: Beat Hard Mushroom Cup Round 1", base_loc_id + 99, "Hockey: Mushroom Cup (Hard)"),
                    LocationData("Hockey: Beat Hard Mushroom Cup Round 2", base_loc_id + 100, "Hockey: Mushroom Cup (Hard)"),
                    LocationData("Hockey: Beat Hard Mushroom Cup Round 3", base_loc_id + 101, "Hockey: Mushroom Cup (Hard)"),
                    LocationData("Hockey: Beat Hard Flower Cup Round 1", base_loc_id + 102, "Hockey: Flower Cup (Hard)"),
                    LocationData("Hockey: Beat Hard Flower Cup Round 2", base_loc_id + 103, "Hockey: Flower Cup (Hard)"),
                    LocationData("Hockey: Beat Hard Flower Cup Round 3", base_loc_id + 104, "Hockey: Flower Cup (Hard)"),
                    LocationData("Hockey: Beat Hard Star Cup Round 1", base_loc_id + 105, "Hockey: Star Cup (Hard)"),
                    LocationData("Hockey: Beat Hard Star Cup Round 2", base_loc_id + 106, "Hockey: Star Cup (Hard)"),
                    LocationData("Hockey: Beat Hard Star Cup Round 3", base_loc_id + 107, "Hockey: Star Cup (Hard)"),
                ]

        if not world or "Sports Mix" in world.options.enabled_sports:
            location_table += [
                LocationData("Sports Mix: Beat Mushroom Cup Round 1", base_loc_id + 120, "Sports Mix: Mushroom Cup"),
                LocationData("Sports Mix: Beat Mushroom Cup Round 2", base_loc_id + 121, "Sports Mix: Mushroom Cup"),
                LocationData("Sports Mix: Beat Mushroom Cup Round 3", base_loc_id + 122, "Sports Mix: Mushroom Cup"),
                LocationData("Sports Mix: Beat Flower Cup Round 1", base_loc_id + 123, "Sports Mix: Flower Cup"),
                LocationData("Sports Mix: Beat Flower Cup Round 2", base_loc_id + 124, "Sports Mix: Flower Cup"),
                LocationData("Sports Mix: Beat Flower Cup Round 3", base_loc_id + 125, "Sports Mix: Flower Cup"),
                LocationData("Sports Mix: Beat Star Cup Round 1", base_loc_id + 126, "Sports Mix: Star Cup"),
                LocationData("Sports Mix: Beat Star Cup Round 2", base_loc_id + 127, "Sports Mix: Star Cup"),
                LocationData("Sports Mix: Beat Star Cup Round 3", base_loc_id + 128, "Sports Mix: Star Cup"),
            ]

    if not world or "Basketball" in world.options.enabled_sports:
        if not world or "Easy" in world.options.exhibition_difficulty:
            location_table += [
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
            ]

        if not world or "Normal" in world.options.exhibition_difficulty:
            location_table += [
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
            ]

        if not world or "Hard" in world.options.exhibition_difficulty:
            location_table += [
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
            ]

        if not world or "Expert" in world.options.exhibition_difficulty:
            location_table += [
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
            ]

 # Dodgeball Exhibition
    if not world or "Dodgeball" in world.options.enabled_sports:
        if not world or "Easy" in world.options.exhibition_difficulty:
            location_table += [
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
            ]

        if not world or "Normal" in world.options.exhibition_difficulty:
            location_table += [
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
            ]

        if not world or "Hard" in world.options.exhibition_difficulty:
            location_table += [
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
            ]

        if not world or "Expert" in world.options.exhibition_difficulty:
            location_table += [
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
            ]

     # Volleyball Exhibition
    if not world or "Volleyball" in world.options.enabled_sports:
        if not world or "Easy" in world.options.exhibition_difficulty:
            location_table += [
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
            ]

        if not world or "Normal" in world.options.exhibition_difficulty:
            location_table += [
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
            ]

        if not world or "Hard" in world.options.exhibition_difficulty:
            location_table += [
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
            ]

        if not world or "Expert" in world.options.exhibition_difficulty:
            location_table += [
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
            ]

 # Hockey Exhibition
    if not world or "Hockey" in world.options.enabled_sports:
        if not world or "Easy" in world.options.exhibition_difficulty:
            location_table += [
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
        if not world or world.options.goal_condition == GoalCondition.option_defeat_behemoth_King:
            location_table += [
                LocationData("Defeated Behemoth!", base_loc_id + 400, "Behemoth Boss Battle"),
            ]

    return location_table

LOCATION_NAME_TO_ID = get_locations(MSMWorld(MSMWorld.multiworld ,MSMWorld.player))

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    #Takes a list of location names and returns a dictionary mapping those names
    #to their respective IDs from the master location list.

    # Create a quick local lookup to avoid searching the list repeatedly
    lookup = {loc.name: loc.code for loc in LOCATION_NAME_TO_ID}
    return {name: lookup.get(name) for name in location_names}


def create_all_locations(world: MSMWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: MSMWorld) -> None:

    b_exhibition = world.get_region("Basketball: Exhibition")
    b_mushroom_cup_n = world.get_region("Basketball: Mushroom Cup (Normal)")
    b_flower_cup_n = world.get_region("Basketball: Flower Cup (Normal)")
    b_star_cup_n = world.get_region("Basketball: Star Cup (Normal)")
    b_mushroom_cup_h = world.get_region("Basketball: Mushroom Cup (Hard)")
    b_flower_cup_h = world.get_region("Basketball: Flower Cup (Hard)")
    b_star_cup_h = world.get_region("Basketball: Star Cup (Hard)")
    b_extra = world.get_region("Basketball: Extra")

    d_exhibition = world.get_region("Dodgeball: Exhibition")
    d_mushroom_cup_n = world.get_region("Dodgeball: Mushroom Cup (Normal)")
    d_flower_cup_n = world.get_region("Dodgeball: Flower Cup (Normal)")
    d_star_cup_n = world.get_region("Dodgeball: Star Cup (Normal)")
    d_mushroom_cup_h = world.get_region("Dodgeball: Mushroom Cup (Hard)")
    d_flower_cup_h = world.get_region("Dodgeball: Flower Cup (Hard)")
    d_star_cup_h = world.get_region("Dodgeball: Star Cup (Hard)")
    d_extra = world.get_region("Dodgeball: Extra")

    v_exhibition = world.get_region("Volleyball: Exhibition")
    v_mushroom_cup_n = world.get_region("Volleyball: Mushroom Cup (Normal)")
    v_flower_cup_n = world.get_region("Volleyball: Flower Cup (Normal)")
    v_star_cup_n = world.get_region("Volleyball: Star Cup (Normal)")
    v_mushroom_cup_h = world.get_region("Volleyball: Mushroom Cup (Hard)")
    v_flower_cup_h = world.get_region("Volleyball: Flower Cup (Hard)")
    v_star_cup_h = world.get_region("Volleyball: Star Cup (Hard)")
    v_extra = world.get_region("Volleyball: Extra")

    h_exhibition = world.get_region("Hockey: Exhibition")
    h_mushroom_cup_n = world.get_region("Hockey: Mushroom Cup (Normal)")
    h_flower_cup_n = world.get_region("Hockey: Flower Cup (Normal)")
    h_star_cup_n = world.get_region("Hockey: Star Cup (Normal)")
    h_mushroom_cup_h = world.get_region("Hockey: Mushroom Cup (Hard)")
    h_flower_cup_h = world.get_region("Hockey: Flower Cup (Hard)")
    h_star_cup_h = world.get_region("Hockey: Star Cup (Hard)")
    h_extra = world.get_region("Hockey: Extra")

    sm_mushroom_cup = world.get_region("Sports Mix: Mushroom Cup")
    sm_flower_cup = world.get_region("Sports Mix: Flower Cup")
    sm_star_cup = world.get_region("Sports Mix: Star Cup")

    # Basketball
    basketball_normal_mushroom = get_location_names_with_ids([
        "Basketball: Beat Normal Mushroom Cup Round 1",
        "Basketball: Beat Normal Mushroom Cup Round 2",
        "Basketball: Beat Normal Mushroom Cup Round 3",
    ])
    b_mushroom_cup_n.add_locations(basketball_normal_mushroom)

    basketball_normal_flower = get_location_names_with_ids([
        "Basketball: Beat Normal Flower Cup Round 1",
        "Basketball: Beat Normal Flower Cup Round 2",
        "Basketball: Beat Normal Flower Cup Round 3",
    ])
    b_flower_cup_n.add_locations(basketball_normal_flower)

    basketball_normal_star = get_location_names_with_ids([
        "Basketball: Beat Normal Star Cup Round 1",
        "Basketball: Beat Normal Star Cup Round 2",
        "Basketball: Beat Normal Star Cup Round 3",
    ])
    b_star_cup_n.add_locations(basketball_normal_star)

    basketball_hard_mushroom = get_location_names_with_ids([
        "Basketball: Beat Hard Mushroom Cup Round 1",
        "Basketball: Beat Hard Mushroom Cup Round 2",
        "Basketball: Beat Hard Mushroom Cup Round 3",
    ])
    b_mushroom_cup_h.add_locations(basketball_hard_mushroom)

    basketball_hard_flower = get_location_names_with_ids([
        "Basketball: Beat Hard Flower Cup Round 1",
        "Basketball: Beat Hard Flower Cup Round 2",
        "Basketball: Beat Hard Flower Cup Round 3",
    ])
    b_flower_cup_h.add_locations(basketball_hard_flower)

    basketball_hard_star = get_location_names_with_ids([
        "Basketball: Beat Hard Star Cup Round 1",
        "Basketball: Beat Hard Star Cup Round 2",
        "Basketball: Beat Hard Star Cup Round 3",
    ])
    b_star_cup_h.add_locations(basketball_hard_star)

    # Dodgeball
    dodgeball_normal_mushroom = get_location_names_with_ids([
        "Dodgeball: Beat Normal Mushroom Cup Round 1",
        "Dodgeball: Beat Normal Mushroom Cup Round 2",
        "Dodgeball: Beat Normal Mushroom Cup Round 3",
    ])
    d_mushroom_cup_n.add_locations(dodgeball_normal_mushroom)

    dodgeball_normal_flower = get_location_names_with_ids([
        "Dodgeball: Beat Normal Flower Cup Round 1",
        "Dodgeball: Beat Normal Flower Cup Round 2",
        "Dodgeball: Beat Normal Flower Cup Round 3",
    ])
    d_flower_cup_n.add_locations(dodgeball_normal_flower)

    dodgeball_normal_star = get_location_names_with_ids([
        "Dodgeball: Beat Normal Star Cup Round 1",
        "Dodgeball: Beat Normal Star Cup Round 2",
        "Dodgeball: Beat Normal Star Cup Round 3",
    ])
    d_star_cup_n.add_locations(dodgeball_normal_star)

    dodgeball_hard_mushroom = get_location_names_with_ids([
        "Dodgeball: Beat Hard Mushroom Cup Round 1",
        "Dodgeball: Beat Hard Mushroom Cup Round 2",
        "Dodgeball: Beat Hard Mushroom Cup Round 3",
    ])
    d_mushroom_cup_h.add_locations(dodgeball_hard_mushroom)

    dodgeball_hard_flower = get_location_names_with_ids([
        "Dodgeball: Beat Hard Flower Cup Round 1",
        "Dodgeball: Beat Hard Flower Cup Round 2",
        "Dodgeball: Beat Hard Flower Cup Round 3",
    ])
    d_flower_cup_h.add_locations(dodgeball_hard_flower)

    dodgeball_hard_star = get_location_names_with_ids([
        "Dodgeball: Beat Hard Star Cup Round 1",
        "Dodgeball: Beat Hard Star Cup Round 2",
        "Dodgeball: Beat Hard Star Cup Round 3",
    ])
    d_star_cup_h.add_locations(dodgeball_hard_star)

    # Volleyball
    volleyball_normal_mushroom = get_location_names_with_ids([
        "Volleyball: Beat Normal Mushroom Cup Round 1",
        "Volleyball: Beat Normal Mushroom Cup Round 2",
        "Volleyball: Beat Normal Mushroom Cup Round 3",
    ])
    v_mushroom_cup_n.add_locations(volleyball_normal_mushroom)

    volleyball_normal_flower = get_location_names_with_ids([
        "Volleyball: Beat Normal Flower Cup Round 1",
        "Volleyball: Beat Normal Flower Cup Round 2",
        "Volleyball: Beat Normal Flower Cup Round 3",
    ])
    v_flower_cup_n.add_locations(volleyball_normal_flower)

    volleyball_normal_star = get_location_names_with_ids([
        "Volleyball: Beat Normal Star Cup Round 1",
        "Volleyball: Beat Normal Star Cup Round 2",
        "Volleyball: Beat Normal Star Cup Round 3",
    ])
    v_star_cup_n.add_locations(volleyball_normal_star)

    volleyball_hard_mushroom = get_location_names_with_ids([
        "Volleyball: Beat Hard Mushroom Cup Round 1",
        "Volleyball: Beat Hard Mushroom Cup Round 2",
        "Volleyball: Beat Hard Mushroom Cup Round 3",
    ])
    v_mushroom_cup_h.add_locations(volleyball_hard_mushroom)

    volleyball_hard_flower = get_location_names_with_ids([
        "Volleyball: Beat Hard Flower Cup Round 1",
        "Volleyball: Beat Hard Flower Cup Round 2",
        "Volleyball: Beat Hard Flower Cup Round 3",
    ])
    v_flower_cup_h.add_locations(volleyball_hard_flower)

    volleyball_hard_star = get_location_names_with_ids([
        "Volleyball: Beat Hard Star Cup Round 1",
        "Volleyball: Beat Hard Star Cup Round 2",
        "Volleyball: Beat Hard Star Cup Round 3",
    ])
    v_star_cup_h.add_locations(volleyball_hard_star)

    # Hockey
    hockey_normal_mushroom = get_location_names_with_ids([
        "Hockey: Beat Normal Mushroom Cup Round 1",
        "Hockey: Beat Normal Mushroom Cup Round 2",
        "Hockey: Beat Normal Mushroom Cup Round 3",
    ])
    h_mushroom_cup_n.add_locations(hockey_normal_mushroom)

    hockey_normal_flower = get_location_names_with_ids([
        "Hockey: Beat Normal Flower Cup Round 1",
        "Hockey: Beat Normal Flower Cup Round 2",
        "Hockey: Beat Normal Flower Cup Round 3",
    ])
    h_flower_cup_n.add_locations(hockey_normal_flower)

    hockey_normal_star = get_location_names_with_ids([
        "Hockey: Beat Normal Star Cup Round 1",
        "Hockey: Beat Normal Star Cup Round 2",
        "Hockey: Beat Normal Star Cup Round 3",
    ])
    h_star_cup_n.add_locations(hockey_normal_star)

    hockey_hard_mushroom = get_location_names_with_ids([
        "Hockey: Beat Hard Mushroom Cup Round 1",
        "Hockey: Beat Hard Mushroom Cup Round 2",
        "Hockey: Beat Hard Mushroom Cup Round 3",
    ])
    h_mushroom_cup_h.add_locations(hockey_hard_mushroom)

    hockey_hard_flower = get_location_names_with_ids([
        "Hockey: Beat Hard Flower Cup Round 1",
        "Hockey: Beat Hard Flower Cup Round 2",
        "Hockey: Beat Hard Flower Cup Round 3",
    ])
    h_flower_cup_h.add_locations(hockey_hard_flower)

    hockey_hard_star = get_location_names_with_ids([
        "Hockey: Beat Hard Star Cup Round 1",
        "Hockey: Beat Hard Star Cup Round 2",
        "Hockey: Beat Hard Star Cup Round 3",
    ])
    h_star_cup_h.add_locations(hockey_hard_star)

    # Sports Mix
    sports_mix_mushroom = get_location_names_with_ids([
        "Sports Mix: Beat Mushroom Cup Round 1",
        "Sports Mix: Beat Mushroom Cup Round 2",
        "Sports Mix: Beat Mushroom Cup Round 3",
    ])
    sm_mushroom_cup.add_locations(sports_mix_mushroom)

    sports_mix_flower = get_location_names_with_ids([
        "Sports Mix: Beat Flower Cup Round 1",
        "Sports Mix: Beat Flower Cup Round 2",
        "Sports Mix: Beat Flower Cup Round 3",
    ])
    sm_flower_cup.add_locations(sports_mix_flower)

    sports_mix_star = get_location_names_with_ids([
        "Sports Mix: Beat Star Cup Round 1",
        "Sports Mix: Beat Star Cup Round 2",
        "Sports Mix: Beat Star Cup Round 3",
    ])
    sm_star_cup.add_locations(sports_mix_star)

    # Basketball Exhibition
    basketball_ex_easy = get_location_names_with_ids([
        "Basketball Ex: Beat Mario Stadium (Easy)", "Basketball Ex: Beat Koopa Troopa Beach (Easy)",
        "Basketball Ex: Beat DK Dock (Easy)", "Basketball Ex: Beat Luigi's Mansion (Easy)",
        "Basketball Ex: Beat Western Junction (Easy)", "Basketball Ex: Beat Daisy Garden (Easy)",
        "Basketball Ex: Beat Bowser Jr. Blvd. (Easy)", "Basketball Ex: Beat Bowser's Castle (Easy)",
        "Basketball Ex: Beat Star Ship (Easy)", "Basketball Ex: Beat Peach's Castle (Easy)",
        "Basketball Ex: Beat Wario Factory (Easy)", "Basketball Ex: Beat Ghoulish Galleon (Easy)",
    ])
    b_exhibition.add_locations(basketball_ex_easy)

    basketball_ex_normal = get_location_names_with_ids([
        "Basketball Ex: Beat Mario Stadium (Normal)", "Basketball Ex: Beat Koopa Troopa Beach (Normal)",
        "Basketball Ex: Beat DK Dock (Normal)", "Basketball Ex: Beat Luigi's Mansion (Normal)",
        "Basketball Ex: Beat Western Junction (Normal)", "Basketball Ex: Beat Daisy Garden (Normal)",
        "Basketball Ex: Beat Bowser Jr. Blvd. (Normal)", "Basketball Ex: Beat Bowser's Castle (Normal)",
        "Basketball Ex: Beat Star Ship (Normal)", "Basketball Ex: Beat Peach's Castle (Normal)",
        "Basketball Ex: Beat Wario Factory (Normal)", "Basketball Ex: Beat Ghoulish Galleon (Normal)",
    ])
    b_exhibition.add_locations(basketball_ex_normal)

    basketball_ex_hard = get_location_names_with_ids([
        "Basketball Ex: Beat Mario Stadium (Hard)", "Basketball Ex: Beat Koopa Troopa Beach (Hard)",
        "Basketball Ex: Beat DK Dock (Hard)", "Basketball Ex: Beat Luigi's Mansion (Hard)",
        "Basketball Ex: Beat Western Junction (Hard)", "Basketball Ex: Beat Daisy Garden (Hard)",
        "Basketball Ex: Beat Bowser Jr. Blvd. (Hard)", "Basketball Ex: Beat Bowser's Castle (Hard)",
        "Basketball Ex: Beat Star Ship (Hard)", "Basketball Ex: Beat Peach's Castle (Hard)",
        "Basketball Ex: Beat Wario Factory (Hard)", "Basketball Ex: Beat Ghoulish Galleon (Hard)",
    ])
    b_exhibition.add_locations(basketball_ex_hard)

    basketball_ex_expert = get_location_names_with_ids([
        "Basketball Ex: Beat Mario Stadium (Expert)", "Basketball Ex: Beat Koopa Troopa Beach (Expert)",
        "Basketball Ex: Beat DK Dock (Expert)", "Basketball Ex: Beat Luigi's Mansion (Expert)",
        "Basketball Ex: Beat Western Junction (Expert)", "Basketball Ex: Beat Daisy Garden (Expert)",
        "Basketball Ex: Beat Bowser Jr. Blvd. (Expert)", "Basketball Ex: Beat Bowser's Castle (Expert)",
        "Basketball Ex: Beat Star Ship (Expert)", "Basketball Ex: Beat Peach's Castle (Expert)",
        "Basketball Ex: Beat Wario Factory (Expert)", "Basketball Ex: Beat Ghoulish Galleon (Expert)",
    ])
    b_exhibition.add_locations(basketball_ex_expert)

    # Dodgeball Exhibition
    dodgeball_ex_easy = get_location_names_with_ids([
        "Dodgeball Ex: Beat Mario Stadium (Easy)", "Dodgeball Ex: Beat Koopa Troopa Beach (Easy)",
        "Dodgeball Ex: Beat Peach's Castle (Easy)", "Dodgeball Ex: Beat DK Dock (Easy)",
        "Dodgeball Ex: Beat Toad Park (Easy)", "Dodgeball Ex: Beat Daisy Garden (Easy)",
        "Dodgeball Ex: Beat Wario Factory (Easy)", "Dodgeball Ex: Beat Bowser's Castle (Easy)",
        "Dodgeball Ex: Beat Star Ship (Easy)", "Dodgeball Ex: Beat Western Junction (Easy)",
        "Dodgeball Ex: Beat Waluigi Pinball (Easy)", "Dodgeball Ex: Beat Ghoulish Galleon (Easy)",
    ])
    d_exhibition.add_locations(dodgeball_ex_easy)

    dodgeball_ex_normal = get_location_names_with_ids([
        "Dodgeball Ex: Beat Mario Stadium (Normal)", "Dodgeball Ex: Beat Koopa Troopa Beach (Normal)",
        "Dodgeball Ex: Beat Peach's Castle (Normal)", "Dodgeball Ex: Beat DK Dock (Normal)",
        "Dodgeball Ex: Beat Toad Park (Normal)", "Dodgeball Ex: Beat Daisy Garden (Normal)",
        "Dodgeball Ex: Beat Wario Factory (Normal)", "Dodgeball Ex: Beat Bowser's Castle (Normal)",
        "Dodgeball Ex: Beat Star Ship (Normal)", "Dodgeball Ex: Beat Western Junction (Normal)",
        "Dodgeball Ex: Beat Waluigi Pinball (Normal)", "Dodgeball Ex: Beat Ghoulish Galleon (Normal)",
    ])
    d_exhibition.add_locations(dodgeball_ex_normal)

    dodgeball_ex_hard = get_location_names_with_ids([
        "Dodgeball Ex: Beat Mario Stadium (Hard)", "Dodgeball Ex: Beat Koopa Troopa Beach (Hard)",
        "Dodgeball Ex: Beat Peach's Castle (Hard)", "Dodgeball Ex: Beat DK Dock (Hard)",
        "Dodgeball Ex: Beat Toad Park (Hard)", "Dodgeball Ex: Beat Daisy Garden (Hard)",
        "Dodgeball Ex: Beat Wario Factory (Hard)", "Dodgeball Ex: Beat Bowser's Castle (Hard)",
        "Dodgeball Ex: Beat Star Ship (Hard)", "Dodgeball Ex: Beat Western Junction (Hard)",
        "Dodgeball Ex: Beat Waluigi Pinball (Hard)", "Dodgeball Ex: Beat Ghoulish Galleon (Hard)",
    ])
    d_exhibition.add_locations(dodgeball_ex_hard)

    dodgeball_ex_expert = get_location_names_with_ids([
        "Dodgeball Ex: Beat Mario Stadium (Expert)", "Dodgeball Ex: Beat Koopa Troopa Beach (Expert)",
        "Dodgeball Ex: Beat Peach's Castle (Expert)", "Dodgeball Ex: Beat DK Dock (Expert)",
        "Dodgeball Ex: Beat Toad Park (Expert)", "Dodgeball Ex: Beat Daisy Garden (Expert)",
        "Dodgeball Ex: Beat Wario Factory (Expert)", "Dodgeball Ex: Beat Bowser's Castle (Expert)",
        "Dodgeball Ex: Beat Star Ship (Expert)", "Dodgeball Ex: Beat Western Junction (Expert)",
        "Dodgeball Ex: Beat Waluigi Pinball (Expert)", "Dodgeball Ex: Beat Ghoulish Galleon (Expert)",
    ])
    d_exhibition.add_locations(dodgeball_ex_expert)

    # Volleyball Exhibition
    volleyball_ex_easy = get_location_names_with_ids([
        "Volleyball Ex: Beat Mario Stadium (Easy)", "Volleyball Ex: Beat Koopa Troopa Beach (Easy)",
        "Volleyball Ex: Beat Peach's Castle (Easy)", "Volleyball Ex: Beat DK Dock (Easy)",
        "Volleyball Ex: Beat Luigi's Mansion (Easy)", "Volleyball Ex: Beat Western Junction (Easy)",
        "Volleyball Ex: Beat Bowser Jr. Blvd. (Easy)", "Volleyball Ex: Beat Bowser's Castle (Easy)",
        "Volleyball Ex: Beat Star Ship (Easy)", "Volleyball Ex: Beat Wario Factory (Easy)",
        "Volleyball Ex: Beat Waluigi Pinball (Easy)", "Volleyball Ex: Beat Ghoulish Galleon (Easy)",
    ])
    v_exhibition.add_locations(volleyball_ex_easy)

    volleyball_ex_normal = get_location_names_with_ids([
        "Volleyball Ex: Beat Mario Stadium (Normal)", "Volleyball Ex: Beat Koopa Troopa Beach (Normal)",
        "Volleyball Ex: Beat Peach's Castle (Normal)", "Volleyball Ex: Beat DK Dock (Normal)",
        "Volleyball Ex: Beat Luigi's Mansion (Normal)", "Volleyball Ex: Beat Western Junction (Normal)",
        "Volleyball Ex: Beat Bowser Jr. Blvd. (Normal)", "Volleyball Ex: Beat Bowser's Castle (Normal)",
        "Volleyball Ex: Beat Star Ship (Normal)", "Volleyball Ex: Beat Wario Factory (Normal)",
        "Volleyball Ex: Beat Waluigi Pinball (Normal)", "Volleyball Ex: Beat Ghoulish Galleon (Normal)",
    ])
    v_exhibition.add_locations(volleyball_ex_normal)

    volleyball_ex_hard = get_location_names_with_ids([
        "Volleyball Ex: Beat Mario Stadium (Hard)", "Volleyball Ex: Beat Koopa Troopa Beach (Hard)",
        "Volleyball Ex: Beat Peach's Castle (Hard)", "Volleyball Ex: Beat DK Dock (Hard)",
        "Volleyball Ex: Beat Luigi's Mansion (Hard)", "Volleyball Ex: Beat Western Junction (Hard)",
        "Volleyball Ex: Beat Bowser Jr. Blvd. (Hard)", "Volleyball Ex: Beat Bowser's Castle (Hard)",
        "Volleyball Ex: Beat Star Ship (Hard)", "Volleyball Ex: Beat Wario Factory (Hard)",
        "Volleyball Ex: Beat Waluigi Pinball (Hard)", "Volleyball Ex: Beat Ghoulish Galleon (Hard)",
    ])
    v_exhibition.add_locations(volleyball_ex_hard)

    volleyball_ex_expert = get_location_names_with_ids([
        "Volleyball Ex: Beat Mario Stadium (Expert)", "Volleyball Ex: Beat Koopa Troopa Beach (Expert)",
        "Volleyball Ex: Beat Peach's Castle (Expert)", "Volleyball Ex: Beat DK Dock (Expert)",
        "Volleyball Ex: Beat Luigi's Mansion (Expert)", "Volleyball Ex: Beat Western Junction (Expert)",
        "Volleyball Ex: Beat Bowser Jr. Blvd. (Expert)", "Volleyball Ex: Beat Bowser's Castle (Expert)",
        "Volleyball Ex: Beat Star Ship (Expert)", "Volleyball Ex: Beat Wario Factory (Expert)",
        "Volleyball Ex: Beat Waluigi Pinball (Expert)", "Volleyball Ex: Beat Ghoulish Galleon (Expert)",
    ])
    v_exhibition.add_locations(volleyball_ex_expert)

    # Hockey Exhibition
    hockey_ex_easy = get_location_names_with_ids([
        "Hockey Ex: Beat Mario Stadium (Easy)", "Hockey Ex: Beat Toad Park (Easy)",
        "Hockey Ex: Beat Peach's Castle (Easy)", "Hockey Ex: Beat Western Junction (Easy)",
        "Hockey Ex: Beat Wario Factory (Easy)", "Hockey Ex: Beat Daisy Garden (Easy)",
        "Hockey Ex: Beat Bowser Jr. Blvd (Easy)", "Hockey Ex: Beat Waluigi Pinball (Easy)",
        "Hockey Ex: Beat Star Ship (Easy)", "Hockey Ex: Beat Koopa Troopa Beach (Easy)",
        "Hockey Ex: Beat Ghoulish Galleon (Easy)", "Hockey Ex: Beat Bowser's Castle (Easy)",
    ])
    h_exhibition.add_locations(hockey_ex_easy)

    hockey_ex_normal = get_location_names_with_ids([
        "Hockey Ex: Beat Mario Stadium (Normal)", "Hockey Ex: Beat Toad Park (Normal)",
        "Hockey Ex: Beat Peach's Castle (Normal)", "Hockey Ex: Beat Western Junction (Normal)",
        "Hockey Ex: Beat Wario Factory (Normal)", "Hockey Ex: Beat Daisy Garden (Normal)",
        "Hockey Ex: Beat Bowser Jr. Blvd (Normal)", "Hockey Ex: Beat Waluigi Pinball (Normal)",
        "Hockey Ex: Beat Star Ship (Normal)", "Hockey Ex: Beat Koopa Troopa Beach (Normal)",
        "Hockey Ex: Beat Ghoulish Galleon (Normal)", "Hockey Ex: Beat Bowser's Castle (Normal)",
    ])
    h_exhibition.add_locations(hockey_ex_normal)

    hockey_ex_hard = get_location_names_with_ids([
        "Hockey Ex: Beat Mario Stadium (Hard)", "Hockey Ex: Beat Toad Park (Hard)",
        "Hockey Ex: Beat Peach's Castle (Hard)", "Hockey Ex: Beat Western Junction (Hard)",
        "Hockey Ex: Beat Wario Factory (Hard)", "Hockey Ex: Beat Daisy Garden (Hard)",
        "Hockey Ex: Beat Bowser Jr. Blvd (Hard)", "Hockey Ex: Beat Waluigi Pinball (Hard)",
        "Hockey Ex: Beat Star Ship (Hard)", "Hockey Ex: Beat Koopa Troopa Beach (Hard)",
        "Hockey Ex: Beat Ghoulish Galleon (Hard)", "Hockey Ex: Beat Bowser's Castle (Hard)",
    ])
    h_exhibition.add_locations(hockey_ex_hard)

    hockey_ex_expert = get_location_names_with_ids([
        "Hockey Ex: Beat Mario Stadium (Expert)", "Hockey Ex: Beat Toad Park (Expert)",
        "Hockey Ex: Beat Peach's Castle (Expert)", "Hockey Ex: Beat Western Junction (Expert)",
        "Hockey Ex: Beat Wario Factory (Expert)", "Hockey Ex: Beat Daisy Garden (Expert)",
        "Hockey Ex: Beat Bowser Jr. Blvd (Expert)", "Hockey Ex: Beat Waluigi Pinball (Expert)",
        "Hockey Ex: Beat Star Ship (Expert)", "Hockey Ex: Beat Koopa Troopa Beach (Expert)",
        "Hockey Ex: Beat Ghoulish Galleon (Expert)", "Hockey Ex: Beat Bowser's Castle (Expert)",
    ])
    h_exhibition.add_locations(hockey_ex_expert)

def create_events(world: MSMWorld) -> None:
    behemoth_boss = world.get_region("Behemoth Boss Battle")
    behemoth_king_boss = world.get_region("Behemoth King Boss Battle")

    if world.options.goal_condition == GoalCondition.option_defeat_behemoth:
        behemoth_boss.add_event(
            "Defeated Behemoth!", "Victory", location_type=MSMLocation, item_type=items.MSMItem
        )

    if world.options.goal_condition == GoalCondition.option_defeat_behemoth_King:
        behemoth_king_boss.add_event(
            "Defeated Behemoth King!", "Victory", location_type=MSMLocation, item_type=items.MSMItem
        )
