from __future__ import annotations
from typing import TYPE_CHECKING

from rule_builder.rules import *
from .options import *

if TYPE_CHECKING:
    from . import MSMWorld

# Stage item mappings used for exhibition and tournament requirements
# The value represents the amount of "Progressive Court" items needed.
STAGES = {
    "Mario Stadium": 1,
    "Koopa Troopa Beach": 2,
    "Toad Park": 3,
    "DK Dock": 4,
    "Peach's Castle": 5,
    "Daisy Garden": 6,
    "Luigi's Mansion": 7,
    "Wario Factory": 8,
    "Bowser Jr. Blvd.": 9,
    "Bowser's Castle": 10,
    "Waluigi Pinball": 11,
    "Western Junction": 12,
    "Ghoulish Galleon": 13,
    "Star Ship": 14,
    "Behemoth Stage": 15,
}


# Helper function to generate progressive logic rules using native Has wrapper
def stage_rule(stage_name: str):
    if stage_name in STAGES:
        # Archipelago rule_builder natively supports count logic inside Has
        return Has("Progressive Court", STAGES[stage_name])
    return Has(stage_name)


# Stages required for each exhibition match category
EXHIBITION_RULES = {
    "Basketball": [
        "Mario Stadium", "Koopa Troopa Beach", "DK Dock", "Luigi's Mansion",
        "Western Junction", "Daisy Garden", "Bowser Jr. Blvd.",
        "Bowser's Castle", "Star Ship", "Peach's Castle",
        "Wario Factory", "Ghoulish Galleon"
    ],
    "Dodgeball": [
        "Mario Stadium", "Koopa Troopa Beach", "DK Dock",
        "Western Junction", "Daisy Garden", "Bowser's Castle",
        "Star Ship", "Peach's Castle", "Wario Factory",
        "Ghoulish Galleon", "Toad Park", "Waluigi Pinball"
    ],
    "Volleyball": [
        "Mario Stadium", "Koopa Troopa Beach", "DK Dock", "Luigi's Mansion",
        "Western Junction", "Bowser Jr. Blvd.", "Bowser's Castle",
        "Star Ship", "Peach's Castle", "Wario Factory",
        "Ghoulish Galleon", "Waluigi Pinball"
    ],
    "Hockey": [
        "Mario Stadium", "Koopa Troopa Beach", "Western Junction",
        "Daisy Garden", "Bowser Jr. Blvd.", "Bowser's Castle",
        "Star Ship", "Peach's Castle", "Wario Factory",
        "Ghoulish Galleon", "Toad Park", "Waluigi Pinball"
    ]
}

# Progressive cup requirements for each sport
TOURNAMENT_RULES = {
    "Basketball": {
        "Mushroom": ["Mario Stadium", "Koopa Troopa Beach", "DK Dock"],
        "Flower": ["Luigi's Mansion", "Western Junction", "Daisy Garden"],
        "Star": ["Bowser Jr. Blvd.", "Bowser's Castle", "Star Ship"]
    },
    "Dodgeball": {
        "Mushroom": ["Mario Stadium", "Koopa Troopa Beach", "Peach's Castle"],
        "Flower": ["DK Dock", "Toad Park", "Daisy Garden"],
        "Star": ["Wario Factory", "Bowser's Castle", "Star Ship"]
    },
    "Volleyball": {
        "Mushroom": ["Mario Stadium", "Koopa Troopa Beach", "Peach's Castle"],
        "Flower": ["DK Dock", "Luigi's Mansion", "Western Junction"],
        "Star": ["Bowser Jr. Blvd.", "Bowser's Castle", "Star Ship"]
    },
    "Hockey": {
        "Mushroom": ["Mario Stadium", "Toad Park", "Peach's Castle"],
        "Flower": ["Western Junction", "Wario Factory", "Daisy Garden"],
        "Star": ["Bowser Jr. Blvd.", "Waluigi Pinball", "Star Ship"]
    }
}

EXHIBITION_DIFFICULTIES = {
    "Easy": "Easy",
    "Normal": "Normal",
    "Hard": "Hard",
    "Expert": "Expert"
}

TOURNAMENT_DIFFICULTIES = {
    "Normal": "Normal",
    "Hard": "Hard"
}

CHARACTER_NAMES = [
    "Mario", "Luigi", "Peach", "Daisy", "Yoshi", "Wario", "Waluigi", "Donkey Kong", "Diddy Kong", "Toad", "Bowser",
    "Bowser Jr", "Moogle", "White Mage", "Black Mage", "Ninja", "Cactuar", "Slime"
]

COSTUME_NAMES = {
    "Pink Yoshi": "Yoshi",
    "Light Blue Yoshi": "Yoshi",
    "Yellow Yoshi": "Yoshi",
    "Blue Toad": "Toad",
    "Green Toad": "Toad",
    "Yellow Toad": "Toad",
    "She-Slime": "Slime",
    "Metal Slime": "Slime",
    "Tennis-wear Peach": "Peach",
    "Tennis-wear Daisy": "Daisy",
    "Shadow White Ninja": "Ninja",
    "Pure White - White Mage": "White Mage",
    "Magic Red Black Mage": "Black Mage"
}


def set_all_rules(world: MSMWorld) -> None:
    set_all_location_rules(world)
    set_all_entrance_rules(world)
    set_goal_rules(world)
    set_completion_condition(world)


def set_all_location_rules(world: MSMWorld) -> None:
    # Exhibition mode rules
    for difficulty in world.options.exhibition_difficulty:
        if difficulty not in EXHIBITION_DIFFICULTIES:
            continue

        for sport, stages in EXHIBITION_RULES.items():
            for stage in stages:
                location = world.get_location(f"{sport} Ex: Beat {stage} ({difficulty})")
                diff_item = f"Exhibition {difficulty}"
                world.set_rule(location, stage_rule(stage) & Has(diff_item))

    # Tournament cup rules
    cup_difficulties = ["Normal"]
    if world.options.hard_tournament_difficulty == HardTournamentDifficulty.option_true:
        cup_difficulties.append("Hard")

    for difficulty in cup_difficulties:
        if difficulty not in TOURNAMENT_DIFFICULTIES:
            continue

        for sport, cups in TOURNAMENT_RULES.items():
            for cup, stages in cups.items():
                for i in range(1, 4):
                    needed = stages[:i]
                    if not needed:
                        rule = Has("")
                    else:
                        rule = stage_rule(needed[0])
                        for stage in needed[1:]:
                            rule &= stage_rule(stage)

                    location = world.get_location(f"{sport}: Beat {difficulty} {cup} Cup Round {i}")
                    world.set_rule(location, rule)

    # Sports Mix Locations
    for cup in ["Mushroom", "Flower", "Star"]:
        for i in range(1, 4):
            if cup == "Star" and i == 3:
                cup_item = f"Sports Mix: Star Cup"
                location = world.get_location("Sports Mix: Beat Star Cup Round 3")
                rule = stage_rule("Star Ship") & Has(cup_item)
            else:
                cup_item = f"Sports Mix: {cup} Cup"
                location = world.get_location(f"Sports Mix: Beat {cup} Cup Round {i}")
                # Requires at least 1 progressive court item to check randomised eligibility
                rule = Has("Progressive Court", 1) & Has(cup_item)

            world.set_rule(location, rule)

    if (world.options.character_sanity == CharacterSanity.option_characters or
            world.options.character_sanity == CharacterSanity.option_characters_and_costumes):
        for character in CHARACTER_NAMES:
            location = world.get_location(f"Play as {character}")
            world.set_rule(location, Has(character))

    if world.options.character_sanity == CharacterSanity.option_characters_and_costumes:
        for costume, char in COSTUME_NAMES.items():
            location = world.get_location(f"Play as {costume}")
            world.set_rule(location, HasAll(char, costume))


def set_goal_rules(world: MSMWorld) -> None:
    behemoth_rule = (
            CanReachLocation("Basketball: Beat Normal Star Cup Round 3", "Basketball: Star Cup (Normal)") &
            CanReachLocation("Dodgeball: Beat Normal Star Cup Round 3", "Dodgeball: Star Cup (Normal)") &
            CanReachLocation("Volleyball: Beat Normal Star Cup Round 3", "Volleyball: Star Cup (Normal)") &
            CanReachLocation("Hockey: Beat Normal Star Cup Round 3", "Hockey: Star Cup (Normal)") &
            stage_rule("Behemoth Stage")
    )

    behemoth_king_rule = (
            (Has("Sports Mix", options=[OptionFilter(SportsMixUnlock, SportsMixUnlock.option_sports_mix_item)]) |
             HasAll(
                 "Sports Crystal: Red", "Sports Crystal: Green",
                 "Sports Crystal: Yellow", "Sports Crystal: Blue",
                 options=[OptionFilter(SportsMixUnlock, SportsMixUnlock.option_sports_crystals)]
             )) & CanReachLocation("Sports Mix: Beat Star Cup Round 3") & stage_rule("Behemoth Stage")
    )

    if world.options.goal_condition == GoalCondition.option_defeat_behemoth:
        world.set_rule(world.get_location("Defeat Behemoth!"), behemoth_rule)
        if world.options.be_mean == BeMean.option_defeat_behemoth_king:
            world.set_rule(world.get_location("Defeat Behemoth King!"), behemoth_king_rule)

    if world.options.goal_condition == GoalCondition.option_defeat_behemoth_king:
        world.set_rule(world.get_location("Defeat Behemoth King!"), behemoth_king_rule)
        if world.options.be_mean == BeMean.option_defeat_behemoth:
            world.set_rule(world.get_location("Defeat Behemoth!"), behemoth_rule)


def set_all_entrance_rules(world: MSMWorld) -> None:
    sports = ["Basketball", "Dodgeball", "Volleyball", "Hockey"]
    cup_tiers = ["Mushroom", "Flower", "Star"]
    hard_enabled = world.options.hard_tournament_difficulty == HardTournamentDifficulty.option_true

    # Main 4 Sports: Normal Cup Entrance Rules (Always Tiers 1, 2, and 3)
    for sport in sports:
        for index, cup in enumerate(cup_tiers):
            entrance = world.get_entrance(f"{sport} -> {cup} Cup (Normal)")
            needed_count = index + 1  # 1, 2, 3
            world.set_rule(entrance, Has(sport) & Has("Progressive Cup", needed_count))

    # Main 4 Sports: Hard Cup Entrance Rules
    if hard_enabled:
        for sport in sports:
            for index, cup in enumerate(cup_tiers):
                entrance = world.get_entrance(f"{sport} -> {cup} Cup (Hard)")
                needed_count = index + 4  # 4, 5, 6 (Pushed ahead of Sports Mix)
                world.set_rule(entrance, Has(sport) & Has("Progressive Cup", needed_count))

    # Sports Mix Entrance Rules (Dynamic Thresholds)
    # Hard Mode ON:  Slots 7, 8, 9
    # Hard Mode OFF: Slots 4, 5, 6
    sm_base_offset = 7 if hard_enabled else 4
    sm_cups = ["Mushroom", "Flower", "Star"]

    for index, cup in enumerate(sm_cups):
        entrance = world.get_entrance(f"Sports Mix -> {cup} Cup")
        needed_count = sm_base_offset + index  # 7,8,9 OR 4,5,6
        world.set_rule(entrance, Has("Progressive Cup", needed_count))


def set_completion_condition(world: MSMWorld) -> None:
    world.set_completion_rule(Has("Victory!"))