from __future__ import annotations
from typing import TYPE_CHECKING
from rule_builder.rules import Has, HasAll, HasAny, CanReachLocation
from .options import GoalCondition, BeMean, HardTournamentDifficulty

if TYPE_CHECKING:
    from . import MSMWorld

# Stage item mappings used for exhibition and tournament requirements
STAGES = {
    "Mario Stadium": "Stage: Mario Stadium",
    "Koopa Troopa Beach": "Stage: Koopa Troopa Beach",
    "Peach's Castle": "Stage: Peach's Castle",
    "Toad Park": "Stage: Toad Park",
    "DK Dock": "Stage: DK Dock",
    "Luigi's Mansion": "Stage: Luigi's Mansion",
    "Daisy Garden": "Stage: Daisy Garden",
    "Wario Factory": "Stage: Wario Factory",
    "Bowser Jr. Blvd.": "Stage: Bowser Jr. Blvd.",
    "Bowser's Castle": "Stage: Bowser's Castle",
    "Waluigi Pinball": "Stage: Waluigi Pinball",
    "Ghoulish Galleon": "Stage: Ghoulish Galleon",
    "Star Ship": "Stage: Star Ship",
    "Western Junction": "Stage: Western Junction",
}

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
# Round 1 = first stage only
# Round 2 = first + second stage
# Round 3 = all three stages
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


# Main rule setup entry point
# Calls all other rule generation functions

def set_all_rules(world: MSMWorld) -> None:
    set_all_location_rules(world)
    set_all_entrance_rules(world)
    set_goal_rules(world)
    set_completion_condition(world)


# Creates all location access rules
# Includes exhibitions, tournaments, and goal locations

def set_all_location_rules(world: MSMWorld) -> None:
    stage_rules = {name: Has(item) for name, item in STAGES.items()}

    # Exhibition mode rules
    # Automatically generates every enabled difficulty
    for difficulty in world.options.exhibition_difficulty:
        if difficulty not in EXHIBITION_DIFFICULTIES:
            continue

        for sport, stages in EXHIBITION_RULES.items():
            for stage in stages:
                location = world.get_location(f"{sport} Ex: Beat {stage} ({difficulty})")
                world.set_rule(location, stage_rules[stage])

    # Tournament cup rules
    # Each round progressively requires more stages
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
                    rule = Has("") if not needed else HasAll(*[STAGES[s] for s in needed])
                    location = world.get_location(
                        f"{sport}: Beat {difficulty} {cup} Cup Round {i}"
                    )
                    world.set_rule(location, rule)


# Goal completion logic
# Handles Behemoth and Behemoth King requirements

def set_goal_rules(world: MSMWorld) -> None:
    behemoth_rule = (
        CanReachLocation("Basketball: Beat Normal Star Cup Round 3", "Basketball: Star Cup (Normal)") &
        CanReachLocation("Dodgeball: Beat Normal Star Cup Round 3", "Dodgeball: Star Cup (Normal)") &
        CanReachLocation("Volleyball: Beat Normal Star Cup Round 3", "Volleyball: Star Cup (Normal)") &
        CanReachLocation("Hockey: Beat Normal Star Cup Round 3", "Hockey: Star Cup (Normal)")
    )

    behemoth_king_rule = (
        (HasAll("Sport: Sports Mix", "Stage: Behemoth Stage") |
        HasAll(
            "Sports Crystal: Red", "Sports Crystal: Green",
            "Sports Crystal: Yellow", "Sports Crystal: Blue",
            "Stage: Behemoth Stage"
        )) & CanReachLocation("Sports Mix: Beat Star Cup Round 3")
    )

    if world.options.goal_condition == GoalCondition.option_defeat_behemoth:
        world.set_rule(world.get_location("Defeat Behemoth!"), behemoth_rule)

    if world.options.goal_condition == GoalCondition.option_defeat_behemoth_king:
        world.set_rule(world.get_location("Defeat Behemoth King!"), behemoth_king_rule)

    if world.options.be_mean == BeMean.option_defeat_behemoth:
        if world.options.goal_condition == GoalCondition.option_defeat_behemoth_king:
            world.set_rule(world.get_location("Defeat Behemoth!"), behemoth_rule)

    if world.options.be_mean == BeMean.option_defeat_behemoth_king:
        if world.options.goal_condition == GoalCondition.option_defeat_behemoth:
            world.set_rule(world.get_location("Defeat Behemoth!"), behemoth_rule)


# Creates entrance access rules for menus and cups
# Entrances require their matching unlock items

def set_all_entrance_rules(world: MSMWorld) -> None:
    sports = ["Basketball", "Dodgeball", "Volleyball", "Hockey"]

    for sport in sports:
        entrance = world.get_entrance(f"Main Menu -> {sport}")
        world.set_rule(entrance, Has(f"Sport: {sport}"))

    sports_mix = world.get_entrance("Main Menu -> Sports Mix")
    world.set_rule(
        sports_mix,
        Has("Sport: Sports Mix") |
        HasAll(
            "Sports Crystal: Red", "Sports Crystal: Green",
            "Sports Crystal: Yellow", "Sports Crystal: Blue"
        )
    )

    for sport in sports:
        for difficulty in TOURNAMENT_DIFFICULTIES:
            for cup in ["Mushroom", "Flower", "Star"]:
                entrance = world.get_entrance(
                    f"{sport} -> {cup} Cup ({difficulty})"
                )
                world.set_rule(
                    entrance,
                    Has(f"{sport}: {cup} Cup ({difficulty})")
                )

    for cup in ["Mushroom", "Flower", "Star"]:
        entrance = world.get_entrance(f"Sports Mix -> {cup} Cup")
        world.set_rule(entrance, Has(f"Sports Mix: {cup} Cup"))


# Player wins after obtaining the Victory! item
def set_completion_condition(world: MSMWorld) -> None:
    world.set_completion_rule(Has("Victory!"))
