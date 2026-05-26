from logging import Logger
from typing import Any
import sys
import psutil
import dolphin_memory_engine as dme
import asyncio


GAME_VERSION = None

class DolphinException(Exception):
    pass

class DolphinClient:
    def __init__(self, logger: Logger):
        self.dme = dme
        self.logger = logger
        self.attempt = 1
        self.told_region = False

    @staticmethod
    def check_for_dolphin():
        # Determine the expected executable name based on the OS
        # Windows uses Dolphin.exe, while Mac/Linux use lowercase 'dolphin'
        if sys.platform == "win32":
            target_process = "dolphin.exe"
        else:
            target_process = "dolphin"

        dolphin_count = 0

        # Iterate through all running processes across the OS
        for proc in psutil.process_iter(['name']):
            try:
                # Lowercase comparison to avoid case-sensitivity issues across different OS environments
                if proc.info['name'] and proc.info['name'].lower() == target_process:
                    dolphin_count += 1
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

        if dolphin_count > 1:
            return 2
        elif dolphin_count == 1:
            return 1
        else:
            return 0


    async def attempt_to_hook(self):
        if not self.dme.is_hooked():
            self.logger.info(f"Attempting to hook: Attempt {self.attempt}")
            self.dme.hook()

        if self.dme.is_hooked():
            self.logger.info("Hooked successfully!")
            self.attempt = 1  # Reset counter on success
        else:
            dolphin_status = self.check_for_dolphin()

            if dolphin_status == 0:
                self.logger.info("Failed to hook! Dolphin isn't running!")
            elif dolphin_status == 1:
                self.logger.info("Failed to hook! Mario Sports Mix isn't running!")
            elif dolphin_status == 2:
                self.logger.info("Failed to hook! Too many Dolphin instances are running!")

            self.attempt += 1
            await asyncio.sleep(5)

    def check_region(self):
        global GAME_VERSION

        byte = self.read_bytes(0x80000000, 6)
        decoded = byte.decode("utf-8", errors="ignore")

        if decoded == "RMKP01":
            detected_version = "PAL"
        elif decoded == "RMKE01":
            detected_version = "NTSC-U"
        else:
            GAME_VERSION = None
            self.told_region = False
            self.logger.info(f"Unsupported or unreadable game ID: {decoded!r}")
            return False

        if GAME_VERSION != detected_version:
            self.told_region = False

        GAME_VERSION = detected_version
        if not self.told_region:
            self.logger.info(f"{detected_version} Detected!")
            self.told_region = True

        return True



    def is_hooked_class(self):
        if self.dme.is_hooked():
            return True
        else:
            return False

    def disconnect(self):
        global GAME_VERSION

        if self.dme.is_hooked():
            self.dme.un_hook()
        GAME_VERSION = None
        self.told_region = False

    def read_byte(self, address: Any) -> Any:
        self.dme.is_hooked()
        result = self.dme.read_byte(address)
        return result

    def read_bytes(self, address: Any, bytes_to_read: int) -> Any:
        self.dme.is_hooked()
        result = self.dme.read_bytes(address, bytes_to_read)
        return result

    def read_word(self, address: Any) -> Any:
        self.dme.is_hooked()
        result = self.dme.read_word(address)
        return result

    def read_float(self, address: Any) -> Any:
        self.dme.is_hooked()
        result = self.dme.read_float(address)
        return result

    def read_string(self, address: int) -> str:
        self.dme.is_hooked()
        byte = self.dme.read_bytes(address, 5)
        # Decode and strip out the invisible null bytes
        decoded = byte.decode("utf-8", errors="ignore").rstrip('\x00')
        return decoded

    def write_string(self, address: Any, string: str) -> Any:
        self.dme.is_hooked()
        encoded = string.encode("utf-8")
        self.dme.write_byte(address, encoded)

    def write_byte(self, address: Any, data: Any):
        self.dme.is_hooked()
        self.dme.write_byte(address, data)

    def write_bytes(self, address: Any, data: Any) -> Any:
        self.dme.is_hooked()
        self.dme.write_bytes(address, data)

    def write_float(self, address: Any, data: Any):
        self.dme.is_hooked()
        self.dme.write_float(address, data)

    def write_word(self, address: Any, data: Any):
        self.dme.is_hooked()
        self.dme.write_word(address, data)

    def follow_pointers(self, address: Any, pointers: list):
        self.dme.is_hooked()
        result = self.dme.follow_pointers(address, list(pointers))
        return result
