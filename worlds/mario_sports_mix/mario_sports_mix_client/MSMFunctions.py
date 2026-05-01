from typing import Any
from .memory_addresses import *
from .. import MSMOptions
import dolphin_memory_engine as dme

def unlock_tabs():
    # Tournament
    dme.write_byte(BasketballAddresses.Tournament.tabs, 3)
    dme.write_byte(DodgeballAddresses.Tournament.tabs, 3)
    dme.write_byte(VolleyballAddresses.Tournament.tabs, 3)
    dme.write_byte(HockeyAddresses.Tournament.tabs, 3)
    # Exhibition
    dme.write_byte(BasketballAddresses.Exhibition.tabs, 15)
    dme.write_byte(DodgeballAddresses.Exhibition.tabs, 15)
    dme.write_byte(VolleyballAddresses.Exhibition.tabs, 15)
    dme.write_byte(HockeyAddresses.Exhibition.tabs, 15)

def lock_all_cups():
    dme.write_byte(BasketballAddresses.Tournament.normal_cups, 8)
    dme.write_byte(BasketballAddresses.Tournament.hard_cups, 8)
    dme.write_byte(DodgeballAddresses.Tournament.normal_cups, 8)
    dme.write_byte(DodgeballAddresses.Tournament.hard_cups, 8)
    dme.write_byte(VolleyballAddresses.Tournament.normal_cups, 8)
    dme.write_byte(VolleyballAddresses.Tournament.hard_cups, 8)
    dme.write_byte(HockeyAddresses.Tournament.normal_cups, 8)
    dme.write_byte(HockeyAddresses.Tournament.hard_cups, 8)