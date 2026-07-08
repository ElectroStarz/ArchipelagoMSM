from __future__ import annotations
from rule_builder.rules import *
from .options import *

if TYPE_CHECKING:
    from . import MSMWorld

# Court item mappings used for exhibition and tournament requirements
courts = {
    "Mario Stadium": 1, "Koopa Troopa Beach": 2, "Toad Park": 3,
    "DK Dock": 4, "Peach's Castle": 5, "Daisy Garden": 6,
    "Luigi's Mansion": 7, "Wario Factory": 8, "Bowser Jr. Blvd.": 9,
    "Bowser's Castle": 10, "Waluigi Pinball": 11, "Western Junction": 12,
    "Ghoulish Galleon": 13, "Star Ship": 14, "Behemoth Stage": 15,
}


# --- NEW HELPER ENGINE ---

def court_rule(world: MSMWorld, stage_name: str, sm: bool, round_num: int | None = 1):
    """Dynamically returns Progressive Court or Individual Court."""
    if world.options.court_unlock_type == CourtUnlockType.option_progressive_court:
        return Has("Progressive Court", courts[stage_name])
    elif sm:
        return sports_mix_court_rule(round_num if round_num is not None else 1)
    else:
        return Has(stage_name)

def get_unified_cup_level(world: MSMWorld, category: str, cup_name: str) -> int:
    """Calculates exactly how many Progressive Cups are needed for a specific tier."""
    cup_tiers = ["Mushroom", "Flower", "Star"]
    base_index = cup_tiers.index(cup_name)  # 0, 1, or 2

    if category == "Normal":
        if world.options.start_with_mushroom_cup == StartWithMushroomCup.option_both:
            if "Mushroom" in cup_name:
                return base_index + 1 # 1
            else:
                return base_index + 2 # 2, 3
        else:
            return base_index + 1 # 1
    elif category == "Hard":
        if world.options.start_with_mushroom_cup == StartWithMushroomCup.option_both:
            if "Mushroom" in cup_name:
                return base_index + 2 # 2nd Prog item is now Mushroom Cup (Hard)
            else:
                return base_index + 4  # 4, 5, 6
        else:
            return base_index + 4  # 4, 5, 6
    elif category == "Sports Mix":
        # Sports Mix shifts to 7,8,9 if Hard mode is on, else 4,5,6
        if world.options.hard_tournament_difficulty == HardTournamentDifficulty.option_true:
            return base_index + 7
        else:
            return base_index + 4
    else:
        return 1

def cup_rule(world: MSMWorld, sport: str, cup_name: str, category: str):
    """Returns either the Unified Progressive item requirement, or the Individual item requirement."""
    if world.options.cup_unlock_type == CupUnlockType.option_progressive_cup:
        needed_count = get_unified_cup_level(world, category, cup_name)
        return Has("Progressive Cup", needed_count)
    else:
        # If Sports Mix
        if category == "Sports Mix" or sport == "Sports Mix":
            return Has(f"Sports Mix: {cup_name} Cup")
        # If Main Sport
        return Has(f"{sport}: {cup_name} Cup ({category})")

def sports_mix_court_rule(round_num: int):
    round_1_courts = ["Mario Stadium", "DK Dock", "Luigi's Mansion", "Western Junction", "Bowser Jr. Blvd.",
                      "Wario Factory"]

    round_2_courts = ["Koopa Troopa Beach", "Western Junction", "Luigi's Mansion", "Toad Park", "Bowser's Castle",
                      "Wario Factory", "Waluigi Pinball"]

    round_3_courts = ["DK Dock", "Peach's Castle", "Daisy Garden", "Western Junction", "Star Ship"]

    if round_num == 1:
        return HasGroup(*round_1_courts)
    elif round_num == 2:
        return HasGroup(*round_2_courts)
    elif round_num == 3:
        return HasGroup(*round_3_courts)
    else:
        return HasAny(*round_1_courts, *round_2_courts, *round_3_courts)

SPORTS = ["Basketball", "Dodgeball", "Hockey", "Volleyball"]
CUPS = ["Mushroom", "Flower", "Star"]

def get_all_cup_locations(hard_mode_enabled):
    locations = []

    # Normal Difficulty
    for sport in SPORTS:
        for cup in CUPS:
            locations.append(f"{sport}: Beat Normal {cup} Cup Round 3")

    # Hard Difficulty (if enabled)
    if hard_mode_enabled:
        for sport in SPORTS:
            for cup in CUPS:
                locations.append(f"{sport}: Beat Hard {cup} Cup Round 3")

    # Sports Mix
    for cup in CUPS:
        locations.append(f"Sports Mix: Beat {cup} Cup Round 3")

    return locations

@dataclasses.dataclass()
class CanCupGoal(Rule["MSMWorld"], game="Mario Sports Mix"):

    @override
    def _instantiate(self, world: "MSMWorld") -> Rule.Resolved:
        valid_cup_locations = get_all_cup_locations(world.options.hard_tournament_difficulty.value)

        # Convert the location strings into actual Rule objects
        location_rules = [CanReachLocation(loc) for loc in valid_cup_locations]


        resolved_rules = tuple([rule.resolve(world) for rule in location_rules])

        return CanCupGoal.Resolved(
            cups_req=world.options.win_cups_amount.value,
            valid_cup_rules=resolved_rules,
            player=world.player,
        )

    class Resolved(Rule.Resolved):
        cups_req: int
        valid_cup_rules: tuple

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            cups_beaten = sum(1 for rule in self.valid_cup_rules if rule(state))
            return cups_beaten >= self.cups_req


# --- END HELPER ENGINE ---


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

EXHIBITION_DIFFICULTIES = {"Easy": "Easy", "Normal": "Normal", "Hard": "Hard", "Expert": "Expert"}
TOURNAMENT_DIFFICULTIES = {"Normal": "Normal", "Hard": "Hard"}

CHARACTER_NAMES = [
    "Mario", "Luigi", "Peach", "Daisy", "Yoshi", "Wario", "Waluigi", "Donkey Kong", "Diddy Kong", "Toad", "Bowser",
    "Bowser Jr", "Moogle", "White Mage", "Black Mage", "Ninja", "Cactuar", "Slime"
]

COSTUME_NAMES = {
    "Pink Yoshi": "Yoshi", "Light Blue Yoshi": "Yoshi", "Yellow Yoshi": "Yoshi",
    "Blue Toad": "Toad", "Green Toad": "Toad", "Yellow Toad": "Toad",
    "She-Slime": "Slime", "Metal Slime": "Slime",
    "Tennis-wear Peach": "Peach", "Tennis-wear Daisy": "Daisy",
    "Shadow White Ninja": "Ninja", "Pure White - White Mage": "White Mage", "Magic Red Black Mage": "Black Mage"
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
                world.set_rule(location, court_rule(world, stage, False) & Has(f"Exhibition {difficulty}"))

    # Tournament cup rules
    cup_difficulties = ["Normal"]
    if world.options.hard_tournament_difficulty == HardTournamentDifficulty.option_true:
        cup_difficulties.append("Hard")

    if world.options.include_tournaments == IncludeTournaments.option_true:
        for difficulty in cup_difficulties:
            for sport, cups in TOURNAMENT_RULES.items():
                for cup, stages in cups.items():
                    base_cup_logic = cup_rule(world, sport, cup, difficulty)

                    for i in range(1, 4):
                        needed = stages[:i]
                        if not needed:
                            court_logic = Has("")
                        else:
                            court_logic = court_rule(world, needed[0], False)
                            for stage in needed[1:]:
                                court_logic &= court_rule(world, stage, False)

                        location = world.get_location(f"{sport}: Beat {difficulty} {cup} Cup Round {i}")
                        world.set_rule(location, Has(sport) & base_cup_logic & court_logic)

    # Sports Mix Locations
    for cup in ["Mushroom", "Flower", "Star"]:
        base_sm_logic = cup_rule(world, "Sports Mix", cup, "Sports Mix")

        for i in range(1, 4):
            if cup == "Star" and i == 3:
                location = world.get_location("Sports Mix: Beat Star Cup Round 3")
                rule = court_rule(world, "Star Ship", False) & base_sm_logic
            else:
                location = world.get_location(f"Sports Mix: Beat {cup} Cup Round {i}")
                # Dynamically maps to Progressive Court 5 or "Peach's Castle" based on options
                rule = court_rule(world, "Peach's Castle", True) & base_sm_logic

            world.set_rule(location, rule)

    # Character Sanity Locations
    if world.options.character_sanity in (CharacterSanity.option_characters,
                                          CharacterSanity.option_characters_and_costumes):
        for character in CHARACTER_NAMES:
            location = world.get_location(f"Win as {character}")
            world.set_rule(location, Has(character))

    if world.options.character_sanity == CharacterSanity.option_characters_and_costumes:
        for costume, char in COSTUME_NAMES.items():
            location = world.get_location(f"Win as {costume}")
            world.set_rule(location, HasAll(char, costume))

    # Court Sanity Locations
    if world.options.court_sanity == CourtSanity.option_true:
        main_courts = ["Mario Stadium", "Koopa Troopa Beach", "Peach's Castle", "Toad Park", "DK Dock",
                       "Luigi's Mansion", "Daisy Garden", "Wario Factory", "Bowser Jr. Blvd.", "Bowser's Castle",
                       "Waluigi Pinball", "Ghoulish Galleon", "Star Ship", "Western Junction"]

        smash_skate_courts = ["Sherbet Sea", "Fire Mountain", "Rowdy Raft"]

        harmony_courts = ["Classic Ocean", "Chocobo Rhythm", "Mario Athletic", "Bloocheep Ocean", "Chocobo Pop",
                          "Punk Athletic", "Punk Ocean", "Chocobo Beat", "Island Athletic", "Mushroom Mix Medley",
                          "Blossom Mix Medley", "Star Mix Medley"]

        # Map of which cups contain which courts for each sport
        sport_court_to_cups = {
            "Basketball": {
                "Mario Stadium": ["Mushroom Cup"],
                "Koopa Troopa Beach": ["Mushroom Cup"],
                "DK Dock": ["Mushroom Cup"],

                "Luigi's Mansion": ["Flower Cup"],
                "Western Junction": ["Flower Cup"],
                "Daisy Garden": ["Flower Cup"],

                "Bowser Jr. Blvd.": ["Star Cup"],
                "Bowser's Castle": ["Star Cup"],
                "Star Ship": ["Star Cup"]
            },

            "Dodgeball": {
                "Mario Stadium": ["Mushroom Cup"],
                "Koopa Troopa Beach": ["Mushroom Cup"],
                "Peach's Castle": ["Mushroom Cup"],

                "DK Dock": ["Flower Cup"],
                "Toad Park": ["Flower Cup"],
                "Daisy Garden": ["Flower Cup"],

                "Wario Factory": ["Star Cup"],
                "Bowser's Castle": ["Star Cup"],
                "Star Ship": ["Star Cup"]
            },

            "Volleyball": {
                "Mario Stadium": ["Mushroom Cup"],
                "Koopa Troopa Beach": ["Mushroom Cup"],
                "Peach's Castle": ["Mushroom Cup"],

                "DK Dock": ["Flower Cup"],
                "Luigi's Mansion": ["Flower Cup"],
                "Western Junction": ["Flower Cup"],

                "Bowser Jr. Blvd.": ["Star Cup"],
                "Bowser's Castle": ["Star Cup"],
                "Star Ship": ["Star Cup"]
            },

            "Hockey": {
                "Mario Stadium": ["Mushroom Cup"],
                "Toad Park": ["Mushroom Cup"],
                "Peach's Castle": ["Mushroom Cup"],

                "Western Junction": ["Flower Cup"],
                "Wario Factory": ["Flower Cup"],
                "Daisy Garden": ["Flower Cup"],

                "Bowser Jr. Blvd.": ["Star Cup"],
                "Waluigi Pinball": ["Star Cup"],
                "Star Ship": ["Star Cup"]
            },

            # Map party modes to their unlock item or an exhibition requirement if needed
            "Smash Skate": {court: ["Smash Skate"] for court in smash_skate_courts},
            "Harmony Hustle": {court: ["Harmony Hustle"] for court in harmony_courts}
        }

        mode_to_court = {
            "Basketball": list(sport_court_to_cups["Basketball"].keys()),
            "Dodgeball": list(sport_court_to_cups["Dodgeball"].keys()),
            "Volleyball": list(sport_court_to_cups["Volleyball"].keys()),
            "Hockey": list(sport_court_to_cups["Hockey"].keys()),
            "Harmony Hustle": harmony_courts,
            "Smash Skate": smash_skate_courts,
        }

        def apply_court_rules(sport_name, courts_available):
            for court_name in courts_available:
                try:
                    win_location = world.get_location(f"Win on {court_name}")

                    # Only get the cups that have those stages
                    cups_list = sport_court_to_cups.get(sport_name, {}).get(court_name, [])
                    formatted_cups = [f"{sport_name}: {cup_name}" for cup_name in cups_list]
                    # Any enabled ex diff will allow the player to get the check
                    ex_diffs = [f"Exhibition {diff}" for diff in world.options.exhibition_difficulty]

                    can_win_rule = (Has(sport_name) & Has(court_name) &

                                    # This section tells the generator "HEY! If this person has this rule on, add this
                                    # to the rule!"
                                    (HasAny(*formatted_cups,
                                    options=[OptionFilter(IncludeTournaments, IncludeTournaments.option_true)])
                                    # If both are on, either one of the cups OR one of the ex diffs will allow them
                                    # to get the check
                                    | HasAny(*ex_diffs,
                                      options=[OptionFilter(IncludeExhibition, IncludeExhibition.option_true)])))

                    # Assign rule for the target location
                    world.set_rule(win_location, can_win_rule)
                except KeyError:
                    continue

        # Main Sports Tournament / Exhibition Logic
        if (world.options.include_tournaments == IncludeTournaments.option_true or
                world.options.include_exhibition == IncludeExhibition.option_true):
            if world.options.enabled_sports:
                for sport in world.options.enabled_sports:
                    if sport in sport_court_to_cups:
                        valid_main_courts = [c for c in sport_court_to_cups[sport] if c in main_courts]
                        apply_court_rules(sport, valid_main_courts)

        def apply_party_rules(party_mode, courts_available):
            for court_name in courts_available:
                try:
                    win_location = world.get_location(f"Win on {court_name}")

                    can_win_rule = Has(party_mode) & Has(court_name)

                    world.set_rule(win_location, can_win_rule)
                except KeyError:
                    continue

        # Party Mode Logic
        if world.options.party_mode:
            for mode in world.options.party_mode:
                if mode in mode_to_court:
                    apply_party_rules(mode, mode_to_court[mode])



def set_goal_rules(world: MSMWorld) -> None:
    # Safely checks if the locations themselves are accessible logically
    behemoth_rule = (
            CanReachLocation("Basketball: Beat Normal Star Cup Round 3") &
            CanReachLocation("Dodgeball: Beat Normal Star Cup Round 3") &
            CanReachLocation("Volleyball: Beat Normal Star Cup Round 3") &
            CanReachLocation("Hockey: Beat Normal Star Cup Round 3") &
            court_rule(world, "Behemoth Stage", False)
    )

    behemoth_king_rule = (
            (Has("Sports Mix", options=[OptionFilter(SportsMixUnlock, SportsMixUnlock.option_sports_mix_item)]) |
             HasAll(
                 "Sports Crystal: Red", "Sports Crystal: Green",
                 "Sports Crystal: Yellow", "Sports Crystal: Blue",
                 options=[OptionFilter(SportsMixUnlock, SportsMixUnlock.option_sports_crystals)]
             )) & CanReachLocation("Sports Mix: Beat Star Cup Round 3") & court_rule(world, "Behemoth Stage", False)
    )


    if world.options.goal_condition == GoalCondition.option_defeat_behemoth:
        world.set_rule(world.get_location("Defeat Behemoth!"), behemoth_rule)
        if world.options.be_mean == BeMean.option_defeat_behemoth_king:
            world.set_rule(world.get_location("Defeat Behemoth King!"), behemoth_king_rule)

    elif world.options.goal_condition == GoalCondition.option_defeat_behemoth_king:
        world.set_rule(world.get_location("Defeat Behemoth King!"), behemoth_king_rule)
        if world.options.be_mean == BeMean.option_defeat_behemoth:
            world.set_rule(world.get_location("Defeat Behemoth!"), behemoth_rule)

    elif world.options.goal_condition == GoalCondition.option_win_cups:
        value = world.options.win_cups_amount.value
        world.set_rule(world.get_location(f"Win {value} Cups!"), CanCupGoal().resolve(world))

        if world.options.be_mean in (BeMean.option_defeat_behemoth, BeMean.option_both):
            world.set_rule(world.get_location("Defeat Behemoth!"), behemoth_rule)

        if world.options.be_mean in (BeMean.option_defeat_behemoth_king, BeMean.option_both):
            world.set_rule(world.get_location("Defeat Behemoth King!"), behemoth_king_rule)


def set_all_entrance_rules(world: MSMWorld) -> None:
    sports = ["Basketball", "Dodgeball", "Volleyball", "Hockey"]
    cup_tiers = ["Mushroom", "Flower", "Star"]
    hard_enabled = world.options.hard_tournament_difficulty == HardTournamentDifficulty.option_true

    sports_mix_rule = (
            (Has("Sports Mix", options=[OptionFilter(SportsMixUnlock, SportsMixUnlock.option_sports_mix_item)]) |
             HasAll(
                 "Sports Crystal: Red", "Sports Crystal: Green",
                 "Sports Crystal: Yellow", "Sports Crystal: Blue",
                 options=[OptionFilter(SportsMixUnlock, SportsMixUnlock.option_sports_crystals)]
             ))
    )

    # Menu rules
    for sport in sports:
        entrance = world.get_entrance(f"Main Menu -> {sport}")
        world.set_rule(entrance, Has(sport))

    sm_entrance = world.get_entrance(f"Main Menu -> Sports Mix")
    world.set_rule(sm_entrance, sports_mix_rule)

    # Normal Cup Entrance Rules
    for sport in sports:
        for cup in cup_tiers:
            entrance = world.get_entrance(f"{sport} -> {cup} Cup (Normal)")
            world.set_rule(entrance, cup_rule(world, sport, cup, "Normal"))

    # Hard Cup Entrance Rules
    if hard_enabled:
        for sport in sports:
            for cup in cup_tiers:
                entrance = world.get_entrance(f"{sport} -> {cup} Cup (Hard)")
                world.set_rule(entrance, cup_rule(world, sport, cup, "Hard"))


    # Sports Mix Entrance Rules
    for cup in cup_tiers:
        entrance = world.get_entrance(f"Sports Mix -> {cup} Cup")
        world.set_rule(entrance, cup_rule(world, "Sports Mix", cup, "Sports Mix"))


def set_completion_condition(world: MSMWorld) -> None:
    world.set_completion_rule(Has("Victory!"))