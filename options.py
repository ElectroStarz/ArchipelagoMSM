from dataclasses import dataclass
from Options import *

class StartWithSports(DefaultOnToggle):
    """Start with 4 sports? HEAVILY RECOMMENDED
Will cause immediate BK if off and you DON'T have any party modes given at the start."""
    display_name = "Start With Sports - READ DESCRIPTION!"

class EnabledSports(OptionSet):
    """Choose which sports to enable

NOTE: You can still do Behemoth without all the 4 main sports enabled however
Behemoth King **requires** Sports Mix enabled"""
    display_name = "Enabled Sports"
    valid_keys = {"Basketball", "Dodgeball", "Volleyball", "Hockey", "Sports Mix"}
    default = {"Basketball", "Dodgeball", "Volleyball", "Hockey", "Sports Mix"}

class IncludeTournaments(DefaultOnToggle):
    """Include tournament locations and items"""
    display_name = "Include Tournaments"

class IncludeExhibition(DefaultOnToggle):
    """Include exhibition locations and items"""
    display_name = "Include Exhibition"

class ExhibitionType(Choice):
    """What type of exhibition locations do you want?

**All Sports**: Exhibition locations will be for all the 4 main sports
**Universal**: Exhibition locations will be for **any** sport"""
    display_name = "Exhibition Type"
    option_all_sports = 0
    option_universal = 1
    default = 0

class StartWithMushroomCup(Choice):
    """Start with Mushroom Cup for Basketball, Dodgeball, Volleyball and Hockey?
(Also unlocks related courts) - Recommended if you don't have party games on!

Random option pulls from both Normal and Hard Cups 
and defaults to both if Progressive Cups are enabled.
Gives all Mushroom Cup Stages as well if Progressive Courts are enabled."""
    display_name = "Start with Mushroom Cup (+Courts)"
    option_none = 0
    option_normal_difficulty = 1
    option_hard_difficulty = 2
    option_both = 3
    option_random_cups = 4
    default = 1

class StartWithRandomMushroomCups(Range):
    """How many random Mushroom Cups should you start with? (1-7)"""
    display_name = "Start with Random Mushroom Cups"
    range_start = 1
    range_end = 7
    default = 1

class StartWithCharacters(Choice):
    """Start with 2 or 3 random characters"""
    display_name = "Start with Random Characters"
    option_none = 0
    option_2_characters = 2
    option_3_characters = 3
    default = 0

class ExhibitionDifficulties(OptionSet):
    """Which exhibition difficulties should be included?
If the difficulty is off, you won't be able to send checks with that difficulty
(Easy, Normal, Hard, Expert)"""
    display_name = "Exhibition Difficulties"
    valid_keys = {"Easy", "Normal", "Hard", "Expert"}
    default = {"Normal", "Hard"}

class CourtUnlockType(Choice):
    """How to unlock courts

**Court Item**: Each court is its own item
**Progressive Court**: Courts are unlocked in a certain order with progressive items
Note: Behemoth Stage is an item! Behemoth Stage is the last court unlocked in Progressive Court"""
    display_name = "Court Unlock Type"
    option_court_item = 0
    option_progressive_court = 1
    default = 0

class CupUnlockType(Choice):
    """How to unlock cups

**Cup Item**: Each cup is its own item
**Progressive Cup**: Cups are unlocked in a certain order with progressive items. (Normal -> Hard (If enabled) ->
Sports Mix)
Note: Progressive Cup will unlock the cup for **every** sport while Cup Item has cups for each sport"""
    display_name = "Cup Unlock Type"
    option_cup_item = 0
    option_progressive_cup = 1
    default = 0

class HardTournamentDifficulty(DefaultOnToggle):
    """Would you like to include locations and items for Hard Tournaments?
Adds 3 Progressive Cups to the pool if Progressive Cup Item is selected"""
    display_name = "Include Hard Tournaments"

class SportsMixUnlock(Choice):
    """Unlock Sports Mix by getting the Sports Mix item or the 4 Sports Crystals"""
    display_name = "Sports Mix Unlock"
    option_sports_mix_item = 0
    option_sports_crystals = 1
    default = 0

class GoalCondition(Choice):
    """What is your goal?

**Defeat Behemoth**: Defeat the Behemoth to goal!
**Defeat Behemoth King**: Defeat the Behemoth King to goal!
**Win Cups**: Win a certain amount of cups to goal!
**Exhibition Tour**: Win every exhibition match for your selected difficulties to goal! (Needs All Sports option)
**Party Palooza**: Win every game in every Party Mode to goal!

NOTE: Exhibition Tour disables the QoL feature for winning exhibition matches, recommended to have 2 difficulties
selected"""
    display_name = "Goal Condition"
    option_defeat_behemoth = 1
    option_defeat_behemoth_king = 2
    option_win_cups = 3
    option_exhibition_tour = 4
    option_party_palooza = 5
    default = 2

class WinCupsAmount(Range):
    """How many cups are required to goal?"""
    display_name = "Win Cups Amount"
    range_start = 1
    range_end = 27
    default = 15

class BossLocations(Choice):
    """Have locations behind bosses even if your goal isn't that boss!
Cannot be the same as the goal condition!"""
    display_name = "Boss Locations"
    option_no = 0
    option_defeat_behemoth = 1
    option_defeat_behemoth_king = 2
    option_both = 3
    default = 0

class BehemothHP(Range):
    """Behemoth Health - 2400 is default
Recommended to edit this in the YAML (2400 - 4000)"""
    display_name = "Behemoth HP"
    range_start = 2400
    range_end = 4000
    default = 2400

class BehemothKingHP(Range):
    """Behemoth King Health - 3000 is default
Recommended to edit this in the YAML (3000 - 7000)"""
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

# === Deathlink Options ===

class Deathlink(DeathLink):
    """When you die, everyone who enabled death link dies. Of course, the reverse is true too.
Toggleable inside client"""
    display_name = "Death Link"
    default = False

class DeathlinkAction(Choice):
    """What counts as sending a deathlink? Requires Deathlink on

NOTE: Every number of points works like normal for everything BUT dodgeball.
In dodgeball, everytime the opponent wins the set a deathlink triggers"""
    display_name = "Death Link Action"
    option_losing_or_tying_a_match = 0
    option_every_number_of_points = 1
    default = 0

class DeathlinkConsequence(Choice):
    """What happens when you receive a deathlink? Requires Deathlink on"""
    display_name = "Death Link Consequence"
    option_lose_match = 0
    option_opponent_gains_points = 1
    default = 0

# --- Action Specific Settings ---
class DeathlinkOpponentScorePoints(Range):
    """How many points should the opponent get to send a deathlink?
Requires Deathlink on & Every Number Of Points action"""
    display_name = "[DL-A] Opponent Scores Points"
    range_start = 1
    range_end = 20
    default = 10

# --- Consequence Specific Settings ---
class DeathlinkOpponentGetPoints(Range):
    """How many points should the opponent get when receiving a deathlink?
Requires Deathlink on & Opponent Gains Point consequence"""
    display_name = "[DL-C] Opponent Gets Points"
    range_start = 1
    range_end = 20
    default = 10

class DeathlinkBossHealthRecovered(Range):
    """What percentage of the boss' health should be recovered when sent a deathlink?
(Behemoth & Behemoth King)"""
    display_name = "[DL-C] Boss % Health Recovered"
    range_start = 0
    range_end = 100
    default = 20

class DeathlinkDodgeballHealthLost(Range):
    """**ONLY FOR DODGEBALL**
How much health will you lose when you get sent a deathlink if you're in dodgeball?"""
    display_name = "[DL-C] Dodgeball Health Lost"
    range_start = 0
    range_end = 100
    default = 20

# === Sanity Settings ===

class CharacterSanity(Choice):
    """Turn on or off Character Sanity
(Winning with a character and/or costume sends a check)"""
    display_name = "Character Sanity"
    option_off = 0
    option_characters = 1
    option_characters_and_costumes = 2
    default = 0

class SendBothCharacterCostume(Toggle):
    """When winning with a costume, send the Character Sanity
check for *both* the character and the costume or just the costume"""
    display_name = "Send both Character Sanity"
    default = False

class ScoreSanity(Toggle):
    """(NOT WORKING) Toggle on or off score sanity"""
    visibility = Visibility.none
    display_name = "Score Sanity"
    default = False

class ScoreSanityPoints(Range):
    """(NOT WORKING) Every number of points will send a check"""
    visibility = Visibility.none
    display_name = "Score Sanity Points"
    range_start = 1
    range_end = 10
    default = 5

class ScoreSanityMax(Range):
    """(NOT WORKING) Score Sanity will go up to this number of points"""
    visibility = Visibility.none
    display_name = "Score Sanity Max"
    range_start = 10
    range_end = 100
    default = 40

class SpecialSanity(Toggle):
    """Using each character's special sends a check"""
    display_name = "Special Sanity"
    default = False

class CourtSanity(Toggle):
    """Winning on each court sends a check"""
    display_name = "Court Sanity"
    default = False

# === Custom Tournament Settings ===

# --- Basketball ---
class BasketTime(Choice):
    """Select the custom amount of time for a Basketball tournament"""
    display_name = "Basketball Tournament Time"
    option_1_min_30_secs = 0
    option_2_mins = 1
    option_2_mins_30_secs = 2
    option_3_mins = 3
    option_3_mins_30_secs = 4
    option_off = 5
    default = 2

    @classmethod
    def get_option_name(cls, value):
        match value:
            case 0: return "1:30"
            case 1: return "2:00"
            case 2: return "2:30"
            case 3: return "3:00"
            case 4: return "3:30"
            case 5: return "OFF"
            case _: return "ERROR"

class EnableBPointsWin(Toggle):
    """Getting a certain amount of points wins you or the opponent the set"""
    display_name = "Enable Points Win"
    default = False

class BPointsToWin(Range):
    """Set the required amount of points to win
NOTE: The requirement for Bowser Jr. Blvd. is (value x 5) + 50 rounded
to the nearest 1 decimal place"""
    display_name = "Points to Win"
    range_start = 10
    range_end = 50
    default = 30

class BPeriod(Range):
    """How many periods do you want to be playing?
Recommended to set a low amount, kinda boring otherwise."""
    display_name = "Period Amount"
    range_start = 1
    range_end = 5
    default = 1

# --- Dodgeball ---
class DodgeTime(Choice):
    """Select the custom amount of time for a Dodgeball tournament"""
    display_name = "Dodgeball Tournament Time"
    option_2_mins = 0
    option_2_mins_30_secs = 1
    option_3_mins = 2
    option_3_mins_30_secs = 3
    option_4_mins = 4
    option_off = 5
    default = 2

    @classmethod
    def get_option_name(cls, value):
        match value:
            case 0: return "2:00"
            case 1: return "2:30"
            case 2: return "3:00"
            case 3: return "3:30"
            case 4: return "4:00"
            case 5: return "OFF"
            case _: return "ERROR"

class DPeriod(Range):
    """How many periods do you want to be playing?
Recommended to set a low amount, kinda boring otherwise."""
    display_name = "Period Amount"
    range_start = 1
    range_end = 5
    default = 1

class DMaxHealth(Choice):
    """How much health should everyone have?"""
    display_name = "Health Amount"
    option_100 = 100
    option_150 = 150
    option_200 = 200
    option_250 = 250
    option_300 = 300
    default = 100

# --- Volleyball ---
class VPointsToWin(Range):
    """Set the required amount of points to win
NOTE: The requirement for Bowser Jr. Blvd. is value x 2 rounded
to the nearest 1 decimal place"""
    display_name = "Points to Win"
    range_start = 10
    range_end = 20
    default = 10

class VPeriod(Range):
    """How many sets do you want to be playing?
Recommended to set a low amount, kinda boring otherwise."""
    display_name = "Set Amount"
    range_start = 1
    range_end = 5
    default = 1

# --- Hockey ---
class HockeyTime(Choice):
    """Select the custom amount of time for a Hockey tournament"""
    display_name = "Hockey Tournament Time"
    option_2_mins = 0
    option_2_mins_30_secs = 1
    option_3_mins = 2
    option_3_mins_30_secs = 3
    option_4_mins = 4
    option_off = 5
    default = 2

    @classmethod
    def get_option_name(cls, value):
        match value:
            case 0: return "2:00"
            case 1: return "2:30"
            case 2: return "3:00"
            case 3: return "3:30"
            case 4: return "4:00"
            case 5: return "OFF"
            case _: return "ERROR"

class EnableHPointsWin(Toggle):
    """Getting a certain amount of points wins you or the opponent the set"""
    display_name = "Enable Points Win"
    default = False

class HPointsToWin(Range):
    """Set the required amount of points to win
NOTE: The requirement for Bowser Jr. Blvd. is (value x 5) + 50 rounded
to the nearest 1 decimal place"""
    display_name = "Points to Win"
    range_start = 10
    range_end = 50
    default = 20

class HPeriod(Range):
    """How many periods do you want to be playing?
Recommended to set a low amount, kinda boring otherwise."""
    display_name = "Period Amount"
    range_start = 1
    range_end = 5
    default = 1

# === Party Mode Options ===
class PartyMode(OptionSet):
    """Which (if any) Party Modes do you want enabled?
(Feed Petey, Harmony Hustle, Bob-omb Dodge, Smash Skate)

NOTE: All are required if your goal is Party Palooza"""
    display_name = "Enabled Party Modes"
    valid_keys = {"Feed Petey", "Harmony Hustle", "Bob-omb Dodge", "Smash Skate"}
    default = {"Feed Petey", "Smash Skate"}

class StartWithParty(Toggle):
    """Start with the enabled party modes
Useful if you're not starting with the sports!"""
    display_name = "Start with Party Modes"

class PartyModeOpponent(Choice):
    """Which CPU will be your main opponent?
(This CPU will get things like points from deathlink, points
from Coins Trap, etc)"""
    display_name = "Party Mode Opponent"
    option_CPU_2 = 0
    option_CPU_3 = 1
    option_CPU_4 = 2
    default = 0

    @classmethod
    def get_option_name(cls, value):
        match value:
            case 0: return "CPU 2 (Red)"
            case 1: return "CPU 3 (Green)"
            case 2: return "CPU 4 (Yellow)"
            case _: return "ERROR"

class IncludeAltPaths(Toggle):
    """Include alternate paths?
    No: Alt Paths will not be included
    Yes: Alt Paths will be included
    LR Split: Alt Paths will be split between Left and Right"""

    display_name = "Include Alternate Paths"
    default = False

class AltPathType(Choice):
    """What Type of Alt Path Locations do you want?
    All Paths: Alt Path locations will be per sport and per difficulty
    Difficulty Universal: Alt Path Locations will be for **any** difficulty
    Sport Universal: Alt Path Locations will be for **any** sport
    Full Universal: Alt Path Locations will be for **any** difficulty/sport
    Progessive Options give Progressive items which unlock the Alt Paths in cup order
    
    IMPORTANT NOTE: Sports Mix will NOT send any alt path checks if alt paths are combined"""

    display_name = "Alternate Path Type"
    option_all_paths = 0
    option_difficulty_combine = 1
    option_sport_combine = 2
    option_full_combine = 3
    option_progressive_sport_combine = 4
    option_progressive_full_combine = 5
    default = 0

class AlwaysSpawnAltPaths(Toggle):
    """Make it so the criteria to spawn Alternate Paths is always enabled

    NOTE: Certain conditions require Special Meter, you can reset to get a better
    position for most of them except the Dodgeball Star Cup Round 2 condition,
    though this is covered in logic."""
    display_name = "Always Spawn Alt Paths"
    default = True

msm_option_groups = [
    OptionGroup("Game Options", [
        EnabledSports,
        IncludeExhibition,
        IncludeTournaments,
        StartWithSports,
        StartWithMushroomCup,
        StartWithRandomMushroomCups,
        CupUnlockType,
        CourtUnlockType,
        StartWithCharacters,
        ExhibitionType,
        ExhibitionDifficulties,
        HardTournamentDifficulty,
        SportsMixUnlock,
        TrapChance,
    ]),
    OptionGroup("Basketball Tournament Options", [
        BasketTime,
        EnableBPointsWin,
        BPointsToWin,
        BPeriod,
    ]),
    OptionGroup("Dodgeball Tournament Options", [
        DodgeTime,
        DPeriod,
        DMaxHealth,
    ]),
    OptionGroup("Volleyball Tournament Options", [
        VPointsToWin,
        VPeriod,
    ]),
    OptionGroup("Hockey Tournament Options", [
        HockeyTime,
        EnableHPointsWin,
        HPointsToWin,
        HPeriod,
    ]),
    OptionGroup("Goal Options", [
        GoalCondition,
        WinCupsAmount,
        BossLocations,
        BehemothHP,
        BehemothKingHP,
    ]),
    OptionGroup("Party Mode Options", [
        PartyMode,
        StartWithParty,
        PartyModeOpponent,
    ]),
    OptionGroup("Alternate Path Options", [
        IncludeAltPaths,
        AltPathType,
        AlwaysSpawnAltPaths,
    ]),
    OptionGroup("Deathlink Options", [
        Deathlink,
        DeathlinkAction,
        DeathlinkOpponentScorePoints,
        DeathlinkConsequence,
        DeathlinkOpponentGetPoints,
        DeathlinkBossHealthRecovered,
        DeathlinkDodgeballHealthLost,
    ]),
    OptionGroup("Sanity Options", [
        CharacterSanity,
        SendBothCharacterCostume,
        CourtSanity,
        SpecialSanity,
        # ScoreSanity,
        # ScoreSanityPoints,
        # ScoreSanityMax,
    ]),
]

@dataclass
class MSMOptions(PerGameCommonOptions):
    enabled_sports: EnabledSports
    include_tournaments: IncludeTournaments
    include_exhibition: IncludeExhibition
    start_with_sports: StartWithSports
    start_with_mushroom_cup: StartWithMushroomCup
    start_with_random_mushroom_cups: StartWithRandomMushroomCups
    cup_unlock_type: CupUnlockType
    court_unlock_type: CourtUnlockType
    start_with_characters: StartWithCharacters
    exhibition_type: ExhibitionType
    exhibition_difficulties: ExhibitionDifficulties
    hard_tournament_difficulty: HardTournamentDifficulty
    sports_mix_unlock: SportsMixUnlock
    goal_condition: GoalCondition
    win_cups_amount: WinCupsAmount
    boss_locations: BossLocations
    behemoth_hp: BehemothHP
    behemoth_king_hp: BehemothKingHP
    trap_chance: TrapChance

    # Alternate Path Options
    include_alt_paths: IncludeAltPaths
    alt_path_type: AltPathType
    always_spawn_alt_paths: AlwaysSpawnAltPaths

    # Tournament Rules
    basket_time: BasketTime
    enable_b_points_win: EnableBPointsWin
    b_points_win: BPointsToWin
    b_period: BPeriod

    dodge_time: DodgeTime
    d_period: DPeriod
    d_max_health: DMaxHealth

    v_points_win: VPointsToWin
    v_period: VPeriod

    hockey_time: HockeyTime
    enable_h_points_win: EnableHPointsWin
    h_points_win: HPointsToWin
    h_period: HPeriod

    # Party Mode
    party_mode: PartyMode
    start_with_party_modes: StartWithParty
    party_mode_opponent: PartyModeOpponent

    # Deathlink
    deathlink: Deathlink
    deathlink_action: DeathlinkAction
    deathlink_consequence: DeathlinkConsequence
    deathlink_opponent_scores_points: DeathlinkOpponentScorePoints
    deathlink_opponent_get_points: DeathlinkOpponentGetPoints
    deathlink_boss_health_recovered: DeathlinkBossHealthRecovered
    deathlink_dodgeball_health_lost: DeathlinkDodgeballHealthLost

    # Sanity Stuff
    character_sanity: CharacterSanity
    send_both_character_sanity: SendBothCharacterCostume
    court_sanity: CourtSanity
    special_sanity: SpecialSanity
    score_sanity: ScoreSanity
    score_sanity_points: ScoreSanityPoints
    score_sanity_max: ScoreSanityMax

    start_inventory_from_pool: StartInventoryPool
