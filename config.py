# libraries
import os
import re
import subprocess
from libqtile import hook, qtile
# -------Changes----------
from settings.keys import mod, keys
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.mouse import mouse
from settings.screens import screens
from settings.widgets import widget_defaults, extension_defaults
# Use super + index_number to change between groups
# Use super + shift + index_number to send the window to a diferent group
# Use super + control + index_number to change the group order
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")
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


# Screen configurations
# This is made for using two screens


# This is very important for me!
# Commands to use when you start the Qtile desktop. See the autostart.sh file
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
