import importlib
from typing import Any

from . import dolphin_connection

# These names are filled after Dolphin's game ID tells us which region is running.
PlayerAddresses: Any = None
OpponentAddresses: Any = None
MatchAddresses: Any = None
BossAddresses: Any = None
BasketballAddresses: Any = None
DodgeballAddresses: Any = None
VolleyballAddresses: Any = None
HockeyAddresses: Any = None
SportsMixAddresses: Any = None
Offsets: Any = None

_ADDRESS_CLASSES = (
    "PlayerAddresses",
    "OpponentAddresses",
    "MatchAddresses",
    "BossAddresses",
    "BasketballAddresses",
    "DodgeballAddresses",
    "VolleyballAddresses",
    "HockeyAddresses",
    "SportsMixAddresses",
    "Offsets",
)

_loaded_game_version = None


def is_memory_loaded() -> bool:
    return dolphin_connection.GAME_VERSION is not None and _loaded_game_version == dolphin_connection.GAME_VERSION


def load_memory_module() -> None:
    global _loaded_game_version

    if dolphin_connection.GAME_VERSION == "PAL":
        module_name = ".memory_addresses_pal"
    elif dolphin_connection.GAME_VERSION == "NTSC-U":
        module_name = ".memory_addresses_ntscu"
    else:
        raise RuntimeError(f"Unsupported GAME_VERSION: {dolphin_connection.GAME_VERSION}")

    module = importlib.import_module(module_name, package=__package__)

    # Callers should use `import memory_loader as ml`; replacing these module
    # globals then updates every future `ml.PlayerAddresses` lookup.
    for name in _ADDRESS_CLASSES:
        globals()[name] = getattr(module, name)

    _loaded_game_version = dolphin_connection.GAME_VERSION
