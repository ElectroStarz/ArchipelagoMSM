from logging import Logger
from typing import Any
import subprocess
import time
import dolphin_memory_engine as dme
import MSMFunctions

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

    def attempt_to_hook(self):
        attempt = 1
        while True:
            if not self.dme.is_hooked():
                print(f"Attempting to connect to Dolphin... Attempt {attempt}.")
                time.sleep(0.5)
                self.dme.hook()

                if self.dme.is_hooked():
                    print("Successfully hooked to Dolphin!")
                    break

                # Is the emulator open?
                if self.check_for_dolphin() == 0:
                    print("Failed to connect. Make sure you're running Dolphin! Retrying in 5 seconds...")
                    attempt += 1
                    time.sleep(5)
                elif self.check_for_dolphin() == 1:
                    print("Failed to connect. Are you running the game? Retrying in 5 seconds...")
                    attempt += 1
                    time.sleep(5)
                elif self.check_for_dolphin() == 2:
                    print("More than one instance of Dolphin is running! Retrying in 5 seconds...")
                    attempt += 1
                    time.sleep(5)
                else:
                    break
            else:
                # Already hooked
                break

    def is_hooked(self):
        try:
            self.dme.is_hooked()
        except DolphinException:
            return False

    def disconnect(self):
        if self.is_hooked():
            self.dme.un_hook()

    def read_byte(self, address: Any) -> Any:
        self.is_hooked()
        result = self.dme.read_byte(address)
        return result

    def read_bytes(self, address: Any, bytes_to_read: int) -> Any:
        self.is_hooked()
        result = self.dme.read_bytes(address, bytes_to_read)
        return result

    def read_word(self, address: Any) -> Any:
        self.is_hooked()
        result = self.dme.read_word(address)
        return result

    def read_float(self, address: Any) -> Any:
        self.is_hooked()
        result = self.dme.read_float(address)
        return result

    def read_string(self, address: Any) -> Any:
        self.is_hooked()
        byte = self.dme.read_bytes(address, 5)
        string = byte.decode("utf-8")
        return string

    def write_string(self, address: Any) -> Any:
        self.is_hooked()
        string = ""
        encoded = string.encode("utf-8")
        self.dme.write_byte(address, encoded)

    def write_byte(self, address: Any, data: Any):
        self.is_hooked()
        result = self.dme.write_byte(address, data)
        return result

    def write_bytes(self, address: Any, data: Any) -> Any:
        self.is_hooked()
        result = self.dme.write_bytes(address, data)
        return result

    def write_float(self, address: Any, data: Any):
        self.is_hooked()
        result = self.dme.write_float(address, data)
        return result

    def write_word(self, address: Any, data: Any):
        self.is_hooked()
        result = self.dme.write_word(address, data)
        return result