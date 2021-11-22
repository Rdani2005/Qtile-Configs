from libqtile import layout
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