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



def get_address(address, offset=0xF80):
    #print(f"[DEBUG] Game Version is: {dc.GAME_VERSION}")
    #print(f"[DEBUG] Input Address (Hex): {hex(address)}")

    if dc.GAME_VERSION == "NTSC-U":
        if address == MatchAddresses.current_stage:
            #print(f"[DEBUG] Current Stage detected! Returning NTSC-U Address {new_addr}")
            new_addr = 0x8047796E
            return new_addr

        #print(f"[DEBUG] Taking away offset from {address}. Result: {new_addr}")
        new_addr = address - offset
        return new_addr

    new_addr = address
    return new_addr