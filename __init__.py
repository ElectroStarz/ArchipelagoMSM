from collections.abc import Mapping
from typing import Any
from BaseClasses import Tutorial
from Options import OptionError
from worlds.LauncherComponents import Component, Type, components, launch, icon_paths
from worlds.AutoWorld import WebWorld, World
from . import regions, rules, locations
from .options import *
from .items import ITEM_NAME_TO_ID, auto_item_groups
from .locations import LOCATION_NAME_TO_ID, auto_location_groups
import json
import pkgutil
from Utils import visualize_regions

def run_client(*args: str) -> None:
    from .mario_sports_mix_client.main_client import launch_mario_sports_mix_client as launch_msm_client
    launch(launch_msm_client, name="Mario Sports Mix Client", args=args)

icon_paths["SportMixIcon"] = f"ap:{__name__}/icon/SportMixIcon.png"
components.append(
    Component(
        "Mario Sports Mix Client",
        func=run_client,
        game_name="Mario Sports Mix",
        component_type=Type.CLIENT,
        supports_uri=True,
        icon="SportMixIcon",

    )
)


# Find world version

# Read the file data from the APWorld
data = pkgutil.get_data(__name__, "archipelago.json")

if data is not None:
    file = json.loads(data.decode("utf-8"))
    WORLD_VERSION = file["world_version"]
else:
    raise FileNotFoundError("Could not find archipelago.json in the APWorld!")


class MSMWebWorld(WebWorld):
    game = "Mario Sports Mix"

    # dirt, grass, grassFlowers, ice, jungle, ocean, partyTime, and stone.
    theme = "partyTime"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Mario Sports Mix for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["ElectroStarz"],
    )

    setup_fr = Tutorial(
        "Guide de configuration Multimonde.",
        "Un guide pour configurer Mario Sports Mix MultiWorld.",
        "Français",
        "setup_fr.md",
        "setup/fr",
        ["Sylaaz", "Solz"]
    )

    tutorials = [setup_en, setup_fr]
    option_groups = msm_option_groups


class MSMWorld(World):
    """
    Mario Sports Mix is a fast-paced Wii sports game that includes basketball, volleyball, dodgeball, and hockey.
    Play as characters from the Mario, Final Fantasy and Dragon Quest franchise in order to defeat the evil in this
    land and conquer all the sports!
    """
    game = "Mario Sports Mix"
    web = MSMWebWorld()

    options_dataclass = MSMOptions
    options: MSMOptions


    location_name_to_id = LOCATION_NAME_TO_ID
    item_name_to_id = ITEM_NAME_TO_ID

    item_name_groups = auto_item_groups
    location_name_groups = auto_location_groups


    origin_region_name = "Main Menu"

    def generate_early(self) -> None:
        if self.options.goal_condition.value == self.options.be_mean.value:
            raise OptionError(
                f"[Mario Sports Mix] {self.player_name}'s Be Mean option is the same as their win condition!"
            )

        points_to_win = {
            "b_points": {"value": self.options.b_points_win.value, "enabled": self.options.enable_b_points_win.value},
            "h_points": {"value": self.options.h_points_win.value, "enabled": self.options.enable_h_points_win.value},
            "v_points": {"value": self.options.v_points_win.value, "enabled": True}, # Volleyball always has win points
        }

        # Filter to get values only if 'enabled' is True
        active_values = [item["value"] for item in points_to_win.values() if item["enabled"]]

        # Perform the comparison
        if (active_values and self.options.deathlink_opponent_scores_points.value > max(active_values)
                and self.options.deathlink.value):
            raise OptionError(
                f"[Mario Sports Mix] {self.player_name}'s Opponent Scores Points value is bigger than one of their "
                f"points to win values, they won't be able to send a deathlink in that sport!"
            )

        if self.options.goal_condition.value in (1, 2, 3) and not self.options.include_tournaments:
            raise OptionError(
                f"[Mario Sports Mix] {self.player_name}'s goal condition requires tournaments but they don't have them on!"
            )

        if self.options.goal_condition.value == 4 and not self.options.include_exhibition.value:
            raise OptionError(
                f"[Mario Sports Mix] {self.player_name}'s goal condition requires exhibitions but they don't have them on!"
            )

        if self.options.goal_condition.value == 5 and len(self.options.party_mode.value) != 4:
            self.options.party_mode.value = {"Feed Petey", "Harmony Hustle", "Bob-Omb Dodge", "Smash Skate"}

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

        # state = self.multiworld.get_all_state(False)
        #
        # state.update_reachable_regions(self.player)
        #
        # visualize_regions(
        #     self.get_region("Main Menu"),
        #     "mario_sports_mix_regions_status.puml",
        #     show_entrance_names=True,
        #     regions_to_highlight=set(state.reachable_regions[self.player])
        # )

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.MSMItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    # Stuff to send to the client/tracker because it needs to know that
    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = {
            "version": WORLD_VERSION,

            # Goal/Boss Stuff
            "goal_condition": self.options.goal_condition.value,
            "behemoth_hp": self.options.behemoth_hp.value,
            "behemoth_king_hp": self.options.behemoth_king_hp.value,
            "win_cups_amount": self.options.win_cups_amount.value,

            # Unlock Stuff
            "enabled_sports": self.options.enabled_sports.value,
            "start_with_mushroom_cup": self.options.start_with_mushroom_cup.value,
            "sports_mix_unlock": self.options.sports_mix_unlock.value,
            "exhibition_difficulty": self.options.exhibition_difficulty.value,
            "hard_tournament_difficulty": self.options.hard_tournament_difficulty.value,
            "court_unlock_type": self.options.court_unlock_type.value,
            "cup_unlock_type": self.options.cup_unlock_type.value,

            # Sanity Stuff
            "character_sanity": self.options.character_sanity.value,
            "send_both_character_sanity": self.options.send_both_character_sanity.value,

            # Deathlink Stuff
            "deathlink": self.options.deathlink.value,
            "deathlink_action": self.options.deathlink_action.value,
            "deathlink_consequence": self.options.deathlink_consequence.value,
            "deathlink_opponent_get_points": self.options.deathlink_opponent_get_points.value,
            "deathlink_opponent_scores_points": self.options.deathlink_opponent_scores_points.value,
            "deathlink_boss_health_recovered": self.options.deathlink_boss_health_recovered.value,
            "deathlink_dodgeball_health_lost": self.options.deathlink_dodgeball_health_lost.value,

            # Custom Tournament Rule Stuff
            "basket_time": self.options.basket_time.value,
            "enable_b_points_win": self.options.enable_b_points_win.value,
            "b_points_win": self.options.b_points_win.value,
            "b_period": self.options.b_period.value,

            "dodge_time": self.options.dodge_time.value,
            "d_period": self.options.d_period.value,
            "d_max_health": self.options.d_max_health.value,

            "v_points_win": self.options.v_points_win.value,
            "v_period": self.options.v_period.value,

            "hockey_time": self.options.hockey_time.value,
            "enable_h_points_win": self.options.enable_h_points_win.value,
            "h_points_win": self.options.h_points_win.value,
            "h_period": self.options.h_period.value,

            # Party Mode Stuff
            "party_mode": self.options.party_mode.value,
            "party_mode_opponent": self.options.party_mode_opponent.value,
        }

        return slot_data
