from collections.abc import Mapping
from typing import Any, TYPE_CHECKING
from BaseClasses import Tutorial, Item, Location, Region
from worlds.AutoWorld import WebWorld, World
from . import regions, rules
from .options import *
from .items import ITEM_NAME_TO_ID
from . import locations


# For our game to display correctly on the website, we need to define a WebWorld subclass.
class MSMWebWorld(WebWorld):
    game = "Mario Sports Mix"

    # You can choose between dirt, grass, grassFlowers, ice, jungle, ocean, partyTime, and stone.
    theme = "partyTime"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Mario Sports Mix for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["ElectroStarz"],
    )
    tutorials = [setup_en]
    option_groups = msm_option_groups



class MSMWorld(World):
    """
    Mario Sports Mix is a fast-paced Wii sports game featuring basketball, volleyball, dodgeball
    and hockey, with characters using power-ups and special moves for chaotic gameplay.
    """
    game = "Mario Sports Mix"
    web = MSMWebWorld()

    options_dataclass = MSMOptions
    options: MSMOptions

    # Our world class must have a static location_name_to_id and item_name_to_id defined.
    # We define these in regions.py and items.py respectively, so we just set them here.


    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    # There is always one region that the generator starts from & assumes you can always go back to.
    # This defaults to "Menu", but you can change it by overriding origin_region_name.
    origin_region_name = "Main Menu"

    # Our world class must have certain functions ("steps") that get called during generation.
    # The main ones are: create_regions, set_rules, create_items.
    # For better structure and readability, we put each of these in their own file.
    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)


    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.MSMItem:
        return items.create_item_with_correct_classification(self, name)


    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

   # Stuff to send to the client because it needs to know that
    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "cup_difficulty", "goal_condition", "special_sanity"
        )