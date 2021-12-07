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
from libqtile.config import Click, Drag, Group, Match, Screen
# Data from other python files
import MyPersonalGroups as MyWorkspace
import MouseConfigs as ExtrasConfigs
import MyWidgets as MyWidgets
import MyLayouts as MyLove


# -------Changes----------
from settings.keys import mod, keys
# Declaration of using the super key


# Keys, see it on MypersonalKey.py file


# Layouts that I use, see them on MyLayouts.py file
layouts = MyLove.init_layouts()

# Desktop Groups that I use. See them on MyPersonalGroups.py file
groups = MyWorkspace.init_groups()

# Use super + index_number to change between groups
# Use super + shift + index_number to send the window to a diferent group
# Use super + control + index_number to change the group order
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")


widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=12,
    padding=2,
    background="#111211"
)
extension_defaults = widget_defaults.copy()

# Screen configurations
# This is made for using two screens
screens = [
    Screen(top=bar.Bar(MyWidgets.init_widgets_list(),opacity=1.0, size=20)),
    Screen(top=bar.Bar(MyWidgets.init_widgets_list(),opacity=1.0, size=20))
]
# trash configs ;)
dgroups_app_rules = [] 
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
# Honestly, I love using stremio and youtube on fullscreen, 
# so this is very important. ;)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"

# Should we use floating layouts on Qtile?
# Honestly, I don't use them, but I'll leave it here.
# Nobody knows when it can be useful
# See the MouseConfigs.py file
mouse = ExtrasConfigs.UsingMouseLayouts()
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='Confirmation'),  # tastyworks exit box
    Match(wm_class='Qalculate!'),  # qualculate-gtk
    Match(wm_class='kdenlive'),  # kdenlive
    Match(wm_class='pinetry-gtk-2'),  # GPG Key pass entry
]) # I prefer using Qtile as it is,
   # a tiling window manager. It is more productive without the floating layouts.

# This is very important for me!
# Commands to use when you start the Qtile desktop. See the autostart.sh file
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
