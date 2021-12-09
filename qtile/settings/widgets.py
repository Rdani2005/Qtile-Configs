from libqtile import widget
from .theme import colors
# TODO: Make changes to this file. It is VERY long
# colors

def base_conf(fg = 'text', bg = 'dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }

def separator():
    return widget.Sep(
            **base_conf(),
            linewidth = 0,
            padding = 5
        )

def icon(fg = 'text', bg = 'dark', fontsize = 16, text = "?"):
    return widget.TextBox(
        **base_conf(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )

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

#widgets
primary_widgets = [
    *my_workspaces(),
    icon(bg="first", text=' '),
    widget.Net(**base_conf(bg='first'), interface='wlp3s0'),
    widget.CurrentLayoutIcon(**base_conf(bg='second'), scale=0.65),
    widget.CurrentLayout(**base_conf(bg='color2'), padding=5),
    icon(bg="third", fontsize=17, text=' '),
    widget.Clock(**base_conf(bg='third'), format='%d/%m/%Y - %H:%M '),
    widget.Systray(background=colors['dark'], padding=5),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 12,
    'padding': 2,

}
    
extension_defaults = widget_defaults.copy()
