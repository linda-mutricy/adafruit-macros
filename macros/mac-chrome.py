# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: web browser for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Mac Chrome', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'FB MSG', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                           'https://www.facebook.com/messages\n']),
        (0x800000, 'Cal', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                            'calendar.google.com\n']),
        (0x101010, 'Email', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                             'https://mail.google.com/mail/u/0/\n']),
        # 2nd row ----------
        (0x000040, 'Reload', [Keycode.COMMAND, 'r']),
        (0x000040, 'Home', [Keycode.COMMAND, 'H']),
        (0x000040, 'New', [Keycode.COMMAND, 't']),
        # 3rd row ----------
        (0x004000, '< Back', [Keycode.COMMAND, '[']),
        (0x004000, 'Fwd >', [Keycode.COMMAND, ']']),
        (0x400000, 'Up', [Keycode.SHIFT, Keycode.UP_ARROW]),      # Scroll up
        # 4th row ----------
        (0x202000, '< Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x202000, 'Tab >', [Keycode.CONTROL, Keycode.TAB]),
        (0x400000, 'Down', [Keycode.SPACE]),                     # Scroll down
        # Encoder button ---
        (0x000000, 'close', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
