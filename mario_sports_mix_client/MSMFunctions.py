import dolphin_memory_engine as dme
from . import dolphin_connection as dc
from .memory_addresses_pal import *

cups_difficulty = ["normal_cups", "hard_cups"]

cups = ["mushroom_cup", "flower_cup", "star_cup", "question_mark_cup"]

characters = [
    "mario", "luigi", "peach", "daisy", "yoshi", "wario", "waluigi", "donkey_kong", "diddy_kong", "toad", "bowser",
    "bowser_jr", "moogle", "white_mage", "black_mage", "ninja", "cactuar", "slime"
]

sports_addresses = [
    BasketballAddresses,
    DodgeballAddresses,
    VolleyballAddresses,
    HockeyAddresses
]


async def unlock_tournament_tabs_option(self, hard_tournament_difficulty):
    """Unlocks the tournament tabs depending on if the player has checked Hard Tournament Difficulty in their YAML"""

    b_address = get_address(BasketballAddresses.Tournament.tabs)
    d_address = get_address(DodgeballAddresses.Tournament.tabs)
    v_address = get_address(VolleyballAddresses.Tournament.tabs)
    h_address = get_address(HockeyAddresses.Tournament.tabs)
    address_list = [b_address, d_address, v_address, h_address]

    if hard_tournament_difficulty:
        for address in address_list:
            new_address = get_address(address)
            value = self.game_interface.dolphin_client.read_byte(new_address)
            if value != 3:
                self.game_interface.dolphin_client.write_byte(new_address, 3)
    else:
        for address in address_list:
            new_address = get_address(address)
            value = self.game_interface.dolphin_client.read_byte(new_address)
            if value != 2:
                self.game_interface.dolphin_client.write_byte(new_address, 2)


def unlock_ex_tabs():
    # Exhibition
    for sport in sports_addresses:
        new_addr = get_address(sport.Exhibition.tabs)
        dme.write_byte(new_addr, 15)


def lock_all_cups():
    for sport in sports_addresses:
        for diff in cups_difficulty:
            addr = getattr(sport.Tournament, diff)
            new_addr = get_address(addr)
            dme.write_byte(new_addr, 8)


def lock_all_stages():
    for sport in sports_addresses:
        for cup in cups:
            addr = getattr(sport.Exhibition, cup)
            new_addr = get_address(addr)
            dme.write_byte(new_addr, 8)


def lock_all_characters():
    for sport in sports_addresses:
        for char in characters:
            addr = getattr(sport.Characters, char)
            new_addr = get_address(addr)
            dme.write_byte(new_addr, 0)


def get_address(address, offset=0xF80):
    """Get the correct address depending on what region the game is"""
    #print(f"[DEBUG] Game Version is: {dc.GAME_VERSION}")
    #print(f"[DEBUG] Input Address (Hex): {hex(address)}")
    exceptions = (BasketballAddresses.Characters, DodgeballAddresses.Characters, VolleyballAddresses.Characters,
                HockeyAddresses.Characters, BasketballAddresses.Tournament, DodgeballAddresses.Tournament,
                VolleyballAddresses.Tournament, HockeyAddresses.Tournament, BasketballAddresses.Exhibition,
                DodgeballAddresses.Exhibition, VolleyballAddresses.Exhibition, HockeyAddresses.Exhibition)

    if dc.GAME_VERSION == "NTSC-U":
        if address == MatchAddresses.current_stage:
            #print(f"[DEBUG] Current Stage detected! Returning NTSC-U Address {new_addr}")
            new_addr = 0x8047796E
            return new_addr

        # Some addresses are the same in PAL and NTSC-U
        if any(address in vars(classes).values() for classes in exceptions):
            return address

        #print(f"[DEBUG] Taking away offset from {address}. Result: {new_addr}")
        new_addr = address - offset
        return new_addr


    return address