class MatchAddresses:
    game_code = 0x800000
    match_status = 0x804D693C
    match_started = 0x805C09F7
    current_stage = 0x8047796E
    current_period = 0x804D684C
    on_loading_screen = 0x804D8354
    special_active = 0x804D0F98
    tournament_diff = 0x804D5038
    exhibition_diff = 0x804D6853

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
    item_held = 0x804D691E

    special_meter = 0x804D000C

    character_1 = 0x804D6888
    character_2 = 0x804D688A
    character_3 = 0x804D688C

    is_cpu = 0x805C1B50

    costume_1 = 0x804D7810
    costume_2 = 0x804D7812
    costume_3 = 0x804D7814

    class Score:
        coins = 0x804D68DC
        score_period_1 = 0x804D6E98
        score_period_2 = 0x804D6E9C
        score_period_3 = 0x804D6EA0
        score_period_4 = 0x804D6EA4
        score_period_5 = 0x804D6EA8

    class Position:
        pos = 0x805C1B50
        rotation = 0x805C1B50


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
    games_played = 0x90228A2C # Word

    class Tournament:
        tabs = 0x90225E18 # Byte
        normal_cups = 0x90225E19 # Byte
        hard_cups = 0x90225E1A # Byte

    class Exhibition:
        tabs = 0x90225DB8 # Byte
        mushroom_cup = 0x90225DB9 # Byte
        flower_cup = 0x90225DBA # Byte
        star_cup = 0x90225DBB # Byte
        question_mark_cup = 0x90225DBC # Byte

    class Characters:
        # All Byte
        mario = 0x902258B9
        luigi = 0x902258C9
        peach = 0x902258D9
        daisy = 0x902258E9
        yoshi = 0x902258F9
        wario = 0x90225909
        waluigi = 0x90225919
        donkey_kong = 0x90225929
        diddy_kong = 0x90225939
        toad = 0x90225949
        bowser = 0x90225959
        bowser_jr = 0x90225969
        moogle = 0x90225979
        cactuar = 0x90225989
        ninja = 0x90225999
        white_mage = 0x902259A9
        slime = 0x902259B9
        black_mage = 0x902259C9


class DodgeballAddresses:
    games_played = 0x90228AB4 # Word

    class Tournament:
        tabs = 0x90225E30 # Byte
        normal_cups = 0x90225E31 # Byte
        hard_cups = 0x90225E32 # Byte

    class Exhibition:
        tabs = 0x90225DD0 # Byte
        mushroom_cup = 0x90225DD1 # Byte
        flower_cup = 0x90225DD2 # Byte
        star_cup = 0x90225DD3 # Byte
        question_mark_cup = 0x90225DD4 # Byte

    class Characters:
        # All Byte
        mario = 0x90225B39
        luigi = 0x90225B49
        peach = 0x90225B59
        daisy = 0x90225B69
        yoshi = 0x90225B79
        wario = 0x90225B89
        waluigi = 0x90225B99
        donkey_kong = 0x90225BA9
        diddy_kong = 0x90225BB9
        toad = 0x90225BC9
        bowser = 0x90225BD9
        bowser_jr = 0x90225BE9
        moogle = 0x90225BF9
        cactuar = 0x90225C09
        ninja = 0x90225C19
        white_mage = 0x90225C29
        slime = 0x90225C39
        black_mage = 0x90225C49


class VolleyballAddresses:
    games_played = 0x90228A70 # Word
    last_held = 0x804D0018

    class Tournament:
        tabs = 0x90225E24 # Byte
        normal_cups = 0x90225E25 # Byte
        hard_cups = 0x90225E26 # Byte

    class Exhibition:
        tabs = 0x90225DC4 # Byte
        mushroom_cup = 0x90225DC5 # Byte
        flower_cup = 0x90225DC6 # Byte
        star_cup = 0x90225DC7 # Byte
        question_mark_cup = 0x90225DC8 # Byte

    class Characters:
        # All Byte
        mario = 0x902259F9
        luigi = 0x90225A09
        peach = 0x90225A19
        daisy = 0x90225A29
        yoshi = 0x90225A39
        wario = 0x90225A49
        waluigi = 0x90225A59
        donkey_kong = 0x90225A69
        diddy_kong = 0x90225A79
        toad = 0x90225A89
        bowser = 0x90225A99
        bowser_jr = 0x90225AA9
        moogle = 0x90225AB9
        cactuar = 0x90225AC9
        ninja = 0x90225AD9
        white_mage = 0x90225AE9
        slime = 0x90225AF9
        black_mage = 0x90225B09


class HockeyAddresses:
    games_played = 0x90228AF8 # Word

    class Tournament:
        tabs = 0x90225E3C # Byte
        normal_cups = 0x90225E3D # Byte
        hard_cups = 0x90225E3E # Byte

    class Exhibition:
        tabs = 0x90225DDC # Byte
        mushroom_cup = 0x90225DDD # Byte
        flower_cup = 0x90225DDE # Byte
        star_cup = 0x90225DDF # Byte
        question_mark_cup = 0x90225DE0 # Byte

    class Characters:
        # All Byte
        mario = 0x90225C79
        luigi = 0x90225C89
        peach = 0x90225C99
        daisy = 0x90225CA9
        yoshi = 0x90225CB9
        wario = 0x90225CC9
        waluigi = 0x90225CD9
        donkey_kong = 0x90225CE9
        diddy_kong = 0x90225CF9
        toad = 0x90225D09
        bowser = 0x90225D19
        bowser_jr = 0x90225D29
        moogle = 0x90225D39
        cactuar = 0x90225D49
        ninja = 0x90225D59
        white_mage = 0x90225D69
        slime = 0x90225D79
        black_mage = 0x90225D89


class SportsMixAddresses:
    is_sports_mix = 0x804D6993
    sports_mix_unlocked = 0x90226D98

    class Tournament:
        cups = 0x90226D9C


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
