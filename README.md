# i3-wm-config by benkaiser

This is my configuration for the i3 window manager.

Uses terminator as the terminal.

I would recommend just copying parts of my config (as certain parts, such as the start up config, may be irrelevent to you). However my workspace_controller.py script is universal.

# Keyboard Shortcuts

Mod Key: Alt key (Mod1)

## i3 keys
Mod + Shift + v = Reload i3 configuration file
Mod + Shift + r = Restart i3 (reload )
Mod + Shift + e = Exit i3

## Applications
Mod + Enter = Terminal
Mod + p = Run dmenu (with mods to open application in the current space)

## Window Operations
Mod + Shift + c = Kill current window
Mod + f = Make current window fullscreen
Mod + g = Make current window fullscreen (across all monitors)
Mod + Shift + space = Make window floating
Mod + y = Move workspace to output left (on dual monitor this is enough to switch between the two)

(my block modifications apply to the following mods)

Mod + Shift + 1 = Move window to workspace 1 in block
Mod + Shift + 2 = Move window to workspace 2 in block
Mod + Shift + 3 = Move window to workspace 3 in block
Mod + Shift + 4 = Move window to workspace 4 in block
Mod + Shift + 5 = Move window to workspace 5 in block
Mod + Shift + 6 = Move window to workspace 6 in block
Mod + Shift + 7 = Move window to workspace 7 in block
Mod + Shift + 8 = Move window to workspace 8 in block
Mod + Shift + 9 = Move window to workspace 9 in block
Mod + Shift + 0 = Move window to workspace 0 in block

Mod + Shift + t = Move window to specific workspace with dmenu (dynamic tiling)

Mod + r = Resize window

## Navigation
Mod + j = Focus window to the left
Mod + k = Focus window down
Mod + l = Focus window up
Mod + ; = Focus window to the right

(my block modifications apply to the following mods)

Mod + 1 = Switch to workspace 1 in block
Mod + 2 = Switch to workspace 2 in block
Mod + 3 = Switch to workspace 3 in block
Mod + 4 = Switch to workspace 4 in block
Mod + 5 = Switch to workspace 5 in block
Mod + 6 = Switch to workspace 6 in block
Mod + 7 = Switch to workspace 7 in block
Mod + 8 = Switch to workspace 8 in block
Mod + 9 = Switch to workspace 9 in block
Mod + 0 = Switch to workspace 0 in block

Mod + t = Jump to specific workspace with dmenu (dynamic tiling)

## Layouts
Mod + h = Split horizontal layout
Mod + v = Split vertical layout
Mod + s = Stacking layout
Mod + w = Tabbed layout
Mod + e = Default layout
Mod + space = Toggle between floating/tiling layers

## System Manipulation
Volume Decrease Key (varies on keyboard) / XF86AudioLowerVolume = Lower volume by 2%
Volume Increase Key (varies on keyboard) / XF86AudioRaiseVolume = Raise volume by 2%
Volume Mute Key (varies on keyboard) / XF86AudioMute = Mute volume

## Block Modifications
Mod + Left = Switch to workspace -1 (e.g. 1 to 0)
Mod + Right = Switch to workspace +1 (e.g 1 to 2)
Mod + Up = Switch to workspace +10 (e.g 1 to 11)
Mod + Down = Switch to workspace -10 (e.g 1 to -9)

The blocks refer to blocks of 10, so if you were on workspace 15 and pressed `Mod + 2` you would move to 12. The same applies to `Mod + Shift + 2` except it moves the window to the selected workspace.

## Other Modifications
Custom color scheme centering around my favourite color #44bbff.
Custom status bar, showing suspend, screensaver and sleep buttons.
