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

    SPORTS = "Sports"
    SPORTS_CRYSTALS = "Sports Crystals"
    CHARACTERS = "Characters"
    COSTUMES = "Costumes"
    COURTS = "Courts"
    PANEL_ITEMS = "?-Panel Items"
    ABILITIES = "Abilities"
    FILLER = "Filler"
    TRAPS = "Traps"

class ItemData(NamedTuple):
    id: int
    classification: IC
    group: ItemGroup


base_id = 1

sport_items = {
    "Basketball": ItemData(base_id + 0, IC.progression|IC.useful, ItemGroup.SPORTS),
    "Dodgeball": ItemData(base_id + 1, IC.progression|IC.useful, ItemGroup.SPORTS),
    "Volleyball": ItemData(base_id + 2, IC.progression|IC.useful, ItemGroup.SPORTS),
    "Hockey": ItemData(base_id + 3, IC.progression|IC.useful, ItemGroup.SPORTS),
}

sports_mix_item = {
    "Sports Mix": ItemData(base_id + 4, IC.progression_skip_balancing|IC.useful, ItemGroup.SPORTS)
}

basketball_items_n = {
    "Basketball: Mushroom Cup (Normal)": ItemData(base_id + 5, IC.progression, ItemGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Flower Cup (Normal)": ItemData(base_id + 6, IC.progression, ItemGroup.BASKETBALL_NORMAL_CUPS),
    "Basketball: Star Cup (Normal)": ItemData(base_id + 7, IC.progression, ItemGroup.BASKETBALL_NORMAL_CUPS),
}

basketball_items_h = {
    "Basketball: Mushroom Cup (Hard)": ItemData(base_id + 8, IC.progression, ItemGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Flower Cup (Hard)": ItemData(base_id + 9, IC.progression, ItemGroup.BASKETBALL_HARD_CUPS),
    "Basketball: Star Cup (Hard)": ItemData(base_id + 10, IC.progression, ItemGroup.BASKETBALL_HARD_CUPS)
}

dodgeball_items_n = {
    "Dodgeball: Mushroom Cup (Normal)": ItemData(base_id + 11, IC.progression, ItemGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Flower Cup (Normal)": ItemData(base_id + 12, IC.progression, ItemGroup.DODGEBALL_NORMAL_CUPS),
    "Dodgeball: Star Cup (Normal)": ItemData(base_id + 13, IC.progression, ItemGroup.DODGEBALL_NORMAL_CUPS)
}

dodgeball_items_h = {
    "Dodgeball: Mushroom Cup (Hard)": ItemData(base_id + 14, IC.progression, ItemGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Flower Cup (Hard)": ItemData(base_id + 15, IC.progression, ItemGroup.DODGEBALL_HARD_CUPS),
    "Dodgeball: Star Cup (Hard)": ItemData(base_id + 16, IC.progression, ItemGroup.DODGEBALL_HARD_CUPS)
}

volleyball_items_n = {
    "Volleyball: Mushroom Cup (Normal)": ItemData(base_id + 17, IC.progression, ItemGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Flower Cup (Normal)": ItemData(base_id + 18, IC.progression, ItemGroup.VOLLEYBALL_NORMAL_CUPS),
    "Volleyball: Star Cup (Normal)": ItemData(base_id + 19, IC.progression, ItemGroup.VOLLEYBALL_NORMAL_CUPS)
}

volleyball_items_h = {
    "Volleyball: Mushroom Cup (Hard)": ItemData(base_id + 20, IC.progression, ItemGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Flower Cup (Hard)": ItemData(base_id + 21, IC.progression, ItemGroup.VOLLEYBALL_HARD_CUPS),
    "Volleyball: Star Cup (Hard)": ItemData(base_id + 22, IC.progression, ItemGroup.VOLLEYBALL_HARD_CUPS)
}

hockey_items_n = {
    "Hockey: Mushroom Cup (Normal)": ItemData(base_id + 23, IC.progression, ItemGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Flower Cup (Normal)": ItemData(base_id + 24, IC.progression, ItemGroup.HOCKEY_NORMAL_CUPS),
    "Hockey: Star Cup (Normal)": ItemData(base_id + 25, IC.progression, ItemGroup.HOCKEY_NORMAL_CUPS)
}

hockey_items_h = {
    "Hockey: Mushroom Cup (Hard)": ItemData(base_id + 26, IC.progression, ItemGroup.HOCKEY_HARD_CUPS),
    "Hockey: Flower Cup (Hard)": ItemData(base_id + 27, IC.progression, ItemGroup.HOCKEY_HARD_CUPS),
    "Hockey: Star Cup (Hard)": ItemData(base_id + 28, IC.progression, ItemGroup.HOCKEY_HARD_CUPS)
}

sports_mix_cups = {
    "Sports Mix: Mushroom Cup": ItemData(base_id + 29, IC.progression_skip_balancing, ItemGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Flower Cup": ItemData(base_id + 30, IC.progression_skip_balancing, ItemGroup.SPORTS_MIX_CUPS),
    "Sports Mix: Star Cup": ItemData(base_id + 31, IC.progression_skip_balancing, ItemGroup.SPORTS_MIX_CUPS)
}

sports_crystals = {
    "Sports Crystal: Red": ItemData(base_id + 32, IC.progression_skip_balancing|IC.useful, ItemGroup.SPORTS_CRYSTALS),
    "Sports Crystal: Green": ItemData(base_id + 33, IC.progression_skip_balancing|IC.useful, ItemGroup.SPORTS_CRYSTALS),
    "Sports Crystal: Yellow": ItemData(base_id + 34, IC.progression_skip_balancing|IC.useful, ItemGroup.SPORTS_CRYSTALS),
    "Sports Crystal: Blue": ItemData(base_id + 35, IC.progression_skip_balancing|IC.useful, ItemGroup.SPORTS_CRYSTALS),
}

individual_stages = {
    "Mario Stadium": ItemData(base_id + 100, IC.progression, ItemGroup.COURTS),
    "Koopa Troopa Beach": ItemData(base_id + 101, IC.progression, ItemGroup.COURTS),
    "Peach's Castle": ItemData(base_id + 102, IC.progression, ItemGroup.COURTS),
    "Toad Park": ItemData(base_id + 103, IC.progression, ItemGroup.COURTS),
    "DK Dock": ItemData(base_id + 104, IC.progression, ItemGroup.COURTS),
    "Luigi's Mansion": ItemData(base_id + 105, IC.progression, ItemGroup.COURTS),
    "Daisy Garden": ItemData(base_id + 106, IC.progression, ItemGroup.COURTS),
    "Wario Factory": ItemData(base_id + 107, IC.progression, ItemGroup.COURTS),
    "Bowser Jr. Blvd.": ItemData(base_id + 108, IC.progression, ItemGroup.COURTS),
    "Bowser's Castle": ItemData(base_id + 109, IC.progression, ItemGroup.COURTS),
    "Waluigi Pinball": ItemData(base_id + 110, IC.progression, ItemGroup.COURTS),
    "Ghoulish Galleon": ItemData(base_id + 111, IC.progression, ItemGroup.COURTS),
    "Star Ship": ItemData(base_id + 112, IC.progression, ItemGroup.COURTS),
    "Western Junction": ItemData(base_id + 113, IC.progression, ItemGroup.COURTS),
    "Behemoth Stage": ItemData(base_id + 114, IC.progression_skip_balancing, ItemGroup.COURTS),
}

progressive_stuff = {
    # "Progressive: Team Size": ItemData(base_id + 120, IC.progression|IC.useful),
    # "Progressive: Team Size": ItemData(base_id + 121, IC.progression|IC.useful),

}

characters = {
    "Mario": ItemData(base_id + 200, IC.useful, ItemGroup.CHARACTERS),
    "Luigi": ItemData(base_id + 201, IC.useful, ItemGroup.CHARACTERS),
    "Peach": ItemData(base_id + 202, IC.useful, ItemGroup.CHARACTERS),
    "Daisy": ItemData(base_id + 203, IC.useful, ItemGroup.CHARACTERS),
    "Yoshi": ItemData(base_id + 204, IC.useful, ItemGroup.CHARACTERS),
    "Wario": ItemData(base_id + 205, IC.useful, ItemGroup.CHARACTERS),
    "Waluigi": ItemData(base_id + 206, IC.useful, ItemGroup.CHARACTERS),
    "Donkey Kong": ItemData(base_id + 207, IC.useful, ItemGroup.CHARACTERS),
    "Diddy Kong": ItemData(base_id + 208, IC.useful, ItemGroup.CHARACTERS),
    "Toad": ItemData(base_id + 209, IC.useful, ItemGroup.CHARACTERS),
    "Bowser": ItemData(base_id + 210, IC.useful, ItemGroup.CHARACTERS),
    "Bowser Jr": ItemData(base_id + 211, IC.useful, ItemGroup.CHARACTERS),
    "Moogle": ItemData(base_id + 212, IC.useful, ItemGroup.CHARACTERS),
    "Cactuar": ItemData(base_id + 213, IC.useful, ItemGroup.CHARACTERS),
    "Ninja": ItemData(base_id + 214, IC.useful, ItemGroup.CHARACTERS),
    "White Mage": ItemData(base_id + 215, IC.useful, ItemGroup.CHARACTERS),
    "Slime": ItemData(base_id + 216, IC.useful, ItemGroup.CHARACTERS),
    "Black Mage": ItemData(base_id + 217, IC.useful, ItemGroup.CHARACTERS),
}

character_costumes = {
    "Light Blue Yoshi": ItemData(base_id + 218, IC.filler, ItemGroup.COSTUMES),
    "Yellow Yoshi": ItemData(base_id + 219, IC.filler, ItemGroup.COSTUMES),
    "Pink Yoshi": ItemData(base_id + 220, IC.filler, ItemGroup.COSTUMES),
    "Tennis-wear Peach": ItemData(base_id + 221, IC.filler, ItemGroup.COSTUMES),
    "Tennis-wear Daisy": ItemData(base_id + 222, IC.filler, ItemGroup.COSTUMES),
    "Blue Toad": ItemData(base_id + 223, IC.filler, ItemGroup.COSTUMES),
    "Yellow Toad": ItemData(base_id + 224, IC.filler, ItemGroup.COSTUMES),
    "Green Toad": ItemData(base_id + 225, IC.filler, ItemGroup.COSTUMES),
    "Shadow White Ninja": ItemData(base_id + 226, IC.filler, ItemGroup.COSTUMES),
    "Pure White - White Mage": ItemData(base_id + 227,IC.filler, ItemGroup.COSTUMES),
    "Magic Red Black Mage": ItemData(base_id + 228,IC.filler, ItemGroup.COSTUMES),
    "She-Slime": ItemData(base_id + 229, IC.filler, ItemGroup.COSTUMES),
    "Metal Slime": ItemData(base_id + 230, IC.filler, ItemGroup.COSTUMES),
}

# Able to use once unlocked
unlockable_panel_items = {
    "? Panel: Green Shell": ItemData(base_id + 300, IC.useful, ItemGroup.PANEL_ITEMS),
    "? Panel: Red Shell": ItemData(base_id + 301, IC.useful, ItemGroup.PANEL_ITEMS),
    "? Panel: Banana": ItemData(base_id + 302, IC.useful, ItemGroup.PANEL_ITEMS),
    "? Panel: Bob-omb": ItemData(base_id + 303, IC.useful, ItemGroup.PANEL_ITEMS),
    "? Panel: Mini Mushroom": ItemData(base_id + 304, IC.useful, ItemGroup.PANEL_ITEMS),
    "? Panel: Super Star": ItemData(base_id + 305, IC.useful, ItemGroup.PANEL_ITEMS),
}

unlockable_abilities = {
    "Special Meter": ItemData(base_id + 307, IC.useful, ItemGroup.ABILITIES),
}

# One time use
one_time_items = {
    "1 Coin": ItemData(base_id + 400, IC.filler, ItemGroup.FILLER),
    "1 Green Shell": ItemData(base_id + 401, IC.filler, ItemGroup.FILLER),
    "1 Red Shell": ItemData(base_id + 402, IC.filler, ItemGroup.FILLER),
    "1 Banana": ItemData(base_id + 403, IC.filler, ItemGroup.FILLER),
    "1 Bob-omb": ItemData(base_id + 404, IC.filler, ItemGroup.FILLER),
    "1 Mini Mushroom": ItemData(base_id + 405, IC.filler, ItemGroup.FILLER),
    "1 Super Star": ItemData(base_id + 406, IC.filler, ItemGroup.FILLER),
}

traps = {
    "Coins Trap": ItemData(base_id + 500, IC.trap, ItemGroup.TRAPS),
    #"Hit Stun": ItemData(base_id + 501, IC.trap, ItemGroup.TRAPS),
    "Timer Trap": ItemData(base_id + 502, IC.trap, ItemGroup.TRAPS),
    "Freeze Character 1 Trap": ItemData(base_id + 503, IC.trap, ItemGroup.TRAPS),
    "Freeze Character 2 Trap": ItemData(base_id + 504, IC.trap, ItemGroup.TRAPS),
    "Freeze Character 3 Trap": ItemData(base_id + 505, IC.trap, ItemGroup.TRAPS),
}


# Put all into a table
item_table: Dict[str, ItemData] = {
    **sport_items,
    **sports_mix_item,
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
    **individual_stages,
    **progressive_stuff,
    **characters,
    **character_costumes,
    **unlockable_panel_items,
    **unlockable_abilities,
    **one_time_items,
    **traps,
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
    traps_list = [name for name, data in traps.items()]
    filler_list = [name for name, data in one_time_items.items()]
    if world.random.randint(0, 99) < world.options.trap_chance:
        return world.random.choice(traps_list)
    return world.random.choice(filler_list)


def create_all_items(world: "MSMWorld") -> None:
    itempool = []
    # Character costume items
    for name, data in character_costumes.items():
        new_item = world.create_item(name)
        itempool.append(new_item)
    # Unlockable panel items
    for name, data in unlockable_panel_items.items():
        new_item = world.create_item(name)
        itempool.append(new_item)
    # Unlockable abilities
    for name, data in unlockable_abilities.items():
        new_item = world.create_item(name)
        itempool.append(new_item)
    # Items in the progressive stuff dict - Does nothing right now
    for name, data in progressive_stuff.items():
        new_item = world.create_item(name)
        itempool.append(new_item)

    # Sports Mix Cups
    for name, data in sports_mix_cups.items():
        new_item = world.create_item(name)
        itempool.append(new_item)

    # Start with random characters option
    row_1 = ["Mario", "Peach", "Wario", "Diddy Kong"]
    row_2 = ["Luigi", "Daisy", "Donkey Kong", "Bowser Jr"]
    row_3 = ["Yoshi", "Waluigi", "Bowser", "Toad"]
    all_rows = [row_1, row_2, row_3]

    if world.options.start_with_characters == StartWithCharacters.option_2_characters:
        selected_1, selected_2 = world.random.sample(all_rows, 2)
        character_1 = world.random.choice(selected_1)
        character_2 = world.random.choice(selected_2)
        item_1 = world.create_item(character_1)
        item_2 = world.create_item(character_2)
        world.push_precollected(item_1)
        world.push_precollected(item_2)

        for name, data in characters.items():
            if name not in (character_1, character_2):
                new_item = world.create_item(name)
                itempool.append(new_item)

    elif world.options.start_with_characters == StartWithCharacters.option_3_characters:
        character_1 = world.random.choice(row_1)
        character_2 = world.random.choice(row_2)
        character_3 = world.random.choice(row_3)
        item_1 = world.create_item(character_1)
        item_2 = world.create_item(character_2)
        item_3 = world.create_item(character_3)
        world.push_precollected(item_1)
        world.push_precollected(item_2)
        world.push_precollected(item_3)

        for name, data in characters.items():
            if name not in (character_1, character_2, character_3):
                new_item = world.create_item(name)
                itempool.append(new_item)

    else:
        for name, data in characters.items():
            new_item = world.create_item(name)
            itempool.append(new_item)


    # Start with sports option
    if world.options.start_with_sports == StartWithSports.option_excluding_sports_mix:
        basketball = world.create_item("Basketball")
        world.push_precollected(basketball)
        dodgeball = world.create_item("Dodgeball")
        world.push_precollected(dodgeball)
        volleyball = world.create_item("Volleyball")
        world.push_precollected(volleyball)
        hockey = world.create_item("Hockey")
        world.push_precollected(hockey)
        if world.options.sports_mix_unlock == SportsMixUnlock.option_sports_mix_item:
            sports_mix = world.create_item("Sports Mix")
            itempool.append(sports_mix)
        elif world.options.sports_mix_unlock == SportsMixUnlock.option_sports_crystals:
            for name, data in sports_crystals.items():
                new_item = world.create_item(name)
                itempool.append(new_item)

    elif world.options.start_with_sports == StartWithSports.option_with_sports_mix:
        basketball = world.create_item("Basketball")
        world.push_precollected(basketball)
        dodgeball = world.create_item("Dodgeball")
        world.push_precollected(dodgeball)
        volleyball = world.create_item("Volleyball")
        world.push_precollected(volleyball)
        hockey = world.create_item("Hockey")
        world.push_precollected(hockey)
        if world.options.sports_mix_unlock == SportsMixUnlock.option_sports_mix_item:
            sports_mix = world.create_item("Sports Mix")
            world.push_precollected(sports_mix)
        elif world.options.sports_mix_unlock == SportsMixUnlock.option_sports_crystals:
            for crystal_name, crystal_data in sports_crystals.items():
                new_item = world.create_item(crystal_name)
                world.push_precollected(new_item)

    else:
        for name, data in sport_items.items():
            new_item = world.create_item(name)
            itempool.append(new_item)
            if world.options.sports_mix_unlock == SportsMixUnlock.option_sports_mix_item:
                sports_mix = world.create_item("Sports Mix")
                itempool.append(sports_mix)
            elif world.options.sports_mix_unlock == SportsMixUnlock.option_sports_crystals:
                for crystal_name, crystal_data in sports_crystals.items():
                    new_item = world.create_item(crystal_name)
                    itempool.append(new_item)


    # Start with mushroom cup option
    if world.options.start_with_mushroom_cup == StartWithMushroomCup.option_normal_difficulty:
        norm_mush_items = ["Basketball: Mushroom Cup (Normal)", "Dodgeball: Mushroom Cup (Normal)",
                           "Volleyball: Mushroom Cup (Normal)", "Hockey: Mushroom Cup (Normal)"]
        for name in norm_mush_items:
            new_item = world.create_item(name)
            world.push_precollected(new_item)

        mush_stages = ["Mario Stadium", "Koopa Troopa Beach", "DK Dock", "Peach's Castle", "Toad Park"]
        for name in mush_stages:
            new_item = world.create_item(name)
            world.push_precollected(new_item)

        # Basketball
        # Create items that aren't in precollected
        for name, data in basketball_items_n.items():
            if name not in norm_mush_items:
                new_item = world.create_item(name)
                itempool.append(new_item)

        # Dodgeball
        for name, data in dodgeball_items_n.items():
            if name not in norm_mush_items:
                new_item = world.create_item(name)
                itempool.append(new_item)

        # Volleyball
        for name, data in volleyball_items_n.items():
            if name not in norm_mush_items:
                new_item = world.create_item(name)
                itempool.append(new_item)

        # Hockey
        for name, data in hockey_items_n.items():
            if name not in norm_mush_items:
                new_item = world.create_item(name)
                itempool.append(new_item)


        if world.options.hard_tournament_difficulty == HardTournamentDifficulty.option_true:
            # Basketball Hard items
            for name, data in basketball_items_h.items():
                new_item = world.create_item(name)
                itempool.append(new_item)

            # Dodgeball Hard items
            for name, data in dodgeball_items_h.items():
                new_item = world.create_item(name)
                itempool.append(new_item)

            # Volleyball Hard items
            for name, data in volleyball_items_h.items():
                new_item = world.create_item(name)
                itempool.append(new_item)

            # Hockey Hard items
            for name, data in hockey_items_h.items():
                new_item = world.create_item(name)
                itempool.append(new_item)


        # Create items for actual stages
        other_stages = ["Luigi's Mansion","Daisy Garden", "Wario Factory", "Bowser Jr. Blvd.", "Bowser's Castle",
                        "Waluigi Pinball", "Ghoulish Galleon", "Star Ship", "Western Junction", "Behemoth Stage"]

        for name in other_stages:
            new_item = world.create_item(name)
            itempool.append(new_item)

    elif world.options.start_with_mushroom_cup == StartWithMushroomCup.option_hard_difficulty:
        hard_mush_items = ["Basketball: Mushroom Cup (Hard)", "Dodgeball: Mushroom Cup (Hard)",
                           "Volleyball: Mushroom Cup (Hard)", "Hockey: Mushroom Cup (Hard)"]
        for name in hard_mush_items:
            new_item = world.create_item(name)
            world.push_precollected(new_item)

        mush_stages = ["Mario Stadium", "Koopa Troopa Beach", "DK Dock", "Peach's Castle", "Toad Park"]
        for name in mush_stages:
            new_item = world.create_item(name)
            world.push_precollected(new_item)

        # Basketball
        for name, data in basketball_items_n.items():
            new_item = world.create_item(name)
            itempool.append(new_item)

        # Dodgeball
        for name, data in dodgeball_items_n.items():
            new_item = world.create_item(name)
            itempool.append(new_item)

        # Volleyball
        for name, data in volleyball_items_n.items():
            new_item = world.create_item(name)
            itempool.append(new_item)

        # Hockey
        for name, data in hockey_items_n.items():
            new_item = world.create_item(name)
            itempool.append(new_item)


        if world.options.hard_tournament_difficulty == HardTournamentDifficulty.option_true:
            # Basketball Hard items
            for name, data in basketball_items_h.items():
                if name not in hard_mush_items:
                    new_item = world.create_item(name)
                    itempool.append(new_item)
            # Dodgeball Hard items
            for name, data in dodgeball_items_h.items():
                if name not in hard_mush_items:
                    new_item = world.create_item(name)
                    itempool.append(new_item)
            # Volleyball Hard items
            for name, data in volleyball_items_h.items():
                if name not in hard_mush_items:
                    new_item = world.create_item(name)
                    itempool.append(new_item)
            # Hockey Hard items
            for name, data in hockey_items_h.items():
                if name not in hard_mush_items:
                    new_item = world.create_item(name)
                    itempool.append(new_item)

        # Create items for actual stages
        other_stages = ["Luigi's Mansion","Daisy Garden", "Wario Factory", "Bowser Jr. Blvd.", "Bowser's Castle",
                        "Waluigi Pinball", "Ghoulish Galleon", "Star Ship", "Western Junction", "Behemoth Stage"]

        for name in other_stages:
            new_item = world.create_item(name)
            itempool.append(new_item)

    elif world.options.start_with_mushroom_cup == StartWithMushroomCup.option_both:
        # Push mushroom cups to precollected
        norm_mush_items = ["Basketball: Mushroom Cup (Normal)", "Dodgeball: Mushroom Cup (Normal)",
                           "Volleyball: Mushroom Cup (Normal)", "Hockey: Mushroom Cup (Normal)"]
        for name in norm_mush_items:
            new_item = world.create_item(name)
            world.push_precollected(new_item)

        hard_mush_items = ["Basketball: Mushroom Cup (Hard)", "Dodgeball: Mushroom Cup (Hard)",
                           "Volleyball: Mushroom Cup (Hard)", "Hockey: Mushroom Cup (Hard)"]
        for name in hard_mush_items:
            new_item = world.create_item(name)
            world.push_precollected(new_item)

        # Push stages to do with mushroom cup to precollected
        mush_stages = ["Mario Stadium", "Koopa Troopa Beach", "DK Dock", "Peach's Castle", "Toad Park"]
        for name in mush_stages:
            new_item = world.create_item(name)
            world.push_precollected(new_item)

        # Create items for actual stages
        other_stages = ["Luigi's Mansion","Daisy Garden", "Wario Factory", "Bowser Jr. Blvd.", "Bowser's Castle",
                        "Waluigi Pinball", "Ghoulish Galleon", "Star Ship", "Western Junction", "Behemoth Stage"]

        for name in other_stages:
            new_item = world.create_item(name)
            itempool.append(new_item)


        # Create items for other items not being pushed
        # Basketball
        for name, data in basketball_items_n.items():
            if name not in norm_mush_items:
                new_item = world.create_item(name)
                itempool.append(new_item)

        # Dodgeball
        for name, data in dodgeball_items_n.items():
            if name not in norm_mush_items:
                new_item = world.create_item(name)
                itempool.append(new_item)

        # Volleyball
        for name, data in volleyball_items_n.items():
            if name not in norm_mush_items:
                new_item = world.create_item(name)
                itempool.append(new_item)

        # Hockey
        for name, data in hockey_items_n.items():
            if name not in norm_mush_items:
                new_item = world.create_item(name)
                itempool.append(new_item)

        if world.options.hard_tournament_difficulty == HardTournamentDifficulty.option_true:
            # Basketball Hard items
            for name, data in basketball_items_h.items():
                if name not in hard_mush_items:
                    new_item = world.create_item(name)
                    itempool.append(new_item)
            # Dodgeball Hard items
            for name, data in dodgeball_items_h.items():
                if name not in hard_mush_items:
                    new_item = world.create_item(name)
                    itempool.append(new_item)
            # Volleyball Hard items
            for name, data in volleyball_items_h.items():
                if name not in hard_mush_items:
                    new_item = world.create_item(name)
                    itempool.append(new_item)
            # Hockey Hard items
            for name, data in hockey_items_h.items():
                if name not in hard_mush_items:
                    new_item = world.create_item(name)
                    itempool.append(new_item)

        else:
            # Basketball
            for name, data in basketball_items_n.items():
                new_item = world.create_item(name)
                itempool.append(new_item)
            # Dodgeball
            for name, data in dodgeball_items_n.items():
                new_item = world.create_item(name)
                itempool.append(new_item)
            # Volleyball
            for name, data in volleyball_items_n.items():
                new_item = world.create_item(name)
                itempool.append(new_item)
            # Hockey
            for name, data in hockey_items_n.items():
                new_item = world.create_item(name)
                itempool.append(new_item)

            if world.options.hard_tournament_difficulty == HardTournamentDifficulty.option_true:
                # Basketball Hard items
                for name, data in basketball_items_h.items():
                    new_item = world.create_item(name)
                    itempool.append(new_item)
                # Dodgeball Hard items
                for name, data in dodgeball_items_h.items():
                    new_item = world.create_item(name)
                    itempool.append(new_item)
                # Volleyball Hard items
                for name, data in volleyball_items_h.items():
                    new_item = world.create_item(name)
                    itempool.append(new_item)
                # Hockey Hard items
                for name, data in hockey_items_h.items():
                    new_item = world.create_item(name)
                    itempool.append(new_item)

            # Stages
            for name, data in individual_stages.items():
                new_item = world.create_item(name)
                itempool.append(new_item)


    # Calculate number of filler items needed, exclude costumes

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # Submit to multiworld
    #print(itempool)
    world.multiworld.itempool += itempool


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