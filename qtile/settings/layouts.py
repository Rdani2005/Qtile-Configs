from libqtile import layout
from libqtile.config import Match
# Config use for the Layouts
layout_theme = {
    "border_width": 2,
    "margin": 7,
    "border_focus":"#062f5e",
    "border_normal":"1D2330"
}

# Layouts that I use
def init_layouts():
    layout_list = [
        layout.Columns(**layout_theme),
        layout.Max(**layout_theme),
        layout.MonadTall(**layout_theme),
        layout.Bsp(**layout_theme),
        layout.TreeTab(
            font = "Ubuntu",
            fontsize = 12,
            sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
            section_fontsize = 16,
            bg_color = "#111211",
            active_bg = "#3630f0",
            inactive_bg = "#111211",
            inactive_foreground = "#2f5c27",
            panel_width = 200

        )
    ]

    return layout_list

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.TreeTab(
        font = "Ubuntu",
        fontsize = 12,
        sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
        section_fontsize = 16,
        bg_color = "#111211",
        active_bg = "#3630f0",
        inactive_bg = "#111211",
        inactive_foreground = "#2f5c27",
        panel_width = 200

    )
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='Confirmation'),  # tastyworks exit box
    Match(wm_class='Qalculate!'),  # qualculate-gtk
    Match(wm_class='kdenlive'),  # kdenlive
    Match(wm_class='pinetry-gtk-2'),  # GPG Key pass entry
]) 