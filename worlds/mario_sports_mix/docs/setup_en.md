# Mario Sports Mix Setup Guide

## Required Software
- [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases) (0.6.7 or newer)
- [Latest version of this APWorld](https://github.com/ElectroStarz/ArchipelagoMSM/releases)
- [Root.zip (In the releases page)](https://github.com/ElectroStarz/ArchipelagoMSM/releases)
- [Dolphin Emulator](https://dolphin-emu.org/download/?ref=btn)
- Your PAL (European) ROM of Mario Sports Mix


## How to install
### Preparations
1) Download the [latest version of Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases)
2) Download the [latest version of this APWorld](https://github.com/ElectroStarz/ArchipelagoMSM/releases) and put it in
your custom_worlds folder
3) Download [Root.zip](https://github.com/ElectroStarz/ArchipelagoMSM/releases)
4) Dump your PAL version of Mario Sports Mix - [Use this guide](https://wii.hacks.guide/dump-games) 
(Requires a modded Wii/Wii U)
5) Put the dump into a folder and set it as a game folder in Dolphin (Config -> Paths)

### Dolphin Prerequisites
1) Extract the Root.zip onto your computer, preferably to somewhere you won't delete it (Yes this can be in another
folder). Feel free to rename the root folder, just **not anything inside the root folder**.
2) Right click Mario Sports Mix and click properties, go to Gecko Codes and click 'Add New Code'. You can name it
anything, put the creator as "Saulf", go to the extracted folder and copy and paste the code in 'Gecko Code.txt' into the
code box. You **MUST** use this gecko code when playing MSM Archipelago. You can now delete the txt file.
3) Right click Mario Sports Mix and click 'Start With Riivolution Patches'. Click 'Open Riivolution XML' and open the
extracted folder and open the XML file included named 'archipelago.xml'. Now where it says 'SD Root', select the root
folder. Make sure 'File Patching' is enabled, click 'Save as Preset' and name this something like 'Mario Sports Mix
Archipelago'. Now you're ready to play!

## Read both!
### Archipelago Notes
- Make sure to use the Mario Sports Mix Client when playing MSM AP, or else it won't work!

### Dolphin notes
- Remember to have the gecko code on whenever you play AP! Enabling/Disabling it for the unmodified rom also does it for
the version we just created and vice versa!
- Your save data for AP is separated from your actual save data, so no need to back anything up!


## Creating a yaml file
### What is a yaml and why do I need one?
A yaml file tells Archipelago how it should generate your game. It may have certain options that can effect your game
like what difficulties are enabled, certain sanities, etc.

### How do I create one?
There are 2 ways of creating your yaml file. The 1st is the recommended way, while the 2nd is the less popular. 
1) Open the Archipelago Launcher and open the Options Creator. Find 'Mario Sports Mix' on the left and select your
options!
2) Open the Archipelago Launcher and click open on 'Generate Template Options'. Navigate to the Archipelago Folder and
open the Players folder, then Templates. Look for 'Mario Sports Mix.yaml' and you can manually edit your yaml using 
notepad.

## Still Having Trouble?
Ask your question in the [Mario Sports Mix Thread](https://discord.com/channels/731205301247803413/1485699253450833942)
in the [Archipelago Discord Server](https://discord.gg/archipelago)!
