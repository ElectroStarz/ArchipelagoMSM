from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Region

if TYPE_CHECKING:
    from . import MSMWorld


def create_and_connect_regions(world: "MSMWorld") -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: "MSMWorld") -> None:
    main_menu = Region("Main Menu", world.player, world.multiworld)
    exhibition = Region("Exhibition", world.player, world.multiworld)

    # Basketball
    basketball = Region("Basketball", world.player, world.multiworld)
    b_exhibition = Region("Basketball: Exhibition", world.player, world.multiworld)
    # Dodgeball
    dodgeball = Region("Dodgeball", world.player, world.multiworld)
    d_exhibition = Region("Dodgeball: Exhibition", world.player, world.multiworld)
    # Volleyball
    volleyball = Region("Volleyball", world.player, world.multiworld)
    v_exhibition = Region("Volleyball: Exhibition", world.player, world.multiworld)
    # Hockey
    hockey = Region("Hockey", world.player, world.multiworld)
    h_exhibition = Region("Hockey: Exhibition", world.player, world.multiworld)
    # Sports Mix
    sports_mix = Region("Sports Mix", world.player, world.multiworld)
    sm_mushroom_cup = Region("Sports Mix: Mushroom Cup", world.player, world.multiworld)
    sm_flower_cup = Region("Sports Mix: Flower Cup", world.player, world.multiworld)
    sm_star_cup = Region("Sports Mix: Star Cup", world.player, world.multiworld)
    sm_mushroom_cup_alternate = Region("Sports Mix: Mushroom Cup Alt Paths", world.player, world.multiworld)
    sm_flower_cup_alternate = Region("Sports Mix: Flower Cup Alt Paths", world.player, world.multiworld)
    sm_star_cup_alternate = Region("Sports Mix: Star Cup Alt Paths", world.player, world.multiworld)

    # Basketball
    b_mushroom_cup_n = Region("Basketball: Mushroom Cup (Normal)", world.player, world.multiworld)
    b_flower_cup_n = Region("Basketball: Flower Cup (Normal)", world.player, world.multiworld)
    b_star_cup_n = Region("Basketball: Star Cup (Normal)", world.player, world.multiworld)
    b_mushroom_cup_alternate_n = Region("Basketball: Mushroom Cup Alt Paths (Normal)", world.player, world.multiworld)
    b_flower_cup_alternate_n = Region("Basketball: Flower Cup Alt Paths (Normal)", world.player, world.multiworld)
    b_star_cup_alternate_n = Region("Basketball: Star Cup Alt Paths (Normal)", world.player, world.multiworld)

    # Dodgeball
    dodgeball = Region("Dodgeball", world.player, world.multiworld)
    d_exhibition = Region("Dodgeball: Exhibition", world.player, world.multiworld)
    d_mushroom_cup_n = Region("Dodgeball: Mushroom Cup (Normal)", world.player, world.multiworld)
    d_flower_cup_n = Region("Dodgeball: Flower Cup (Normal)", world.player, world.multiworld)
    d_star_cup_n = Region("Dodgeball: Star Cup (Normal)", world.player, world.multiworld)
    d_mushroom_cup_alternate_n = Region("Dodgeball: Mushroom Cup Alt Paths (Normal)", world.player, world.multiworld)
    d_flower_cup_alternate_n = Region("Dodgeball: Flower Cup Alt Paths (Normal)", world.player, world.multiworld)
    d_star_cup_alternate_n = Region("Dodgeball: Star Cup Alt Paths (Normal)", world.player, world.multiworld)

    # Volleyball
    volleyball = Region("Volleyball", world.player, world.multiworld)
    v_exhibition = Region("Volleyball: Exhibition", world.player, world.multiworld)
    v_mushroom_cup_n = Region("Volleyball: Mushroom Cup (Normal)", world.player, world.multiworld)
    v_flower_cup_n = Region("Volleyball: Flower Cup (Normal)", world.player, world.multiworld)
    v_star_cup_n = Region("Volleyball: Star Cup (Normal)", world.player, world.multiworld)
    v_mushroom_cup_alternate_n = Region("Volleyball: Mushroom Cup Alt Paths (Normal)", world.player, world.multiworld)
    v_flower_cup_alternate_n = Region("Volleyball: Flower Cup Alt Paths (Normal)", world.player, world.multiworld)
    v_star_cup_alternate_n = Region("Volleyball: Star Cup Alt Paths (Normal)", world.player, world.multiworld)

    # Hockey
    h_mushroom_cup_n = Region("Hockey: Mushroom Cup (Normal)", world.player, world.multiworld)
    h_flower_cup_n = Region("Hockey: Flower Cup (Normal)", world.player, world.multiworld)
    h_star_cup_n = Region("Hockey: Star Cup (Normal)", world.player, world.multiworld)
    h_mushroom_cup_alternate_n = Region("Hockey: Mushroom Cup Alt Paths (Normal)", world.player, world.multiworld)
    h_flower_cup_alternate_n = Region("Hockey: Flower Cup Alt Paths (Normal)", world.player, world.multiworld)
    h_star_cup_alternate_n = Region("Hockey: Star Cup Alt Paths (Normal)", world.player, world.multiworld)

    # Global Sport
    g_mushroom_cup_alternate_n = Region("Global: Mushroom Cup Alt Paths (Normal)", world.player, world.multiworld)
    g_flower_cup_alternate_n = Region("Global: Flower Cup Alt Paths (Normal)", world.player, world.multiworld)
    g_star_cup_alternate_n = Region("Global: Star Cup Alt Paths (Normal)", world.player, world.multiworld)

    # Basketball
    b_mushroom_cup_h = Region("Basketball: Mushroom Cup (Hard)", world.player, world.multiworld)
    b_flower_cup_h = Region("Basketball: Flower Cup (Hard)", world.player, world.multiworld)
    b_star_cup_h = Region("Basketball: Star Cup (Hard)", world.player, world.multiworld)
    b_mushroom_cup_alternate_h = Region("Basketball: Mushroom Cup Alt Paths (Hard)", world.player, world.multiworld)
    b_flower_cup_alternate_h = Region("Basketball: Flower Cup Alt Paths (Hard)", world.player, world.multiworld)
    b_star_cup_alternate_h = Region("Basketball: Star Cup Alt Paths (Hard)", world.player, world.multiworld)

    # Dodgeball
    d_mushroom_cup_h = Region("Dodgeball: Mushroom Cup (Hard)", world.player, world.multiworld)
    d_flower_cup_h = Region("Dodgeball: Flower Cup (Hard)", world.player, world.multiworld)
    d_star_cup_h = Region("Dodgeball: Star Cup (Hard)", world.player, world.multiworld)
    d_mushroom_cup_alternate_h = Region("Dodgeball: Mushroom Cup Alt Paths (Hard)", world.player, world.multiworld)
    d_flower_cup_alternate_h = Region("Dodgeball: Flower Cup Alt Paths (Hard)", world.player, world.multiworld)
    d_star_cup_alternate_h = Region("Dodgeball: Star Cup Alt Paths (Hard)", world.player, world.multiworld)

    # Volleyball
    v_mushroom_cup_h = Region("Volleyball: Mushroom Cup (Hard)", world.player, world.multiworld)
    v_flower_cup_h = Region("Volleyball: Flower Cup (Hard)", world.player, world.multiworld)
    v_star_cup_h = Region("Volleyball: Star Cup (Hard)", world.player, world.multiworld)
    v_mushroom_cup_alternate_h = Region("Volleyball: Mushroom Cup Alt Paths (Hard)", world.player, world.multiworld)
    v_flower_cup_alternate_h = Region("Volleyball: Flower Cup Alt Paths (Hard)", world.player, world.multiworld)
    v_star_cup_alternate_h = Region("Volleyball: Star Cup Alt Paths (Hard)", world.player, world.multiworld)

    # Hockey
    hockey = Region("Hockey", world.player, world.multiworld)
    h_exhibition = Region("Hockey: Exhibition", world.player, world.multiworld)
    h_mushroom_cup_n = Region("Hockey: Mushroom Cup (Normal)", world.player, world.multiworld)
    h_flower_cup_n = Region("Hockey: Flower Cup (Normal)", world.player, world.multiworld)
    h_star_cup_n = Region("Hockey: Star Cup (Normal)", world.player, world.multiworld)
    h_mushroom_cup_h = Region("Hockey: Mushroom Cup (Hard)", world.player, world.multiworld)
    h_flower_cup_h = Region("Hockey: Flower Cup (Hard)", world.player, world.multiworld)
    h_star_cup_h = Region("Hockey: Star Cup (Hard)", world.player, world.multiworld)
    h_mushroom_cup_alternate_h = Region("Hockey: Mushroom Cup Alt Paths (Hard)", world.player, world.multiworld)
    h_flower_cup_alternate_h = Region("Hockey: Flower Cup Alt Paths (Hard)", world.player, world.multiworld)
    h_star_cup_alternate_h = Region("Hockey: Star Cup Alt Paths (Hard)", world.player, world.multiworld)

    # Global Sport
    g_mushroom_cup_alternate_h = Region("Global: Mushroom Cup Alt Paths (Hard)", world.player, world.multiworld)
    g_flower_cup_alternate_h = Region("Global: Flower Cup Alt Paths (Hard)", world.player, world.multiworld)
    g_star_cup_alternate_h = Region("Global: Star Cup Alt Paths (Hard)", world.player, world.multiworld)

    # Global Alt Path Regions
    # Basketball
    b_mushroom_cup_alternate_g = Region("Basketball: Mushroom Cup Alt Paths (Global)", world.player, world.multiworld)
    b_flower_cup_alternate_g = Region("Basketball: Flower Cup Alt Paths (Global)", world.player, world.multiworld)
    b_star_cup_alternate_g = Region("Basketball: Star Cup Alt Paths (Global)", world.player, world.multiworld)

    # Dodgeball
    d_mushroom_cup_alternate_g = Region("Dodgeball: Mushroom Cup Alt Paths (Global)", world.player, world.multiworld)
    d_flower_cup_alternate_g = Region("Dodgeball: Flower Cup Alt Paths (Global)", world.player, world.multiworld)
    d_star_cup_alternate_g = Region("Dodgeball: Star Cup Alt Paths (Global)", world.player, world.multiworld)

    # Volleyball
    v_mushroom_cup_alternate_g = Region("Volleyball: Mushroom Cup Alt Paths (Global)", world.player, world.multiworld)
    v_flower_cup_alternate_g = Region("Volleyball: Flower Cup Alt Paths (Global)", world.player, world.multiworld)
    v_star_cup_alternate_g = Region("Volleyball: Star Cup Alt Paths (Global)", world.player, world.multiworld)

    # Hockey
    h_mushroom_cup_alternate_g = Region("Hockey: Mushroom Cup Alt Paths (Global)", world.player, world.multiworld)
    h_flower_cup_alternate_g = Region("Hockey: Flower Cup Alt Paths (Global)", world.player, world.multiworld)
    h_star_cup_alternate_g = Region("Hockey: Star Cup Alt Paths (Global)", world.player, world.multiworld)

    # Global Sport
    g_mushroom_cup_alternate_g = Region("Global: Mushroom Cup Alt Paths (Global)", world.player, world.multiworld)
    g_flower_cup_alternate_g = Region("Global: Flower Cup Alt Paths (Global)", world.player, world.multiworld)
    g_star_cup_alternate_g = Region("Global: Star Cup Alt Paths (Global)", world.player, world.multiworld)

    # Party Mode Stuff
    feed_petey = Region("Feed Petey", world.player, world.multiworld)
    harmony_hustle = Region("Harmony Hustle", world.player, world.multiworld)
    bob_omb_dodge = Region("Bob-omb Dodge", world.player, world.multiworld)
    smash_skate = Region("Smash Skate", world.player, world.multiworld)

    # Boss stuff
    behemoth_boss = Region("Behemoth Boss Battle", world.player, world.multiworld)
    behemoth_king_boss = Region("Behemoth King Boss Battle", world.player, world.multiworld)

    regions = [
        main_menu, exhibition,
        # Basketball
        basketball, b_exhibition,
        b_mushroom_cup_n, b_flower_cup_n, b_star_cup_n,
        b_mushroom_cup_h, b_flower_cup_h, b_star_cup_h,
        b_mushroom_cup_alternate_n, b_flower_cup_alternate_n, b_star_cup_alternate_n,
        b_mushroom_cup_alternate_h, b_flower_cup_alternate_h, b_star_cup_alternate_h,
        b_mushroom_cup_alternate_g, b_flower_cup_alternate_g, b_star_cup_alternate_g,
        # Dodgeball
        dodgeball, d_exhibition,
        d_mushroom_cup_n, d_flower_cup_n, d_star_cup_n,
        d_mushroom_cup_h, d_flower_cup_h, d_star_cup_h,
        d_mushroom_cup_alternate_n, d_flower_cup_alternate_n, d_star_cup_alternate_n,
        d_mushroom_cup_alternate_h, d_flower_cup_alternate_h, d_star_cup_alternate_h,
        d_mushroom_cup_alternate_g, d_flower_cup_alternate_g, d_star_cup_alternate_g,
        # Volleyball
        volleyball, v_exhibition,
        v_mushroom_cup_n, v_flower_cup_n, v_star_cup_n,
        v_mushroom_cup_h, v_flower_cup_h, v_star_cup_h,
        v_mushroom_cup_alternate_n, v_flower_cup_alternate_n, v_star_cup_alternate_n,
        v_mushroom_cup_alternate_h, v_flower_cup_alternate_h, v_star_cup_alternate_h,
        v_mushroom_cup_alternate_g, v_flower_cup_alternate_g, v_star_cup_alternate_g,
        # Hockey
        hockey, h_exhibition,
        h_mushroom_cup_n, h_flower_cup_n, h_star_cup_n,
        h_mushroom_cup_h, h_flower_cup_h, h_star_cup_h,
        h_mushroom_cup_alternate_n, h_flower_cup_alternate_n, h_star_cup_alternate_n,
        h_mushroom_cup_alternate_h, h_flower_cup_alternate_h, h_star_cup_alternate_h,
        h_mushroom_cup_alternate_g, h_flower_cup_alternate_g, h_star_cup_alternate_g,
        # Sports Mix
        sports_mix,
        sm_mushroom_cup, sm_flower_cup, sm_star_cup,
        sm_mushroom_cup_alternate, sm_flower_cup_alternate, sm_star_cup_alternate,
        # Global Alt Paths
        g_mushroom_cup_alternate_n, g_flower_cup_alternate_n, g_star_cup_alternate_n,
        g_mushroom_cup_alternate_h, g_flower_cup_alternate_h, g_star_cup_alternate_h,
        g_mushroom_cup_alternate_g, g_flower_cup_alternate_g, g_star_cup_alternate_g,
        # Party Mode
        feed_petey, harmony_hustle, bob_omb_dodge, smash_skate,
        # Bosses
        behemoth_boss, behemoth_king_boss,
    ]

    # Add regions to AP multiworld so it knows it exists
    world.multiworld.regions += regions


def connect_regions(world: MSMWorld) -> None:
    # Get all regions
    main_menu = world.get_region("Main Menu")
    exhibition = world.get_region("Exhibition")

    # Basketball
    basketball = world.get_region("Basketball")
    b_exhibition = world.get_region("Basketball: Exhibition")
    b_mushroom_cup_n = world.get_region("Basketball: Mushroom Cup (Normal)")
    b_flower_cup_n = world.get_region("Basketball: Flower Cup (Normal)")
    b_star_cup_n = world.get_region("Basketball: Star Cup (Normal)")
    b_mushroom_cup_alternate_n = world.get_region("Basketball: Mushroom Cup Alt Paths (Normal)")
    b_flower_cup_alternate_n = world.get_region("Basketball: Flower Cup Alt Paths (Normal)")
    b_star_cup_alternate_n = world.get_region("Basketball: Star Cup Alt Paths (Normal)")
    b_mushroom_cup_h = world.get_region("Basketball: Mushroom Cup (Hard)")
    b_flower_cup_h = world.get_region("Basketball: Flower Cup (Hard)")
    b_star_cup_h = world.get_region("Basketball: Star Cup (Hard)")
    b_mushroom_cup_alternate_h = world.get_region("Basketball: Mushroom Cup Alt Paths (Hard)")
    b_flower_cup_alternate_h = world.get_region("Basketball: Flower Cup Alt Paths (Hard)")
    b_star_cup_alternate_h = world.get_region("Basketball: Star Cup Alt Paths (Hard)")
    b_mushroom_cup_alternate_g = world.get_region("Basketball: Mushroom Cup Alt Paths (Global)")
    b_flower_cup_alternate_g = world.get_region("Basketball: Flower Cup Alt Paths (Global)")
    b_star_cup_alternate_g = world.get_region("Basketball: Star Cup Alt Paths (Global)")

    # Dodgeball
    dodgeball = world.get_region("Dodgeball")
    d_exhibition = world.get_region("Dodgeball: Exhibition")
    d_mushroom_cup_n = world.get_region("Dodgeball: Mushroom Cup (Normal)")
    d_flower_cup_n = world.get_region("Dodgeball: Flower Cup (Normal)")
    d_star_cup_n = world.get_region("Dodgeball: Star Cup (Normal)")
    d_mushroom_cup_alternate_n = world.get_region("Dodgeball: Mushroom Cup Alt Paths (Normal)")
    d_flower_cup_alternate_n = world.get_region("Dodgeball: Flower Cup Alt Paths (Normal)")
    d_star_cup_alternate_n = world.get_region("Dodgeball: Star Cup Alt Paths (Normal)")
    d_mushroom_cup_h = world.get_region("Dodgeball: Mushroom Cup (Hard)")
    d_flower_cup_h = world.get_region("Dodgeball: Flower Cup (Hard)")
    d_star_cup_h = world.get_region("Dodgeball: Star Cup (Hard)")
    d_mushroom_cup_alternate_h = world.get_region("Dodgeball: Mushroom Cup Alt Paths (Hard)")
    d_flower_cup_alternate_h = world.get_region("Dodgeball: Flower Cup Alt Paths (Hard)")
    d_star_cup_alternate_h = world.get_region("Dodgeball: Star Cup Alt Paths (Hard)")
    d_mushroom_cup_alternate_g = world.get_region("Dodgeball: Mushroom Cup Alt Paths (Global)")
    d_flower_cup_alternate_g = world.get_region("Dodgeball: Flower Cup Alt Paths (Global)")
    d_star_cup_alternate_g = world.get_region("Dodgeball: Star Cup Alt Paths (Global)")

    # Volleyball
    volleyball = world.get_region("Volleyball")
    v_exhibition = world.get_region("Volleyball: Exhibition")
    v_mushroom_cup_n = world.get_region("Volleyball: Mushroom Cup (Normal)")
    v_flower_cup_n = world.get_region("Volleyball: Flower Cup (Normal)")
    v_star_cup_n = world.get_region("Volleyball: Star Cup (Normal)")
    v_mushroom_cup_alternate_n = world.get_region("Volleyball: Mushroom Cup Alt Paths (Normal)")
    v_flower_cup_alternate_n = world.get_region("Volleyball: Flower Cup Alt Paths (Normal)")
    v_star_cup_alternate_n = world.get_region("Volleyball: Star Cup Alt Paths (Normal)")
    v_mushroom_cup_h = world.get_region("Volleyball: Mushroom Cup (Hard)")
    v_flower_cup_h = world.get_region("Volleyball: Flower Cup (Hard)")
    v_star_cup_h = world.get_region("Volleyball: Star Cup (Hard)")
    v_mushroom_cup_alternate_h = world.get_region("Volleyball: Mushroom Cup Alt Paths (Hard)")
    v_flower_cup_alternate_h = world.get_region("Volleyball: Flower Cup Alt Paths (Hard)")
    v_star_cup_alternate_h = world.get_region("Volleyball: Star Cup Alt Paths (Hard)")
    v_mushroom_cup_alternate_g = world.get_region("Volleyball: Mushroom Cup Alt Paths (Global)")
    v_flower_cup_alternate_g = world.get_region("Volleyball: Flower Cup Alt Paths (Global)")
    v_star_cup_alternate_g = world.get_region("Volleyball: Star Cup Alt Paths (Global)")

    # Hockey
    hockey = world.get_region("Hockey")
    h_exhibition = world.get_region("Hockey: Exhibition")
    h_mushroom_cup_n = world.get_region("Hockey: Mushroom Cup (Normal)")
    h_flower_cup_n = world.get_region("Hockey: Flower Cup (Normal)")
    h_star_cup_n = world.get_region("Hockey: Star Cup (Normal)")
    h_mushroom_cup_alternate_n = world.get_region("Hockey: Mushroom Cup Alt Paths (Normal)")
    h_flower_cup_alternate_n = world.get_region("Hockey: Flower Cup Alt Paths (Normal)")
    h_star_cup_alternate_n = world.get_region("Hockey: Star Cup Alt Paths (Normal)")
    h_mushroom_cup_h = world.get_region("Hockey: Mushroom Cup (Hard)")
    h_flower_cup_h = world.get_region("Hockey: Flower Cup (Hard)")
    h_star_cup_h = world.get_region("Hockey: Star Cup (Hard)")
    h_mushroom_cup_alternate_h = world.get_region("Hockey: Mushroom Cup Alt Paths (Hard)")
    h_flower_cup_alternate_h = world.get_region("Hockey: Flower Cup Alt Paths (Hard)")
    h_star_cup_alternate_h = world.get_region("Hockey: Star Cup Alt Paths (Hard)")
    h_mushroom_cup_alternate_g = world.get_region("Hockey: Mushroom Cup Alt Paths (Global)")
    h_flower_cup_alternate_g = world.get_region("Hockey: Flower Cup Alt Paths (Global)")
    h_star_cup_alternate_g = world.get_region("Hockey: Star Cup Alt Paths (Global)")

    # Sports Mix
    sports_mix = world.get_region("Sports Mix")
    sm_mushroom_cup = world.get_region("Sports Mix: Mushroom Cup")
    sm_flower_cup = world.get_region("Sports Mix: Flower Cup")
    sm_star_cup = world.get_region("Sports Mix: Star Cup")
    sm_mushroom_cup_alternate = world.get_region("Sports Mix: Mushroom Cup Alt Paths")
    sm_flower_cup_alternate = world.get_region("Sports Mix: Flower Cup Alt Paths")
    sm_star_cup_alternate = world.get_region("Sports Mix: Star Cup Alt Paths")

    # Global Sport
    g_mushroom_cup_alternate_n = world.get_region("Global: Mushroom Cup Alt Paths (Normal)")
    g_flower_cup_alternate_n = world.get_region("Global: Flower Cup Alt Paths (Normal)")
    g_star_cup_alternate_n = world.get_region("Global: Star Cup Alt Paths (Normal)")
    g_mushroom_cup_alternate_h = world.get_region("Global: Mushroom Cup Alt Paths (Hard)")
    g_flower_cup_alternate_h = world.get_region("Global: Flower Cup Alt Paths (Hard)")
    g_star_cup_alternate_h = world.get_region("Global: Star Cup Alt Paths (Hard)")
    g_mushroom_cup_alternate_g = world.get_region("Global: Mushroom Cup Alt Paths (Global)")
    g_flower_cup_alternate_g = world.get_region("Global: Flower Cup Alt Paths (Global)")
    g_star_cup_alternate_g = world.get_region("Global: Star Cup Alt Paths (Global)")

    # Party Mode
    feed_petey = world.get_region("Feed Petey")
    harmony_hustle = world.get_region("Harmony Hustle")
    bob_omb_dodge = world.get_region("Bob-omb Dodge")
    smash_skate = world.get_region("Smash Skate")

    # Boss
    behemoth_boss = world.get_region("Behemoth Boss Battle")
    behemoth_king_boss = world.get_region("Behemoth King Boss Battle")

    # Connect menu to main_sports
    main_menu.connect(basketball, "Main Menu -> Basketball")
    main_menu.connect(dodgeball, "Main Menu -> Dodgeball")
    main_menu.connect(volleyball, "Main Menu -> Volleyball")
    main_menu.connect(hockey, "Main Menu -> Hockey")
    main_menu.connect(sports_mix, "Main Menu -> Sports Mix")

    main_menu.connect(feed_petey, "Main Menu -> Feed Petey")
    main_menu.connect(harmony_hustle, "Main Menu -> Harmony Hustle")
    main_menu.connect(bob_omb_dodge, "Main Menu -> Bob-omb Dodge")
    main_menu.connect(smash_skate, "Main Menu -> Smash Skate")

    main_menu.connect(exhibition, "Main Menu -> Exhibition")

    # Connect Basketball to everything
    basketball.connect(b_exhibition, "Basketball -> Exhibition")
    basketball.connect(b_mushroom_cup_n, "Basketball -> Mushroom Cup (Normal)")
    basketball.connect(b_flower_cup_n, "Basketball -> Flower Cup (Normal)")
    basketball.connect(b_star_cup_n, "Basketball -> Star Cup (Normal)")
    basketball.connect(b_mushroom_cup_h, "Basketball -> Mushroom Cup (Hard)")
    basketball.connect(b_flower_cup_h, "Basketball -> Flower Cup (Hard)")
    basketball.connect(b_star_cup_h, "Basketball -> Star Cup (Hard)")

    # Connect Dodgeball to everything
    dodgeball.connect(d_exhibition, "Dodgeball -> Exhibition")
    dodgeball.connect(d_mushroom_cup_n, "Dodgeball -> Mushroom Cup (Normal)")
    dodgeball.connect(d_flower_cup_n, "Dodgeball -> Flower Cup (Normal)")
    dodgeball.connect(d_star_cup_n, "Dodgeball -> Star Cup (Normal)")
    dodgeball.connect(d_mushroom_cup_h, "Dodgeball -> Mushroom Cup (Hard)")
    dodgeball.connect(d_flower_cup_h, "Dodgeball -> Flower Cup (Hard)")
    dodgeball.connect(d_star_cup_h, "Dodgeball -> Star Cup (Hard)")

    # Connect Volleyball to everything
    volleyball.connect(v_exhibition, "Volleyball -> Exhibition")
    volleyball.connect(v_mushroom_cup_n, "Volleyball -> Mushroom Cup (Normal)")
    volleyball.connect(v_flower_cup_n, "Volleyball -> Flower Cup (Normal)")
    volleyball.connect(v_star_cup_n, "Volleyball -> Star Cup (Normal)")
    volleyball.connect(v_mushroom_cup_h, "Volleyball -> Mushroom Cup (Hard)")
    volleyball.connect(v_flower_cup_h, "Volleyball -> Flower Cup (Hard)")
    volleyball.connect(v_star_cup_h, "Volleyball -> Star Cup (Hard)")

    # Connect Hockey to everything
    hockey.connect(h_exhibition, "Hockey -> Exhibition")
    hockey.connect(h_mushroom_cup_n, "Hockey -> Mushroom Cup (Normal)")
    hockey.connect(h_flower_cup_n, "Hockey -> Flower Cup (Normal)")
    hockey.connect(h_star_cup_n, "Hockey -> Star Cup (Normal)")
    hockey.connect(h_mushroom_cup_h, "Hockey -> Mushroom Cup (Hard)")
    hockey.connect(h_flower_cup_h, "Hockey -> Flower Cup (Hard)")
    hockey.connect(h_star_cup_h, "Hockey -> Star Cup (Hard)")

    # Connect Sports Mix to everything
    sports_mix.connect(sm_mushroom_cup, "Sports Mix -> Mushroom Cup")
    sports_mix.connect(sm_flower_cup, "Sports Mix -> Flower Cup")
    sports_mix.connect(sm_star_cup, "Sports Mix -> Star Cup")

    # Connect alt paths to cups. Global Difficulty connected

    # Basketball
    b_mushroom_cup_n.connect(b_mushroom_cup_alternate_n,
                             "Basketball: Mushroom Cup (Normal) -> Mushroom Cup Alt Paths (Normal)")
    b_flower_cup_n.connect(b_flower_cup_alternate_n, "Basketball: Flower Cup (Normal) -> Flower Cup Alt Paths (Normal)")
    b_star_cup_n.connect(b_star_cup_alternate_n, "Basketball: Star Cup (Normal) -> Star Cup Alt Paths (Normal)")
    b_mushroom_cup_h.connect(b_mushroom_cup_alternate_h,
                             "Basketball: Mushroom Cup (Hard) -> Mushroom Cup Alt Paths (Hard)")
    b_flower_cup_h.connect(b_flower_cup_alternate_h, "Basketball: Flower Cup (Hard) -> Flower Cup Alt Paths (Hard)")
    b_star_cup_h.connect(b_star_cup_alternate_h, "Basketball: Star Cup (Hard) -> Star Cup Alt Paths (Hard)")

    b_mushroom_cup_n.connect(b_mushroom_cup_alternate_g,
                             "Basketball: Mushroom Cup (Normal) -> Mushroom Cup Alt Paths (Global)")
    b_flower_cup_n.connect(b_flower_cup_alternate_g, "Basketball: Flower Cup (Normal) -> Flower Cup Alt Paths (Global)")
    b_star_cup_n.connect(b_star_cup_alternate_g, "Basketball: Star Cup (Normal) -> Star Cup Alt Paths (Global)")
    b_mushroom_cup_h.connect(b_mushroom_cup_alternate_g,
                             "Basketball: Mushroom Cup (Hard) -> Mushroom Cup Alt Paths (Global)")
    b_flower_cup_h.connect(b_flower_cup_alternate_g, "Basketball: Flower Cup (Hard) -> Flower Cup Alt Paths (Global)")
    b_star_cup_h.connect(b_star_cup_alternate_g, "Basketball: Star Cup (Hard) -> Star Cup Alt Paths (Global)")

    # Dodgeball
    d_mushroom_cup_n.connect(d_mushroom_cup_alternate_n,
                             "Dodgeball: Mushroom Cup (Normal) -> Mushroom Cup Alt Paths (Normal)")
    d_flower_cup_n.connect(d_flower_cup_alternate_n, "Dodgeball: Flower Cup (Normal) -> Flower Cup Alt Paths (Normal)")
    d_star_cup_n.connect(d_star_cup_alternate_n, "Dodgeball: Star Cup (Normal) -> Star Cup Alt Paths (Normal)")
    d_mushroom_cup_h.connect(d_mushroom_cup_alternate_h,
                             "Dodgeball: Mushroom Cup (Hard) -> Mushroom Cup Alt Paths (Hard)")
    d_flower_cup_h.connect(d_flower_cup_alternate_h, "Dodgeball: Flower Cup (Hard) -> Flower Cup Alt Paths (Hard)")
    d_star_cup_h.connect(d_star_cup_alternate_h, "Dodgeball: Star Cup (Hard) -> Star Cup Alt Paths (Hard)")

    d_mushroom_cup_n.connect(d_mushroom_cup_alternate_g,
                             "Dodgeball: Mushroom Cup (Normal) -> Mushroom Cup Alt Paths (Global)")
    d_flower_cup_n.connect(d_flower_cup_alternate_g, "Dodgeball: Flower Cup (Normal) -> Flower Cup Alt Paths (Global)")
    d_star_cup_n.connect(d_star_cup_alternate_g, "Dodgeball: Star Cup (Normal) -> Star Cup Alt Paths (Global)")
    d_mushroom_cup_h.connect(d_mushroom_cup_alternate_g,
                             "Dodgeball: Mushroom Cup (Hard) -> Mushroom Cup Alt Paths (Global)")
    d_flower_cup_h.connect(d_flower_cup_alternate_g, "Dodgeball: Flower Cup (Hard) -> Flower Cup Alt Paths (Global)")
    d_star_cup_h.connect(d_star_cup_alternate_g, "Dodgeball: Star Cup (Hard) -> Star Cup Alt Paths (Global)")

    # Volleyball
    v_mushroom_cup_n.connect(v_mushroom_cup_alternate_n,
                             "Volleyball: Mushroom Cup (Normal) -> Mushroom Cup Alt Paths (Normal)")
    v_flower_cup_n.connect(v_flower_cup_alternate_n, "Volleyball: Flower Cup (Normal) -> Flower Cup Alt Paths (Normal)")
    v_star_cup_n.connect(v_star_cup_alternate_n, "Volleyball: Star Cup (Normal) -> Star Cup Alt Paths (Normal)")
    v_mushroom_cup_h.connect(v_mushroom_cup_alternate_h,
                             "Volleyball: Mushroom Cup (Hard) -> Mushroom Cup Alt Paths (Hard)")
    v_flower_cup_h.connect(v_flower_cup_alternate_h, "Volleyball: Flower Cup (Hard) -> Flower Cup Alt Paths (Hard)")
    v_star_cup_h.connect(v_star_cup_alternate_h, "Volleyball: Star Cup (Hard) -> Star Cup Alt Paths (Hard)")

    v_mushroom_cup_n.connect(v_mushroom_cup_alternate_g,
                             "Volleyball: Mushroom Cup (Normal) -> Mushroom Cup Alt Paths (Global)")
    v_flower_cup_n.connect(v_flower_cup_alternate_g, "Volleyball: Flower Cup (Normal) -> Flower Cup Alt Paths (Global)")
    v_star_cup_n.connect(v_star_cup_alternate_g, "Volleyball: Star Cup (Normal) -> Star Cup Alt Paths (Global)")
    v_mushroom_cup_h.connect(v_mushroom_cup_alternate_g,
                             "Volleyball: Mushroom Cup (Hard) -> Mushroom Cup Alt Paths (Global)")
    v_flower_cup_h.connect(v_flower_cup_alternate_g, "Volleyball: Flower Cup (Hard) -> Flower Cup Alt Paths (Global)")
    v_star_cup_h.connect(v_star_cup_alternate_g, "Volleyball: Star Cup (Hard) -> Star Cup Alt Paths (Global)")

    # Hockey
    h_mushroom_cup_n.connect(h_mushroom_cup_alternate_n,
                             "Hockey: Mushroom Cup (Normal) -> Mushroom Cup Alt Paths (Normal)")
    h_flower_cup_n.connect(h_flower_cup_alternate_n, "Hockey: Flower Cup (Normal) -> Flower Cup Alt Paths (Normal)")
    h_star_cup_n.connect(h_star_cup_alternate_n, "Hockey: Star Cup (Normal) -> Star Cup Alt Paths (Normal)")
    h_mushroom_cup_h.connect(h_mushroom_cup_alternate_h, "Hockey: Mushroom Cup (Hard) -> Mushroom Cup Alt Paths (Hard)")
    h_flower_cup_h.connect(h_flower_cup_alternate_h, "Hockey: Flower Cup (Hard) -> Flower Cup Alt Paths (Hard)")
    h_star_cup_h.connect(h_star_cup_alternate_h, "Hockey: Star Cup (Hard) -> Star Cup Alt Paths (Hard)")

    h_mushroom_cup_n.connect(h_mushroom_cup_alternate_g,
                             "Hockey: Mushroom Cup (Normal) -> Mushroom Cup Alt Paths (Global)")
    h_flower_cup_n.connect(h_flower_cup_alternate_g, "Hockey: Flower Cup (Normal) -> Flower Cup Alt Paths (Global)")
    h_star_cup_n.connect(h_star_cup_alternate_g, "Hockey: Star Cup (Normal) -> Star Cup Alt Paths (Global)")
    h_mushroom_cup_h.connect(h_mushroom_cup_alternate_g,
                             "Hockey: Mushroom Cup (Hard) -> Mushroom Cup Alt Paths (Global)")
    h_flower_cup_h.connect(h_flower_cup_alternate_g, "Hockey: Flower Cup (Hard) -> Flower Cup Alt Paths (Global)")
    h_star_cup_h.connect(h_star_cup_alternate_g, "Hockey: Star Cup (Hard) -> Star Cup Alt Paths (Global)")

    # Sports Mix
    sm_mushroom_cup.connect(sm_mushroom_cup_alternate, "Sports Mix: Mushroom Cup -> Mushroom Cup Alt Paths")
    sm_flower_cup.connect(sm_flower_cup_alternate, "Sports Mix: Flower Cup -> Flower Cup Alt Paths")
    sm_star_cup.connect(sm_star_cup_alternate, "Sports Mix: Star Cup -> Star Cup Alt Paths")

    # Global Sport (Can be acc)
    b_mushroom_cup_n.connect(g_mushroom_cup_alternate_n,
                             "Basketball: Mushroom Cup (Normal) -> Global: Mushroom Cup Alt Paths (Normal)")
    d_mushroom_cup_n.connect(g_mushroom_cup_alternate_n,
                             "Dodgeball: Mushroom Cup (Normal) -> Global: Mushroom Cup Alt Paths (Normal)")
    v_mushroom_cup_n.connect(g_mushroom_cup_alternate_n,
                             "Volleyball: Mushroom Cup (Normal) -> Global: Mushroom Cup Alt Paths (Normal)")
    h_mushroom_cup_n.connect(g_mushroom_cup_alternate_n,
                             "Hockey: Mushroom Cup (Normal) -> Global: Mushroom Cup Alt Paths (Normal)")
    sm_mushroom_cup.connect(g_mushroom_cup_alternate_n,
                            "Sports Mix: Mushroom Cup -> Global: Mushroom Cup Alt Paths (Normal)")

    b_flower_cup_n.connect(g_flower_cup_alternate_n,
                           "Basketball: Flower Cup (Normal) -> Global: Flower Cup Alt Paths (Normal)")
    d_flower_cup_n.connect(g_flower_cup_alternate_n,
                           "Dodgeball: Flower Cup (Normal) -> Global: Flower Cup Alt Paths (Normal)")
    v_flower_cup_n.connect(g_flower_cup_alternate_n,
                           "Volleyball: Flower Cup (Normal) -> Global: Flower Cup Alt Paths (Normal)")
    h_flower_cup_n.connect(g_flower_cup_alternate_n,
                           "Hockey: Flower Cup (Normal) -> Global: Flower Cup Alt Paths (Normal)")
    sm_flower_cup.connect(g_flower_cup_alternate_n, "Sports Mix: Flower Cup -> Global: Flower Cup Alt Paths (Normal)")

    b_star_cup_n.connect(g_star_cup_alternate_n, "Basketball: Star Cup (Normal) -> Global: Star Cup Alt Paths (Normal)")
    d_star_cup_n.connect(g_star_cup_alternate_n, "Dodgeball: Star Cup (Normal) -> Global: Star Cup Alt Paths (Normal)")
    v_star_cup_n.connect(g_star_cup_alternate_n, "Volleyball: Star Cup (Normal) -> Global: Star Cup Alt Paths (Normal)")
    h_star_cup_n.connect(g_star_cup_alternate_n, "Hockey: Star Cup (Normal) -> Global: Star Cup Alt Paths (Normal)")
    sm_star_cup.connect(g_star_cup_alternate_n, "Sports Mix: Star Cup -> Global: Star Cup Alt Paths (Normal)")

    b_mushroom_cup_h.connect(g_mushroom_cup_alternate_h,
                             "Basketball: Mushroom Cup (Hard) -> Global: Mushroom Cup Alt Paths (Hard)")
    d_mushroom_cup_h.connect(g_mushroom_cup_alternate_h,
                             "Dodgeball: Mushroom Cup (Hard) -> Global: Mushroom Cup Alt Paths (Hard)")
    v_mushroom_cup_h.connect(g_mushroom_cup_alternate_h,
                             "Volleyball: Mushroom Cup (Hard) -> Global: Mushroom Cup Alt Paths (Hard)")
    h_mushroom_cup_h.connect(g_mushroom_cup_alternate_h,
                             "Hockey: Mushroom Cup (Hard) -> Global: Mushroom Cup Alt Paths (Hard)")

    b_flower_cup_h.connect(g_flower_cup_alternate_h,
                           "Basketball: Flower Cup (Hard) -> Global: Flower Cup Alt Paths (Hard)")
    d_flower_cup_h.connect(g_flower_cup_alternate_h,
                           "Dodgeball: Flower Cup (Hard) -> Global: Flower Cup Alt Paths (Hard)")
    v_flower_cup_h.connect(g_flower_cup_alternate_h,
                           "Volleyball: Flower Cup (Hard) -> Global: Flower Cup Alt Paths (Hard)")
    h_flower_cup_h.connect(g_flower_cup_alternate_h, "Hockey: Flower Cup (Hard) -> Global: Flower Cup Alt Paths (Hard)")

    b_star_cup_h.connect(g_star_cup_alternate_h, "Basketball: Star Cup (Hard) -> Global: Star Cup Alt Paths (Hard)")
    d_star_cup_h.connect(g_star_cup_alternate_h, "Dodgeball: Star Cup (Hard) -> Global: Star Cup Alt Paths (Hard)")
    v_star_cup_h.connect(g_star_cup_alternate_h, "Volleyball: Star Cup (Hard) -> Global: Star Cup Alt Paths (Hard)")
    h_star_cup_h.connect(g_star_cup_alternate_h, "Hockey: Star Cup (Hard) -> Global: Star Cup Alt Paths (Hard)")

    b_mushroom_cup_n.connect(g_mushroom_cup_alternate_g,
                             "Basketball: Mushroom Cup (Normal) -> Global: Mushroom Cup Alt Paths (Global)")
    d_mushroom_cup_n.connect(g_mushroom_cup_alternate_g,
                             "Dodgeball: Mushroom Cup (Normal) -> Global: Mushroom Cup Alt Paths (Global)")
    v_mushroom_cup_n.connect(g_mushroom_cup_alternate_g,
                             "Volleyball: Mushroom Cup (Normal) -> Global: Mushroom Cup Alt Paths (Global)")
    h_mushroom_cup_n.connect(g_mushroom_cup_alternate_g,
                             "Hockey: Mushroom Cup (Normal) -> Global: Mushroom Cup Alt Paths (Global)")
    b_mushroom_cup_h.connect(g_mushroom_cup_alternate_g,
                             "Basketball: Mushroom Cup (Hard) -> Global: Mushroom Cup Alt Paths (Global)")
    d_mushroom_cup_h.connect(g_mushroom_cup_alternate_g,
                             "Dodgeball: Mushroom Cup (Hard) -> Global: Mushroom Cup Alt Paths (Global)")
    v_mushroom_cup_h.connect(g_mushroom_cup_alternate_g,
                             "Volleyball: Mushroom Cup (Hard) -> Global: Mushroom Cup Alt Paths (Global)")
    h_mushroom_cup_h.connect(g_mushroom_cup_alternate_g,
                             "Hockey: Mushroom Cup (Hard) -> Global: Mushroom Cup Alt Paths (Global)")

    b_flower_cup_n.connect(g_flower_cup_alternate_g,
                           "Basketball: Flower Cup (Normal) -> Global: Flower Cup Alt Paths (Global)")
    d_flower_cup_n.connect(g_flower_cup_alternate_g,
                           "Dodgeball: Flower Cup (Normal) -> Global: Flower Cup Alt Paths (Global)")
    v_flower_cup_n.connect(g_flower_cup_alternate_g,
                           "Volleyball: Flower Cup (Normal) -> Global: Flower Cup Alt Paths (Global)")
    h_flower_cup_n.connect(g_flower_cup_alternate_g,
                           "Hockey: Flower Cup (Normal) -> Global: Flower Cup Alt Paths (Global)")
    b_flower_cup_h.connect(g_flower_cup_alternate_g,
                           "Basketball: Flower Cup (Hard) -> Global: Flower Cup Alt Paths (Global)")
    d_flower_cup_h.connect(g_flower_cup_alternate_g,
                           "Dodgeball: Flower Cup (Hard) -> Global: Flower Cup Alt Paths (Global)")
    v_flower_cup_h.connect(g_flower_cup_alternate_g,
                           "Volleyball: Flower Cup (Hard) -> Global: Flower Cup Alt Paths (Global)")
    h_flower_cup_h.connect(g_flower_cup_alternate_g,
                           "Hockey: Flower Cup (Hard) -> Global: Flower Cup Alt Paths (Global)")

    b_star_cup_n.connect(g_star_cup_alternate_g, "Basketball: Star Cup (Normal) -> Global: Star Cup Alt Paths (Global)")
    d_star_cup_n.connect(g_star_cup_alternate_g, "Dodgeball: Star Cup (Normal) -> Global: Star Cup Alt Paths (Global)")
    v_star_cup_n.connect(g_star_cup_alternate_g, "Volleyball: Star Cup (Normal) -> Global: Star Cup Alt Paths (Global)")
    h_star_cup_n.connect(g_star_cup_alternate_g, "Hockey: Star Cup (Normal) -> Global: Star Cup Alt Paths (Global)")
    b_star_cup_h.connect(g_star_cup_alternate_g, "Basketball: Star Cup (Hard) -> Global: Star Cup Alt Paths (Global)")
    d_star_cup_h.connect(g_star_cup_alternate_g, "Dodgeball: Star Cup (Hard) -> Global: Star Cup Alt Paths (Global)")
    v_star_cup_h.connect(g_star_cup_alternate_g, "Volleyball: Star Cup (Hard) -> Global: Star Cup Alt Paths (Global)")
    h_star_cup_h.connect(g_star_cup_alternate_g, "Hockey: Star Cup (Hard) -> Global: Star Cup Alt Paths (Global)")

    # Behemoth is accessed by completing all normal star cups, connect all to the Behemoth Boss region
    # Note: Add rule if 3 other star cups have been beaten, Note : "has cleared" is the same as "can reach"
    b_star_cup_n.connect(behemoth_boss, "Basketball Star Cup (Normal) -> Behemoth Boss")
    d_star_cup_n.connect(behemoth_boss, "Dodgeball Star Cup (Normal) -> Behemoth Boss")
    v_star_cup_n.connect(behemoth_boss, "Volleyball Star Cup (Normal) -> Behemoth Boss")
    h_star_cup_n.connect(behemoth_boss, "Hockey Star Cup (Normal) -> Behemoth Boss")

    b_star_cup_h.connect(behemoth_boss, "Basketball Star Cup (Hard) -> Behemoth Boss")
    d_star_cup_h.connect(behemoth_boss, "Dodgeball Star Cup (Hard) -> Behemoth Boss")
    v_star_cup_h.connect(behemoth_boss, "Volleyball Star Cup (Hard) -> Behemoth Boss")
    h_star_cup_h.connect(behemoth_boss, "Hockey Star Cup (Hard) -> Behemoth Boss")
    # Behemoth King is only accessed by beating the Sports Mix Star Cup
    sm_star_cup.connect(behemoth_king_boss, "Sports Mix Star Cup -> Behemoth King Boss")