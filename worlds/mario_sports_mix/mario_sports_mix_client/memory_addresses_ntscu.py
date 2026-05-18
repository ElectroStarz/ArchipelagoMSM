class MatchAddresses:
    game_code = 0x800000
    match_status = 0x804D693C
    match_started = 0x805C09F7
    current_stage = 0x8047796E
    current_period = 0x804D684C
    special_active = 0x804D0F98
    tournament_diff = 0x804D5038
    exhibition_diff = 0x804D6853
    paused = 0x804CF71B
    cutscene_on = 0x805C0A19
    loading_screen_active = 0x804D73D4

    shot_clock = 0x804D6864
    time_remaining = 0x804D6864

    game_layout = 0x804D6846

class BossAddresses:
    behemoth_hp = 0x804CFFF4


class CupsWonMultiple:
    class Basketball:
        mushroom_cup = 0x902299B0
        flower_cup = 0x902299B2
        star_cup = 0x902299B4

    class Dodgeball:
        mushroom_cup = 0x90229A38
        flower_cup = 0x90229A3A
        star_cup = 0x90229A3C

    class Volleyball:
        mushroom_cup = 0x902299F4
        flower_cup = 0x902299F6
        star_cup = 0x902299F8

    class Hockey:
        mushroom_cup = 0x90229A7C
        flower_cup = 0x90229A7E
        star_cup = 0x90229A80


class PlayerAddresses:
    item_held = 0x804D691C

    special_meter = 0x804D000C

    character_1 = 0x804D6888
    character_2 = 0x804D688A
    character_3 = 0x804D688C

    is_cpu = 0x805C1B50

    costume_1 = 0x804D6890
    costume_2 = 0x804D6892
    costume_3 = 0x804D6894

    class Score:
        coins = 0x804D68DC
        score_period_1 = 0x804D6E98
        score_period_2 = 0x804D6E9C
        score_period_3 = 0x804D6EA0
        score_period_4 = 0x804D6EA4
        score_period_5 = 0x804D6EA8

    class Position:
        pos = 0x805C0BD0
        rotation = 0x805C0BD0

class OpponentAddresses:
    item_held = 0x804D6922

    class Score:
        coins = 0x804D68E0
        score_period_1 = 0x804D6EAC
        score_period_2 = 0x804D6EB0
        score_period_3 = 0x804D6EB4
        score_period_4 = 0x804D6EB8
        score_period_5 = 0x804D6EBC

class BasketballAddresses:
    games_played = 0x902299AC # Word
    time = 0x804D89F7 # Byte

    class Tournament:
        tabs = 0x90226D98 # Byte
        normal_cups = 0x90226D99 # Byte
        hard_cups = 0x90226D9A # Byte

    class Exhibition:
        tabs = 0x90226D38 # Byte
        mushroom_cup = 0x90226D39 # Byte
        flower_cup = 0x90226D3A # Byte
        star_cup = 0x90226D3B # Byte
        question_mark_cup = 0x90226D3C # Byte

    class Characters:
        # All Byte
        mario = 0x90226839
        luigi = 0x90226849
        peach = 0x90226859
        daisy = 0x90226869
        yoshi = 0x90226879
        wario = 0x90226889
        waluigi = 0x90226899
        donkey_kong = 0x902268A9
        diddy_kong = 0x902268B9
        toad = 0x902268C9
        bowser = 0x902268D9
        bowser_jr = 0x902268E9
        moogle = 0x902268F9
        cactuar = 0x90226909
        ninja = 0x90226919
        white_mage = 0x90226929
        slime = 0x90226939
        black_mage = 0x90226949

class DodgeballAddresses:
    games_played = 0x90229A34 # Word
    time = 0x804D8A2B # Byte

    class Tournament:
        tabs = 0x90226DB0 # Byte
        normal_cups = 0x90226DB1 # Byte
        hard_cups = 0x90226DB2 # Byte

    class Exhibition:
        tabs = 0x90226D50 # Byte
        mushroom_cup = 0x90226D51 # Byte
        flower_cup = 0x90226D52 # Byte
        star_cup = 0x90226D53 # Byte
        question_mark_cup = 0x90226D54 # Byte

    class Characters:
        # All Byte
        mario = 0x90226AB9
        luigi = 0x90226AC9
        peach = 0x90226AD9
        daisy = 0x90226AE9
        yoshi = 0x90226AF9
        wario = 0x90226B09
        waluigi = 0x90226B19
        donkey_kong = 0x90226B29
        diddy_kong = 0x90226B39
        toad = 0x90226B49
        bowser = 0x90226B59
        bowser_jr = 0x90226B69
        moogle = 0x90226B79
        cactuar = 0x90226B89
        ninja = 0x90226B99
        white_mage = 0x90226BA9
        slime = 0x90226BB9
        black_mage = 0x90226BC9

class VolleyballAddresses:
    games_played = 0x902299F0 # Word
    last_held = 0x804D0F98

    class Tournament:
        tabs = 0x90226DA4 # Byte
        normal_cups = 0x90226DA5 # Byte
        hard_cups = 0x90226DA6 # Byte

    class Exhibition:
        tabs = 0x90226D44 # Byte
        mushroom_cup = 0x90226D45 # Byte
        flower_cup = 0x90226D46 # Byte
        star_cup = 0x90226D47 # Byte
        question_mark_cup = 0x90226D48 # Byte

    class Characters:
        # All Byte
        mario = 0x90226979
        luigi = 0x90226989
        peach = 0x90226999
        daisy = 0x902269A9
        yoshi = 0x902269B9
        wario = 0x902269C9
        waluigi = 0x902269D9
        donkey_kong = 0x902269E9
        diddy_kong = 0x902269F9
        toad = 0x90226A09
        bowser = 0x90226A19
        bowser_jr = 0x90226A29
        moogle = 0x90226A39
        cactuar = 0x90226A49
        ninja = 0x90226A59
        white_mage = 0x90226A69
        slime = 0x90226A79
        black_mage = 0x90226A89

class HockeyAddresses:
    games_played = 0x90229A78 # Word
    time = 0x804D8A4B # Byte

    class Tournament:
        tabs = 0x90226DBC # Byte
        normal_cups = 0x90226DBD # Byte
        hard_cups = 0x90226DBE # Byte

    class Exhibition:
        tabs = 0x90226D5C # Byte
        mushroom_cup = 0x90226D5D # Byte
        flower_cup = 0x90226D5E # Byte
        star_cup = 0x90226D5F # Byte
        question_mark_cup = 0x90226D60 # Byte

    class Characters:
        # All Byte
        mario = 0x90226BF9
        luigi = 0x90226C09
        peach = 0x90226C19
        daisy = 0x90226C29
        yoshi = 0x90226C39
        wario = 0x90226C49
        waluigi = 0x90226C59
        donkey_kong = 0x90226C69
        diddy_kong = 0x90226C79
        toad = 0x90226C89
        bowser = 0x90226C99
        bowser_jr = 0x90226CA9
        moogle = 0x90226CB9
        cactuar = 0x90226CC9
        ninja = 0x90226CD9
        white_mage = 0x90226CE9
        slime = 0x90226CF9
        black_mage = 0x90226D09

class SportsMixAddresses:
    is_sports_mix = 0x804D7913 # Byte
    sports_mix_unlocked = 0x90226D98 # Byte | Same as basketball tournament tabs, set to 11 if Sports Mix unlocked

    class Tournament:
        cups = 0x90226D9C # Byte


class Offsets:
    class Player:
        special_meter_offsets = [0x10, 0x10C]
        special_active_offsets = [0xE0, 0x154]

        class B1:
            class Position:
                x_offsets = [0x54,0x0,0x90,0x98]
                y_offsets = [0x54,0x0,0x90,0x9C]
                z_offsets = [0x54,0x0,0x90,0xA0]
                rotation_offsets = [0x54,0x0,0x90,0xB4]
                is_cpu = [0x54, 0x0, 0x6F]

        class B2:
            class Position:
                x_offsets = [0x54,0x8,0x90,0x98]
                y_offsets = [0x54,0x8,0x90,0x9C]
                z_offsets = [0x54,0x8,0x90,0xA0]
                rotation_offsets = [0x54,0x8,0x90,0xB4]
                is_cpu = [0x54, 0x8, 0x6F]
                
        class B3:
            class Position:
                x_offsets = [0x54,0x10,0x90,0x98]
                y_offsets = [0x54,0x10, 0x90,0x9C]
                z_offsets = [0x54,0x10,0x90,0xA0]
                rotation_offsets = [0x54,0x10,0x90,0xB4]
                is_cpu = [0x54, 0x10, 0x6F]

    class Volleyball:
        last_held_offsets = [0x24, 0x214, 0x134]

    class Boss:
        behemoth_hp_offsets = [0x20, 0x34, 0x1F0]
        max_hp_offsets = [0x20, 0x34, 0x1F4]
