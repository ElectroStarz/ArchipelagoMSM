from functools import cached_property
from .memory_addresses_pal import *
from .MSMFunctions import get_address


# This is a file with commonly used addresses. These values are cached and saved as the user if probably not going to
# change regions midway through a sync/async. If needed though, there is a command to reset these values in the client.

class AddressLib:

    @cached_property
    def vbp_addr(self):
        return get_address(PlayerAddresses.various_ball_pointers)

    @cached_property
    def current_court_addr(self):
        return get_address(MatchAddresses.current_court)

    @cached_property
    def current_module_addr(self):
        return get_address(MatchAddresses.current_module)

    @cached_property
    def match_status_addr(self):
        return get_address(MatchAddresses.match_status)

    @cached_property
    def game_layout_addr(self):
        return get_address(MatchAddresses.game_layout)

    @cached_property
    def paused_addr(self):
        return get_address(MatchAddresses.paused)

    @cached_property
    def timer_addr(self):
        return get_address(MatchAddresses.time_remaining)

    @cached_property
    def max_time_addr(self):
        return get_address(MatchAddresses.max_time)

    @cached_property
    def current_period_addr(self):
        return get_address(MatchAddresses.current_period)

    @cached_property
    def cutscene_active_addr(self):
        return get_address(MatchAddresses.cutscene_active)

    @cached_property
    def loading_screen_addr(self):
        return get_address(MatchAddresses.loading_screen_active)

    @cached_property
    def behemoth_hp_addr(self):
        return get_address(BossAddresses.behemoth_hp)

    @cached_property
    def basket_time_addr(self):
        return get_address(BasketballAddresses.time)

    @cached_property
    def dodge_time_addr(self):
        return get_address(DodgeballAddresses.time)

    @cached_property
    def hockey_time_addr(self):
        return get_address(HockeyAddresses.time)

    @cached_property
    def is_sports_mix_addr(self):
        return get_address(SportsMixAddresses.is_sports_mix)

    @cached_property
    def exhibition_diff_addr(self):
        return get_address(MatchAddresses.exhibition_diff)

    @cached_property
    def tournament_diff_addr(self):
        return get_address(MatchAddresses.tournament_diff)

    @cached_property
    def p_pos_addr(self):
        return get_address(PlayerAddresses.Position.pos)

    @cached_property
    def p_item_held_addr(self):
        return get_address(PlayerAddresses.item_held)

    @cached_property
    def p_coins_addr(self):
        return get_address(PlayerAddresses.Score.coins)

    @cached_property
    def o_item_held_addr(self):
        return get_address(OpponentAddresses.item_held)

    @cached_property
    def o_coins_addr(self):
        return get_address(OpponentAddresses.Score.coins)

    @cached_property
    def p_special_meter_addr(self):
        return get_address(PlayerAddresses.special_meter)

    @cached_property
    def alt_path_spawn_addr(self):
        return get_address(TournamentAddresses.alt_path_condition_fufilled)

    @cached_property
    def current_node_addr(self):
        return get_address(GlobalTournament.current_node)

    @cached_property
    def mushroom_cup_alt_unlocked_addr(self):
        return get_address(TournamentAddresses.mushroom_alt_paths_unlocked)

    @cached_property
    def flower_cup_alt_unlocked_addr(self):
        return get_address(TournamentAddresses.flower_alt_paths_unlocked)

    @cached_property
    def flower_cup_alt_bridges_inner_addr(self):
        return get_address(TournamentAddresses.flower_inner_bridges_toggle)

    @cached_property
    def flower_cup_alt_bridges_outer_addr(self):
        return get_address(TournamentAddresses.flower_outer_bridges_toggle)

    @cached_property
    def star_cup_alt_unlocked_addr(self):
        return get_address(TournamentAddresses.star_alt_paths_unlocked)

    @cached_property
    def current_tournament_round_addr(self):
        return get_address(GlobalTournament.current_round)

    @cached_property
    def current_tournament_cup_addr(self):
        return get_address(GlobalTournament.current_cup)

    @cached_property
    def current_tournament_map_sport_addr(self):
        return get_address(TournamentAddresses.current_tournament_sport_variation)

    @cached_property
    def current_tournament_sport_addr(self):
        return get_address(GlobalTournament.current_tournament_sport)

    address_properties = [
        "current_stage_addr", "current_module_addr", "match_status_addr", "game_layout_addr",
        "paused_addr", "timer_addr", "current_period_addr", "cutscene_active_addr",
        "loading_screen_addr", "behemoth_hp_addr", "volley_last_held_addr",
        "basket_time_addr", "dodge_time_addr", "hockey_time_addr",
        "is_sports_mix_addr", "exhibition_diff_addr", "tournament_diff_addr",
        "p_pos_addr", "p_item_held_addr", "p_coins_addr",
        "o_coins_addr", "o_item_held_addr", "p_special_meter_addr",
        "alt_path_spawn_addr", "current_node_addr", "mushroom_cup_alt_unlocked_addr",
        "flower_cup_alt_unlocked_addr", "flower_cup_alt_bridges_inner_addr",
        "flower_cup_alt_bridges_outer_addr", "star_cup_alt_unlocked_addr",
        "current_tournament_round_addr", "current_tournament_cup_addr",
        "current_tournament_map_sport_addr", "current_tournament_sport_addr"
    ]

    def reset_all_addresses(self, logger):
        """Forces the client to re-read memory by clearing all cached addresses."""

        cleared_count = 0

        for prop in self.address_properties:
            # We must check if it actually exists in the cache first.
            # If we try to delete something that isn't cached yet, Python will crash with an AttributeError!
            if prop in self.__dict__:
                delattr(self, prop)
                cleared_count += 1

        logger.info(f"Successfully cleared {cleared_count} cached addresses. They will be re-read on next access.")