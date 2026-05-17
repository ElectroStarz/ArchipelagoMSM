class MatchAddresses:
    game_code = 0x800000
    match_status = 0x804D693C
    match_started = 0x805C1977
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
    behemoth_hp = 0x804D0F74


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

    special_meter = 0x804D0F8C

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