# Named msm_settings due to naming conflicts with settings

import os
import shutil
from pathlib import Path
from typing import Union, Sequence, Any

import Utils
from Utils import T
import settings


class MSMSettings(settings.Group):
    settings_key = "mario_sports_mix_settings"

    class AutoOpenMSM(settings.Bool):
        """Enabling this will automatically open Mario Sports Mix when opening the client.
        Automatically patches the roster when opening"""

    class MSMISOPath(settings.UserFilePath):
        """A path to your Mario Sports Mix ISO file

        If your game is not an ISO you can convert it in Dolphin by right-clicking -> Convert File and then select ISO"""
        is_exe = False
        required = True

        def browse(self: T, filetypes: Sequence[tuple[str, Sequence[str]]] | None = None, **kwargs: Any) -> T | None:
            if filetypes is None:
                filetypes = [("ISO File", ".iso")]

            return super().browse(filetypes, **kwargs)


    class DolphinExePath(settings.UserFilePath):
        """A path to your installation of Dolphin Emulator"""
        is_exe = True
        required = True

        def browse(self, filetypes=None, **kwargs):
            from Utils import is_windows

            # Set up the file filter based on the operating system
            if not filetypes:
                # Windows uses .exe, macOS uses .app (or no extension for Linux binaries)
                valid_exts = [".exe"] if is_windows else ["", ".app"]
                filetypes = [("Dolphin Emulator", valid_exts)]

            return super().browse(filetypes, **kwargs)


    auto_open: AutoOpenMSM | bool = False
    msm_iso_path: MSMISOPath | str = MSMISOPath("mario_sports_mix.iso")
    dolphin_exe_path: DolphinExePath | str = DolphinExePath("dolphin.exe")