# ----------------- Libraries -----------------
from libqtile import layout
from libqtile.config import Match
from .theme import colors
# Config use for the Layouts
layout_theme = {
    "border_width": 1,
    "margin": 7,
    "border_focus":colors['focus'],
    "border_normal":colors['dark']
}

# ----------- Layouts that I use -------------------
layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Columns(**layout_theme),
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

# Configs for floating layouts (I don't use them)
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='Confirmation'),
    Match(wm_class='Qalculate!'), 
    Match(wm_class='kdenlive'),  
    Match(wm_class='pinetry-gtk-2'),
]) 