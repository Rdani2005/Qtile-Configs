#-------- Libraries ----------
from libqtile import widget
from .theme import colors
# REMEMBER TO INSTALL NERD-FONTS
# yay -S nerd-fonts-ubuntu-mono
# ------------- Methods ---------
# Return a basic config
def base_conf(fg = 'text', bg = 'dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }
# Returns a sep between widgets
def separator():
    return widget.Sep(
            **base_conf(),
            linewidth = 0,
            padding = 5
        )

# Returns the icons used for widgets
def icon(fg = 'text', bg = 'dark', fontsize = 16, text = "?"):
    return widget.TextBox(
        **base_conf(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )

# Returns the beginning of the widgets group
def beggining(fg = 'first', bg='dark'):
    return widget.TextBox(
        **base_conf(fg, bg),
        fontsize = 30,
        padding = -2,
        text=""
    )
# Stopped using this, but I'll consider if using this or not in a future
# def end_widget_group(fg = 'first', bg='dark'):
#     return widget.TextBox(
#         **base_conf(fg, bg),
#         fontsize = 30,
#         padding = -1.8,
#         text=""
#     )
# Returns the workspace that I need
def my_workspaces():
    return [
        separator(),
        widget.GroupBox(
            **base_conf(fg='light'),
            font="UbuntuMono Nerd Font",
            fontsize = 20,
            margin_y = 3,
            margin_x = 0,
            padding_y = 5,
            padding_x = 3,
            border_width = 2,
            active = colors['active'],
            inactive = colors['inactive'],
            highlight_method = "block",
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey']
        ),
        separator(),
        widget.WindowName(**base_conf(fg='focus'), fontsize=14, padding=5),
        separator()
    ]

#------------ Widget List ------------------------
# Main widgets (used for the main screen)
primary_widgets = [
    separator(),
    *my_workspaces(),
    # First Group (battery, updates)
    beggining(),
    icon(bg="first", fontsize=17, text="⟳"),
    widget.CheckUpdates(
        **base_conf(bg='first'),
        update_interval = 1800,
        distro = "Arch_checkupdates",
        display_format="{updates} Updates",
        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty' + ' -e sudo pacman -Syu')}
    ),
    icon(bg="first", fontsize=17, text="  "),
    widget.Battery(**base_conf(bg="first"), padding=5),
    # Second Group (layout)
    beggining(fg = 'second', bg = 'first'),
    widget.CurrentLayoutIcon(**base_conf(bg='second'), scale=0.65),
    widget.CurrentLayout(**base_conf(bg='second'), padding=5),
    beggining(fg = 'third', bg = 'second'),
    icon(bg="third", fontsize=17, text=' '),
    widget.Clock(**base_conf(bg='third'), format='%d/%m/%Y - %H:%M '),
    # third group (system info)
    beggining(fg='dark', bg='third'),
    widget.Systray(background=colors['dark'], padding=5),
    separator(),
]
# Secundary widgets (used for external screen settings)
secundary_widgets = [
    separator(),
    *my_workspaces(),
    beggining(fg = 'first', bg = 'dark'),
    widget.CPU(**base_conf(bg="first")),
    icon(bg = "first", fontsize=20, text=' '),
    widget.Memory(**base_conf(bg='first')),
    beggining(fg = 'second', bg = 'first'),
    widget.CurrentLayoutIcon(**base_conf(bg='second'), scale=0.65),
    widget.CurrentLayout(**base_conf(bg='second'), padding=5),
    beggining(fg = 'third', bg = 'second'),
    icon(bg="third", fontsize=17, text=' '),
    widget.Clock(**base_conf(bg='third'), format='%d/%m/%Y - %H:%M '),
    separator(),
]
# Defaults widgets
widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 12,
    'padding': 2,

}
# I don't know why Qtile needs this
extension_defaults = widget_defaults.copy()
