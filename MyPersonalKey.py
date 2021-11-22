from libqtile.lazy import lazy
from libqtile.command import lazy
from libqtile.config import Key, KeyChord

mod = "mod4"

my_apps = [
    "alacritty",
    "firefox",
    "code",
    "rofi -show drun"
]

# Keymaps that i use
def init_keymaps():
    keys_list = [
        # Terminal
        Key([mod], "Return", lazy.spawn(my_apps[0]), desc="Launch terminal"),
        # Apps
        Key([mod], "b", lazy.spawn(my_apps[1]), desc="Open a browser"),
        Key([mod], "c", lazy.spawn(my_apps[2]), desc="Open code editor"),
        # menu app
        Key([mod, "shift"], "Return", lazy.spawn(my_apps[3]), desc="Open menu app"),
        #Kill the process
        Key([mod, "control"], "w", lazy.window.kill(), desc="Kill focused window"),
        
        # Switch between windows
        Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
        Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

        # Move windows
        Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
        Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
        Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
        #Grow Windows
        Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        Key([mod, "control"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
        # Toggle between different layouts as defined below
        Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        #Restart and shutdown qtile
        Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    ]
    return keys_list