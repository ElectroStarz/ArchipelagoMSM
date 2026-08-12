from __future__ import annotations
from rule_builder.rules import *
from .options import *
from .MSMUtils import *

if TYPE_CHECKING:
    from . import MSMWorld

main_sports = ["Basketball", "Dodgeball", "Hockey", "Volleyball"]
all_sports = ["Basketball", "Dodgeball", "Hockey", "Volleyball", "Sports Mix"]
cups = ["Mushroom", "Flower", "Star"]

# Court item mappings used for exhibition and tournament requirements
courts_dict = {
    "Mario Stadium": 1, "Koopa Troopa Beach": 2, "Toad Park": 3,
    "DK Dock": 4, "Peach's Castle": 5, "Daisy Garden": 6,
    "Luigi's Mansion": 7, "Wario Factory": 8, "Bowser Jr. Blvd.": 9,
    "Bowser's Castle": 10, "Waluigi Pinball": 11, "Western Junction": 12,
    "Ghoulish Galleon": 13, "Star Ship": 14, "Behemoth Stage": 15,
}

cup_dict = {
    "Mushroom (Normal)": 1,
    "Flower (Normal)": 2,
    "Star (Normal)": 3,
    "Mushroom (Hard)": 4,
    "Flower (Hard)": 5,
    "Star (Hard)": 6,
    "Mushroom (Global)": 1,
    "Flower (Global)": 2,
    "Star (Global)": 3
}

courts_list = [
    "Mario Stadium", "Koopa Troopa Beach", "Toad Park", "DK Dock",
    "Peach's Castle", "Daisy Garden", "Luigi's Mansion", "Wario Factory",
    "Bowser Jr. Blvd.", "Bowser's Castle", "Waluigi Pinball", "Western Junction",
    "Ghoulish Galleon", "Star Ship"
]

exhibition_rules = {
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

tournament_rules = {
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

exhibition_difficulties = ["Easy", "Normal", "Hard", "Expert"]
tournament_difficulties = ["Normal", "Hard"]

character_names = [
    "Mario", "Luigi", "Peach", "Daisy", "Yoshi", "Wario", "Waluigi", "Donkey Kong", "Diddy Kong", "Toad", "Bowser",
    "Bowser Jr", "Moogle", "White Mage", "Black Mage", "Ninja", "Cactuar", "Slime", "Mii (Male)", "Mii (Female)"
]

costume_names = {
    "Pink Yoshi": "Yoshi", "Light Blue Yoshi": "Yoshi", "Yellow Yoshi": "Yoshi",
    "Blue Toad": "Toad", "Green Toad": "Toad", "Yellow Toad": "Toad",
    "She-Slime": "Slime", "Metal Slime": "Slime",
    "Tennis-wear Peach": "Peach", "Tennis-wear Daisy": "Daisy",
    "Shadow White Ninja": "Ninja", "Pure White - White Mage": "White Mage", "Magic Red Black Mage": "Black Mage"
}

feed_petey_courts = ["Daisy Garden", "DK Dock", "Wario Factory"]

harmony_hustle_songs = ["Classic Ocean", "Chocobo Rhythm", "Mario Athletic", "Mushroom Mix Medley", "Bloocheep Ocean",
                        "Chocobo Pop", "Punk Athletic", "Blossom Mix Medley", "Punk Ocean", "Chocobo Beat",
                        "Island Athletic", "Star Mix Medley"]

harmony_hustle_courts = ["Peach's Castle", "DK Dock", "Bowser Jr. Blvd."]

bob_omb_dodge_courts = ["Mario Stadium", "Ghoulish Galleon", "Western Junction"]

smash_skate_courts = ["Sherbet Sea", "Rowdy Raft", "Fire Mountain"]


# --- NEW HELPER ENGINE ---

def court_rule(world: MSMWorld, court_name: str, sm: bool = False, pm: bool = False, round_num: int | None = 1,
               cup_name: str | None = None):
    """Dynamically returns Progressive Court or Individual Court."""
    if sm:
        return sports_mix_court_rule(world, cup_name if cup_name is not None else "Mushroom",
                                     round_num if round_num is not None else 1)
    elif pm:
        return Has(court_name)
    elif world.options.court_unlock_type.value == CourtUnlockType.option_progressive_court:
        return Has("Progressive Court", courts_dict[court_name])
    else:
        return Has(court_name)


def alternate_path_rule(world: MSMWorld, sport: str, cup_name: str, category: str, round_num: int | None = 1):
    """Returns rule for Progressive Alt Paths or Individual Alt Paths."""

    logic = False_()

    if sport == "Global":
        for enabled_sport in world.options.enabled_sports.value:

            if enabled_sport != "Sports Mix":

                court_logic = True_()

                if category == "Global":
                    cup_logic = cup_rule(world, enabled_sport, cup_name, "Normal") | cup_rule(world, enabled_sport,
                                                                                              cup_name, "Hard")
                else:
                    cup_logic = cup_rule(world, enabled_sport, cup_name, category)

                for i in range(round_num if round_num is not None else 1):
                    court_logic &= court_rule(world, tournament_rules[enabled_sport][cup_name][i], False)

                combined_logic = cup_logic & court_logic
                logic = logic | combined_logic

        if world.options.alt_path_type.value == 4 or world.options.alt_path_type.value == 5:
            progressive_logic = Has("Progressive Alternate Path", cup_dict[f"{cup_name} ({category})"])
            logic &= progressive_logic
        else:
            logic &= Has(f"{cup_name} Cup Alt Paths ({category})")

        return logic

    else:

        court_logic = True_()
        if sport == "Sports Mix":

            for i in range(round_num if round_num is not None else 1):
                court_logic &= sports_mix_court_rule(world, cup_name, i + 1)
        else:
            for i in range(round_num if round_num is not None else 1):
                court_logic &= court_rule(world, tournament_rules[sport][cup_name][i], False)

        if category == "Global":
            cup_logic = cup_rule(world, sport, cup_name, "Normal") | cup_rule(world, sport, cup_name, "Hard")
        else:
            cup_logic = cup_rule(world, sport, cup_name, category)

        logic = cup_logic & court_logic

        if world.options.alt_path_type.value == 4 or world.options.alt_path_type.value == 5:
            progressive_logic = Has("Progressive Alternate Path", cup_dict[f"{cup_name} ({category})"])
            logic &= progressive_logic
        else:
            if sport == "Sports Mix":
                logic &= Has(f"Sports Mix: {cup_name} Cup Alt Paths")
            else:
                logic &= Has(f"{sport}: {cup_name} Cup Alt Paths ({category})")

        return logic


def get_unified_cup_level(world: MSMWorld, category: str, cup_name: str) -> int:
    """Calculates exactly how many Progressive Cups are needed for a specific tier."""
    cup_tiers = ["Mushroom", "Flower", "Star"]
    base_index = cup_tiers.index(cup_name)  # 0, 1, or 2

    if category == "Normal":
        if world.options.start_with_mushroom_cup == StartWithMushroomCup.option_both:
            if "Mushroom" in cup_name:
                return base_index + 1  # 1
            else:
                return base_index + 2  # 2, 3
        else:
            return base_index + 1  # 1
    elif category == "Hard":
        if world.options.start_with_mushroom_cup == StartWithMushroomCup.option_both:
            if "Mushroom" in cup_name:
                return base_index + 2  # 2nd Prog item is now Mushroom Cup (Hard)
            else:
                return base_index + 4  # 4, 5, 6
        else:
            return base_index + 4  # 4, 5, 6
    elif category == "Sports Mix":
        # Sports Mix shifts to 7,8,9 if Hard mode is on, else 4,5,6
        if world.options.hard_tournament_difficulty:
            return base_index + 7
        else:
            return base_index + 4
    else:
        return 1


def cup_rule(world: MSMWorld, sport: str, cup_name: str, category: str):
    """Returns either the Unified Progressive item requirement, or the Individual item requirement."""
    if world.options.cup_unlock_type.value == CupUnlockType.option_progressive_cup:
        needed_count = get_unified_cup_level(world, category, cup_name)
        return Has("Progressive Cup", needed_count)
    else:
        # If Sports Mix
        if category == "Sports Mix" or sport == "Sports Mix":
            return Has(f"Sports Mix: {cup_name} Cup")
        # If Main Sport
        return Has(f"{sport}: {cup_name} Cup ({category})")


# Credit to Puffy for adding Progressive Court compatibility!!
# Added compatibility with Restrict Sports Mix.
def sports_mix_court_rule(world: MSMWorld, cup_name: str, round_num: int):
    enabled_sports = [sport for sport in world.options.enabled_sports.value]

    if not world.options.restrict_sports_mix:
        enabled_sports = ["Basketball", "Dodgeball", "Volleyball", "Hockey"]

    required_courts = set()

    for i in range(round_num):
        for sport in enabled_sports:
            if sport != "Sports Mix":
                possible_court = tournament_rules[sport][cup_name][i]
                required_courts.add(possible_court)

    if world.options.court_unlock_type.value == CourtUnlockType.option_progressive_court:
        needed_count = 0
        for court in required_courts:
            if courts_dict[court] > needed_count:
                needed_count = courts_dict[court]

        return Has("Progressive Court", needed_count)

    else:
        return HasAll(*required_courts)


def get_all_cup_locations(world):
    locations = []

    diffs = ["Normal"]
    if world.options.hard_tournament_difficulty.value:
        diffs.append("Hard")

    # Normal Difficulty
    for sport in world.options.enabled_sports.value:
        if sport != "Sports Mix":
            for diff in diffs:
                for cup in cups:
                    locations.append(f"{sport}: Beat {diff} {cup} Cup Round 3")

    # Sports Mix
    if "Sports Mix" in world.options.enabled_sports.value:
        for cup in cups:
            locations.append(f"Sports Mix: Beat {cup} Cup Round 3")

    return locations


def get_all_party_location_rules(world: MSMWorld):
    sub_rules = []

    # Party Mode Locations
    party_mode_to_courts = {
        "Feed Petey": feed_petey_courts,
        "Harmony Hustle": harmony_hustle_songs,
        "Bob-omb Dodge": bob_omb_dodge_courts,
        "Smash Skate": smash_skate_courts,
    }

    party_mode_to_tabs = {
        "Feed Petey": ["Apple", "Watermelon"],
        "Bob-omb Dodge": ["Bob-omb", "Cannon"],
        "Smash Skate": ["Hockey Stick", "Hockey Skate"],
    }

    for mode in world.options.party_mode.value:
        courts = party_mode_to_courts[mode]

        if mode == "Harmony Hustle":
            tabs = None
        else:
            tabs = party_mode_to_tabs[mode]

        for court in courts:
            if tabs is not None:
                for tab in tabs:
                    location = f"{mode}: Beat {court} ({tab})"
                    sub_rules.append(CanReachLocation(location))
            else:
                location = f"{mode}: Beat {court}"
                sub_rules.append(CanReachLocation(location))

    if not sub_rules:
        return Rule()

    combined_rule = sub_rules[0]
    for rule in sub_rules[1:]:
        combined_rule &= rule

    return combined_rule


def _any_reachable_location(location_names: list[str]) -> Rule:
    """Return a rule that is true when at least one listed location is reachable."""
    if not location_names:
        return False_()

    rules = [CanReachLocation(name) for name in location_names]
    combined_rule = rules[0]
    for rule in rules[1:]:
        combined_rule |= rule
    return combined_rule


def can_play_any_cup(world: MSMWorld) -> Rule:
    """Return whether at least one generated tournament match can be played."""
    if not world.options.include_tournaments.value:
        return False_()

    location_names = []
    difficulties = ["Normal"]
    if world.options.hard_tournament_difficulty.value:
        difficulties.append("Hard")

    for sport in world.options.enabled_sports.value:
        if sport in main_sports:
            for difficulty in difficulties:
                for cup in cups:
                    location_names.append(f"{sport}: Beat {difficulty} {cup} Cup Round 1")
        elif sport == "Sports Mix":
            for cup in cups:
                location_names.append(f"Sports Mix: Beat {cup} Cup Round 1")

    return _any_reachable_location(location_names)


def can_play_any_ex(world: MSMWorld) -> Rule:
    """Return whether at least one generated exhibition match can be played."""
    if (not world.options.include_exhibition.value or
            not world.options.exhibition_difficulties.value or
            not any(sport in main_sports for sport in world.options.enabled_sports.value)):
        return False_()

    location_names = generate_exhibition_locations(
        world.options.enabled_sports.value,
        world.options.exhibition_type.value,
        world.options.exhibition_difficulties.value,
    )
    return _any_reachable_location(location_names)


def can_play_any_party(world: MSMWorld) -> Rule:
    """Return whether at least one generated Party Mode match can be played."""
    location_names = []
    party_mode_to_courts = {
        "Feed Petey": feed_petey_courts,
        "Harmony Hustle": harmony_hustle_songs,
        "Bob-omb Dodge": bob_omb_dodge_courts,
        "Smash Skate": smash_skate_courts,
    }
    party_mode_to_tabs = {
        "Feed Petey": ["Apple", "Watermelon"],
        "Bob-omb Dodge": ["Bob-omb", "Cannon"],
        "Smash Skate": ["Hockey Stick", "Hockey Skate"],
    }

    for mode in world.options.party_mode.value:
        courts = party_mode_to_courts.get(mode, [])
        if mode == "Harmony Hustle":
            location_names.extend(f"{mode}: Beat {song}" for song in courts)
        else:
            for court in courts:
                for tab in party_mode_to_tabs.get(mode, []):
                    location_names.append(f"{mode}: Beat {court} ({tab})")

    return _any_reachable_location(location_names)


@dataclasses.dataclass()
class CanCupGoal(Rule["MSMWorld"], game="Mario Sports Mix"):

    @override
    def _instantiate(self, world: "MSMWorld") -> Rule.Resolved:
        valid_cup_locations = get_all_cup_locations(world)

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


@dataclasses.dataclass()
class CanExGoal(Rule["MSMWorld"], game="Mario Sports Mix"):

    @override
    def _instantiate(self, world: "MSMWorld") -> Rule.Resolved:
        valid_ex_locations = generate_exhibition_locations(world.options.enabled_sports.value,
                                                           world.options.exhibition_type.value,
                                                           world.options.exhibition_difficulties.value)

        # Convert the location strings into actual Rule objects
        location_rules = [CanReachLocation(loc) for loc in valid_ex_locations]

        resolved_rules = tuple([rule.resolve(world) for rule in location_rules])

        return CanExGoal.Resolved(
            num_ex_locations=find_num_exhibition_locs(world.options.enabled_sports.value,
                                                      world.options.exhibition_type.value,
                                                      world.options.exhibition_difficulties.value),
            valid_ex_rules=resolved_rules,
            player=world.player,
        )

    class Resolved(Rule.Resolved):
        num_ex_locations: int
        valid_ex_rules: tuple

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            ex_locations_checked = sum(1 for rule in self.valid_ex_rules if rule(state))
            return ex_locations_checked >= self.num_ex_locations


# --- END HELPER ENGINE ---


def set_all_rules(world: MSMWorld) -> None:
    set_all_location_rules(world)
    set_all_entrance_rules(world)

    set_goal_rules(world)
    set_completion_condition(world)


def set_all_location_rules(world: MSMWorld) -> None:
    # Exhibition mode rules
    if world.options.include_exhibition:
        for difficulty in world.options.exhibition_difficulties.value:
            if difficulty not in exhibition_difficulties:
                continue

            if world.options.exhibition_type.value == ExhibitionType.option_all_sports:
                for sport, courts in exhibition_rules.items():
                    if sport in world.options.enabled_sports.value:
                        for court in courts:
                            location = world.get_location(f"{sport} Ex: Beat {court} ({difficulty})")
                            world.set_rule(location,
                                           Has(sport) & court_rule(world, court, False) & Has(
                                               f"Exhibition {difficulty}"))
            else:
                enabled_main_sports = [
                    sport for sport in world.options.enabled_sports.value
                    if sport in main_sports
                ]
                if not enabled_main_sports:
                    continue

                for court in courts_list:
                    location = world.get_location(f"Exhibition: Beat {court} ({difficulty})")
                    world.set_rule(
                        location,
                        HasAny(*enabled_main_sports)
                        & court_rule(world, court, False)
                        & Has(f"Exhibition {difficulty}")
                    )

    # Tournament cup rules
    cup_difficulties = ["Normal"]
    if world.options.hard_tournament_difficulty:
        cup_difficulties.append("Hard")

    if world.options.include_tournaments:
        # Main Sports Locations
        for difficulty in cup_difficulties:
            for sport, tournament_cups in tournament_rules.items():
                if sport in world.options.enabled_sports.value:
                    for cup, courts in tournament_cups.items():
                        base_cup_logic = cup_rule(world, sport, cup, difficulty)

                        for i in range(1, 4):
                            needed = courts[:i]
                            if not needed:
                                court_logic = Has("")
                            else:
                                court_logic = court_rule(world, needed[0], False)
                                for court in needed[1:]:
                                    court_logic &= court_rule(world, court, False)

                            location = world.get_location(f"{sport}: Beat {difficulty} {cup} Cup Round {i}")
                            world.set_rule(location, Has(sport) & base_cup_logic & court_logic)

        # Sports Mix Locations
        if "Sports Mix" in world.options.enabled_sports.value:
            for cup in ["Mushroom", "Flower", "Star"]:
                base_sm_logic = cup_rule(world, "Sports Mix", cup, "Sports Mix")

                for i in range(1, 4):
                    location = world.get_location(f"Sports Mix: Beat {cup} Cup Round {i}")
                    rule = court_rule(world, "Peach's Castle", True, round_num=i, cup_name=cup) & base_sm_logic

                    world.set_rule(location, rule)

        # Alternate Path Nodes that Require Round 2
        # make sure to edit when proper node names get added
        alt_path_r2_nodes = {
            "Mushroom": ["Node 25", "Node 29", "Node 39"],
            "Flower": [],
            "Star": ["Node 23"]
        }

        alt_path_type = world.options.alt_path_type.value

        if world.options.include_alt_paths.value:

            if alt_path_type == 0:
                for difficulty in cup_difficulties:
                    for sport in world.options.enabled_sports.value:
                        for cup in cups:
                            for node in alt_path_r2_nodes[cup]:
                                if sport != "Sports Mix":
                                    location = world.get_location(f"{sport} {cup} Cup Alt Path {difficulty} {node}")

                                    # Apparantely Dodgeball is the only sport to have a node locked off by special meter and its literally just this one im crine
                                    if cup == "Star" and sport == "Dodgeball" and not world.options.always_spawn_alt_paths.value:
                                        world.set_rule(location,
                                                       alternate_path_rule(world, "Dodgeball", "Star", difficulty,
                                                                           round_num=2) & Has("Special Meter"))
                                    else:
                                        world.set_rule(location,
                                                       alternate_path_rule(world, sport, cup, difficulty, round_num=2))

                if "Sports Mix" in world.options.enabled_sports.value:
                    for cup in cups:
                        for node in alt_path_r2_nodes[cup]:
                            location = world.get_location(f"Sports Mix {cup} Cup Alt Path {node}")
                            world.set_rule(location,
                                           court_rule(world, "Waluigi Pinball", True, round_num=2, cup_name=cup))

            if alt_path_type == 1:
                for sport in world.options.enabled_sports.value:
                    if sport != "Sports Mix":
                        for cup in cups:
                            for node in alt_path_r2_nodes[cup]:
                                location = world.get_location(f"{sport} {cup} Cup Alt Path {node}")
                                if cup == "Star" and sport == "Dodgeball" and not world.options.always_spawn_alt_paths.value:
                                    world.set_rule(location, alternate_path_rule(world, "Dodgeball", "Star", "Global",
                                                                                 round_num=2) & Has("Special Meter"))
                                else:
                                    world.set_rule(location,
                                                   alternate_path_rule(world, sport, cup, "Global", round_num=2))

            if alt_path_type == 2 or alt_path_type == 4:
                for difficulty in cup_difficulties:
                    for cup in cups:
                        for node in alt_path_r2_nodes[cup]:
                            location = world.get_location(f"{cup} Cup Alt Path {difficulty} {node}")
                            # Just to be on the safe side
                            if cup == "Star" and not world.options.always_spawn_alt_paths.value:
                                world.set_rule(location, alternate_path_rule(world, "Global", "Star", difficulty,
                                                                             round_num=2) & Has("Special Meter"))
                            else:
                                world.set_rule(location,
                                               alternate_path_rule(world, "Global", cup, difficulty, round_num=2))

            if alt_path_type == 3 or alt_path_type == 5:
                for cup in cups:
                    for node in alt_path_r2_nodes[cup]:
                        location = world.get_location(f"{cup} Cup Alt Path {node}")
                        if cup == "Star" and not world.options.always_spawn_alt_paths.value:
                            world.set_rule(location,
                                           alternate_path_rule(world, "Global", "Star", "Global", round_num=2) & Has(
                                               "Special Meter"))
                        else:
                            world.set_rule(location, alternate_path_rule(world, "Global", cup, "Global", round_num=2))

    # Party Mode Locations
    party_mode_to_courts = {
        "Feed Petey": feed_petey_courts,
        "Harmony Hustle": harmony_hustle_songs,
        "Bob-omb Dodge": bob_omb_dodge_courts,
        "Smash Skate": smash_skate_courts,
    }

    party_mode_to_tabs = {
        "Feed Petey": ["Apple", "Watermelon"],
        "Bob-omb Dodge": ["Bob-omb", "Cannon"],
        "Smash Skate": ["Hockey Stick", "Hockey Skate"],
    }

    if world.options.party_mode:
        for mode in world.options.party_mode.value:
            courts = party_mode_to_courts[mode]

            if mode == "Harmony Hustle":
                tabs = None
            else:
                tabs = party_mode_to_tabs[mode]

            for court in courts:
                if tabs is not None:
                    for tab in tabs:
                        location = world.get_location(f"{mode}: Beat {court} ({tab})")
                        world.set_rule(location, Has(mode) & court_rule(world, court, pm=True))
                else:
                    location = world.get_location(f"{mode}: Beat {court}")
                    world.set_rule(location, Has(mode) & court_rule(world, court, pm=True))

    # === Sanity Locations ===

    # Character Sanity Locations
    playable_match_rule = can_play_any_cup(world) | can_play_any_ex(world)

    if world.options.character_sanity.value in (CharacterSanity.option_characters,
                                                CharacterSanity.option_characters_and_costumes):
        for character in character_names:
            location = world.get_location(f"Win as {character}")
            world.set_rule(location, Has(character) & (playable_match_rule | can_play_any_party(world)))

    if world.options.character_sanity.value == CharacterSanity.option_characters_and_costumes:
        for costume, char in costume_names.items():
            location = world.get_location(f"Win as {costume}")
            world.set_rule(location, HasAll(char, costume) & (playable_match_rule | can_play_any_party(world)))

    # Court Sanity Locations
    if world.options.court_sanity.value:
        tournament_court_rounds = {
            sport: {court: (cup, round_num)
                    for cup, court_list in cup_map.items()
                    for round_num, court in enumerate(court_list, start=1)}
            for sport, cup_map in tournament_rules.items()
        }

        hh_court_to_song = {
            "Peach's Castle": ["Classic Ocean", "Bloocheep Ocean", "Punk Ocean", "Mushroom Mix Medley"],
            "Bowser Jr. Blvd.": ["Chocobo Rhythm", "Chocobo Pop", "Chocobo Beat", "Star Mix Medley"],
            "DK Dock": ["Mario Athletic", "Punk Athletic", "Island Athletic", "Blossom Mix Medley"],
        }
        party_mode_courts = {
            "Feed Petey": feed_petey_courts,
            "Harmony Hustle": harmony_hustle_courts,
            "Bob-omb Dodge": bob_omb_dodge_courts,
            "Smash Skate": smash_skate_courts,
        }
        party_mode_tabs = {
            "Feed Petey": ["Apple", "Watermelon"],
            "Bob-omb Dodge": ["Bob-omb", "Cannon"],
            "Smash Skate": ["Hockey Stick", "Hockey Skate"],
        }

        for win_location in [loc for loc in world.multiworld.get_locations(world.player)
                             if loc.name.startswith("Win on ")]:
            court_name = win_location.name.removeprefix("Win on ")
            match_locations = []

            if world.options.include_tournaments.value:
                difficulties = ["Normal"]
                if world.options.hard_tournament_difficulty.value:
                    difficulties.append("Hard")

                for sport in world.options.enabled_sports.value:
                    court_data = tournament_court_rounds.get(sport, {}).get(court_name)
                    if court_data is None:
                        continue
                    cup, round_num = court_data
                    for difficulty in difficulties:
                        match_locations.append(
                            f"{sport}: Beat {difficulty} {cup} Cup Round {round_num}"
                        )

            if (world.options.include_exhibition.value and
                    world.options.exhibition_difficulties.value):
                if world.options.exhibition_type.value == ExhibitionType.option_all_sports:
                    for sport in world.options.enabled_sports.value:
                        if court_name in exhibition_rules.get(sport, []):
                            for difficulty in world.options.exhibition_difficulties.value:
                                match_locations.append(
                                    f"{sport} Ex: Beat {court_name} ({difficulty})"
                                )
                elif any(sport in main_sports for sport in world.options.enabled_sports.value):
                    if court_name in courts_list:
                        for difficulty in world.options.exhibition_difficulties.value:
                            match_locations.append(
                                f"Exhibition: Beat {court_name} ({difficulty})"
                            )

            for mode in world.options.party_mode.value:
                if court_name not in party_mode_courts.get(mode, []):
                    continue
                if mode == "Harmony Hustle":
                    match_locations.extend(
                        f"Harmony Hustle: Beat {song}"
                        for song in hh_court_to_song.get(court_name, [])
                    )
                else:
                    match_locations.extend(
                        f"{mode}: Beat {court_name} ({tab})"
                        for tab in party_mode_tabs.get(mode, [])
                    )

            world.set_rule(win_location, _any_reachable_location(match_locations))

    if world.options.special_sanity.value:
        for character in character_names:
            location = world.get_location(f"Use {character}'s Special")
            world.set_rule(location, Has("Special Meter") & Has(character) & playable_match_rule)


def set_all_entrance_rules(world: MSMWorld) -> None:
    cup_tiers = ["Mushroom", "Flower", "Star"]
    hard_enabled = bool(world.options.hard_tournament_difficulty.value)

    sports_mix_rule = (
        (Has("Sports Mix", options=[OptionFilter(SportsMixUnlock, SportsMixUnlock.option_sports_mix_item)]) |
         HasAll(
             "Sports Crystal: Red", "Sports Crystal: Green",
             "Sports Crystal: Yellow", "Sports Crystal: Blue",
             options=[OptionFilter(SportsMixUnlock, SportsMixUnlock.option_sports_crystals)]
         ))
    )

    # Menu rules
    for sport in world.options.enabled_sports.value:
        if sport != "Sports Mix":
            entrance = world.get_entrance(f"Main Menu -> {sport}")
            world.set_rule(entrance, Has(sport))
        else:
            sm_entrance = world.get_entrance(f"Main Menu -> Sports Mix")
            world.set_rule(sm_entrance, sports_mix_rule)

    # Tournament Rules
    if world.options.include_tournaments:
        for sport in world.options.enabled_sports.value:
            if sport != "Sports Mix":
                for cup in cup_tiers:
                    entrance = world.get_entrance(f"{sport} -> {cup} Cup (Normal)")
                    world.set_rule(entrance, cup_rule(world, sport, cup, "Normal"))

        if hard_enabled:
            for sport in world.options.enabled_sports.value:
                if sport != "Sports Mix":
                    for cup in cup_tiers:
                        entrance = world.get_entrance(f"{sport} -> {cup} Cup (Hard)")
                        world.set_rule(entrance, cup_rule(world, sport, cup, "Hard"))

        if "Sports Mix" in world.options.enabled_sports.value:
            for cup in cup_tiers:
                entrance = world.get_entrance(f"Sports Mix -> {cup} Cup")
                world.set_rule(entrance, cup_rule(world, "Sports Mix", cup, "Sports Mix"))

        # Alternate Path Rules
        if world.options.include_alt_paths:

            alt_path_type = world.options.alt_path_type.value

            # Yeah its the same as the tournament sue me it works :P
            if alt_path_type == 0:
                for sport in world.options.enabled_sports.value:
                    if sport != "Sports Mix":
                        for cup in cup_tiers:
                            entrance = world.get_entrance(
                                f"{sport}: {cup} Cup (Normal) -> {cup} Cup Alt Paths (Normal)")
                            world.set_rule(entrance, alternate_path_rule(world, sport, cup, "Normal"))

                if hard_enabled:
                    for sport in world.options.enabled_sports.value:
                        if sport != "Sports Mix":
                            for cup in cup_tiers:
                                entrance = world.get_entrance(
                                    f"{sport}: {cup} Cup (Hard) -> {cup} Cup Alt Paths (Hard)")
                                world.set_rule(entrance, alternate_path_rule(world, sport, cup, "Hard"))

                if "Sports Mix" in world.options.enabled_sports.value:
                    for cup in cup_tiers:
                        entrance = world.get_entrance(f"Sports Mix: {cup} Cup -> {cup} Cup Alt Paths")
                        world.set_rule(entrance, alternate_path_rule(world, "Sports Mix", cup, "Sports Mix"))

            elif alt_path_type == 1:
                for sport in world.options.enabled_sports.value:
                    if sport != "Sports Mix":
                        for cup in cup_tiers:
                            entrance_n = world.get_entrance(
                                f"{sport}: {cup} Cup (Normal) -> {cup} Cup Alt Paths (Global)")
                            entrance_h = world.get_entrance(
                                f"{sport}: {cup} Cup (Hard) -> {cup} Cup Alt Paths (Global)")
                            world.set_rule(entrance_n, alternate_path_rule(world, sport, cup, "Global"))
                            world.set_rule(entrance_h, alternate_path_rule(world, sport, cup, "Global"))

            elif alt_path_type == 2 or alt_path_type == 4:
                for sport in world.options.enabled_sports.value:
                    if sport != "Sports Mix":
                        for cup in cup_tiers:
                            entrance = world.get_entrance(
                                f"{sport}: {cup} Cup (Normal) -> Global: {cup} Cup Alt Paths (Normal)")
                            world.set_rule(entrance, alternate_path_rule(world, "Global", cup, "Normal"))

                if hard_enabled:
                    for sport in world.options.enabled_sports.value:
                        if sport != "Sports Mix":
                            for cup in cup_tiers:
                                entrance = world.get_entrance(
                                    f"{sport}: {cup} Cup (Hard) -> Global: {cup} Cup Alt Paths (Hard)")
                                world.set_rule(entrance, alternate_path_rule(world, "Global", cup, "Hard"))

            elif alt_path_type == 3 or alt_path_type == 5:
                for sport in world.options.enabled_sports.value:
                    if sport != "Sports Mix":
                        for cup in cup_tiers:
                            entrance_n = world.get_entrance(
                                f"{sport}: {cup} Cup (Normal) -> Global: {cup} Cup Alt Paths (Global)")
                            entrance_h = world.get_entrance(
                                f"{sport}: {cup} Cup (Hard) -> Global: {cup} Cup Alt Paths (Global)")
                            world.set_rule(entrance_n, alternate_path_rule(world, "Global", cup, "Global"))
                            world.set_rule(entrance_h, alternate_path_rule(world, "Global", cup, "Global"))

    # Party Mode Entrance Rules
    if world.options.party_mode:
        for mode in world.options.party_mode.value:
            entrance = world.get_entrance(f"Main Menu -> {mode}")
            world.set_rule(entrance, Has(mode))


def set_goal_rules(world: MSMWorld) -> None:
    # Safely checks if the locations themselves are accessible logically

    valid_behemoth_normal_rules = []
    valid_behemoth_hard_rules = []

    for sport in world.options.enabled_sports.value:
        if sport != "Sports Mix":
            valid_behemoth_normal_rules.append(CanReachLocation(f"{sport}: Beat Normal Star Cup Round 3"))

            if world.options.hard_tournament_difficulty:
                valid_behemoth_hard_rules.append(CanReachLocation(f"{sport}: Beat Hard Star Cup Round 3"))

    if valid_behemoth_normal_rules:
        behemoth_normal_rule = valid_behemoth_normal_rules[0]
        for access_rule in valid_behemoth_normal_rules[1:]:
            behemoth_normal_rule &= access_rule
    else:
        behemoth_normal_rule = False_()

    if valid_behemoth_hard_rules:
        behemoth_hard_rule = valid_behemoth_hard_rules[0]
        for access_rule in valid_behemoth_hard_rules[1:]:
            behemoth_hard_rule &= access_rule
    else:
        behemoth_hard_rule = False_()

    final_behemoth_rule = (behemoth_normal_rule | behemoth_hard_rule) & court_rule(world, "Behemoth Stage", False)

    behemoth_king_rule = (
            (Has("Sports Mix", options=[OptionFilter(SportsMixUnlock, SportsMixUnlock.option_sports_mix_item)]) |
             HasAll(
                 "Sports Crystal: Red", "Sports Crystal: Green",
                 "Sports Crystal: Yellow", "Sports Crystal: Blue",
                 options=[OptionFilter(SportsMixUnlock, SportsMixUnlock.option_sports_crystals)]
             )) & CanReachLocation("Sports Mix: Beat Star Cup Round 3") & court_rule(world, "Behemoth Stage", False)
    )

    if world.options.goal_condition.value == GoalCondition.option_defeat_behemoth:
        world.set_rule(world.get_location("Defeat Behemoth!"), final_behemoth_rule)
        if world.options.boss_locations.value == BossLocations.option_defeat_behemoth_king:
            world.set_rule(world.get_location("Defeat Behemoth King!"), behemoth_king_rule)

    elif world.options.goal_condition.value == GoalCondition.option_defeat_behemoth_king:
        world.set_rule(world.get_location("Defeat Behemoth King!"), behemoth_king_rule)
        if world.options.boss_locations.value == BossLocations.option_defeat_behemoth:
            world.set_rule(world.get_location("Defeat Behemoth!"), final_behemoth_rule)

    elif world.options.goal_condition.value == GoalCondition.option_win_cups:
        win_cup_value = world.options.win_cups_amount.value
        world.set_rule(world.get_location(f"Win {win_cup_value} Cups!"), CanCupGoal().resolve(world))

        if world.options.boss_locations.value in (BossLocations.option_defeat_behemoth, BossLocations.option_both):
            world.set_rule(world.get_location("Defeat Behemoth!"), final_behemoth_rule)

        if world.options.boss_locations.value in (BossLocations.option_defeat_behemoth_king, BossLocations.option_both):
            world.set_rule(world.get_location("Defeat Behemoth King!"), behemoth_king_rule)

    elif world.options.goal_condition.value == GoalCondition.option_exhibition_tour:
        amount = find_num_exhibition_locs(world.options.enabled_sports.value, world.options.exhibition_type.value,
                                          world.options.exhibition_difficulties.value)

        world.set_rule(world.get_location(f"Win {amount} Exhibition Matches!"), CanExGoal().resolve(world))

        if world.options.boss_locations.value in (BossLocations.option_defeat_behemoth, BossLocations.option_both):
            world.set_rule(world.get_location("Defeat Behemoth!"), final_behemoth_rule)

        if world.options.boss_locations.value in (BossLocations.option_defeat_behemoth_king, BossLocations.option_both):
            world.set_rule(world.get_location("Defeat Behemoth King!"), behemoth_king_rule)

    elif world.options.goal_condition.value == GoalCondition.option_party_palooza:
        world.set_rule(world.get_location("Win Party Mode!"), get_all_party_location_rules(world))

        if world.options.boss_locations.value in (BossLocations.option_defeat_behemoth, BossLocations.option_both):
            world.set_rule(world.get_location("Defeat Behemoth!"), final_behemoth_rule)

        if world.options.boss_locations.value in (BossLocations.option_defeat_behemoth_king, BossLocations.option_both):
            world.set_rule(world.get_location("Defeat Behemoth King!"), behemoth_king_rule)


def set_completion_condition(world: MSMWorld) -> None:
    world.set_completion_rule(Has("Victory!"))
    # Player is granted the "Victory!" item upon goaling