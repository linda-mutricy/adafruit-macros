# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: Adapted from the Evernote web application for Mac
# Contributed by Redditor s010sdc

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Mac Slack', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x4A154B, 'New Nt', [Keycode.COMMAND, 'n']),
        (0x4A154B, 'New Bk', [Keycode.SHIFT, Keycode.COMMAND, 'n']),
        (0x4A154B, 'CP Lnk', [Keycode.CONTROL, Keycode.OPTION, Keycode.COMMAND, 'c']),
        # 2nd row ----------
        (0x36C5F0, 'Move', [Keycode.CONTROL, Keycode.COMMAND, 'm']),
        (0x36C5F0, 'Find', [Keycode.OPTION, Keycode.COMMAND, 'f']),
        (0x36C5F0, 'Emoji', [Keycode.CONTROL, Keycode.COMMAND, ' ']),
        # 3rd row ----------
        (0x2EB67D, 'Bullets', [Keycode.SHIFT, Keycode.COMMAND, 'u']),
        (0x2EB67D, 'Nums', [Keycode.SHIFT, Keycode.COMMAND, 'o']),
        (0x2EB67D, 'Check', [Keycode.SHIFT, Keycode.COMMAND, 't']),
        # 4th row ----------
        (0xECB22E, 'Date', [Keycode.SHIFT, Keycode.COMMAND, 'D']),
        (0xECB22E, 'Time', [Keycode.OPTION, Keycode.SHIFT, Keycode.COMMAND, 'D']),
        (0xECB22E, 'Divider', [Keycode.SHIFT, Keycode.COMMAND, 'H']),
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
