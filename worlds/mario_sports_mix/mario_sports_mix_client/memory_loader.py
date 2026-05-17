import importlib
from . import dolphin_connection

memory = None

def load_memory_module():
    global memory

    if dolphin_connection.GAME_VERSION == "PAL":
        memory = importlib.import_module(
            ".memory_addresses",
            package=__package__
        )

    elif dolphin_connection.GAME_VERSION == "NTSC-U":
        memory = importlib.import_module(
            ".memory_addresses_ntscu",
            package=__package__
        )

    else:
        raise ValueError(
            f"Unsupported GAME_VERSION: {dolphin_connection.GAME_VERSION}"
        )