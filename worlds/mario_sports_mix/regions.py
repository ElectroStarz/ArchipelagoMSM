from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Region
from .options import GoalCondition

if TYPE_CHECKING:
    from . import MSMWorld


def create_and_connect_regions(world: "MSMWorld") -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: "MSMWorld") -> None:
    main_menu = Region("Main Menu", world.player, world.multiworld)
    # Basketball
    basketball = Region("Basketball", world.player, world.multiworld)
    b_exhibition_e = Region("Basketball: Exhibition (Easy)", world.player, world.multiworld)
    b_exhibition_n = Region("Basketball: Exhibition (Normal)", world.player, world.multiworld)
    b_exhibition_h = Region("Basketball: Exhibition (Hard)", world.player, world.multiworld)
    b_exhibition_ex = Region("Basketball: Exhibition (Expert)", world.player, world.multiworld)
    b_extra = Region("Basketball: Extra", world.player, world.multiworld)
    # Dodgeball
    dodgeball = Region("Dodgeball", world.player, world.multiworld)
    d_exhibition_e = Region("Dodgeball: Exhibition (Easy)", world.player, world.multiworld)
    d_exhibition_n = Region("Dodgeball: Exhibition (Normal)", world.player, world.multiworld)
    d_exhibition_h = Region("Dodgeball: Exhibition (Hard)", world.player, world.multiworld)
    d_exhibition_ex = Region("Dodgeball: Exhibition (Expert)", world.player, world.multiworld)
    d_extra = Region("Dodgeball: Extra", world.player, world.multiworld)
    # Volleyball
    volleyball = Region("Volleyball", world.player, world.multiworld)
    v_exhibition_e = Region("Volleyball: Exhibition (Easy)", world.player, world.multiworld)
    v_exhibition_n = Region("Volleyball: Exhibition (Normal)", world.player, world.multiworld)
    v_exhibition_h = Region("Volleyball: Exhibition (Hard)", world.player, world.multiworld)
    v_exhibition_ex = Region("Volleyball: Exhibition (Expert)", world.player, world.multiworld)
    v_extra = Region("Volleyball: Extra", world.player, world.multiworld)
    # Hockey
    hockey = Region("Hockey", world.player, world.multiworld)
    h_exhibition_e = Region("Hockey: Exhibition (Easy)", world.player, world.multiworld)
    h_exhibition_n = Region("Hockey: Exhibition (Normal)", world.player, world.multiworld)
    h_exhibition_h = Region("Hockey: Exhibition (Hard)", world.player, world.multiworld)
    h_exhibition_ex = Region("Hockey: Exhibition (Expert)", world.player, world.multiworld)
    h_extra = Region("Hockey: Extra", world.player, world.multiworld)
    # Sports Mix
    sports_mix = Region("Sports Mix", world.player, world.multiworld)
    sm_mushroom_cup = Region("Sports Mix: Mushroom Cup", world.player, world.multiworld)
    sm_flower_cup = Region("Sports Mix: Flower Cup", world.player, world.multiworld)
    sm_star_cup = Region("Sports Mix: Star Cup", world.player, world.multiworld)
    # Party mode
    party_mode = Region("Party Mode", world.player, world.multiworld)
    regions = [main_menu, basketball, b_exhibition_e, b_exhibition_n, b_exhibition_h, b_exhibition_ex, b_extra,
               dodgeball, d_exhibition_e, d_exhibition_n, d_exhibition_h, d_exhibition_ex, d_extra,
               volleyball, v_exhibition_e, v_exhibition_n, v_exhibition_h, v_exhibition_ex, v_extra,
               hockey, h_exhibition_e, h_exhibition_n, h_exhibition_h, h_exhibition_ex, h_extra,
               sports_mix, sm_mushroom_cup, sm_flower_cup, sm_star_cup,
               party_mode]

    # Regions based on options
    if "Normal" in world.options.exhibition_difficulty:
        # Basketball
        b_mushroom_cup_n = Region("Basketball: Mushroom Cup (Normal)", world.player, world.multiworld)
        b_flower_cup_n = Region("Basketball: Flower Cup (Normal)", world.player, world.multiworld)
        b_star_cup_n = Region("Basketball: Star Cup (Normal)", world.player, world.multiworld)
        # Dodgeball
        d_mushroom_cup_n = Region("Dodgeball: Mushroom Cup (Normal)", world.player, world.multiworld)
        d_flower_cup_n = Region("Dodgeball: Flower Cup (Normal)", world.player, world.multiworld)
        d_star_cup_n = Region("Dodgeball: Star Cup (Normal)", world.player, world.multiworld)
        # Volleyball
        v_mushroom_cup_n = Region("Volleyball: Mushroom Cup (Normal)", world.player, world.multiworld)
        v_flower_cup_n = Region("Volleyball: Flower Cup (Normal)", world.player, world.multiworld)
        v_star_cup_n = Region("Volleyball: Star Cup (Normal)", world.player, world.multiworld)
        # Hockey
        h_mushroom_cup_n = Region("Hockey: Mushroom Cup (Normal)", world.player, world.multiworld)
        h_flower_cup_n = Region("Hockey: Flower Cup (Normal)", world.player, world.multiworld)
        h_star_cup_n = Region("Hockey: Star Cup (Normal)", world.player, world.multiworld)
        # Append to regions list
        # Basketball
        regions.append(b_mushroom_cup_n)
        regions.append(b_flower_cup_n)
        regions.append(b_star_cup_n)
        # Dodgeball
        regions.append(d_mushroom_cup_n)
        regions.append(d_flower_cup_n)
        regions.append(d_star_cup_n)
        # Volleyball
        regions.append(v_mushroom_cup_n)
        regions.append(v_flower_cup_n)
        regions.append(v_star_cup_n)
        # Hockey
        regions.append(h_mushroom_cup_n)
        regions.append(h_flower_cup_n)
        regions.append(h_star_cup_n)

    if "Hard" in world.options.exhibition_difficulty:
        # Basketball
        b_mushroom_cup_h = Region("Basketball: Mushroom Cup (Hard)", world.player, world.multiworld)
        b_flower_cup_h = Region("Basketball: Flower Cup (Hard)", world.player, world.multiworld)
        b_star_cup_h = Region("Basketball: Star Cup (Hard)", world.player, world.multiworld)
        # Dodgeball
        d_mushroom_cup_h = Region("Dodgeball: Mushroom Cup (Hard)", world.player, world.multiworld)
        d_flower_cup_h = Region("Dodgeball: Flower Cup (Hard)", world.player, world.multiworld)
        d_star_cup_h = Region("Dodgeball: Star Cup (Hard)", world.player, world.multiworld)
        # Volleyball
        v_mushroom_cup_h = Region("Volleyball: Mushroom Cup (Hard)", world.player, world.multiworld)
        v_flower_cup_h = Region("Volleyball: Flower Cup (Hard)", world.player, world.multiworld)
        v_star_cup_h = Region("Volleyball: Star Cup (Hard)", world.player, world.multiworld)
        # Hockey
        h_mushroom_cup_h = Region("Hockey: Mushroom Cup (Hard)", world.player, world.multiworld)
        h_flower_cup_h = Region("Hockey: Flower Cup (Hard)", world.player, world.multiworld)
        h_star_cup_h = Region("Hockey: Star Cup (Hard)", world.player, world.multiworld)
        # Append to regions list
        # Basketball
        regions.append(b_mushroom_cup_h)
        regions.append(b_flower_cup_h)
        regions.append(b_star_cup_h)
        # Dodgeball
        regions.append(d_mushroom_cup_h)
        regions.append(d_flower_cup_h)
        regions.append(d_star_cup_h)
        # Volleyball
        regions.append(v_mushroom_cup_h)
        regions.append(v_flower_cup_h)
        regions.append(v_star_cup_h)
        # Hockey
        regions.append(h_mushroom_cup_h)
        regions.append(h_flower_cup_h)
        regions.append(h_star_cup_h)

    if "Feed Petey" in world.options.party_mode:
        feed_petey = Region("Party Mode: Feed Petey", world.player, world.multiworld)
        regions.append(feed_petey)
    if "Harmony Hustle" in world.options.party_mode:
        harmony_hustle = Region("Party Mode: Harmony Hustle", world.player, world.multiworld)
        regions.append(harmony_hustle)
    if  "Bob-omb Dodge" in world.options.party_mode:
        bobomb_dodge = Region("Party Mode: Bob-omb Dodge", world.player, world.multiworld)
        regions.append(bobomb_dodge)
    if "Smash Skate" in world.options.party_mode:
        smash_skate = Region("Party Mode: Smash Skate", world.player, world.multiworld)
        regions.append(smash_skate)


    # Boss stuff
    if world.options.goal_condition == GoalCondition.option_defeat_behemoth:
        behemoth_boss_stuff = Region("Behemoth Boss Battle", world.player, world.multiworld)
        regions.append(behemoth_boss_stuff)
    if world.options.goal_condition == GoalCondition.option_defeat_behemoth_king:
        behemoth_boss_stuff = Region("Behemoth Boss Battle", world.player, world.multiworld)
        behemoth_king_boss_stuff = Region("Behemoth King Boss Battle", world.player, world.multiworld)
        regions.append(behemoth_boss_stuff)
        regions.append(behemoth_king_boss_stuff)
    # Add regions to AP multiworld so it knows it exists
    world.multiworld.regions += regions




def connect_regions(world: MSMWorld) -> None:
    # Get all regions
    main_menu = world.get_region("Main Menu")

    # Basketball
    basketball = world.get_region("Basketball")
    b_exhibition_e = world.get_region("Basketball: Exhibition (Easy)")
    b_exhibition_n = world.get_region("Basketball: Exhibition (Normal)")
    b_exhibition_h = world.get_region("Basketball: Exhibition (Hard)")
    b_exhibition_ex = world.get_region("Basketball: Exhibition (Expert)")
    b_mushroom_cup_n = world.get_region("Basketball: Mushroom Cup (Normal)")
    b_flower_cup_n = world.get_region("Basketball: Flower Cup (Normal)")
    b_star_cup_n = world.get_region("Basketball: Star Cup (Normal)")
    b_mushroom_cup_h = world.get_region("Basketball: Mushroom Cup (Hard)")
    b_flower_cup_h = world.get_region("Basketball: Flower Cup (Hard)")
    b_star_cup_h = world.get_region("Basketball: Star Cup (Hard)")
    b_extra = world.get_region("Basketball: Extra")

    # Dodgeball
    dodgeball = world.get_region("Dodgeball")
    d_exhibition_e = world.get_region("Dodgeball: Exhibition (Easy)")
    d_exhibition_n = world.get_region("Dodgeball: Exhibition (Normal)")
    d_exhibition_h = world.get_region("Dodgeball: Exhibition (Hard)")
    d_exhibition_ex = world.get_region("Dodgeball: Exhibition (Expert)")
    d_mushroom_cup_n = world.get_region("Dodgeball: Mushroom Cup (Normal)")
    d_flower_cup_n = world.get_region("Dodgeball: Flower Cup (Normal)")
    d_star_cup_n = world.get_region("Dodgeball: Star Cup (Normal)")
    d_mushroom_cup_h = world.get_region("Dodgeball: Mushroom Cup (Hard)")
    d_flower_cup_h = world.get_region("Dodgeball: Flower Cup (Hard)")
    d_star_cup_h = world.get_region("Dodgeball: Star Cup (Hard)")
    d_extra = world.get_region("Dodgeball: Extra")

    # Volleyball
    volleyball = world.get_region("Volleyball")
    v_exhibition_e = world.get_region("Volleyball: Exhibition (Easy)")
    v_exhibition_n = world.get_region("Volleyball: Exhibition (Normal)")
    v_exhibition_h = world.get_region("Volleyball: Exhibition (Hard)")
    v_exhibition_ex = world.get_region("Volleyball: Exhibition (Expert)")
    v_mushroom_cup_n = world.get_region("Volleyball: Mushroom Cup (Normal)")
    v_flower_cup_n = world.get_region("Volleyball: Flower Cup (Normal)")
    v_star_cup_n = world.get_region("Volleyball: Star Cup (Normal)")
    v_mushroom_cup_h = world.get_region("Volleyball: Mushroom Cup (Hard)")
    v_flower_cup_h = world.get_region("Volleyball: Flower Cup (Hard)")
    v_star_cup_h = world.get_region("Volleyball: Star Cup (Hard)")
    v_extra = world.get_region("Volleyball: Extra")

    # Hockey
    hockey = world.get_region("Hockey")
    h_exhibition_e = world.get_region("Hockey: Exhibition (Easy)")
    h_exhibition_n = world.get_region("Hockey: Exhibition (Normal)")
    h_exhibition_h = world.get_region("Hockey: Exhibition (Hard)")
    h_exhibition_ex = world.get_region("Hockey: Exhibition (Expert)")
    h_mushroom_cup_n = world.get_region("Hockey: Mushroom Cup (Normal)")
    h_flower_cup_n = world.get_region("Hockey: Flower Cup (Normal)")
    h_star_cup_n = world.get_region("Hockey: Star Cup (Normal)")
    h_mushroom_cup_h = world.get_region("Hockey: Mushroom Cup (Hard)")
    h_flower_cup_h = world.get_region("Hockey: Flower Cup (Hard)")
    h_star_cup_h = world.get_region("Hockey: Star Cup (Hard)")
    h_extra = world.get_region("Hockey: Extra")

    # Sports Mix
    sports_mix = world.get_region("Sports Mix")
    sm_mushroom_cup = world.get_region("Sports Mix: Mushroom Cup")
    sm_flower_cup = world.get_region("Sports Mix: Flower Cup")
    sm_star_cup = world.get_region("Sports Mix: Star Cup")

    if world.options.goal_condition == GoalCondition.option_defeat_behemoth:
        behemoth_boss = world.get_region("Behemoth Boss Battle")
    if world.options.goal_condition == GoalCondition.option_defeat_behemoth_king:
        behemoth_king_boss = world.get_region("Behemoth King Boss Battle")

    # Party Mode
    party_mode = world.get_region("Party Mode")
    feed_petey = world.get_region("Party Mode: Feed Petey")
    harmony_hustle = world.get_region("Party Mode: Harmony Hustle")
    bob_omb_dodge = world.get_region("Party Mode: Bob-omb Dodge")
    smash_strike = world.get_region("Party Mode: Smash Skate")

    # Connect menu to sports
    main_menu.connect(basketball, "Main Menu -> Basketball", lambda state: state.has("Sport: Basketball", world.player))
    main_menu.connect(dodgeball, "Main Menu -> Dodgeball", lambda state: state.has("Sport: Dodgeball", world.player))
    main_menu.connect(volleyball, "Main Menu -> Volleyball", lambda state: state.has("Sport: Volleyball", world.player))
    main_menu.connect(hockey, "Main Menu -> Hockey", lambda state: state.has("Sport: Hockey", world.player))
    main_menu.connect(sports_mix, "Main Menu -> Sports Mix", lambda state: state.has("Sport: Sports Mix", world.player))
    main_menu.connect(party_mode, "Main Menu -> Party Mode")
    party_mode.connect(feed_petey, "Party Mode -> Feed Petey")
    party_mode.connect(harmony_hustle, "Party Mode -> Harmony Hustle")
    party_mode.connect(bob_omb_dodge, "Party Mode -> Bob Omb Dodge")
    party_mode.connect(smash_strike, "Party Mode -> Smash Strike")

    # Connect Basketball to everything
    basketball.connect(b_exhibition_e, "Basketball -> Exhibition (Easy)")
    basketball.connect(b_exhibition_n, "Basketball -> Exhibition (Normal)")
    basketball.connect(b_exhibition_h, "Basketball -> Exhibition (Hard)")
    basketball.connect(b_exhibition_ex, "Basketball -> Exhibition (Expert)")
    basketball.connect(b_mushroom_cup_n, "Basketball -> Mushroom Cup (Normal)")
    basketball.connect(b_flower_cup_n, "Basketball -> Flower Cup (Normal)")
    basketball.connect(b_star_cup_n, "Basketball -> Star Cup (Normal)")
    basketball.connect(b_mushroom_cup_h, "Basketball -> Mushroom Cup (Hard)")
    basketball.connect(b_flower_cup_h, "Basketball -> Flower Cup (Hard)")
    basketball.connect(b_star_cup_h, "Basketball -> Star Cup (Hard)")
    basketball.connect(b_extra, "Basketball -> Extra")

    # Connect Dodgeball to everything
    dodgeball.connect(d_exhibition_e, "Dodgeball -> Exhibition (Easy)")
    dodgeball.connect(d_exhibition_n, "Dodgeball -> Exhibition (Normal)")
    dodgeball.connect(d_exhibition_h, "Dodgeball -> Exhibition (Hard)")
    dodgeball.connect(d_exhibition_ex, "Dodgeball -> Exhibition (Expert)")
    dodgeball.connect(d_mushroom_cup_n, "Dodgeball -> Mushroom Cup (Normal)")
    dodgeball.connect(d_flower_cup_n, "Dodgeball -> Flower Cup (Normal)")
    dodgeball.connect(d_star_cup_n, "Dodgeball -> Star Cup (Normal)")
    dodgeball.connect(d_mushroom_cup_h, "Dodgeball -> Mushroom Cup (Hard)")
    dodgeball.connect(d_flower_cup_h, "Dodgeball -> Flower Cup (Hard)")
    dodgeball.connect(d_star_cup_h, "Dodgeball -> Star Cup (Hard)")
    dodgeball.connect(d_extra, "Dodgeball -> Extra")

    # Connect Volleyball to everything
    volleyball.connect(v_exhibition_e, "Volleyball -> Exhibition (Easy)")
    volleyball.connect(v_exhibition_n, "Volleyball -> Exhibition (Normal)")
    volleyball.connect(v_exhibition_h, "Volleyball -> Exhibition (Hard)")
    volleyball.connect(v_exhibition_ex, "Volleyball -> Exhibition (Expert)")
    volleyball.connect(v_mushroom_cup_n, "Volleyball -> Mushroom Cup (Normal)")
    volleyball.connect(v_flower_cup_n, "Volleyball -> Flower Cup (Normal)")
    volleyball.connect(v_star_cup_n, "Volleyball -> Star Cup (Normal)")
    volleyball.connect(v_mushroom_cup_h, "Volleyball -> Mushroom Cup (Hard)")
    volleyball.connect(v_flower_cup_h, "Volleyball -> Flower Cup (Hard)")
    volleyball.connect(v_star_cup_h, "Volleyball -> Star Cup (Hard)")
    volleyball.connect(v_extra, "Volleyball -> Extra")

    # Connect Hockey to everything
    hockey.connect(h_exhibition_e, "Hockey -> Exhibition (Easy)")
    hockey.connect(h_exhibition_n, "Hockey -> Exhibition (Normal)")
    hockey.connect(h_exhibition_h, "Hockey -> Exhibition (Hard)")
    hockey.connect(h_exhibition_ex, "Hockey -> Exhibition (Expert)")
    hockey.connect(h_mushroom_cup_n, "Hockey -> Mushroom Cup (Normal)")
    hockey.connect(h_flower_cup_n, "Hockey -> Flower Cup (Normal)")
    hockey.connect(h_star_cup_n, "Hockey -> Star Cup (Normal)")
    hockey.connect(h_mushroom_cup_h, "Hockey -> Mushroom Cup (Hard)")
    hockey.connect(h_flower_cup_h, "Hockey -> Flower Cup (Hard)")
    hockey.connect(h_star_cup_h, "Hockey -> Star Cup (Hard)")
    hockey.connect(h_extra, "Hockey -> Extra")

    # Connect Sports Mix to everything
    sports_mix.connect(sm_mushroom_cup, "Sports Mix -> Mushroom Cup", lambda state: state.has("Sports Mix: Mushroom Cup", world.player))
    sports_mix.connect(sm_flower_cup, "Sports Mix -> Flower Cup", lambda state: state.has("Sports Mix: Flower Cup", world.player))
    sports_mix.connect(sm_star_cup, "Sports Mix -> Star Cup", lambda state: state.has("Sports Mix: Star Cup", world.player))

    # Behemoth is accessed by completing all normal star cups, connect all to the Behemoth Boss region
    # Note: Add rule if 3 other star cups have been beaten, gonna have to figure out something
    if world.options.goal_condition == GoalCondition.option_defeat_behemoth:
        b_star_cup_n.connect(behemoth_boss, "Basketball Star Cup (Normal) -> Behemoth Boss")
        d_star_cup_n.connect(behemoth_boss, "Dodgeball Star Cup (Normal) -> Behemoth Boss")
        v_star_cup_n.connect(behemoth_boss, "Volleyball Star Cup (Normal) -> Behemoth Boss")
        h_star_cup_n.connect(behemoth_boss, "Hockey Star Cup (Normal) -> Behemoth Boss")
    # Behemoth King is only accessed by beating the Sports Mix Star Cup
    if world.options.goal_condition == GoalCondition.option_defeat_behemoth_king:
        sm_star_cup.connect(behemoth_king_boss, "Sports Mix Star Cup -> Behemoth King Boss")

