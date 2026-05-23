#from . import memory_loader as ml
import dolphin_memory_engine
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


def unlock_tabs():
    # Tournament
    for sport in sports_addresses:
        new_addr = get_address(sport.Tournament.tabs)
        dme.write_byte(new_addr, 3)

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


# Map the PAL addresses to their exact NTSC-U equivalents
NTSC_U_EXCEPTIONS = {
    MatchAddresses.current_stage: 0x8047796E,
}


def get_address(address, offset=0xF80):
    #print(f"[DEBUG] Game Version is: {dc.GAME_VERSION}")
    #print(f"[DEBUG] Input Address (Hex): {hex(address)}")
    #print(f"[DEBUG] Target Match (Hex): {hex(target_match_address)}")

    if dc.GAME_VERSION == "NTSC-U":
        if address == MatchAddresses.current_stage:
            #print("[DEBUG] EXCEPTION MATCHED! Returning hardcoded string address.")
            return 0x8047796E

        #print("[DEBUG] Exception failed. Returning standard math offset.")
        return address - offset

    return address