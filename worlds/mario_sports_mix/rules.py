from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import MSMWorld


def set_all_rules(world: MSMWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.

    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: MSMWorld) -> None:
    # First, we need to actually grab our entrances. Luckily, there is a helper method for this.
    # overworld_to_bottom_right_room = world.get_entrance("Overworld to Bottom Right Room")
    # overworld_to_top_left_room = world.get_entrance("Overworld to Top Left Room")
    # right_room_to_final_boss_room = world.get_entrance("Right Room to Final Boss Room")
    menu_to_basketball = world.get_entrance("Main Menu -> Basketball")
    menu_to_dodgeball = world.get_entrance("Main Menu -> Dodgeball")
    menu_to_volleyball = world.get_entrance("Main Menu -> Volleyball")
    menu_to_hockey = world.get_entrance("Main Menu -> Hockey")
    menu_to_sports_mix = world.get_entrance("Main Menu -> Sports Mix")

    # Basketball Cup Entrances
    basketball_to_mush_n = world.get_entrance("Basketball -> Mushroom Cup (Normal)")
    basketball_to_mush_h = world.get_entrance("Basketball -> Mushroom Cup (Hard)")
    basketball_to_flower_n = world.get_entrance("Basketball -> Flower Cup (Normal)")
    basketball_to_flower_h = world.get_entrance("Basketball -> Flower Cup (Hard)")
    basketball_to_star_n = world.get_entrance("Basketball -> Star Cup (Normal)")
    basketball_to_star_h = world.get_entrance("Basketball -> Star Cup (Hard)")

    # Dodgeball Cup Entrances
    dodgeball_to_mush_n = world.get_entrance("Dodgeball -> Mushroom Cup (Normal)")
    dodgeball_to_mush_h = world.get_entrance("Dodgeball -> Mushroom Cup (Hard)")
    dodgeball_to_flower_n = world.get_entrance("Dodgeball -> Flower Cup (Normal)")
    dodgeball_to_flower_h = world.get_entrance("Dodgeball -> Flower Cup (Hard)")
    dodgeball_to_star_n = world.get_entrance("Dodgeball -> Star Cup (Normal)")
    dodgeball_to_star_h = world.get_entrance("Dodgeball -> Star Cup (Hard)")

    # Volleyball Cup Entrances
    volleyball_to_mush_n = world.get_entrance("Volleyball -> Mushroom Cup (Normal)")
    volleyball_to_mush_h = world.get_entrance("Volleyball -> Mushroom Cup (Hard)")
    volleyball_to_flower_n = world.get_entrance("Volleyball -> Flower Cup (Normal)")
    volleyball_to_flower_h = world.get_entrance("Volleyball -> Flower Cup (Hard)")
    volleyball_to_star_n = world.get_entrance("Volleyball -> Star Cup (Normal)")
    volleyball_to_star_h = world.get_entrance("Volleyball -> Star Cup (Hard)")

    # Hockey Cup Entrances
    hockey_to_mush_n = world.get_entrance("Hockey -> Mushroom Cup (Normal)")
    hockey_to_mush_h = world.get_entrance("Hockey -> Mushroom Cup (Hard)")
    hockey_to_flower_n = world.get_entrance("Hockey -> Flower Cup (Normal)")
    hockey_to_flower_h = world.get_entrance("Hockey -> Flower Cup (Hard)")
    hockey_to_star_n = world.get_entrance("Hockey -> Star Cup (Normal)")
    hockey_to_star_h = world.get_entrance("Hockey -> Star Cup (Hard)")

    # Sports Mix Entrances
    sports_mix_to_mush = world.get_entrance("Sports Mix -> Mushroom Cup")
    sports_mix_to_flower = world.get_entrance("Sports Mix -> Flower Cup")
    sports_mix_to_star = world.get_entrance("Sports Mix -> Star Cup")

    # Boss Entrances
    star_cup_to_behemoth =
    sm_star_cup_to_king = world.get_entrance("Sports Mix Star Cup -> Behemoth King Boss")

    # An access rule is a function. We can define this function like any other function.
    # This function must accept exactly one parameter: A "CollectionState".
    # A CollectionState describes the current progress of the players in the multiworld, i.e. what items they have,
    # which regions they've reached, etc.
    # In an access rule, we can ask whether the player has a collected a certain item.
    # We can do this via the state.has(...) function.
    # This function takes an item name, a player number, and an optional count parameter (more on that below)
    # Since a rule only takes a CollectionState parameter, but we also need the player number in the state.has call,
    # our function needs to be locally defined so that it has access to the player number from the outer scope.
    # In our case, we are inside a function that has access to the "world" parameter, so we can use world.player.
    def can_destroy_bush(state: CollectionState) -> bool:
        return state.has("Sword", world.player)

    def can_play_mushroom_cup(state: CollectionState) -> bool:
        return state.has("Mushroom Cup", world.player)

    # Now we can set our "can_destroy_bush" rule to our entrance which requires slashing a bush to clear the path.
    # One way to set rules is via the set_rule() function, which works on both Entrances and Locations.
    set_rule(overworld_to_bottom_right_room, can_destroy_bush)
    set_rule(mushroom_cup, can_play_mushroom_cup)

    # Because the function has to be defined locally, most worlds prefer the lambda syntax.
    set_rule(overworld_to_top_left_room, lambda state: state.has("Key", world.player))
    set_rule(flower_cup, lambda state: state.has("Flower Cup", world.player))

    # Conditions can depend on event items.
    set_rule(right_room_to_final_boss_room, lambda state: state.has("Top Left Room Button Pressed", world.player))
    set_rule(menu_to_basketball, lambda state: state.has("A button to basketball pressed", world.player))

    # Some entrance rules may only apply if the player enabled certain options.
    # In our case, if the hammer option is enabled, we need to add the Hammer requirement to the Entrance from
    # Overworld to the Top Middle Room.
    if world.options.hammer:
        overworld_to_top_middle_room = world.get_entrance("Overworld to Top Middle Room")
        set_rule(overworld_to_top_middle_room, lambda state: state.has("Hammer", world.player))
    if "Hockey" in world.options.enabled_sports:
        set_rule(menu_to_hockey, lambda state: state.has("Hockey", world.player))


def set_all_location_rules(world: MSMWorld) -> None:
    # Location rules work no differently from Entrance rules.
    # Most of our locations are chests that can simply be opened by walking up to them.
    # Thus, their logical requirements are covered by the Entrance rules of the Entrances that were required to
    # reach the region that the chest sits in.
    # However, our two enemies work differently.
    # Entering the room with the enemy is not enough, you also need to have enough combat items to be able to defeat it.
    # So, we need to set requirements on the Locations themselves.
    # Since combat is a bit more complicated, we'll use this chance to cover some advanced access rule concepts.

    # Sometimes, you may want to have different rules depending on the player's chosen options.
    # There is a wrong way to do this, and a right way to do this. Let's do the wrong way first.
    right_room_enemy = world.get_location("Right Room Enemy Drop")
    beat_mario_stadium = world.get_location("Beat Mario Stadium")

    # DON'T DO THIS!!!!
    set_rule(
        right_room_enemy,
        lambda state: (
            state.has("Sword", world.player)
            and (not world.options.hard_mode or state.has_any(("Shield", "Health Upgrade"), world.player))
        ),
    )
    # DON'T DO THIS!!!!

    # Now, what's actually wrong with this? It works perfectly fine, right?
    # If hard mode disabled, Sword is enough. If hard mode is enabled, we also need a Shield or a Health Upgrade.
    # The access rule we just wrote does this correctly, so what's the problem?
    # The problem is performance.
    # Most of your world code doesn't need to be perfectly performant, since it just runs once per slot.
    # However, access rules in particular are by far the hottest code path in Archipelago.
    # An access rule will potentially be called thousands or even millions of times over the course of one generation.
    # As a result, access rules are the one place where it's really worth putting in some effort to optimize.
    # What's the performance problem here?
    # Every time our access rule is called, it has to evaluate whether world.options.hard_mode is True or False.
    # Wouldn't it be better if in easy mode, the access rule only checked for Sword to begin with?
    # Wouldn't it also be better if in hard mode, it already knew it had to check Shield and Health Upgrade as well?
    # Well, we can achieve this by doing the "if world.options.hard_mode" check outside the set_rule call,
    # and instead having two *different* set_rule calls depending on which case we're in.

    if world.options.hard_mode:
        # If you have multiple conditions, you can obviously chain them via "or" or "and".
        # However, there are also the nice helper functions "state.has_any" and "state.has_all".
        set_rule(
            right_room_enemy,
            lambda state: (
                state.has("Sword", world.player) and state.has_any(("Shield", "Health Upgrade"), world.player)
            ),
        )
    else:
        set_rule(right_room_enemy, lambda state: state.has("Sword", world.player))

    if "Mario Stadium" in world.options.enabled_stages:
        set_rule(beat_mario_stadium, lambda state: state.has("Mario Stadium", world.player))

    # Another way to chain multiple conditions is via the add_rule function.
    # This makes the access rules a bit slower though, so it should only be used if your structure justifies it.
    # In our case, it's pretty useful because hard mode and easy mode have different requirements.
    final_boss = world.get_location("Final Boss Defeated")
    win = world.get_location("A button to basketball pressed")

    # For the "known" requirements, it's still better to chain them using a normal "and" condition.
    add_rule(final_boss, lambda state: state.has_all(("Sword", "Shield"), world.player))

    if world.options.hard_mode:
        # You can check for multiple copies of an item by using the optional count parameter of state.has().
        add_rule(final_boss, lambda state: state.has("Health Upgrade", world.player, 2))


def set_completion_condition(world: MSMWorld) -> None:
    # Finally, we need to set a completion condition for our world, defining what the player needs to win the game.
    # You can just set a completion condition directly like any other condition, referencing items the player receives:
    world.multiworld.completion_condition[world.player] = lambda state: state.has_all(("Sword", "Shield"), world.player)

    # In our case, we went for the Victory event design pattern (see create_events() in locations.py).
    # So lets undo what we just did, and instead set the completion condition to:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
