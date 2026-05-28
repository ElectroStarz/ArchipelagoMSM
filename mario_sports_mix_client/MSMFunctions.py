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


async def unlock_tournament_tabs_option(self, hard_tournament_difficulty: bool, unlocked_sports_mix: bool):
    """Unlocks the tournament tabs depending on YAML settings."""

    # If Sports Mix is unlocked, stop right here and do absolutely nothing.
    if unlocked_sports_mix:
        return

    # 1. Resolve the addresses exactly ONCE here
    address_list = [
        get_address(BasketballAddresses.Tournament.tabs),
        get_address(DodgeballAddresses.Tournament.tabs),
        get_address(VolleyballAddresses.Tournament.tabs),
        get_address(HockeyAddresses.Tournament.tabs)
    ]

    # 2. Determine what value we want to write (3 for hard, 2 for normal)
    target_value = 3 if hard_tournament_difficulty else 2

    # 3. Run the memory check/write loop exactly once
    for address in address_list:
        current_value = self.game_interface.dolphin_client.read_byte(address)

        # Only write if the value needs changing to avoid spamming the emulator
        if current_value != target_value:
            self.game_interface.dolphin_client.write_byte(address, target_value)


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

    # Some addresses are the same in PAL and NTSC-U
    if any(address in vars(classes).values() for classes in exceptions):
        return address

    if dc.GAME_VERSION == "NTSC-U":
        if address == MatchAddresses.current_stage:
            #print(f"[DEBUG] Current Stage detected! Returning NTSC-U Address {new_addr}")
            new_addr = 0x8047796E
            return new_addr


        new_addr = address - offset
        # print(f"[DEBUG] Taking away offset from {address}. Result: {new_addr}")
        return new_addr

    return address