from typing import Dict, NamedTuple, TYPE_CHECKING, Optional
from BaseClasses import Item, ItemClassification
from .options import StageUnlockType

if TYPE_CHECKING:
    from .world import MSMWorld

class MSMItem(Item):
    game: str = "Mario Sports Mix"

class ItemData(NamedTuple):
    code: int
    classification: ItemClassification

base_id = 0

sport_items = {
    "Sport: Basketball": ItemData(base_id + 0, ItemClassification.progression|ItemClassification.useful),
    "Sport: Dodgeball": ItemData(base_id + 1, ItemClassification.progression|ItemClassification.useful),
    "Sport: Volleyball": ItemData(base_id + 2, ItemClassification.progression|ItemClassification.useful),
    "Sport: Hockey": ItemData(base_id + 3, ItemClassification.progression|ItemClassification.useful),
    "Sport: Sports Mix": ItemData(base_id + 4, ItemClassification.progression_skip_balancing|ItemClassification.useful),
}

basketball_items_n = {
    "Basketball: Mushroom Cup (Normal)": ItemData(base_id + 5, ItemClassification.progression),
    "Basketball: Flower Cup (Normal)": ItemData(base_id + 6, ItemClassification.progression),
    "Basketball: Star Cup (Normal)": ItemData(base_id + 7, ItemClassification.progression),
}

basketball_items_h = {
    "Basketball: Mushroom Cup (Hard)": ItemData(base_id + 8, ItemClassification.progression),
    "Basketball: Flower Cup (Hard)": ItemData(base_id + 9, ItemClassification.progression),
    "Basketball: Star Cup (Hard)": ItemData(base_id + 10, ItemClassification.progression)
}

dodgeball_items_n = {
    "Dodgeball: Mushroom Cup (Normal)": ItemData(base_id + 11, ItemClassification.progression),
    "Dodgeball: Flower Cup (Normal)": ItemData(base_id + 12, ItemClassification.progression),
    "Dodgeball: Star Cup (Normal)": ItemData(base_id + 13, ItemClassification.progression)
}

dodgeball_items_h = {
    "Dodgeball: Mushroom Cup (Hard)": ItemData(base_id + 14, ItemClassification.progression),
    "Dodgeball: Flower Cup (Hard)": ItemData(base_id + 15, ItemClassification.progression),
    "Dodgeball: Star Cup (Hard)": ItemData(base_id + 16, ItemClassification.progression)
}

volleyball_items_n = {
    "Volleyball: Mushroom Cup (Normal)": ItemData(base_id + 17, ItemClassification.progression),
    "Volleyball: Flower Cup (Normal)": ItemData(base_id + 18, ItemClassification.progression),
    "Volleyball: Star Cup (Normal)": ItemData(base_id + 19, ItemClassification.progression)
}

volleyball_items_h = {
    "Volleyball: Mushroom Cup (Hard)": ItemData(base_id + 20, ItemClassification.progression),
    "Volleyball: Flower Cup (Hard)": ItemData(base_id + 21, ItemClassification.progression),
    "Volleyball: Star Cup (Hard)": ItemData(base_id + 22, ItemClassification.progression)
}

hockey_items_n = {
    "Hockey: Mushroom Cup (Normal)": ItemData(base_id + 23, ItemClassification.progression),
    "Hockey: Flower Cup (Normal)": ItemData(base_id + 24, ItemClassification.progression),
    "Hockey: Star Cup (Normal)": ItemData(base_id + 25, ItemClassification.progression)
}

hockey_items_h = {
    "Hockey: Mushroom Cup (Hard)": ItemData(base_id + 26, ItemClassification.progression),
    "Hockey: Flower Cup (Hard)": ItemData(base_id + 27, ItemClassification.progression),
    "Hockey: Star Cup (Hard)": ItemData(base_id + 28, ItemClassification.progression)
}

sports_mix_items = {
    "Sports Mix: Mushroom Cup": ItemData(base_id + 29, ItemClassification.progression_skip_balancing),
    "Sports Mix: Flower Cup": ItemData(base_id + 30, ItemClassification.progression_skip_balancing),
    "Sports Mix: Star Cup": ItemData(base_id + 31, ItemClassification.progression_skip_balancing)
}

# May or may not need
# all_cup_unlocks_n = {
#     "Mushroom Cup (Normal)": ItemData(base_id + 32, ItemClassification.progression),
#     "Flower Cup (Normal)": ItemData(base_id + 33, ItemClassification.progression),
#     "Star Cup (Normal)": ItemData(base_id + 33, ItemClassification.progression),
# }
#
# all_cup_unlocks_h = {
#     "Mushroom Cup (Hard)": ItemData(base_id + 34, ItemClassification.progression),
#     "Flower Cup (Hard)": ItemData(base_id + 35, ItemClassification.progression),
#     "Star Cup (Hard)": ItemData(base_id + 36, ItemClassification.progression),
# }

mushroom_cup_rounds = {
    "Mushroom Cup Round 1": ItemData(base_id + 37, ItemClassification.progression),
    "Mushroom Cup Round 2": ItemData(base_id + 38, ItemClassification.progression),
    "Mushroom Cup Round 3": ItemData(base_id + 39, ItemClassification.progression)
}

flower_cup_rounds = {
    "Flower Cup Round 1": ItemData(base_id + 40, ItemClassification.progression),
    "Flower Cup Round 2": ItemData(base_id + 41, ItemClassification.progression),
    "Flower Cup Round 3": ItemData(base_id + 42, ItemClassification.progression)
}

star_cup_rounds = {
    "Star Cup Round 1": ItemData(base_id + 43, ItemClassification.progression),
    "Star Cup Round 2": ItemData(base_id + 44, ItemClassification.progression),
    "Star Cup Round 3": ItemData(base_id + 45, ItemClassification.progression)
}

extra_stages = {
    "Extra Stage 1": ItemData(base_id + 43, ItemClassification.progression),
    "Extra Stage 2": ItemData(base_id + 44, ItemClassification.progression),
    "Extra Stage 3": ItemData(base_id + 45, ItemClassification.progression)
}

exhibition_difficulties = {
    "Exhibition: Easy": ItemData(base_id + 46, ItemClassification.progression|ItemClassification.useful),
    "Exhibition: Normal": ItemData(base_id + 47, ItemClassification.progression|ItemClassification.useful),
    "Exhibition: Hard": ItemData(base_id + 48, ItemClassification.progression|ItemClassification.useful),
    "Exhibition: Expert": ItemData(base_id + 49, ItemClassification.progression|ItemClassification.useful),
}

individual_stages = {
    "Stage: Mario Stadium": ItemData(base_id + 100, ItemClassification.progression),
    "Stage: Koopa Troopa Beach": ItemData(base_id + 101, ItemClassification.progression),
    "Stage: Peach's Castle": ItemData(base_id + 102, ItemClassification.progression),
    "Stage: Toad Park": ItemData(base_id + 103, ItemClassification.progression),
    "Stage: DK Dock": ItemData(base_id + 104, ItemClassification.progression),
    "Stage: Luigi's Mansion": ItemData(base_id + 105, ItemClassification.progression),
    "Stage: Daisy Garden": ItemData(base_id + 106, ItemClassification.progression),
    "Stage: Wario Factory": ItemData(base_id + 107, ItemClassification.progression),
    "Stage: Bowser Jr. Blvd.": ItemData(base_id + 108, ItemClassification.progression),
    "Stage: Bowser's Castle": ItemData(base_id + 109, ItemClassification.progression),
    "Stage: Waluigi Pinball": ItemData(base_id + 110, ItemClassification.progression),
    "Stage: Ghoulish Galleon": ItemData(base_id + 111, ItemClassification.progression),
    "Stage: Star Ship": ItemData(base_id + 112, ItemClassification.progression),
    "Stage: Western Junction": ItemData(base_id + 113, ItemClassification.progression),
    "Boss Stage": ItemData(base_id + 114, ItemClassification.progression_skip_balancing),
}

progressive_stuff = {
    "Progressive Team Size": ItemData(base_id + 120, ItemClassification.progression),

}

characters = {
    "Character: Mario": ItemData(base_id + 200, ItemClassification.progression),
    "Character: Luigi": ItemData(base_id + 201, ItemClassification.progression),
    "Character: Peach": ItemData(base_id + 202, ItemClassification.progression),
    "Character: Daisy": ItemData(base_id + 203, ItemClassification.progression),
    "Character: Yoshi": ItemData(base_id + 204, ItemClassification.progression),
    "Character: Wario": ItemData(base_id + 205, ItemClassification.progression),
    "Character: Waluigi": ItemData(base_id + 206, ItemClassification.progression),
    "Character: Donkey Kong": ItemData(base_id + 207, ItemClassification.progression),
    "Character: Diddy Kong": ItemData(base_id + 208, ItemClassification.progression),
    "Character: Toad": ItemData(base_id + 209, ItemClassification.progression),
    "Character: Bowser": ItemData(base_id + 210, ItemClassification.progression),
    "Character: Bowser Jr.": ItemData(base_id + 211, ItemClassification.progression),
    "Character: Moogle": ItemData(base_id + 212, ItemClassification.progression),
    "Character: Cactuar": ItemData(base_id + 213, ItemClassification.progression),
    "Character: Ninja": ItemData(base_id + 214, ItemClassification.progression),
    "Character: White Mage": ItemData(base_id + 215, ItemClassification.progression),
    "Character: Slime": ItemData(base_id + 216, ItemClassification.progression),
    "Character: Black Mage": ItemData(base_id + 217, ItemClassification.progression),
}


character_costumes = {
    "Costume: Light Blue Yoshi": ItemData(base_id + 218, ItemClassification.filler|ItemClassification.deprioritized),
    "Costume: Yellow Yoshi": ItemData(base_id + 219, ItemClassification.filler|ItemClassification.deprioritized),
    "Costume: Pink Yoshi": ItemData(base_id + 220, ItemClassification.filler|ItemClassification.deprioritized),
    "Costume: Tennis-wear Peach": ItemData(base_id + 221, ItemClassification.filler|ItemClassification.deprioritized),
    "Costume: Tennis-wear Daisy": ItemData(base_id + 222, ItemClassification.filler|ItemClassification.deprioritized),
    "Costume: Blue Toad": ItemData(base_id + 223, ItemClassification.filler|ItemClassification.deprioritized),
    "Costume: Yellow Toad": ItemData(base_id + 224, ItemClassification.filler|ItemClassification.deprioritized),
    "Costume: Green Toad": ItemData(base_id + 225, ItemClassification.filler|ItemClassification.deprioritized),
    "Costume: Shadow White Ninja": ItemData(base_id + 226, ItemClassification.filler|ItemClassification.deprioritized),
    "Costume: Pure White - White Mage": ItemData(base_id + 227,ItemClassification.filler|ItemClassification.deprioritized),
    "Costume: Magic Red Black Mage": ItemData(base_id + 228,ItemClassification.filler|ItemClassification.deprioritized),
    "Costume: She-Slime": ItemData(base_id + 229, ItemClassification.filler|ItemClassification.deprioritized),
    "Costume: Metal Slime": ItemData(base_id + 230, ItemClassification.filler|ItemClassification.deprioritized),
}

# Able to use once unlocked
unlockable_items = {
    "Question Mark Panel: Coin": ItemData(base_id + 300, ItemClassification.useful),
    "Question Mark Panel: Green Shell": ItemData(base_id + 301, ItemClassification.useful),
    "Question Mark Panel: Red Shell": ItemData(base_id + 302, ItemClassification.useful),
    "Question Mark Panel: Banana": ItemData(base_id + 303, ItemClassification.useful),
    "Question Mark Panel: Bob-omb": ItemData(base_id + 304, ItemClassification.useful),
    "Question Mark Panel: Mini Mushroom": ItemData(base_id + 305, ItemClassification.useful),
    "Question Mark Panel: Super Star": ItemData(base_id + 306, ItemClassification.useful),
    "Special Meter": ItemData(base_id + 307, ItemClassification.useful),
}

# One time use
one_time_items = {
    "1 Time Coin": ItemData(base_id + 400, ItemClassification.filler),
    "1 Time Green Shell": ItemData(base_id + 401, ItemClassification.filler),
    "1 Time Red Shell": ItemData(base_id + 402, ItemClassification.filler),
    "1 Time Banana": ItemData(base_id + 403, ItemClassification.filler),
    "1 Time Bob-omb": ItemData(base_id + 404, ItemClassification.filler),
    "1 Time Mini Mushroom": ItemData(base_id + 405, ItemClassification.filler),
    "1 Time Super Star": ItemData(base_id + 406, ItemClassification.filler),
}

traps = {
    "Trap: Negative Coin": ItemData(base_id + 500, ItemClassification.trap),
    "Trap: Hit Stun": ItemData(base_id + 501, ItemClassification.trap),
}



# Put all into a table
item_table: Dict[str, ItemData] = {
    **sport_items,
    **basketball_items_n,
    **basketball_items_h,
    **dodgeball_items_n,
    **dodgeball_items_h,
    **volleyball_items_n,
    **volleyball_items_h,
    **hockey_items_n,
    **hockey_items_h,
    **sports_mix_items,
    #**all_cup_unlocks_n,
    #**all_cup_unlocks_h,
    **exhibition_difficulties,
    **mushroom_cup_rounds,
    **flower_cup_rounds,
    **star_cup_rounds,
    **extra_stages,
    **individual_stages,
    **progressive_stuff,
    **characters,
    **character_costumes,
    **unlockable_items,
    **one_time_items,
    **traps,
}



#What item group is this item in?
def get_item_group(item_name: str) -> str:
    if item_name in sport_items:
        return "Sport Items"
    elif item_name in basketball_items_n:
        return "Basketball Normal Cups"
    elif item_name in basketball_items_h:
        return "Basketball Hard Cups"
    elif item_name in dodgeball_items_n:
        return "Dodgeball Normal Cups"
    elif item_name in dodgeball_items_h:
        return "Dodgeball Hard Cups"
    elif item_name in volleyball_items_n:
        return "Volleyball Normal Cups"
    elif item_name in volleyball_items_h:
        return "Volleyball Hard Cups"
    elif item_name in hockey_items_n:
        return "Hockey Normal Cups"
    elif item_name in hockey_items_h:
        return "Hockey Hard Cups"
    elif item_name in sports_mix_items:
        return "Sports Mix Cups"
    # elif item_name in all_cup_unlocks_n:
    #     return "Normal Cup unlocks for all sports"
    # elif item_name in all_cup_unlocks_h:
    #     return "Hard Cup unlocks for all sports"
    elif item_name in exhibition_difficulties:
        return "Exhibition Difficulties"
    elif item_name in mushroom_cup_rounds:
        return "Mushroom Cup Rounds"
    elif item_name in flower_cup_rounds:
        return "Flower Cup Rounds"
    elif item_name in star_cup_rounds:
        return "Star Cup Rounds"
    elif item_name in extra_stages:
        return "Extra Stages"
    elif item_name in individual_stages:
        return "Individual stages"
    elif item_name in progressive_stuff:
        return "Progressive stuff"
    elif item_name in characters:
        return "Characters"
    elif item_name in character_costumes:
        return "Character costumes"
    elif item_name in unlockable_items:
        return "Unlockable items"
    elif item_name in one_time_items:
        return "One time items"
    elif item_name in traps:
        return "Traps"
    return "No item group for this item"

ITEM_NAME_TO_ID: Dict[str, int] = {item_name: data.code for item_name, data in item_table.items()}

def get_random_filler_item_name(world: "MSMWorld") -> str:
    traps_list = [name for name, data in traps.items()]
    filler_list = [name for name, data in one_time_items.items()]
    if world.random.randint(0, 99) < world.options.trap_chance:
        return world.random.choice(traps_list)

    return world.random.choice(filler_list)


def create_all_items(world: "MSMWorld") -> None:
    itempool = []
    for name, data in characters.items():
        new_item = world.create_item(name)
        itempool.append(new_item)
    for name, data in character_costumes.items():
        new_item = world.create_item(name)
        itempool.append(new_item)
    for name, data in unlockable_items.items():
        new_item = world.create_item(name)
        itempool.append(new_item)
    for name, data in progressive_stuff.items():
        new_item = world.create_item(name)
        itempool.append(new_item)
    # for name, data in one_time_items.items():
    #     new_item = world.create_item(name)
    #     itempool.append(new_item)
    # for name, data in traps.items():
    #     new_item = world.create_item(name)
    #     itempool.append(new_item)
    sports_mix = world.create_item("Sport: Sports Mix")
    itempool.append(sports_mix)

    if world.options.start_with_sports:
        basketball = world.create_item("Sport: Basketball")
        world.push_precollected(basketball)
        dodgeball = world.create_item("Sport: Dodgeball")
        world.push_precollected(dodgeball)
        volleyball = world.create_item("Sport: Volleyball")
        world.push_precollected(volleyball)
        hockey = world.create_item("Sport: Hockey")
        world.push_precollected(hockey)
    else:
        for name, data in sport_items.items():
            new_item = world.create_item(name)
            itempool.append(new_item)

    if "Basketball" in world.options.enabled_sports:
        if "Normal" in world.options.cup_difficulty:
            for name, data in basketball_items_n.items():
                new_item = world.create_item(name)
                itempool.append(new_item)
        if "Hard" in world.options.cup_difficulty:
            for name, data in basketball_items_h.items():
                new_item = world.create_item(name)
                itempool.append(new_item)

    if "Dodgeball" in world.options.enabled_sports:
        if "Normal" in world.options.cup_difficulty:
            for name, data in basketball_items_n.items():
                new_item = world.create_item(name)
                itempool.append(new_item)
        if "Hard" in world.options.cup_difficulty:
            for name, data in basketball_items_h.items():
                new_item = world.create_item(name)
                itempool.append(new_item)

    if "Volleyball" in world.options.enabled_sports:
        if "Normal" in world.options.cup_difficulty:
            for name, data in basketball_items_n.items():
                new_item = world.create_item(name)
                itempool.append(new_item)
        if "Hard" in world.options.cup_difficulty:
            for name, data in basketball_items_h.items():
                new_item = world.create_item(name)
                itempool.append(new_item)

    if "Hockey" in world.options.enabled_sports:
        if "Normal" in world.options.cup_difficulty:
            for name, data in basketball_items_n.items():
                new_item = world.create_item(name)
                itempool.append(new_item)
        if "Hard" in world.options.cup_difficulty:
            for name, data in basketball_items_h.items():
                new_item = world.create_item(name)
                itempool.append(new_item)

    if "Sports Mix" in world.options.enabled_sports:
        for name, data in sports_mix_items:
            new_item = world.create_item(name)
            itempool.append(new_item)

    if world.options.stage_unlock_type == StageUnlockType.option_by_stage_name:
        for name, data in individual_stages:
            new_item = world.create_item(name)
            itempool.append(new_item)
    if world.options.stage_unlock_type == StageUnlockType.option_by_cup_round:
        for name, data in mushroom_cup_rounds:
            new_item = world.create_item(name)
            itempool.append(new_item)
        for name, data in flower_cup_rounds:
            new_item = world.create_item(name)
            itempool.append(new_item)
        for name, data in star_cup_rounds:
            new_item = world.create_item(name)
            itempool.append(new_item)
        for name, data in extra_stages:
            new_item = world.create_item(name)
            itempool.append(new_item)

    # Calculate number of filler items needed, exclude costumes
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # Submit to multiworld
    world.multiworld.itempool += itempool


def create_item_with_correct_classification(world: "MSMWorld", name: str) -> MSMItem:
    """Creates an MSMItem for the given player based on the item name."""
    if name not in item_table:
        raise KeyError(f"Item '{name}' not found in the item table.")

    item_data = item_table[name]

    # Provide the MSMItem with the details from our table
    return MSMItem(
        name,
        item_data.classification,
        item_data.code,
        world.player
    )