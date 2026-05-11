from .memory_addresses import *
import dolphin_memory_engine as dme

sports_addresses = [
    BasketballAddresses,
    DodgeballAddresses,
    VolleyballAddresses,
    HockeyAddresses,
]

cups_difficulty = ["normal_cups", "hard_cups"]

cups = ["mushroom_cup", "flower_cup", "star_cup", "question_mark_cup"]

characters = [
    "mario", "luigi", "peach", "daisy", "yoshi", "wario", "waluigi", "donkey_kong", "diddy_kong", "toad", "bowser",
    "bowser_jr", "moogle", "white_mage", "black_mage", "ninja", "cactuar", "slime"
]

def unlock_tabs():
    # Tournament
    for sport in sports_addresses:
        dme.write_byte(sport.Tournament.tabs, 3)

    # Exhibition
    for sport in sports_addresses:
        dme.write_byte(sport.Exhibition.tabs, 15)


def lock_all_cups():
    for sport in sports_addresses:
        for diff in cups_difficulty:
            addr = getattr(sport.Tournament, diff)
            dme.write_byte(addr, 8)


def lock_all_stages():
    for sport in sports_addresses:
        for cup in cups:
            addr = getattr(sport.Exhibition, cup)
            dme.write_byte(addr, 8)


def lock_all_characters():
    for sport in sports_addresses:
        for char in characters:
            addr = getattr(sport.Characters, char)
            dme.write_byte(addr, 0)
