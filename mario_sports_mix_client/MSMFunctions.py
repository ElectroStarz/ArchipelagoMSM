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


def unlock_tabs(hard_tournament_difficulty):
    unlock_tournament_tabs(hard_tournament_difficulty)
    unlock_ex_tabs()
    unlock_party_tabs()

def unlock_tournament_tabs(hard_tournament_difficulty: bool):
    """Unlocks the tournament tabs depending on YAML settings."""

    address_list = [
        get_address(BasketballAddresses.Tournament.tabs),
        get_address(DodgeballAddresses.Tournament.tabs),
        get_address(VolleyballAddresses.Tournament.tabs),
        get_address(HockeyAddresses.Tournament.tabs)
    ]

    # Determine what value we want to write (3 for hard, 2 for normal)
    target_value = 3 if hard_tournament_difficulty else 2

    for address in address_list:
        dme.write_byte(address, target_value)

def unlock_ex_tabs():
    """Unlocks all the exhibition tabs by setting their value to 15"""
    target_value = 15

    for sport in sports_addresses:
        new_addr = get_address(sport.Exhibition.tabs)
        dme.write_byte(new_addr, target_value)

def unlock_party_tabs():
    """Unlocks all the tabs in party mode"""

    dme.write_byte(get_address(PartyMode.FeedPetey.Tabs.tabs), 3)
    dme.write_byte(get_address(PartyMode.HarmonyHustle.Tabs.tabs), 7)
    dme.write_byte(get_address(PartyMode.BobOmbDodge.Tabs.tabs), 3)
    dme.write_byte(get_address(PartyMode.SmashSkate.Tabs.tabs), 3)


def lock_all_cups():
    """Locks all the cups by setting their value to 8"""

    for sport in sports_addresses:
        for diff in cups_difficulty:
            addr = getattr(sport.Tournament, diff)
            new_addr = get_address(addr)
            dme.write_byte(new_addr, 8)

def lock_all_stages():
    """Locks all the stages by setting their value to 8"""

    for sport in sports_addresses:
        for cup in cups:
            addr = getattr(sport.Exhibition, cup)
            new_addr = get_address(addr)
            dme.write_byte(new_addr, 8)

def lock_all_characters():
    """Locks all the characters by setting their value to 0"""

    for sport in sports_addresses:
        for char in characters:
            addr = getattr(sport.Characters, char)
            new_addr = get_address(addr)
            dme.write_byte(new_addr, 0)


def is_exception(address):
    exceptions = (BasketballAddresses.Characters, BasketballAddresses.Tournament, BasketballAddresses.Exhibition,
                  DodgeballAddresses.Characters,  DodgeballAddresses.Tournament,  DodgeballAddresses.Exhibition,
                  VolleyballAddresses.Characters, VolleyballAddresses.Tournament, VolleyballAddresses.Exhibition,
                  HockeyAddresses.Characters,     HockeyAddresses.Tournament,     HockeyAddresses.Exhibition,
                                                  SportsMixAddresses.Tournament,

                  PartyMode.FeedPetey.Tabs, PartyMode.HarmonyHustle.Tabs,
                  PartyMode.BobOmbDodge.Tabs, PartyMode.SmashSkate.Tabs,

                  CupsWonMultiple, GamesPlayed,
    )

    if any(address in vars(classes).values() for classes in exceptions):
        return True
    else:
        return False

def is_ntscu(address):
    if address in vars(NTSCUAddresses).values():
        return True
    else:
        return False

def get_address(address, offset=0xF80):
    """Get the correct address depending on what region the game is.
    Address inputted should be a PAL address which will then be converted to NTSC-U & vice versa"""
    #print(f"[DEBUG] Game Version is: {dc.GAME_VERSION}")
    #print(f"[DEBUG] Input Address (Hex): {hex(address)}")
    if is_exception(address):
        return address

    # Some addresses are the same in PAL and NTSC-U

    if dc.GAME_VERSION == "NTSC-U":
        if address == MatchAddresses.current_court:
            #print(f"[DEBUG] Current Stage detected! Returning NTSC-U Address {new_addr}")
            new_addr = 0x8047796E
            return new_addr

        new_addr = address - offset
        # print(f"[DEBUG] Taking away offset from {address}. Result: {new_addr}")
        return new_addr
    else:
        if is_ntscu(address):
            return address + offset
        else:
            return address