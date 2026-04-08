from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Region
from .options import EnabledSports, GoalCondition

if TYPE_CHECKING:
    from .world import MSMWorld


# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).


def create_and_connect_regions(world: "MSMWorld") -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: "MSMWorld") -> None:
    # Creating a region is as simple as calling the constructor of the Region class.
    main_menu = Region("Main Menu", world.player, world.multiworld)

    # Let's put all these regions in a list.
    regions = [main_menu]

    if "Basketball" in world.options.enabled_sports:
        basketball = Region("Basketball", world.player, world.multiworld)
        b_exhibition = Region("Basketball: Exhibition", world.player, world.multiworld)
        b_stages = Region("Basketball: Stages", world.player, world.multiworld)
        b_mushroom_cup_n = Region("Basketball: Mushroom Cup (Normal)", world.player, world.multiworld)
        b_flower_cup_n = Region("Basketball: Flower Cup (Normal)", world.player, world.multiworld)
        b_star_cup_n = Region("Basketball: Star Cup (Normal)", world.player, world.multiworld)
        b_mushroom_cup_h = Region("Basketball: Mushroom Cup (Hard)", world.player, world.multiworld)
        b_flower_cup_h = Region("Basketball: Flower Cup (Hard)", world.player, world.multiworld)
        b_star_cup_h = Region("Basketball: Star Cup (Hard)", world.player, world.multiworld)
        b_extra = Region("Basketball: Extra", world.player, world.multiworld)
        regions.append(basketball)
        regions.append(b_exhibition)
        regions.append(b_stages)
        regions.append(b_mushroom_cup_n)
        regions.append(b_flower_cup_n)
        regions.append(b_star_cup_n)
        regions.append(b_mushroom_cup_h)
        regions.append(b_flower_cup_h)
        regions.append(b_star_cup_h)
        regions.append(b_extra)
    if "Dodgeball" in world.options.enabled_sports:
        dodgeball = Region("Dodgeball", world.player, world.multiworld)
        d_exhibition = Region("Dodgeball: Exhibition", world.player, world.multiworld)
        d_stages = Region("Dodgeball: Stages", world.player, world.multiworld)
        d_mushroom_cup_n = Region("Dodgeball: Mushroom Cup (Normal)", world.player, world.multiworld)
        d_flower_cup_n = Region("Dodgeball: Flower Cup (Normal)", world.player, world.multiworld)
        d_star_cup_n = Region("Dodgeball: Star Cup (Normal)", world.player, world.multiworld)
        d_mushroom_cup_h = Region("Dodgeball: Mushroom Cup (Hard)", world.player, world.multiworld)
        d_flower_cup_h = Region("Dodgeball: Flower Cup (Hard)", world.player, world.multiworld)
        d_star_cup_h = Region("Dodgeball: Star Cup (Hard)", world.player, world.multiworld)
        d_extra = Region("Dodgeball: Extra", world.player, world.multiworld)
        regions.append(dodgeball)
        regions.append(d_exhibition)
        regions.append(d_stages)
        regions.append(d_mushroom_cup_n)
        regions.append(d_flower_cup_n)
        regions.append(d_star_cup_n)
        regions.append(d_mushroom_cup_h)
        regions.append(d_flower_cup_h)
        regions.append(d_star_cup_h)
        regions.append(d_extra)
    if "Volleyball" in world.options.enabled_sports:
        volleyball = Region("Volleyball", world.player, world.multiworld)
        v_exhibition = Region("Volleyball: Exhibition", world.player, world.multiworld)
        v_stages = Region("Volleyball: Stages", world.player, world.multiworld)
        v_mushroom_cup_n = Region("Volleyball: Mushroom Cup (Normal)", world.player, world.multiworld)
        v_flower_cup_n = Region("Volleyball: Flower Cup (Normal)", world.player, world.multiworld)
        v_star_cup_n = Region("Volleyball: Star Cup (Normal)", world.player, world.multiworld)
        v_mushroom_cup_h = Region("Volleyball: Mushroom Cup (Hard)", world.player, world.multiworld)
        v_flower_cup_h = Region("Volleyball: Flower Cup (Hard)", world.player, world.multiworld)
        v_star_cup_h = Region("Volleyball: Star Cup (Hard)", world.player, world.multiworld)
        v_extra = Region("Volleyball: Extra", world.player, world.multiworld)
        regions.append(volleyball)
        regions.append(v_exhibition)
        regions.append(v_stages)
        regions.append(v_mushroom_cup_n)
        regions.append(v_flower_cup_n)
        regions.append(v_star_cup_n)
        regions.append(v_mushroom_cup_h)
        regions.append(v_flower_cup_h)
        regions.append(v_star_cup_h)
        regions.append(v_extra)
    if "Hockey" in world.options.enabled_sports:
        hockey = Region("Hockey", world.player, world.multiworld)
        h_exhibition = Region("Hockey: Exhibition", world.player, world.multiworld)
        h_stages = Region("Hockey: Stages", world.player, world.multiworld)
        h_mushroom_cup_n = Region("Hockey: Mushroom Cup (Normal)", world.player, world.multiworld)
        h_flower_cup_n = Region("Hockey: Flower Cup (Normal)", world.player, world.multiworld)
        h_star_cup_n = Region("Hockey: Star Cup (Normal)", world.player, world.multiworld)
        h_mushroom_cup_h = Region("Hockey: Mushroom Cup (Hard)", world.player, world.multiworld)
        h_flower_cup_h = Region("Hockey: Flower Cup (Hard)", world.player, world.multiworld)
        h_star_cup_h = Region("Hockey: Star Cup (Hard)", world.player, world.multiworld)
        h_extra = Region("Hockey: Extra", world.player, world.multiworld)
        regions.append(hockey)
        regions.append(h_exhibition)
        regions.append(h_stages)
        regions.append(h_mushroom_cup_n)
        regions.append(h_flower_cup_n)
        regions.append(h_star_cup_n)
        regions.append(h_mushroom_cup_h)
        regions.append(h_flower_cup_h)
        regions.append(h_star_cup_h)
        regions.append(h_extra)
    if "Sports Mix" in world.options.enabled_sports:
        sports_mix = Region("Sports Mix", world.player, world.multiworld)
        sm_mushroom_cup = Region("Sports Mix: Mushroom Cup", world.player, world.multiworld)
        sm_flower_cup = Region("Sports Mix: Flower Cup", world.player, world.multiworld)
        sm_star_cup = Region("Sports Mix: Star Cup", world.player, world.multiworld)
        regions.append(sports_mix)
        regions.append(sm_mushroom_cup)
        regions.append(sm_flower_cup)
        regions.append(sm_star_cup)
    if world.options.goal_condition == GoalCondition.option_defeat_behemoth:
        behemoth_boss_stuff = Region("Behemoth Boss Battle", world.player, world.multiworld)
        regions.append(behemoth_boss_stuff)
    if world.options.goal_condition == GoalCondition.option_defeat_behemoth_King:
        behemoth_boss_stuff = Region("Behemoth Boss Battle", world.player, world.multiworld)
        behemoth_king_boss_stuff = Region("Behemoth King Boss Battle", world.player, world.multiworld)
        regions.append(behemoth_boss_stuff)
        regions.append(behemoth_king_boss_stuff)
    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: MSMWorld) -> None:
    # We have regions now, but still need to connect them to each other.
    # But wait, we no longer have access to the region variables we created in create_all_regions()!
    # Luckily, once you've submitted your regions to multiworld.regions,
    # you can get them at any time using world.get_region(...).
    main_menu = world.get_region("Main Menu")

    basketball = world.get_region("Basketball")
    b_exhibition = world.get_region("Basketball: Exhibition")
    b_stages = world.get_region("Basketball: Stages")
    b_mushroom_cup_n = world.get_region("Basketball: Mushroom Cup (Normal)")
    b_flower_cup_n = world.get_region("Basketball: Flower Cup (Normal)")
    b_star_cup_n = world.get_region("Basketball: Star Cup (Normal)")
    b_mushroom_cup_h = world.get_region("Basketball: Mushroom Cup (Hard)")
    b_flower_cup_h = world.get_region("Basketball: Flower Cup (Hard)")
    b_star_cup_h = world.get_region("Basketball: Star Cup (Hard)")
    b_extra = world.get_region("Basketball: Extra")

    dodgeball = world.get_region("Dodgeball")
    d_exhibition = world.get_region("Dodgeball: Exhibition")
    d_stages = world.get_region("Dodgeball: Stages")
    d_mushroom_cup_n = world.get_region("Dodgeball: Mushroom Cup (Normal)")
    d_flower_cup_n = world.get_region("Dodgeball: Flower Cup (Normal)")
    d_star_cup_n = world.get_region("Dodgeball: Star Cup (Normal)")
    d_mushroom_cup_h = world.get_region("Dodgeball: Mushroom Cup (Hard)")
    d_flower_cup_h = world.get_region("Dodgeball: Flower Cup (Hard)")
    d_star_cup_h = world.get_region("Dodgeball: Star Cup (Hard)")
    d_extra = world.get_region("Dodgeball: Extra")

    volleyball = world.get_region("Volleyball")
    v_exhibition = world.get_region("Volleyball: Exhibition")
    v_stages = world.get_region("Volleyball: Stages")
    v_mushroom_cup_n = world.get_region("Volleyball: Mushroom Cup (Normal)")
    v_flower_cup_n = world.get_region("Volleyball: Flower Cup (Normal)")
    v_star_cup_n = world.get_region("Volleyball: Star Cup (Normal)")
    v_mushroom_cup_h = world.get_region("Volleyball: Mushroom Cup (Hard)")
    v_flower_cup_h = world.get_region("Volleyball: Flower Cup (Hard)")
    v_star_cup_h = world.get_region("Volleyball: Star Cup (Hard)")
    v_extra = world.get_region("Volleyball: Extra")

    hockey = world.get_region("Hockey")
    h_exhibition = world.get_region("Hockey: Exhibition")
    h_stages = world.get_region("Hockey: Stages")
    h_mushroom_cup_n = world.get_region("Hockey: Mushroom Cup (Normal)")
    h_flower_cup_n = world.get_region("Hockey: Flower Cup (Normal)")
    h_star_cup_n = world.get_region("Hockey: Star Cup (Normal)")
    h_mushroom_cup_h = world.get_region("Hockey: Mushroom Cup (Hard)")
    h_flower_cup_h = world.get_region("Hockey: Flower Cup (Hard)")
    h_star_cup_h = world.get_region("Hockey: Star Cup (Hard)")
    h_extra = world.get_region("Hockey: Extra")

    sports_mix = world.get_region("Sports Mix")
    sm_mushroom_cup = world.get_region("Sports Mix: Mushroom Cup")
    sm_flower_cup = world.get_region("Sports Mix: Flower Cup")
    sm_star_cup = world.get_region("Sports Mix: Star Cup")
    behemoth_boss = world.get_region("Behemoth Boss Battle")
    behemoth_king_boss = world.get_region("Behemoth King Boss Battle")

    # An even easier way is to use the region.connect helper.
    main_menu.connect(basketball, "Main Menu -> Basketball", lambda state: state.has("Sport: Basketball", world.player))
    main_menu.connect(dodgeball, "Main Menu -> Dodgeball", lambda state: state.has("Sport: Dodgeball", world.player))
    main_menu.connect(volleyball, "Main Menu -> Volleyball", lambda state: state.has("Sport: Volleyball", world.player))
    main_menu.connect(hockey, "Main Menu -> Hockey", lambda state: state.has("Sport: Hockey", world.player))
    main_menu.connect(sports_mix, "Main Menu -> Sports Mix", lambda state: state.has("Sport: Sports Mix", world.player))

    basketball.connect(b_exhibition, "Basketball -> Exhibition")
    basketball.connect(b_stages, "Basketball -> Stages")
    basketball.connect(b_mushroom_cup_n, "Basketball -> Mushroom Cup (Normal)")
    basketball.connect(b_flower_cup_n, "Basketball -> Flower Cup (Normal)")
    basketball.connect(b_star_cup_n, "Basketball -> Star Cup (Normal)")
    basketball.connect(b_mushroom_cup_h, "Basketball -> Mushroom Cup (Hard)")
    basketball.connect(b_flower_cup_h, "Basketball -> Flower Cup (Hard)")
    basketball.connect(b_star_cup_h, "Basketball -> Star Cup (Hard)")
    basketball.connect(b_extra, "Basketball -> Extra")

    dodgeball.connect(d_exhibition, "Dodgeball -> Exhibition")
    dodgeball.connect(d_stages, "Dodgeball -> Stages")
    dodgeball.connect(d_mushroom_cup_n, "Dodgeball -> Mushroom Cup (Normal)")
    dodgeball.connect(d_flower_cup_n, "Dodgeball -> Flower Cup (Normal)")
    dodgeball.connect(d_star_cup_n, "Dodgeball -> Star Cup (Normal)")
    dodgeball.connect(d_mushroom_cup_h, "Dodgeball -> Mushroom Cup (Hard)")
    dodgeball.connect(d_flower_cup_h, "Dodgeball -> Flower Cup (Hard)")
    dodgeball.connect(d_star_cup_h, "Dodgeball -> Star Cup (Hard)")
    dodgeball.connect(d_extra, "Dodgeball -> Extra")

    volleyball.connect(v_exhibition, "Volleyball -> Exhibition")
    volleyball.connect(v_stages, "Volleyball -> Stages")
    volleyball.connect(v_mushroom_cup_n, "Volleyball -> Mushroom Cup (Normal)")
    volleyball.connect(v_flower_cup_n, "Volleyball -> Flower Cup (Normal)")
    volleyball.connect(v_star_cup_n, "Volleyball -> Star Cup (Normal)")
    volleyball.connect(v_mushroom_cup_h, "Volleyball -> Mushroom Cup (Hard)")
    volleyball.connect(v_flower_cup_h, "Volleyball -> Flower Cup (Hard)")
    volleyball.connect(v_star_cup_h, "Volleyball -> Star Cup (Hard)")
    volleyball.connect(v_extra, "Volleyball -> Extra")

    hockey.connect(h_exhibition, "Hockey -> Exhibition")
    hockey.connect(h_stages, "Hockey -> Stages")
    hockey.connect(h_mushroom_cup_n, "Hockey -> Mushroom Cup (Normal)")
    hockey.connect(h_flower_cup_n, "Hockey -> Flower Cup (Normal)")
    hockey.connect(h_star_cup_n, "Hockey -> Star Cup (Normal)")
    hockey.connect(h_mushroom_cup_h, "Hockey -> Mushroom Cup (Hard)")
    hockey.connect(h_flower_cup_h, "Hockey -> Flower Cup (Hard)")
    hockey.connect(h_star_cup_h, "Hockey -> Star Cup (Hard)")
    hockey.connect(h_extra, "Hockey -> Extra")

    sports_mix.connect(sm_mushroom_cup, "Sports Mix -> Mushroom Cup")
    sports_mix.connect(sm_flower_cup, "Sports Mix -> Flower Cup")
    sports_mix.connect(sm_star_cup, "Sports Mix -> Star Cup")

    b_star_cup_n.connect(behemoth_boss, "Basketball Star Cup (Normal) -> Behemoth Boss")
    sm_star_cup.connect(behemoth_king_boss, "Sports Mix Star Cup -> Behemoth King Boss")


    # The region.connect helper even allows adding a rule immediately.
    # We'll talk more about rule creation in the set_all_rules() function in rules.py.
    # overworld.connect(top_left_room, "Overworld to Top Left Room", lambda state: state.has("Key", world.player))

    # Some Entrances may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
