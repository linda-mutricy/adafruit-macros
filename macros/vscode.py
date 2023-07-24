# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: Adapted from the VSCode application for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'VSCode', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xFFA07A, 'Del CL', [Keycode.COMMAND, Keycode.SHIFT, 'k']),
        (0x4A154B, 'Sel CL', [Keycode.COMMAND, 'l']),
        (0x4A154B, 'Sel wrd', [Keycode.COMMAND, 'd']),
        # 2nd row ----------
        (0x7CFC00, 'L up', [Keycode.OPTION, Keycode.UP_ARROW]),
        (0x36C5F0, 'Import', [Keycode.COMMAND, 'i']),
        (0xFFA07A, 'L down', [Keycode.OPTION, Keycode.UP_ARROW]),
        # 3rd row ----------
        (0x7CFC00, 'Up', [Keycode.COMMAND, Keycode.UP_ARROW]),
        (0x4A154B, 'Sel all', [Keycode.COMMAND, 'd', Keycode.OPTION, Keycode.ENTER]),
        (0xFFA07A, 'Down', [Keycode.COMMAND, Keycode.DOWN_ARROW]),
        # 4th row ----------
        (0x7CFC00, 'Outdent', [Keycode.COMMAND, Keycode.LEFT_BRACKET]),
        (0xECB22E, 'Find', [Keycode.COMMAND, 'f']),
        (0xFFA07A, 'Indent', [Keycode.COMMAND, Keycode.RIGHT_BRACKET]),
        # Encoder button ---
        (0x000000, 'Save', [Keycode.COMMAND, 's'])
    ]
}
