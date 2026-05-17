import importlib
from . import dolphin_connection

def load_memory_module():
    if dolphin_connection.GAME_VERSION == "PAL":
        module = importlib.import_module(
            ".memory_addresses",
            package=__package__
        )

    elif dolphin_connection.GAME_VERSION == "NTSC-U":
        module = importlib.import_module(
            ".memory_addresses_ntscu",
            package=__package__
        )

    else:
        raise RuntimeError(
            f"Unsupported GAME_VERSION: {dolphin_connection.GAME_VERSION}"
        )

    globals().update(vars(module))