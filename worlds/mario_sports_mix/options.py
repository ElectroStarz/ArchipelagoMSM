from dataclasses import dataclass

from Options import Choice, OptionSet, PerGameCommonOptions, Range, Toggle, DefaultOnToggle, OptionGroup

class StartWithSports(DefaultOnToggle):
    """Start with the sports? HEAVILY RECOMMENDED
Will cause immediate BK if off"""
    display_name = "Start With Sports"

class ExhibitionDifficulty(OptionSet):
    """ Beating a stage on each difficulty will send a check
(Easy, Normal, Hard, Expert)"""
    display_name = "Exhibition Difficulty"
    valid_keys = {"Easy","Normal", "Hard", "Expert"}
    default = {"Normal", "Hard"}

class CupDifficulty(OptionSet):
    """Beating a cup on each difficulty will send a check
(Normal, Hard, Expert - NOT IMPLEMENTED)"""
    display_name = "Cup Difficulty"
    valid_keys = {"Normal", "Hard"}
    default = {"Normal", "Hard"}

class StageUnlockType(Choice):
    """How do you want stages to be unlocked?"""
    display_name = "Stage Unlock Type"
    option_by_cup_round = 0
    option_by_stage_name = 1
    default = 1

class GoalCondition(Choice):
    """What is your goal?"""
    display_name = "Goal Condition"
    option_defeat_behemoth = 0
    option_defeat_behemoth_king = 1
    option_win_cups = 2
    default = 1

class BehemothHP(Range):
    """Behemoth Health - 2400 is base game
Recommended to edit this in the yaml"""
    display_name = "Behemoth HP"
    range_start = 2400
    range_end = 7000
    default = 2400

class BehemothKingHP(Range):
    """Behemoth King Health - 3000 is base game
Recommended to edit this in the yaml"""
    display_name = "Behemoth King HP"
    range_start = 3000
    range_end = 7000
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
    default = 0

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
        ExhibitionDifficulty,
        CupDifficulty,
        StageUnlockType,
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
    exhibition_difficulty: ExhibitionDifficulty
    cup_difficulty: CupDifficulty
    stage_unlock_type: StageUnlockType
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