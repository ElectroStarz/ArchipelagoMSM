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
    "Bowser Jr", "Moogle", "White Mage", "Black Mage", "Ninja", "Cactuar", "Slime"
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

def court_rule(world: MSMWorld, court_name: str, sm: bool = False, pm: bool = False, round_num: int | None = 1):
    """Dynamically returns Progressive Court or Individual Court."""
    if sm:
        return sports_mix_court_rule(round_num if round_num is not None else 1)
    elif pm:
        return Has(court_name)
    elif world.options.court_unlock_type == CourtUnlockType.option_progressive_court:
        return Has("Progressive Court", courts_dict[court_name])
    else:
        return Has(court_name)


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
        return HasAll(*round_1_courts)
    elif round_num == 2:
        return HasAll(*round_2_courts) & HasAll(*round_1_courts)
    elif round_num == 3:
        return HasAll(*round_3_courts) & HasAll(*round_1_courts) & HasAll(*round_2_courts)
    else:
        return HasAny(*round_1_courts, *round_2_courts, *round_3_courts)

def get_all_cup_locations(hard_mode_enabled):
    locations = []

    # Normal Difficulty
    for sport in main_sports:
        for cup in cups:
            locations.append(f"{sport}: Beat Normal {cup} Cup Round 3")

    # Hard Difficulty (if enabled)
    if hard_mode_enabled:
        for sport in main_sports:
            for cup in cups:
                locations.append(f"{sport}: Beat Hard {cup} Cup Round 3")

    # Sports Mix
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


def can_play_any_cup(world: MSMWorld) -> Rule:
    """
    Returns a combined Rule representing:
    (Has(Cup1) & Has(first_court)) | (Has(Cup2) & Has(first_court)) | ...
    """
    sub_rules = []

    for sport in all_sports:
        sport_data = tournament_rules.get(sport, {})

        for cup in cups:
            associated_courts = sport_data.get(cup, []) if sport != "Sports Mix" else courts_list
            first_court = associated_courts[0]
            if not associated_courts:
                continue

            # Determine cup requirement logic depending on progressive settings
            if world.options.cup_unlock_type == CupUnlockType.option_progressive_cup:
                needed_normal = get_unified_cup_level(world, "Normal", cup)
                cup_rule_cond = Has("Progressive Cup", needed_normal)

                if world.options.hard_tournament_difficulty:
                    needed_hard = get_unified_cup_level(world, "Hard", cup)
                    cup_rule_cond |= Has("Progressive Cup", needed_hard)
            else:
                if sport != "Sports Mix":
                    cup_rule_cond = Has(f"{sport}: {cup} Cup (Normal)")
                    if world.options.hard_tournament_difficulty:
                        cup_rule_cond |= Has(f"{sport}: {cup} Cup (Hard)")
                else:
                    cup_rule_cond = Has(f"Sports Mix: {cup} Cup")

            any_cup_rule = cup_rule_cond & Has(first_court)
            sub_rules.append(any_cup_rule)

    if not sub_rules:
        return Rule()

    # Safely chain the rules together with the OR (|) operator
    combined_rule = sub_rules[0]
    for rule in sub_rules[1:]:
        combined_rule |= rule

    return combined_rule


def can_play_any_ex() -> Rule:
    """Returns if the player has any main sport, ex diff and any court"""

    ex_diffs = ["Exhibition Easy", "Exhibition Normal", "Exhibition Hard", "Exhibition Expert"]
    return HasAny(*main_sports) & HasAny(*ex_diffs) & HasAny(*courts_list)


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


@dataclasses.dataclass()
class CanExGoal(Rule["MSMWorld"], game="Mario Sports Mix"):

    @override
    def _instantiate(self, world: "MSMWorld") -> Rule.Resolved:
        valid_ex_locations = generate_exhibition_locations(world.options.enabled_sports.value, world.options.exhibition_difficulties.value)

        # Convert the location strings into actual Rule objects
        location_rules = [CanReachLocation(loc) for loc in valid_ex_locations]

        resolved_rules = tuple([rule.resolve(world) for rule in location_rules])

        return CanExGoal.Resolved(
            num_ex_locations = find_num_exhibition_locs(world.options.enabled_sports.value, world.options.exhibition_difficulties.value),
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

            if world.options.exhibition_type == ExhibitionType.option_all_sports:
                for sport, courts in exhibition_rules.items():
                    if sport in world.options.enabled_sports.value:
                        for court in courts:
                            location = world.get_location(f"{sport} Ex: Beat {court} ({difficulty})")
                            world.set_rule(location,
                                           Has(sport) & court_rule(world, court, False) & Has(f"Exhibition {difficulty}"))
            else:
                for court in courts_list:
                    location = world.get_location(f"Exhibition: Beat {court} ({difficulty})")
                    world.set_rule(location,
                                   HasAny(*main_sports) & court_rule(world, court, False) & Has(f"Exhibition {difficulty}"))

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
                    if cup == "Star" and i == 3:
                        location = world.get_location("Sports Mix: Beat Star Cup Round 3")
                        rule = court_rule(world, "Star Ship", False, round_num=3) & base_sm_logic
                    else:
                        location = world.get_location(f"Sports Mix: Beat {cup} Cup Round {i}")
                        rule = court_rule(world, "Peach's Castle", True, round_num=i) & base_sm_logic

                    world.set_rule(location, rule)

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
    if world.options.character_sanity in (CharacterSanity.option_characters,
                                          CharacterSanity.option_characters_and_costumes):
        for character in character_names:
            location = world.get_location(f"Win as {character}")
            world.set_rule(location, Has(character) & (can_play_any_cup(world) | can_play_any_ex()))

    if world.options.character_sanity == CharacterSanity.option_characters_and_costumes:
        for costume, char in costume_names.items():
            location = world.get_location(f"Win as {costume}")
            world.set_rule(location, HasAll(char, costume) & (can_play_any_cup(world) | can_play_any_ex()))

    # Court Sanity Locations
    if world.options.court_sanity:
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
                "Star Ship": ["Star Cup"],
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
                "Star Ship": ["Star Cup"],
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
                "Star Ship": ["Star Cup"],
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
                "Star Ship": ["Star Cup"],
            },
        }

        mode_to_court = {
            "Basketball": list(sport_court_to_cups.get("Basketball", {}).keys()),
            "Dodgeball": list(sport_court_to_cups.get("Dodgeball", {}).keys()),
            "Volleyball": list(sport_court_to_cups.get("Volleyball", {}).keys()),
            "Hockey": list(sport_court_to_cups.get("Hockey", {}).keys()),
            "Feed Petey": feed_petey_courts,
            "Harmony Hustle": harmony_hustle_courts,
            "Bob-omb Dodge": bob_omb_dodge_courts,
            "Smash Skate": smash_skate_courts,
        }

        hh_court_to_song = {
            "Peach's Castle": ["Classic Ocean", "Bloocheep Ocean", "Punk Ocean", "Mushroom Mix Medley"],
            "Bowser Jr. Blvd.": ["Chocobo Rhythm", "Chocobo Pop", "Chocobo Beat", "Star Mix Medley"],
            "DK Dock": ["Mario Athletic", "Punk Athletic", "Island Athletic", "Blossom Mix Medley"],
        }

        def apply_all_court_rules():
            all_unique_courts = set()
            for courts in mode_to_court.values():
                all_unique_courts.update(courts)

            for court_name in all_unique_courts:
                try:
                    win_location = world.get_location(f"Win on {court_name}")
                except KeyError:
                    continue

                court_valid_rules = []

                if world.options.include_tournaments or world.options.include_exhibition:
                    for sport_name in world.options.enabled_sports.value:
                        tournament_cups = sport_court_to_cups.get(sport_name, {}).get(court_name, [])
                        has_exhibition_match = court_name in exhibition_rules.get(sport_name, [])

                        if tournament_cups or has_exhibition_match:
                            base_sport_rule = Has(sport_name) & Has(court_name)

                            formatted_cups = [f"{sport_name}: {cup_name} ({diff})" for cup_name in tournament_cups
                                              for diff in cup_difficulties]

                            allowed_modes = []

                            if formatted_cups:
                                allowed_modes.append(
                                    HasAny(*formatted_cups, options=[OptionFilter(IncludeTournaments, IncludeTournaments.option_true)])
                                )
                            if has_exhibition_match:
                                ex_diffs = [f"Exhibition {diff}"
                                            for diff in world.options.exhibition_difficulties.value]
                                allowed_modes.append(
                                    HasAny(*ex_diffs, options=[OptionFilter(IncludeExhibition, IncludeExhibition.option_true)])
                                )

                            if allowed_modes:
                                mode_rule = allowed_modes[0]
                                for mode in allowed_modes[1:]:
                                    mode_rule |= mode

                                court_valid_rules.append(base_sport_rule & mode_rule)

                for party_name in world.options.party_mode.value:
                    if party_name in mode_to_court and court_name in mode_to_court[party_name]:
                        if party_name == "Harmony Hustle":
                            hh_court_list = hh_court_to_song[court_name]
                            party_rule = Has(party_name) & Has(court_name) & HasAny(*hh_court_list)
                        else:
                            party_rule = Has(party_name) & Has(court_name)

                        court_valid_rules.append(party_rule)

                if court_valid_rules:
                    final_court_rule = court_valid_rules[0]
                    for court_rule in court_valid_rules[1:]:
                        final_court_rule |= court_rule
                    world.set_rule(win_location, final_court_rule)
                else:
                    world.set_rule(win_location, False_())

        apply_all_court_rules()

    if world.options.special_sanity:
        for character in character_names:
            location = world.get_location(f"Use {character}'s Special")
            world.set_rule(location, Has("Special Meter") & Has(character) &
                           (can_play_any_cup(world) | can_play_any_ex()))

def set_all_entrance_rules(world: MSMWorld) -> None:
    cup_tiers = ["Mushroom", "Flower", "Star"]
    hard_enabled = bool(world.options.hard_tournament_difficulty)

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

    behemoth_normal_rule = valid_behemoth_normal_rules[0]
    for access_rule in valid_behemoth_normal_rules[1:]:
        behemoth_normal_rule &= access_rule

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

    if world.options.goal_condition == GoalCondition.option_defeat_behemoth:
        world.set_rule(world.get_location("Defeat Behemoth!"), final_behemoth_rule)
        if world.options.boss_locations == BossLocations.option_defeat_behemoth_king:
            world.set_rule(world.get_location("Defeat Behemoth King!"), behemoth_king_rule)

    elif world.options.goal_condition == GoalCondition.option_defeat_behemoth_king:
        world.set_rule(world.get_location("Defeat Behemoth King!"), behemoth_king_rule)
        if world.options.boss_locations == BossLocations.option_defeat_behemoth:
            world.set_rule(world.get_location("Defeat Behemoth!"), final_behemoth_rule)

    elif world.options.goal_condition == GoalCondition.option_win_cups:
        win_cup_value = world.options.win_cups_amount.value
        world.set_rule(world.get_location(f"Win {win_cup_value} Cups!"), CanCupGoal().resolve(world))

        if world.options.boss_locations in (BossLocations.option_defeat_behemoth, BossLocations.option_both):
            world.set_rule(world.get_location("Defeat Behemoth!"), final_behemoth_rule)

        if world.options.boss_locations in (BossLocations.option_defeat_behemoth_king, BossLocations.option_both):
            world.set_rule(world.get_location("Defeat Behemoth King!"), behemoth_king_rule)

    elif world.options.goal_condition == GoalCondition.option_exhibition_tour:
        amount = find_num_exhibition_locs(world.options.enabled_sports.value, world.options.exhibition_difficulties.value)

        world.set_rule(world.get_location(f"Win {amount} Exhibition Matches!"), CanExGoal().resolve(world))

        if world.options.boss_locations in (BossLocations.option_defeat_behemoth, BossLocations.option_both):
            world.set_rule(world.get_location("Defeat Behemoth!"), final_behemoth_rule)

        if world.options.boss_locations in (BossLocations.option_defeat_behemoth_king, BossLocations.option_both):
            world.set_rule(world.get_location("Defeat Behemoth King!"), behemoth_king_rule)

    elif world.options.goal_condition == GoalCondition.option_party_palooza:
        world.set_rule(world.get_location("Win Party Mode!"), get_all_party_location_rules(world))

        if world.options.boss_locations in (BossLocations.option_defeat_behemoth, BossLocations.option_both):
            world.set_rule(world.get_location("Defeat Behemoth!"), final_behemoth_rule)

        if world.options.boss_locations in (BossLocations.option_defeat_behemoth_king, BossLocations.option_both):
            world.set_rule(world.get_location("Defeat Behemoth King!"), behemoth_king_rule)

def set_completion_condition(world: MSMWorld) -> None:
    world.set_completion_rule(Has("Victory!"))
    # Player is granted the "Victory!" item upon goaling
