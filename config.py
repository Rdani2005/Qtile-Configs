# libraries
import os
import re
import socket
import subprocess
from typing import List
from libqtile import hook
from libqtile.lazy import lazy
from libqtile.command import lazy
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
# Data from other python files
import MyWidgets as MyWidgets
import MyPersonalKey as MyPersonalThings
import MyLayouts as MyLove
colors = MyWidgets.colors

#Essencials
mod = "mod4"
my_apps = [
    "alacritty", # terminal
    "firefox", # browser
    "code",  # code editor
    "rofi -show drun" # menu app
]

# Keys, see it on MypersonalKey.py file
keys = MyPersonalThings.init_keymaps()

# Desktop Groups that I use
def init_groups():
    list_group = [
        Group("DEV", layout="monadtall"),
        Group("WEB", layout="monadtall"),
        Group("GFX", layout="monadtall"),
        Group("SYS", layout="monadtall"),
        Group("VBOX",layout="monadtall"),
        Group("DOC", layout="monadtall"),
        Group("VIDEOS",layout="monadtall"),
        Group("CHAT", layout="monadtall"),
        Group("GAMES", layout="monadtall")
    ]
    return list_group


groups = init_groups()

# Use super + index_number to change between groups
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")

# Layouts that I use, see them on MyLayouts.py file
layouts = MyLove.init_layouts()

widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=12,
    padding=2,
    background=colors[7]
)
extension_defaults = widget_defaults.copy()

#Screen configurations
screens = [
    Screen(top=bar.Bar(MyWidgets.init_widgets_list(),opacity=1.0, size=20)),
    Screen(top=bar.Bar(MyWidgets.init_widgets_list(),opacity=1.0, size=20))
]

# Multiple screens configurations
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]


dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='Confirmation'),  # tastyworks exit box
    Match(wm_class='Qalculate!'),  # qualculate-gtk
    Match(wm_class='kdenlive'),  # kdenlive
    Match(wm_class='pinetry-gtk-2'),  # GPG Key pass entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True


wmname = "LG3D"


# Commands to use when you start the Qtile desktop. See the autostart.sh file
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
