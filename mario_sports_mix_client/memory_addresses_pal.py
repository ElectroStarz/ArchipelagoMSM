class MatchAddresses:
    game_code = 0x800000 # String
    match_status = 0x804D78BC  # Byte | 0=Ongoing, 1=Win, 2=Lose, 3=Tie | In CAL
    match_started = 0x805C1977 # Byte | 1 = Yes, 0 = No
    current_stage = 0x8047888E  # String | Uses -0xF20 for NTSC-U | In CAL
    current_period = 0x804D77CC # Byte | Starts at 0 | In CAL
    max_periods = 0x804D77CB # Byte | Uses normal 1, 2, 3, 4 & 5
    current_module = 0x804D1154 # Word | Has Pointers | In CAL
    special_active = 0x804D0F98 # Word | Has Pointers
    tournament_diff = 0x804D5FB8 # Byte | Mushroom Cup uses one less (0 for Normal, 1 for Hard) | In CAL
    exhibition_diff = 0x804D77D3 # Byte | In CAL
    ex_diff_on_menu = 0x902319E3  # Byte | UNRELIABLE
    paused = 0x804D069B # Byte | In CAL
    cutscene_active = 0x805C1999 # Byte | In CAL
    loading_screen_active = 0x804D8354  # Word | In CAL
    set_break = 0x804D1178 # Word | Has Pointers
    game_speed = 0x804D77F4 # Float

    shot_clock = 0x804D77F0  # Float
    time_remaining = 0x804D77E4  # Float | In CAL
    max_time = 0x804D77E0 # Float | In CAL

    # 4 = 2v2, 0 = 3v3
    game_layout = 0x804D77C6 # Byte | In CAL

class CupsWonMultiple:
    # All are halfwords (2 bytes)
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

class GamesPlayed:
    basketball = 0x902299AC # Word
    dodgeball = 0x90229A34 # Word
    volleyball = 0x902299F0 # Word
    hockey = 0x90229A78  # Word

class PlayerAddresses:
    item_held = 0x804D789C  # Word | In CAL
    various_ball_pointers = 0x804D0F98 # Word | Has Pointers | In CAL
    human_players = 0x804d8e14 # Byte | Is 0 in demo

    special_meter = 0x804D0F8C # Float | Has Pointers | In CAL

    # Characters and costumes
    character_1 = 0x804D7808  # Byte
    character_2 = 0x804D780A  # Byte
    character_3 = 0x804D780C  # Byte

    costume_1 = 0x804D7810  # Byte
    costume_2 = 0x804D7812  # Byte
    costume_3 = 0x804D7814  # Byte

    dodge_damage = 0x805C1C70 # Word | Has Pointers
    dodge_max_health = 0x804D78D0 # Word

    is_cpu = 0x805C1B50 # Byte | Has Pointers

    # Score and coins
    class Score:
        coins = 0x804D785C  # Word | In CAL
        score_period_1 = 0x804D7E18  # Word
        score_period_2 = 0x804D7E1C  # Word
        score_period_3 = 0x804D7E20  # Word
        score_period_4 = 0x804D7E24  # Word
        score_period_5 = 0x804D7E28  # Word

    class Position:
        pos = 0x805C1B50 # Float | Has Pointers | In CAL

class OpponentAddresses:
    item_held = 0x804D78A0 # Word | In CAL
    dodge_max_health = 0x804D78D4 # Word

    # Score and coins
    class Score:
        coins = 0x804D7860 # Word | In CAL
        score_period_1 = 0x804D7E2C # Word
        score_period_2 = 0x804D7E30 # Word
        score_period_3 = 0x804D7E34 # Word
        score_period_4 = 0x804D7E38 # Word
        score_period_5 = 0x804D7E3C # Word

class BasketballAddresses:
    time = 0x804D9977 # Byte | In CAL

    class Tournament:
        tabs = 0x90226D98 # Byte | 2 = Normal, 3 = Normal + Hard
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
    time = 0x804D99AB # Byte | In CAL

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
    throw_timer = 0x805C1B50 # Word | Has Pointers
    points_to_win = 0x804D7807 # Byte

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
    time = 0x804D99CB # Byte | In CAL

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
    is_sports_mix = 0x804D7913 # Byte | In CAL
    sports_mix_unlocked = 0x90226D98 # Byte | Same as basketball tournament tabs, set to 11 if Sports Mix unlocked

    class Tournament:
        cups = 0x90226D9C # Byte

class BossAddresses:
    behemoth_hp = 0x804D0F74 # Float | Has Pointers | In CAL

class NTSCUAddresses:
    pass # Remove pass once an address has been added

class Pointers:
    class Match:
        current_module_offsets = [0x1F5]
        set_break_offsets = [0x94]

    class VBP: # Various Ball Pointers
        item_ball = [0x18, 0x2D] # B+H+V: 0 = Regular, 1 = Item | D: 1= Regular, 2 = Item
        v_last_held_offsets = [0x24, 0x214, 0x134]

    class Player:
        special_meter_offsets = [0x10,0x10C]
        special_active_offsets = [0xE0,0x154]

        class B1:
            dodge_damage = [0x1F4]
            is_cpu = [0x54, 0x0, 0x6F]
            class Position:
                x_offsets = [0x54,0x0,0x90,0x98]
                y_offsets = [0x54,0x0,0x90,0x9C]
                z_offsets = [0x54,0x0,0x90,0xA0]
                rotation_offsets = [0x54,0x0,0x90,0xB4]


        class B2:
            dodge_damage = [0x1FC]
            is_cpu = [0x54, 0x8, 0x6F]
            class Position:
                x_offsets = [0x54,0x8,0x90,0x98]
                y_offsets = [0x54,0x8,0x90,0x9C]
                z_offsets = [0x54,0x8,0x90,0xA0]
                rotation_offsets = [0x54,0x8,0x90,0xB4]


        class B3:
            dodge_damage = [0x204]
            is_cpu = [0x54, 0x10, 0x6F]
            class Position:
                x_offsets = [0x54,0x10,0x90,0x98]
                y_offsets = [0x54,0x10, 0x90,0x9C]
                z_offsets = [0x54,0x10,0x90,0xA0]
                rotation_offsets = [0x54,0x10,0x90,0xB4]

    class Volleyball:

        class ThrowTimeOffsets:
            b1 = [0x54,0x0,0x90,0x1B4]

    class Boss:
        behemoth_hp_offsets = [0x20, 0x34, 0x1F0]
        max_hp_offsets = [0x20, 0x34, 0x1F4]

class GeckoCodes:
    gecko_codes_pal = {
        # One Character Random
        0x8013f8a0: b'\x4B\xEC\x09\x38',
        0x800001d8: b'\x38\x60\x00\x00\x2C\x17\x00\x01\x40\x82\x00\x0C\x72\xD6\xF0\x00\x62\xD6\x00\x50\x48\x13\xf6\xb8',

        # Fix Unlocks
        0x801c4418: b'\x7C\x00\x00\x39',
        0x801c3f2c: b'\x7C\x63\x18\x39',

        # No Fill Button
        0x801b75c4: b'\x4B\xE4\x8B\xEC',
        0x800001b0: b'\x7c\x8c\x7e\x70\x2c\x0c\x00\x01\x40\x82\x00\x14\x2c\x00\x00\x00\x40\x82\x00\x0c\x38\x80\x00\x00\x60\x84\x80\x50\x7c\x08\x02\xa6\x60\x00\x00\x00\x48\x1B\x73\xF4',

        # Select More than Once (ONLY WRITE WHEN IN THE MENU MODULE; only needs to be written after module loads)
        0x815B40B0: b'\x60\x00\x00\x00',
        0x815B40B4: b'\x60\x00\x00\x00',
        0x815B41A0: b'\x38\x60\x00\x01',
        0x815B41A4: b'\x4E\x80\x00\x20',
        0x81618F64: b'\x38\xA0\x00\x00',
        0x81619250: b'\x38\x00\x00\x03',
        0x8161925c: b'\x38\x00\x00\x03',
        0x81619268: b'\x38\x00\x00\x03',
        0x81619274: b'\x38\x00\x00\x03',
        0x816186b0: b'\x7E\x9E\xA3\x78',
        0x816188d4: b'\x72\x84\xF0\x00',
        0x8161868c: b'\x72\x9E\xF0\x00',
        0x81618898: b'\x72\x84\xF0\x00',
        0x8161b538: b'\x38\xA0\x00\x13',
    }

    gecko_codes_ntscu = {
        # One Character Random
        0x8013f81c: b'\x4B\xEC\x09\xBC',
        0x800001d8: b'\x38\x60\x00\x00\x2C\x17\x00\x01\x40\x82\x00\x0C\x72\xD6\xF0\x00\x62\xD6\x00\x50\x48\x13\xF6\x34',

        # No fix unlocks for NTSC-U currently

        # No Fill Button
        0x801b7540: b'\x4B\xE4\x8C\x70',
        0x800001b0: b'\x7c\x8c\x7e\x70\x2c\x0c\x00\x01\x40\x82\x00\x14\x2c\x00\x00\x00\x40\x82\x00\x0c\x38\x80\x00\x00\x60\x84\x80\x50\x7c\x08\x02\xa6\x60\x00\x00\x00\x48\x1B\x73\x70',

        # Select More than Once (ONLY WRITE WHEN IN THE MENU MODULE; only needs to be written after module loads)
        0x815B5270: b'\x60\x00\x00\x00',
        0x815B5274: b'\x60\x00\x00\x00',
        0x815B5360: b'\x38\x60\x00\x01',
        0x815B5364: b'\x4E\x80\x00\x20',
        0x8161a124: b'\x38\xA0\x00\x00',
        0x8161A410: b'\x38\x00\x00\x03',
        0x8161A41C: b'\x38\x00\x00\x03',
        0x8161A428: b'\x38\x00\x00\x03',
        0x8161A434: b'\x38\x00\x00\x03',
        0x81619870: b'\x7E\x9E\xA3\x78',
        0x81619A94: b'\x72\x84\xF0\x00',
        0x8161984C: b'\x72\x9E\xF0\x00',
        0x81619A58: b'\x72\x84\xF0\x00',
        0x8161C6F8: b'\x38\xA0\x00\x13',
    }