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


colors = MyWidgets.colors
#Essencials
mod = "mod4"
# terminal = 'alacritty'
# browser = "firefox"
# code_editor = "code"
# menu_app = "rofi -show drun"
my_apps = [
    "alacritty", # terminal
    "firefox", # browser
    "code",  # code editor
    "rofi -show drun" # menu app
]
keys = MyPersonalThings.init_keymaps()

#Groups
groups = [
    Group("DEV", layout="monadtall"),
    Group("WEB", layout="monadtall"),
    Group("GFX", layout="monadtall"),
    Group("SYS", layout="monadtall"),
    Group("VBOX", layout="monadtall"),
    Group("DOC", layout="monadtall"),
    Group("VIDEOS", layout="monadtall"),
    Group("CHAT", layout="monadtall")
]

from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")



layout_theme = {
    "border_width": 2,
    "margin": 7,
    "border_focus":"#062f5e",
    "border_normal":"1D2330"
}

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    layout.MonadTall(**layout_theme),
]

widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=12,
    padding=2,
    background=colors[7]
)
extension_defaults = widget_defaults.copy()

screens = [Screen(top=bar.Bar(MyWidgets.init_widgets_list(),20))]

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
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
