# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: Adobe Photoshop for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Photoshop 2', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Lasso', 'l'),
        (0x004000, 'Shift', [Keycode.SHIFT]),
        (0x000040, 'Wand', 'w'),   # Cycle brush modes

        # 2nd row ----------
        (0x101010, 'Marq', 'M'), # Cycle rect/ellipse marquee (select)
        (0x000020, 'Trans', [Keycode.CONTROL, 't']), 
        (0x0E0007, 'Desel', [Keycode.CONTROL, 'd']),  # Brush+

        # 3rd row ----------
        (0x101010, 'Dup', [Keycode.CONTROL, 'j']),    
        (0x101010, 'Copy', [Keycode.CONTROL, 'c']),    
        (0x000040, 'Paste', [Keycode.CONTROL, 'v']),    
        
        # 4th row ----------
        (0x101010, 'Bucket', 'g'), # Cycle eyedropper/measure modes
        (0x101010, 'Move', 'v'),    # Cycle "magic wand" (selection) modes
        (0x000040, 'Enter', [Keycode.ENTER]),    # Cycle "healing" modes

        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, Keycode.ALT, 'S']) # Save As
    ]
}


"""
Extra commands
(0x101010, 'B&W', 'd'),     # Default colors
(0x101010, 'Marquee', 'M'), # Cycle rect/ellipse marquee (select)
"""

