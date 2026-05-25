from functools import cached_property
from .memory_addresses_pal import *
from .MSMFunctions import get_address

# This is a file with commonly used addresses. These values are cached and saved as the user if probably not going to
# change regions midway through a sync/async. If needed though, there is a command to reset these values in the client.

class AddressLib:

    @cached_property
    def current_stage_addr(self):
        return get_address(MatchAddresses.current_stage)

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
    def current_period(self):
        return get_address(MatchAddresses.current_period)

    @cached_property
    def cutscene_active_addr(self):
        return get_address(MatchAddresses.cutscene_on)

    @cached_property
    def loading_screen_addr(self):
        return get_address(MatchAddresses.loading_screen_active)

    @cached_property
    def behemoth_hp_addr(self):
        return get_address(BossAddresses.behemoth_hp)

    @cached_property
    def volley_last_held_addr(self):
        return get_address(VolleyballAddresses.last_held)

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
    def o_coins_addr(self):
        return get_address(OpponentAddresses.Score.coins)

    @cached_property
    def p_special_meter_addr(self):
        return get_address(PlayerAddresses.special_meter)


    def reset_all_addresses(self):
        """Safely clears the cache for all memory addresses."""

        address_properties = [
            "current_stage_addr", "match_status_addr", "game_layout_addr",
            "paused_addr", "timer_addr", "current_period", "cutscene_active_addr",
            "loading_screen_addr", "behemoth_hp_addr", "volley_last_held_addr",
            "basket_time_addr", "dodge_time_addr", "hockey_time_addr",
            "is_sports_mix_addr", "exhibition_diff_addr", "tournament_diff_addr",
            "p_pos_addr", "p_item_held_addr", "p_coins_addr",
            "o_coins_addr", "p_special_meter_addr"
        ]

        # Loop through the list and delete the cached variables if they exist
        for prop in address_properties:
            if prop in self.__dict__:
                delattr(self, prop)