from dataclasses import dataclass

from Options import Choice, OptionSet, PerGameCommonOptions, Range, Toggle, DefaultOnToggle, OptionGroup, Visibility

class StartWithSports(Choice):
    """Start with the sports? HEAVILY RECOMMENDED
Will cause immediate BK if off"""
    visibility = Visibility.none
    display_name = "Start With Sports - READ DESCRIPTION!"
    option_none = 0
    option_excluding_sports_mix = 1
    option_with_sports_mix = 2
    default = 1

class StartWithMushroomCup(Choice):
    """Start with Mushroom Cup for Basketball, Dodgeball, Volleyball and Hockey? (Also unlocks related stages)
Heavily recommended, may break some things if off"""
    display_name = "Start with Mushroom Cup (+Stages) - READ DESCRIPTION!"
    option_none = 0
    option_normal_difficulty = 1
    option_hard_difficulty = 2
    option_both = 3
    default = 1

class StartWithCharacters(Choice):
    """Start with 2 or 3 random characters"""
    display_name = "Start with Random Characters"
    option_none = 0
    option_2_characters = 2
    option_3_characters = 3
    default = 0

class ExhibitionDifficulty(OptionSet):
    """Which exhibition difficulties should be included? If the difficulty is off, you won't be able to send checks with
that difficulty
(Easy, Normal, Hard, Expert)"""
    display_name = "Exhibition Difficulty"
    valid_keys = {"Easy", "Normal", "Hard", "Expert"}
    default = {"Normal", "Hard"}

class TournamentDifficulty(OptionSet):
    """What tournament difficulty would you like to include? If a difficulty is off, you will not receive the item for
that difficulty.
    (Normal, Hard)"""
    display_name = "Tournament Difficulty"
    valid_keys = {"Normal", "Hard"}
    default = {"Normal", "Hard"}

class PartyMode(OptionSet):
    """What party mode games do you want to include?
(Feed Petey, Harmony Hustle, Bob-omb Dodge, Smash Skate)
Doesn't work at the moment"""
    visibility = Visibility.none
    display_name = "Party Mode Games"
    valid_keys = {"Feed Petey", "Harmony Hustle", "Bob-omb Dodge", "Smash Skate"}
    default = {}

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
    default = 1

class BeMean(Choice):
    """Have locations behind bosses even if your goal isn't that boss!
Cannot be the same as the goal condition!"""
    display_name = "Be mean?"
    option_no = 0
    option_defeat_behemoth = 1
    option_defeat_behemoth_king = 2
    default = 0

class BehemothHP(Range):
    """Behemoth Health - 2400 is default
Recommended to edit this in the yaml (2400 - 4000)"""
    display_name = "Behemoth HP"
    range_start = 2400
    range_end = 4000
    default = 2400

class BehemothKingHP(Range):
    """Behemoth King Health - 3000 is default
Recommended to edit this in the yaml (3000 - 7000)"""
    display_name = "Behemoth King HP"
    range_start = 3000
    range_end = 7000
    default = 3000

class TrapChance(Range):
    """The chance a filler is swapped with a trap"""
    display_name = "Trap Chance"
    range_start = 0
    range_end = 100
    default = 25

# class TeamSanity(Choice):
#     """(NOT WORKING) Turn on or off team sanity
#     (Playing with every team combination sends a check)"""
#     display_name = "Team Sanity"
#     option_off = 0
#     option_characters = 1
#     option_characters_and_costumes = 2
#     default = 0
#
# class ScoreSanity(Toggle):
#     """(NOT WORKING) Toggle on or off score sanity"""
#     display_name = "Score Sanity"
#     default = False
#
# class ScoreSanityPoints(Range):
#     """(NOT WORKING) Every number of points will send a check"""
#     display_name = "Score Sanity Points"
#     range_start = 1
#     range_end = 10
#     default = 5
#
# class ScoreSanityMax(Range):
#     """(NOT WORKING) Score Sanity will go up to this number of points"""
#     display_name = "Score Sanity Max"
#     range_start = 10
#     range_end = 100
#     default = 40
#
# class SpecialSanity(Toggle):
#     """(NOT WORKING) Using each character's special sends a check"""
#     display_name = "Special Sanity"
#     default = False
#
# class StageSanity(Choice):
#     """(NOT WORKING) Playing and/or winning on each stage sends a check"""
#     display_name = "Stage Sanity"
#     option_off = 0
#     option_playing = 1
#     option_winning = 2
#     option_both = 3
#     default = 0

msm_option_groups = [
    OptionGroup("Game Options", [
        StartWithSports,
        StartWithMushroomCup,
        StartWithCharacters,
        ExhibitionDifficulty,
        TournamentDifficulty,
        SportsMixUnlock,
        TrapChance,
    ]),
    OptionGroup("Goal Options", [
        GoalCondition,
        BeMean,
        BehemothHP,
        BehemothKingHP,
    ]),
    # OptionGroup("Sanity Options (NOT WORKING)", [
    #     TeamSanity,
    #     ScoreSanity,
    #     ScoreSanityPoints,
    #     ScoreSanityMax,
    #     SpecialSanity,
    #     StageSanity,
    # ])
]

@dataclass()
class MSMOptions(PerGameCommonOptions):
    start_with_sports: StartWithSports
    start_with_mushroom_cup: StartWithMushroomCup
    start_with_characters: StartWithCharacters
    exhibition_difficulty: ExhibitionDifficulty
    tournament_difficulty: TournamentDifficulty
    party_mode: PartyMode
    sports_mix_unlock: SportsMixUnlock
    goal_condition: GoalCondition
    be_mean: BeMean
    behemoth_hp: BehemothHP
    behemoth_king_hp: BehemothKingHP
    trap_chance: TrapChance
    # team_sanity: TeamSanity
    # score_sanity: ScoreSanity
    # score_sanity_points: ScoreSanityPoints
    # score_sanity_max: ScoreSanityMax
    # special_sanity: SpecialSanity
    # stage_sanity: StageSanity