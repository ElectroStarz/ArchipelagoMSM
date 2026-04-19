from dataclasses import dataclass

from Options import Choice, OptionSet, PerGameCommonOptions, Range, Toggle, DefaultOnToggle, OptionGroup, Visibility

class StartWithSports(Choice):
    """Start with the sports? HEAVILY RECOMMENDED
Will cause immediate BK if off"""
    display_name = "Start With Sports - Recommended!"
    option_none = 0
    option_excluding_sports_mix = 1
    option_with_sports_mix = 2
    default = 1

class StartWithMushroomCup(Choice):
    """Start with Mushroom Cup for all Sports? (Also unlocks related stages)
Also heavily recommended"""
    display_name = "Start with Mushroom Cup (+Stages) - Recommended!"
    option_none = 0
    option_normal_difficulty = 1
    option_hard_difficulty = 2
    option_both = 3
    default = 1

class ExhibitionDifficulty(OptionSet):
    """ Beating a stage on each difficulty will send an item
(Easy, Normal, Hard, Expert)"""
    display_name = "Exhibition Difficulty"
    valid_keys = {"Easy","Normal", "Hard", "Expert"}
    default = {"Easy", "Normal", "Hard", "Expert"}

class CupDifficulty(OptionSet):
    """Beating a cup on each difficulty will send an item
(Normal, Hard, Expert - NOT IMPLEMENTED)"""
    display_name = "Cup Difficulty"
    valid_keys = {"Normal", "Hard"}
    default = {"Normal", "Hard"}

class PartyMode(OptionSet):
    """What party mode games do you want to include?
(Feed Petey, Harmony Hustle, Bob-omb Dodge, Smash Skate)"""
    visibility = Visibility.none
    display_name = "Party Mode Games"
    valid_keys = {"Feed Petey", "Harmony Hustle", "Bob-omb Dodge", "Smash Skate"}
    default = {"Feed Petey", "Harmony Hustle", "Bob-omb Dodge", "Smash Skate"}

class StageUnlockType(Choice):
    """How do you want stages to be unlocked?"""
    visibility = Visibility.none
    display_name = "Stage Unlock Type"
    option_by_cup_round = 0
    option_by_stage_name = 1
    default = 1

class SportsMixUnlock(Choice):
    """Unlock Sports Mix by getting 4 Sports Crystals from other players (Or yourself!)
or get Sports Mix as an item"""
    display_name = "Sports Mix Unlock"
    option_sports_mix_item = 0
    option_sports_crystals = 1
    default = 0

class GoalCondition(Choice):
    """What is your goal?"""
    display_name = "Goal Condition"
    option_defeat_behemoth = 0
    option_defeat_behemoth_king = 1
    option_win_cups = 2
    default = 1

class BehemothHP(Range):
    """Behemoth Health - 2400 is base game
Recommended to edit this in the yaml (2400 - 7000)"""
    display_name = "Behemoth HP"
    range_start = 2400
    range_end = 7000
    default = 2400

class BehemothKingHP(Range):
    """Behemoth King Health - 3000 is base game
Recommended to edit this in the yaml (3000 - 10000)"""
    display_name = "Behemoth King HP"
    range_start = 3000
    range_end = 10000
    default = 3000

class CupsRequired(Range):
    """Cups required for goal"""
    display_name = "Required Cups to goal"
    range_start = 5
    range_end = 27
    default = 10

class TrapChance(Range):
    """The chance a filler is swapped with a trap"""
    display_name = "Trap Chance"
    range_start = 0
    range_end = 100
    default = 25

class TeamSanity(Choice):
    """(NOT WORKING) Turn on or off team sanity
(Playing with every team combination sends a check, requires Progressive Team Size level 2)"""
    display_name = "Team Sanity"
    option_off = 0
    option_characters = 1
    option_characters_and_costumes = 2
    default = 2

class ScoreSanity(Toggle):
    """(NOT WORKING) Toggle on or off score sanity"""
    display_name = "Score Sanity"
    default = False

class ScoreSanityPoints(Range):
    """(NOT WORKING) Every number of points will send a check"""
    display_name = "Score Sanity Points"
    range_start = 1
    range_end = 10
    default = 5

class ScoreSanityMax(Range):
    """(NOT WORKING) Score Sanity will go up to this number of points"""
    display_name = "Score Sanity Max"
    range_start = 10
    range_end = 100
    default = 40

class SpecialSanity(DefaultOnToggle):
    """(NOT WORKING) Using each character's special sends a check"""
    display_name = "Special Sanity"

class CourtSanity(Choice):
    """(NOT WORKING) Playing and/or winning on each court sends a check"""
    display_name = "Court Sanity"
    option_off = 0
    option_playing = 1
    option_winning = 2
    option_both = 3
    default = 0

msm_option_groups = [
    OptionGroup("Game Options", [
        StartWithSports,
        StartWithMushroomCup,
        ExhibitionDifficulty,
        CupDifficulty,
        StageUnlockType,
        SportsMixUnlock,
        TrapChance
    ]),
    OptionGroup("Goal Options", [
        GoalCondition,
        BehemothHP,
        BehemothKingHP,
        CupsRequired
    ]),
    OptionGroup("Sanity Options (Only Special Sanity Works)", [
        TeamSanity,
        ScoreSanity,
        ScoreSanityPoints,
        ScoreSanityMax,
        SpecialSanity,
        CourtSanity
    ])
]

@dataclass()
class MSMOptions(PerGameCommonOptions):
    start_with_sports: StartWithSports
    start_with_mushroom_cup: StartWithMushroomCup
    exhibition_difficulty: ExhibitionDifficulty
    cup_difficulty: CupDifficulty
    party_mode: PartyMode
    stage_unlock_type: StageUnlockType
    sports_mix_unlock: SportsMixUnlock
    goal_condition : GoalCondition
    behemoth_hp: BehemothHP
    behemoth_king_hp: BehemothKingHP
    cups_required: CupsRequired
    trap_chance: TrapChance
    team_sanity: TeamSanity
    score_sanity: ScoreSanity
    score_sanity_points: ScoreSanityPoints
    score_sanity_max: ScoreSanityMax
    special_sanity: SpecialSanity
    court_sanity: CourtSanity