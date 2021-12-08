from libqtile.lazy import lazy
from libqtile.command import lazy
from libqtile.config import Key, KeyChord

mod = "mod4"

my_apps = [
    "alacritty",
    "firefox",
    "code",
    "rofi -show drun",
    "nautilus"
]

# Keymaps that i use
keys = [Key(key[0], key[1], *key[2:]) for key in [
    #---------Apps that I need--------------------
    # Terminal
    ([mod], "Return", lazy.spawn(my_apps[0])),
    # Browser and Code Editor
    ([mod], "b", lazy.spawn(my_apps[1])),
    ([mod], "c", lazy.spawn(my_apps[2])),
    # Menu App
    ([mod, "shift"], "Return", lazy.spawn(my_apps[3])),
    # File browser
    ([mod], "m", lazy.spawn(my_apps[4])),
    #----------Some Qtile Configs---------------------
    # Exit an app
    ([mod, "control"], "w", lazy.window.kill()),
    # Focus Windows
    ([mod], "Left", lazy.layout.left()),
    ([mod], "Right", lazy.layout.right()),
    ([mod], "Down", lazy.layout.down()),
    ([mod], "Up", lazy.layout.up()),
    ([mod], "space", lazy.layout.next()),
    # Move windows
    ([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    ([mod, "shift"], "Right", lazy.layout.shuffle_right()),
    ([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    ([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    #Grow windows
    ([mod, "control"], "Left", lazy.layout.grow_left()),
    ([mod, "control"], "Right", lazy.layout.grow_right()),
    ([mod, "control"], "Down", lazy.layout.grow_down()),
    ([mod, "control"], "Up", lazy.layout.grow_up()),
    ([mod, "control"], "n", lazy.layout.normalize()),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    ([mod, "control"], "Return", lazy.layout.toggle_split()),
    # Toggle between different layouts
    ([mod], "Tab", lazy.next_layout()),
    #Restart and shutdown qtile
    ([mod, "control"], "r", lazy.restart()),
    ([mod, "control"], "q", lazy.shutdown()),
    #------------Hardware configs-----------------
    ([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    ([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    ([], "XF86AudioMute", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ toggle"))
]]
