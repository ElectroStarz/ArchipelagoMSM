from enum import Enum
from typing import Dict, NamedTuple, TYPE_CHECKING
from BaseClasses import Item, ItemClassification as IC
from .options import *

if TYPE_CHECKING:
    from . import MSMWorld

class MSMItem(Item):
    game: str = "Mario Sports Mix"

class ItemGroup(str, Enum):
    BASKETBALL_NORMAL_CUPS = "Basketball Normal Cups"
    BASKETBALL_HARD_CUPS = "Basketball Hard Cups"

    DODGEBALL_NORMAL_CUPS = "Dodgeball Normal Cups"
    DODGEBALL_HARD_CUPS = "Dodgeball Hard Cups"

    VOLLEYBALL_NORMAL_CUPS = "Volleyball Normal Cups"
    VOLLEYBALL_HARD_CUPS = "Volleyball Hard Cups"

    HOCKEY_NORMAL_CUPS = "Hockey Normal Cups"
    HOCKEY_HARD_CUPS = "Hockey Hard Cups"

    SPORTS_MIX_CUPS = "Sports Mix Cups"

    PROGRESSIVE_CUPS = "Progressive Cups"
    PROGRESSIVE_COURTS = "Progressive Courts"

    EXHIBITION_DIFFICULTIES = "Exhibition Difficulties"

    SPORTS = "Sports"
    SPORTS_CRYSTALS = "Sports Crystals"
    CHARACTERS = "Characters"
    COSTUMES = "Costumes"
    COURTS = "Courts"
    PANEL_ITEMS = "?-Panel Items"
    ABILITIES = "Abilities"
    FILLER = "Filler"
    TRAPS = "Traps"

    FEED_PETEY = "Feed Petey"
    HARMONY_HUSTLE = "Harmony Hustle"
    BOB_OMB_DODGE = "Bob-Omb Dodge"
    SMASH_SKATE = "Smash Skate"

class ItemData(NamedTuple):
    id: int
    classification: IC
    group: ItemGroup


base_id = 0

# Core Unlocks (1 - 99 range)
sport_items = {
    "Basketball":                        ItemData(base_id + 1, IC.progression|IC.useful, ItemGroup.SPORTS),
    "Dodgeball":                         ItemData(base_id + 2, IC.progression|IC.useful, ItemGroup.SPORTS),
    "Volleyball":                        ItemData(base_id + 3, IC.progression|IC.useful, ItemGroup.SPORTS),
    "Hockey":                            ItemData(base_id + 4, IC.progression|IC.useful, ItemGroup.SPORTS),
}

sports_mix_item = {
    "Sports Mix":                        ItemData(base_id + 5, IC.progression_skip_balancing|IC.useful, ItemGroup.SPORTS),
}

ex_difficulties = {
    "Exhibition Easy":                   ItemData(base_id + 6, IC.progression|IC.useful, ItemGroup.EXHIBITION_DIFFICULTIES),
    "Exhibition Normal":                 ItemData(base_id + 7, IC.progression|IC.useful, ItemGroup.EXHIBITION_DIFFICULTIES),
    "Exhibition Hard":                   ItemData(base_id + 8, IC.progression|IC.useful, ItemGroup.EXHIBITION_DIFFICULTIES),
    "Exhibition Expert":                 ItemData(base_id + 9, IC.progression|IC.useful, ItemGroup.EXHIBITION_DIFFICULTIES),
}

# Cups / Tournaments (100 range)
basketball_items_n = {
    "Basketball: Mushroom Cup (Normal)": ItemData(base_id + 101, IC.progression, ItemGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Flower Cup (Normal)":   ItemData(base_id + 102, IC.progression, ItemGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Star Cup (Normal)":     ItemData(base_id + 103, IC.progression, ItemGroup.BASKETBALL_NORMAL_CUPS),
}

basketball_items_h = {
    "Basketball: Mushroom Cup (Hard)":   ItemData(base_id + 111, IC.progression, ItemGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Flower Cup (Hard)":     ItemData(base_id + 112, IC.progression, ItemGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Star Cup (Hard)":       ItemData(base_id + 113, IC.progression, ItemGroup.BASKETBALL_HARD_CUPS),
}

dodgeball_items_n = {
    "Dodgeball: Mushroom Cup (Normal)":  ItemData(base_id + 121, IC.progression, ItemGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Flower Cup (Normal)":    ItemData(base_id + 122, IC.progression, ItemGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Star Cup (Normal)":      ItemData(base_id + 123, IC.progression, ItemGroup.DODGEBALL_NORMAL_CUPS),
}

dodgeball_items_h = {
    "Dodgeball: Mushroom Cup (Hard)":    ItemData(base_id + 131, IC.progression, ItemGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Flower Cup (Hard)":      ItemData(base_id + 132, IC.progression, ItemGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Star Cup (Hard)":        ItemData(base_id + 133, IC.progression, ItemGroup.DODGEBALL_HARD_CUPS),
}

volleyball_items_n = {
    "Volleyball: Mushroom Cup (Normal)": ItemData(base_id + 141, IC.progression, ItemGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Flower Cup (Normal)":   ItemData(base_id + 142, IC.progression, ItemGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Star Cup (Normal)":     ItemData(base_id + 143, IC.progression, ItemGroup.VOLLEYBALL_NORMAL_CUPS),
}

volleyball_items_h = {
    "Volleyball: Mushroom Cup (Hard)":   ItemData(base_id + 151, IC.progression, ItemGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Flower Cup (Hard)":     ItemData(base_id + 152, IC.progression, ItemGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Star Cup (Hard)":       ItemData(base_id + 153, IC.progression, ItemGroup.VOLLEYBALL_HARD_CUPS),
}

hockey_items_n = {
    "Hockey: Mushroom Cup (Normal)":     ItemData(base_id + 161, IC.progression, ItemGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Flower Cup (Normal)":       ItemData(base_id + 162, IC.progression, ItemGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Star Cup (Normal)":         ItemData(base_id + 163, IC.progression, ItemGroup.HOCKEY_NORMAL_CUPS),
}

hockey_items_h = {
    "Hockey: Mushroom Cup (Hard)":       ItemData(base_id + 171, IC.progression, ItemGroup.HOCKEY_HARD_CUPS),
    "Hockey: Flower Cup (Hard)":         ItemData(base_id + 172, IC.progression, ItemGroup.HOCKEY_HARD_CUPS),
    "Hockey: Star Cup (Hard)":           ItemData(base_id + 173, IC.progression, ItemGroup.HOCKEY_HARD_CUPS),
}

sports_mix_cups = {
    "Sports Mix: Mushroom Cup":          ItemData(base_id + 181, IC.progression_skip_balancing, ItemGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Flower Cup":            ItemData(base_id + 182, IC.progression_skip_balancing, ItemGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Star Cup":              ItemData(base_id + 183, IC.progression_skip_balancing, ItemGroup.SPORTS_MIX_CUPS),
}

# Crystals (200 range)
sports_crystals = {
    "Sports Crystal: Red":               ItemData(base_id + 201, IC.progression_skip_balancing|IC.useful, ItemGroup.SPORTS_CRYSTALS),
    "Sports Crystal: Green":             ItemData(base_id + 202, IC.progression_skip_balancing|IC.useful, ItemGroup.SPORTS_CRYSTALS),
    "Sports Crystal: Yellow":            ItemData(base_id + 203, IC.progression_skip_balancing|IC.useful, ItemGroup.SPORTS_CRYSTALS),
    "Sports Crystal: Blue":              ItemData(base_id + 204, IC.progression_skip_balancing|IC.useful, ItemGroup.SPORTS_CRYSTALS),
}

# Courts (300 range)
individual_courts = {
    "Mario Stadium":                     ItemData(base_id + 301, IC.progression, ItemGroup.COURTS),
    "Koopa Troopa Beach":                ItemData(base_id + 302, IC.progression, ItemGroup.COURTS),
    "Peach's Castle":                    ItemData(base_id + 303, IC.progression, ItemGroup.COURTS),
    "Toad Park":                         ItemData(base_id + 304, IC.progression, ItemGroup.COURTS),
    "DK Dock":                           ItemData(base_id + 305, IC.progression, ItemGroup.COURTS),
    "Luigi's Mansion":                   ItemData(base_id + 306, IC.progression, ItemGroup.COURTS),
    "Daisy Garden":                      ItemData(base_id + 307, IC.progression, ItemGroup.COURTS),
    "Wario Factory":                     ItemData(base_id + 308, IC.progression, ItemGroup.COURTS),
    "Bowser Jr. Blvd.":                  ItemData(base_id + 309, IC.progression, ItemGroup.COURTS),
    "Bowser's Castle":                   ItemData(base_id + 310, IC.progression, ItemGroup.COURTS),
    "Waluigi Pinball":                   ItemData(base_id + 311, IC.progression, ItemGroup.COURTS),
    "Ghoulish Galleon":                  ItemData(base_id + 312, IC.progression, ItemGroup.COURTS),
    "Star Ship":                         ItemData(base_id + 313, IC.progression, ItemGroup.COURTS),
    "Western Junction":                  ItemData(base_id + 314, IC.progression, ItemGroup.COURTS),
    "Behemoth Stage":                    ItemData(base_id + 315, IC.progression_skip_balancing, ItemGroup.COURTS),
}

progressive_items = {
    "Progressive Court":                 ItemData(base_id + 316, IC.progression, ItemGroup.PROGRESSIVE_COURTS),
    "Progressive Cup":                   ItemData(base_id + 317, IC.progression, ItemGroup.PROGRESSIVE_CUPS),
}

# Characters (400 range)
characters = {
    "Mario":                             ItemData(base_id + 401, IC.useful, ItemGroup.CHARACTERS),
    "Luigi":                             ItemData(base_id + 402, IC.useful, ItemGroup.CHARACTERS),
    "Peach":                             ItemData(base_id + 403, IC.useful, ItemGroup.CHARACTERS),
    "Daisy":                             ItemData(base_id + 404, IC.useful, ItemGroup.CHARACTERS),
    "Yoshi":                             ItemData(base_id + 405, IC.useful, ItemGroup.CHARACTERS),
    "Wario":                             ItemData(base_id + 406, IC.useful, ItemGroup.CHARACTERS),
    "Waluigi":                           ItemData(base_id + 407, IC.useful, ItemGroup.CHARACTERS),
    "Donkey Kong":                       ItemData(base_id + 408, IC.useful, ItemGroup.CHARACTERS),
    "Diddy Kong":                        ItemData(base_id + 409, IC.useful, ItemGroup.CHARACTERS),
    "Toad":                              ItemData(base_id + 410, IC.useful, ItemGroup.CHARACTERS),
    "Bowser":                            ItemData(base_id + 411, IC.useful, ItemGroup.CHARACTERS),
    "Bowser Jr":                         ItemData(base_id + 412, IC.useful, ItemGroup.CHARACTERS),
    "Moogle":                            ItemData(base_id + 413, IC.useful, ItemGroup.CHARACTERS),
    "Cactuar":                           ItemData(base_id + 414, IC.useful, ItemGroup.CHARACTERS),
    "Ninja":                             ItemData(base_id + 415, IC.useful, ItemGroup.CHARACTERS),
    "White Mage":                        ItemData(base_id + 416, IC.useful, ItemGroup.CHARACTERS),
    "Slime":                             ItemData(base_id + 417, IC.useful, ItemGroup.CHARACTERS),
    "Black Mage":                        ItemData(base_id + 418, IC.useful, ItemGroup.CHARACTERS),
}

# Costumes (500 range)
character_costumes = {
    "Light Blue Yoshi":                  ItemData(base_id + 501, IC.filler, ItemGroup.COSTUMES),
    "Yellow Yoshi":                      ItemData(base_id + 502, IC.filler, ItemGroup.COSTUMES),
    "Pink Yoshi":                        ItemData(base_id + 503, IC.filler, ItemGroup.COSTUMES),
    "Tennis-wear Peach":                 ItemData(base_id + 504, IC.filler, ItemGroup.COSTUMES),
    "Tennis-wear Daisy":                 ItemData(base_id + 505, IC.filler, ItemGroup.COSTUMES),
    "Blue Toad":                         ItemData(base_id + 506, IC.filler, ItemGroup.COSTUMES),
    "Yellow Toad":                       ItemData(base_id + 507, IC.filler, ItemGroup.COSTUMES),
    "Green Toad":                        ItemData(base_id + 508, IC.filler, ItemGroup.COSTUMES),
    "Shadow White Ninja":                ItemData(base_id + 509, IC.filler, ItemGroup.COSTUMES),
    "Pure White - White Mage":           ItemData(base_id + 510, IC.filler, ItemGroup.COSTUMES),
    "Magic Red Black Mage":              ItemData(base_id + 511, IC.filler, ItemGroup.COSTUMES),
    "She-Slime":                         ItemData(base_id + 512, IC.filler, ItemGroup.COSTUMES),
    "Metal Slime":                       ItemData(base_id + 513, IC.filler, ItemGroup.COSTUMES),
}

# Abilities & Panel Items (600 range)
unlockable_panel_items = {
    "? Panel: Green Shell":              ItemData(base_id + 601, IC.useful, ItemGroup.PANEL_ITEMS),
    "? Panel: Red Shell":                ItemData(base_id + 602, IC.useful, ItemGroup.PANEL_ITEMS),
    "? Panel: Banana":                   ItemData(base_id + 603, IC.useful, ItemGroup.PANEL_ITEMS),
    "? Panel: Bob-omb":                  ItemData(base_id + 604, IC.useful, ItemGroup.PANEL_ITEMS),
    "? Panel: Mini Mushroom":            ItemData(base_id + 605, IC.useful, ItemGroup.PANEL_ITEMS),
    "? Panel: Super Star":               ItemData(base_id + 606, IC.useful, ItemGroup.PANEL_ITEMS),
}

unlockable_abilities = {
    "Special Meter":                     ItemData(base_id + 610, IC.useful, ItemGroup.ABILITIES),
}

# 1 time use / Filler (700 range)
one_time_items = {
    "1 Coin":                            ItemData(base_id + 701, IC.filler, ItemGroup.FILLER),
    "1 Green Shell":                     ItemData(base_id + 702, IC.filler, ItemGroup.FILLER),
    "1 Red Shell":                       ItemData(base_id + 703, IC.filler, ItemGroup.FILLER),
    "1 Banana":                          ItemData(base_id + 704, IC.filler, ItemGroup.FILLER),
    "1 Bob-omb":                         ItemData(base_id + 705, IC.filler, ItemGroup.FILLER),
    "1 Mini Mushroom":                   ItemData(base_id + 706, IC.filler, ItemGroup.FILLER),
    "1 Super Star":                      ItemData(base_id + 707, IC.filler, ItemGroup.FILLER),
    "Special Meter Charge":              ItemData(base_id + 708, IC.filler, ItemGroup.FILLER)
}

# Traps (800 range)
traps = {
    "Coins Trap":                        ItemData(base_id + 801, IC.trap, ItemGroup.TRAPS),
    "Timer Trap":                        ItemData(base_id + 802, IC.trap, ItemGroup.TRAPS),
    "Freeze Character 1 Trap":           ItemData(base_id + 803, IC.trap, ItemGroup.TRAPS),
    "Freeze Character 2 Trap":           ItemData(base_id + 804, IC.trap, ItemGroup.TRAPS),
    "Freeze Character 3 Trap":           ItemData(base_id + 805, IC.trap, ItemGroup.TRAPS),
    "Fast Trap":                         ItemData(base_id + 806, IC.trap, ItemGroup.TRAPS),
    "Slow Trap":                         ItemData(base_id + 807, IC.trap, ItemGroup.TRAPS),
    "Teleport Character 1 Trap":         ItemData(base_id + 808, IC.trap, ItemGroup.TRAPS),
    "Teleport Character 2 Trap":         ItemData(base_id + 809, IC.trap, ItemGroup.TRAPS),
    "Teleport Character 3 Trap":         ItemData(base_id + 810, IC.trap, ItemGroup.TRAPS),
    #"Swap Trap":                         ItemData(base_id + 811, IC.trap, ItemGroup.TRAPS),
}

# Party Mode Items (900 - 1300 range)
feed_petey_items = {
    "Feed Petey":                        ItemData(base_id + 900, IC.useful, ItemGroup.FEED_PETEY)
}

harmony_hustle_items = {
    "Harmony Hustle":                    ItemData(base_id + 1000, IC.useful, ItemGroup.HARMONY_HUSTLE),
    "Classic Ocean":                     ItemData(base_id + 1001, IC.useful, ItemGroup.HARMONY_HUSTLE),
    "Chocobo Rhythm":                    ItemData(base_id + 1002, IC.useful, ItemGroup.HARMONY_HUSTLE),
    "Mario Athletic":                    ItemData(base_id + 1003, IC.useful, ItemGroup.HARMONY_HUSTLE),
    "Bloocheep Ocean":                   ItemData(base_id + 1004, IC.useful, ItemGroup.HARMONY_HUSTLE),
    "Chocobo Pop":                       ItemData(base_id + 1005, IC.useful, ItemGroup.HARMONY_HUSTLE),
    "Punk Athletic":                     ItemData(base_id + 1006, IC.useful, ItemGroup.HARMONY_HUSTLE),
    "Punk Ocean":                        ItemData(base_id + 1007, IC.useful, ItemGroup.HARMONY_HUSTLE),
    "Chocobo Beat":                      ItemData(base_id + 1008, IC.useful, ItemGroup.HARMONY_HUSTLE),
    "Island Athletic":                   ItemData(base_id + 1009, IC.useful, ItemGroup.HARMONY_HUSTLE),
}

bob_omb_dodge_items = {
    "Bob-Omb Dodge":                     ItemData(base_id + 1100, IC.useful, ItemGroup.BOB_OMB_DODGE)
}

smash_skate_items = {
    "Smash Skate":                       ItemData(base_id + 1200, IC.useful, ItemGroup.SMASH_SKATE),
    "Sherbet Sea":                       ItemData(base_id + 1201, IC.useful, ItemGroup.SMASH_SKATE),
    "Rowdy Raft":                        ItemData(base_id + 1202, IC.useful, ItemGroup.SMASH_SKATE),
    "Fire Mountain":                     ItemData(base_id + 1203, IC.useful, ItemGroup.SMASH_SKATE),
}


# Put all into a table
item_table: Dict[str, ItemData] = {
    **sport_items,
    **sports_mix_item,
    **ex_difficulties,
    **basketball_items_n,
    **basketball_items_h,
    **dodgeball_items_n,
    **dodgeball_items_h,
    **volleyball_items_n,
    **volleyball_items_h,
    **hockey_items_n,
    **hockey_items_h,
    **sports_mix_cups,
    **sports_crystals,
    **individual_courts,
    **progressive_items,
    **characters,
    **character_costumes,
    **unlockable_panel_items,
    **unlockable_abilities,
    **one_time_items,
    **traps,
    **feed_petey_items,
    **harmony_hustle_items,
    **bob_omb_dodge_items,
    **smash_skate_items,
}

ITEM_NAME_TO_ID: Dict[str, int] = {item_name: data.id for item_name, data in item_table.items()}

auto_item_groups = {}

# Loop through every single location
for item_name, item_data in item_table.items():

    # Grab the string name of the group from the Enum
    # (e.g., "Basketball Exhibition Easy")
    group_name = item_data.group.value
    # If this group isn't in our dictionary yet, create an empty set for it
    if group_name not in auto_item_groups:
        auto_item_groups[group_name] = set()

    # Add the location's name into that group's set
    auto_item_groups[group_name].add(item_name)


def get_random_filler_item_name(world: "MSMWorld") -> str:
    traps_list = [name for name in traps]
    filler_list = [name for name in one_time_items]
    if world.random.randint(0, 99) < world.options.trap_chance:
        return world.random.choice(traps_list)
    return world.random.choice(filler_list)


def create_all_items(world: "MSMWorld") -> None:
    itempool = []
    # Character costume items
    for costume in character_costumes:
        itempool.append(world.create_item(costume))

    # Unlockable panel items
    for panel in unlockable_panel_items:
        itempool.append(world.create_item(panel))

    # Unlockable abilities
    for ability in unlockable_abilities:
        itempool.append(world.create_item(ability))



    # Start with random characters option
    # This only uses the main roster as getting characters outside
    # the main roster before getting characters in the roster can bug
    # the game and make them not appear
    row_1 = ["Mario", "Peach", "Wario", "Diddy Kong"]
    row_2 = ["Luigi", "Daisy", "Donkey Kong", "Bowser Jr"]
    row_3 = ["Yoshi", "Waluigi", "Bowser", "Toad"]
    all_rows = [row_1, row_2, row_3]

    if world.options.start_with_characters == StartWithCharacters.option_2_characters:
        # Pick 2 random rows
        selected_1, selected_2 = world.random.sample(all_rows, 2)
        # Select random characters from said rows
        character_1 = world.random.choice(selected_1)
        character_2 = world.random.choice(selected_2)
        world.push_precollected(world.create_item(character_1))
        world.push_precollected(world.create_item(character_2))

        for name in characters:
            if name not in (character_1, character_2):
                itempool.append(world.create_item(name))

    elif world.options.start_with_characters == StartWithCharacters.option_3_characters:
        character_1 = world.random.choice(row_1)
        character_2 = world.random.choice(row_2)
        character_3 = world.random.choice(row_3)

        world.push_precollected(world.create_item(character_1))
        world.push_precollected(world.create_item(character_2))
        world.push_precollected(world.create_item(character_3))

        for name in characters:
            if name not in (character_1, character_2, character_3):
                itempool.append(world.create_item(name))

    else:
        for name in characters:
            itempool.append(world.create_item(name))

    # Exhibition Difficulty Items
    selected_difficulties = world.options.exhibition_difficulty.value

    for difficulty in ["Easy", "Normal", "Hard", "Expert"]:
        if difficulty in selected_difficulties:
            itempool.append(world.create_item(f"Exhibition {difficulty}"))

    enabled_sports = world.options.enabled_sports.value

    # Start with sports option
    if world.options.start_with_sports == StartWithSports.option_excluding_sports_mix:
        for sport in sport_items:
            if sport in enabled_sports:
                world.push_precollected(world.create_item(sport))

        if world.options.sports_mix_unlock == SportsMixUnlock.option_sports_mix_item:
            if "Sports Mix" in enabled_sports:
                itempool.append(world.create_item("Sports Mix"))

        elif world.options.sports_mix_unlock == SportsMixUnlock.option_sports_crystals:
            for crystal in sports_crystals:
                itempool.append(world.create_item(crystal))

    elif world.options.start_with_sports == StartWithSports.option_with_sports_mix:
        for sport in sport_items:
            if sport in enabled_sports:
                world.push_precollected(world.create_item(sport))

        if world.options.sports_mix_unlock == SportsMixUnlock.option_sports_mix_item:
            if "Sports Mix" in enabled_sports:
                world.push_precollected(world.create_item("Sports Mix"))

        elif world.options.sports_mix_unlock == SportsMixUnlock.option_sports_crystals:
            for crystal_name in sports_crystals:
                if "Sports Mix" in enabled_sports:
                    world.push_precollected(world.create_item(crystal_name))

    else:
        for sport in sport_items:
            if sport in enabled_sports:
                itempool.append(world.create_item(sport))

        if world.options.sports_mix_unlock == SportsMixUnlock.option_sports_mix_item:
            if "Sports Mix" in enabled_sports:
                itempool.append(world.create_item("Sports Mix"))

        elif world.options.sports_mix_unlock == SportsMixUnlock.option_sports_crystals:
            if "Sports Mix" in enabled_sports:
                for crystal_name in sports_crystals:
                    itempool.append(world.create_item(crystal_name))

    party_mode_to_dict = {
        "Feed Petey": feed_petey_items,
        "Harmony Hustle": harmony_hustle_items,
        "Bob-Omb Dodge": bob_omb_dodge_items,
        "Smash Skate": smash_skate_items,
    }

    # Have we enabled any party modes?
    if world.options.party_mode:

        # For every item in the enabled modes:
        for enabled in world.options.party_mode:

            # Get the dictionary of items to do with it
            create_dict = party_mode_to_dict[enabled]

            for item in create_dict:
                # Create all the items and add them to the itempool
                itempool.append(world.create_item(item))

    # Create cups based on options
    create_cups(world, itempool)

    # Create stages based on options
    create_courts(world, itempool)

    # Calculate number of filler items needed, exclude costumes

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # Submit to multiworld
    #print(itempool)
    world.multiworld.itempool += itempool


def create_courts(world: "MSMWorld", itempool):
    if world.options.court_unlock_type == CourtUnlockType.option_court_item:
        if world.options.start_with_mushroom_cup != StartWithMushroomCup.option_none:
            mush_courts = ["Mario Stadium", "Koopa Troopa Beach", "DK Dock", "Peach's Castle", "Toad Park"]
            for court in mush_courts:
                world.push_precollected(world.create_item(court))

            other_courts = ["Luigi's Mansion", "Daisy Garden", "Wario Factory", "Bowser Jr. Blvd.", "Bowser's Castle",
                            "Waluigi Pinball", "Ghoulish Galleon", "Star Ship", "Western Junction", "Behemoth Stage"]
            for court in other_courts:
                itempool.append(world.create_item(court))
        else:
            for court in individual_courts:
                itempool.append(world.create_item(court))

    elif world.options.court_unlock_type == CourtUnlockType.option_progressive_court:
        total_stages = 15

        if world.options.start_with_mushroom_cup != StartWithMushroomCup.option_none:
            # Precollect the first 5 progressive items
            for _ in range(5):
                world.push_precollected(world.create_item("Progressive Court"))

            # Put the remaining 10 items into the item pool
            for _ in range(total_stages - 5):
                itempool.append(world.create_item("Progressive Court"))
        else:
            # Put all 15 progressive items directly into the pool
            for _ in range(total_stages):
                itempool.append(world.create_item("Progressive Court"))

def create_cups(world: "MSMWorld", itempool):
    enabled_sports = world.options.enabled_sports.value

    # --- Progressive Cups ---
    if world.options.cup_unlock_type == CupUnlockType.option_progressive_cup:
        # Base: 3 Standard Cups (Mushroom, Flower, Star)
        total_progressive_cups = 3

        # If Hard mode is enabled, add 3 more for the Hard Tournament tiers
        if world.options.hard_tournament_difficulty:
            total_progressive_cups += 3  # 6 items

        if "Sports Mix" in enabled_sports:
            total_progressive_cups += 3 # 9 items max

        start_option = world.options.start_with_mushroom_cup

        # Determine how many starting levels the player gets for free
        precollected_count = 0
        if start_option == StartWithMushroomCup.option_normal_difficulty:
            precollected_count = 1  # Starts with Tier 1
        elif start_option == StartWithMushroomCup.option_hard_difficulty:
            precollected_count = 1  # Starts with Tier 1
        elif start_option == StartWithMushroomCup.option_both:
            precollected_count = 2  # Starts with Tier 1 and Tier 2 equivalent

        # Push free starting levels to inventory
        for _ in range(precollected_count):
            world.push_precollected(world.create_item("Progressive Cup"))

        # Fill the multiworld pool with the rest of the progressive items
        remaining_cups = total_progressive_cups - precollected_count
        for _ in range(remaining_cups):
            itempool.append(world.create_item("Progressive Cup"))


    # --- Individual Cups ---
    else:
        all_normal_items = {
                **basketball_items_n, **dodgeball_items_n, **volleyball_items_n, **hockey_items_n
        }
        all_hard_items = {
                **basketball_items_h, **dodgeball_items_h, **volleyball_items_h, **hockey_items_h
        }

        precollect_names = set()
        start_option = world.options.start_with_mushroom_cup

        if start_option in (StartWithMushroomCup.option_normal_difficulty, StartWithMushroomCup.option_both):
            precollect_names.update([
                "Basketball: Mushroom Cup (Normal)", "Dodgeball: Mushroom Cup (Normal)",
                "Volleyball: Mushroom Cup (Normal)", "Hockey: Mushroom Cup (Normal)"
            ])

        if start_option in (StartWithMushroomCup.option_hard_difficulty, StartWithMushroomCup.option_both):
            precollect_names.update([
                "Basketball: Mushroom Cup (Hard)", "Dodgeball: Mushroom Cup (Hard)",
                "Volleyball: Mushroom Cup (Hard)", "Hockey: Mushroom Cup (Hard)"
            ])

        prefix_to_sport = {"B": "Basketball", "D": "Dodgeball", "V": "Volleyball", "H": "Hockey"}

        # Push free individual starting items
        for name in precollect_names:
            sport = prefix_to_sport[name[:1]]
            if sport in enabled_sports:
                world.push_precollected(world.create_item(name))

        # Add Normal Cups to the pool
        for name in all_normal_items:
            sport = prefix_to_sport[name[:1]]
            if sport in enabled_sports:
                if name not in precollect_names:
                    itempool.append(world.create_item(name))

        # Add Hard Cups to the pool (if enabled)
        if world.options.hard_tournament_difficulty:
            for name in all_hard_items:
                sport = prefix_to_sport[name[:1]]
                if sport in enabled_sports:
                    if name not in precollect_names:
                        itempool.append(world.create_item(name))

        # Sports Mix Cups
        if "Sports Mix" in enabled_sports:
            for cup in sports_mix_cups:
                itempool.append(world.create_item(cup))

def create_item_with_correct_classification(world: "MSMWorld", name: str) -> MSMItem:
    classification = item_table[name].classification

    # Character Sanity (Characters)
    if (world.options.character_sanity == CharacterSanity.option_characters or
        world.options.character_sanity == CharacterSanity.option_characters_and_costumes):
        if name in characters:
            classification = IC.progression

    # Character Sanity (Costumes)
    if world.options.character_sanity == CharacterSanity.option_characters_and_costumes:
        if name in character_costumes:
            classification = IC.progression

    return MSMItem(name, classification, ITEM_NAME_TO_ID[name], world.player)