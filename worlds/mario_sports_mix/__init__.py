from collections.abc import Mapping
from typing import Any, TYPE_CHECKING
from BaseClasses import Tutorial, Item, Location, Region, Rule
from worlds.AutoWorld import WebWorld, World
from .options import *
from .locations import location_table
from .items import ITEM_NAME_TO_ID


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


    location_name_to_id = {name: data.code for name, data in location_table.items() if data.code is not None}
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

    # Our world class must also have a create_item function that can create any one of our items by name at any time.
    # We also put this in a different file, the same one that create_items is in.
    def create_item(self, name: str) -> items.MSMItem:
        return items.create_item_with_correct_classification(self, name)

    # For features such as item links and panic-method start inventory, AP may ask your world to create extra filler.
    # The way it does this is by calling get_filler_item_name.
    # For this purpose, your world *must* have at least one infinitely repeatable item (usually filler).
    # You must override this function and return this infinitely repeatable item's name.
    # In our case, we defined a function called get_random_filler_item_name for this purpose in our items.py.
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    # There may be data that the game client will need to modify the behavior of the game.
    # This is what slot_data exists for. Upon every client connection, the slot's slot_data is sent to the client.
    # slot_data is just a dictionary using basic types, that will be converted to json when sent to the client.
    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return self.options.as_dict(
            "enabled_sports", "cup_difficulty", "exhibition_difficulty"
        )