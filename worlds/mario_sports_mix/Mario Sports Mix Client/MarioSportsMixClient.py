import asyncio
import dolphin_memory_engine as dme
from collections import deque
import time
import threading
import logging
import utils
from CommonClient import (
    ClientCommandProcessor,
    CommonContext,
    logger,
    server_loop,
    gui_enabled,
    get_base_parser,
)

def connect_to_dolphin():
    """
    Basic task loop for connecting to dolphin
    """
    attempt = 1
    logger.info("Connecting to dolphin, use /dolphin for status info")
    while True:
        dme.hook()
        logger.info(f"Attempting to connect to dolphin, attempt {attempt}")
        if dme.is_hooked():
            logger.info("Connected to dolphin!")
            break
        else:
            logger.info("Failed to connect, retrying in 5 seconds")
            time.sleep(5)
            attempt += 1

connect_to_dolphin()