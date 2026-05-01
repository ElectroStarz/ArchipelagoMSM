from collections.abc import Mapping
from typing import Any, TYPE_CHECKING
from BaseClasses import Tutorial, Item, Location, Region
from worlds.AutoWorld import WebWorld, World
from . import regions, rules
from .options import *
from .items import ITEM_NAME_TO_ID
from . import locations


class MSMWebWorld(WebWorld):
    game = "Mario Sports Mix"

    # dirt, grass, grassFlowers, ice, jungle, ocean, partyTime, and stone.
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
    Mario Sports Mix is a fast-paced Wii sports game that includes basketball, volleyball, dodgeball, and hockey.
    Play as characters from the Mario, Final Fantasy and Dragon Quest franchise in order to defeat the evil in this
    land and conquer all the sports!
    """
    game = "Mario Sports Mix"
    web = MSMWebWorld()

    options_dataclass = MSMOptions
    options: MSMOptions


    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID


    origin_region_name = "Main Menu"


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
            "cup_difficulty", "exhibition_difficulty", "goal_condition", "behemoth_hp", "behemoth_king_hp",
            "special_sanity", "sports_mix_unlock", "deathlink_toggle", "deathlink_action", "deathlink_consequence"
        )
