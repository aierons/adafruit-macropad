# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Browser', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x0de05e, 'Cut', [Keycode.CONTROL, 'x']),
        (0x0de05e, 'Copy', [Keycode.CONTROL, 'c']),
        (0x0de05e, 'Paste', [Keycode.CONTROL, 'v']),

        # 2nd row ----------
        (0x0de05e, 'Undo', [Keycode.CONTROL, 'z']),
        (0x004000, 'Back', [Keycode.ALT, Keycode.LEFT_ARROW]),
        (0x004000, 'Fwd', [Keycode.ALT, Keycode.RIGHT_ARROW]),

        # 3rd row ----------
        (0x000040, 'Reload', [Keycode.CONTROL, 'r']),
        (0x095E06, '< Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x095E06, 'Tab >', [Keycode.CONTROL, Keycode.TAB]),

        # 4th row ----------
        (0x770de0, 'Tab+', [Keycode.CONTROL, 't']), # New Tab
        (0x770de0, 'Win+', [Keycode.CONTROL, 'n']), # New Window
        (0x000040, 'Private', [Keycode.CONTROL, 'N']),

        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close tab
    ]
}


"""
Extra commands
(0x202000, 'Size-', [Keycode.CONTROL, Keycode.KEYPAD_MINUS]),
(0x202000, 'Size +', [Keycode.CONTROL, Keycode.KEYPAD_PLUS]),
(0x400000, 'Up', [Keycode.SHIFT, ' ']),      # Scroll up
(0x400000, 'Down', ' '),                     # Scroll down
(0x0de05e, 'Select All', [Keycode.CONTROL, 'a']), #Select All
"""
