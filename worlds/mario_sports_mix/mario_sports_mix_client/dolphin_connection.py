from logging import Logger
from typing import Any
import subprocess
import dolphin_memory_engine as dme
import asyncio




class DolphinException(Exception):
    pass

class DolphinClient:
    def __init__(self, logger: Logger):
        self.dme = dme
        self.logger = logger

    @staticmethod
    def check_for_dolphin():
        cmd = 'tasklist /FI "IMAGENAME eq Dolphin.exe"'
        output = subprocess.check_output(cmd, shell=True).decode()
        dolphin_amount = output.count("Dolphin.exe")

        if "Dolphin.exe" in output:
            if dolphin_amount > 1:
                return 2
            else:
                return 1
        else:
            return 0

    attempt = 1

    async def attempt_to_hook(self):
        # Only hook if not already hooked
        if not self.dme.is_hooked():
            self.logger.info(f"Attempting to hook: Attempt {self.attempt}")
            await asyncio.sleep(1)
            self.dme.hook()

        if self.dme.is_hooked():
            self.logger.info("Hooked successfully!")
        else:
            if self.check_for_dolphin() == 0:
                self.logger.info("Failed to hook! Dolphin isn't running!")
                self.attempt += 1
                await asyncio.sleep(3)
            elif self.check_for_dolphin() == 1:
                self.logger.info("Failed to hook! Mario Sports Mix isn't running!")
                self.attempt += 1
                await asyncio.sleep(3)
            elif self.check_for_dolphin() == 2:
                self.logger.info("Failed to hook! Too many Dolphin are running!")
                self.attempt += 1
                await asyncio.sleep(3)


    def is_hooked_class(self):
        if self.dme.is_hooked():
            return True
        else:
            return False


    def disconnect(self):
        if self.dme.is_hooked():
            self.dme.un_hook()

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

    def read_string(self, address: Any) -> Any:
        self.dme.is_hooked()
        byte = self.dme.read_bytes(address, 5)
        string = byte.decode("utf-8")
        return string

    def write_string(self, address: Any) -> Any:
        self.dme.is_hooked()
        string = ""
        encoded = string.encode("utf-8")
        self.dme.write_byte(address, encoded)

    def write_byte(self, address: Any, data: Any):
        self.dme.is_hooked()
        result = self.dme.write_byte(address, data)
        return result

    def write_bytes(self, address: Any, data: Any) -> Any:
        self.dme.is_hooked()
        result = self.dme.write_bytes(address, data)
        return result

    def write_float(self, address: Any, data: Any):
        self.dme.is_hooked()
        result = self.dme.write_float(address, data)
        return result

    def write_word(self, address: Any, data: Any):
        self.dme.is_hooked()
        result = self.dme.write_word(address, data)
        return result

    def follow_pointers(self, address: Any, pointers: list):
        self.dme.is_hooked()
        result = self.dme.follow_pointers(address, list(pointers))
        return result