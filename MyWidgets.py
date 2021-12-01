from libqtile import widget
# TODO: Make changes to this file. It is VERY long
# colors
colors = [
    "#26c70a", # group text active color
    "#2f5c27", # group text inactive color
    "#3630f0", # first widget group color
    "#831fc2", # second widget group color
    "#f20cf2", # third widget group color
    "#f20c17", # fourth widget group color
    "#ffffff", # text color
    "#111211"  # Bar color
]
#widgets
def init_widgets_list():
    widget_list = [
        widget.Sep(
            linewidth = 0,
            padding = 6,
            foreground=colors[2],
            background=colors[7]
        ),
        widget.GroupBox(
            font="Ubuntu Bold",
            fontsize = 10,
            margin_y = 3,
            margin_x = 0,
            padding_y = 5,
            padding_x = 3,
            border_width = 3,
            active = colors[0],
            highlight_color = colors[7],
            highlight_method = "line",
            inactive = colors[1],
            foreground=colors[2],
            background=colors[7]
        ),
        widget.Sep(
            linewidth = 0,
            padding = 40,
            foreground=colors[2],
            background=colors[7]
        ),
                
        widget.WindowName(
            foreground=colors[2],
            background=colors[7],
            padding = 10
        ),
                
        widget.Systray(
            icon_size = 15,
            background = colors[7]
        ),
        widget.Sep(
            linewidth = 0,
            padding = 6,
            foreground=colors[2],
            background=colors[7]
        ),
        #beggining of first group of icons
        widget.TextBox(
            text = "",
            fontsize = 30,
            foreground = colors[2],
            background = colors[7],
            padding = -6
        ),
        widget.TextBox(
            foreground = colors[6],
            background = colors[2],
            fontsize = 15,
            text=""
        ),
        widget.ThermalSensor(
            foreground = colors[6],
            background = colors[2],
            threshold = 70,
            tag_sensor = "Core 0",
            fmt = "T1: {}",
            fontsize = 10
        ),
        widget.ThermalSensor(
            foreground = colors[6],
            background = colors[2],
            threshold = 70,
            tag_sensor = "Core 1",
            fmt = "T2: {}",
            fontsize = 10
        ),
        widget.TextBox(
            text = "",
            fontsize = 20,
            foreground = colors[6],
            background = colors[2],
            padding = 0
        ),

        widget.Memory(
            foreground = colors[6],
            background = colors[2]
        ),
        widget.TextBox(
            fontsize = 30,
            foreground = colors[2],
            background = colors[2],
        ),
        #end of first group of icons
                
        #Beggining of the second group of icons
        widget.TextBox(
            fontsize = 30,
            foreground = colors[3],
            background = colors[3],
        ),
        widget.TextBox(
            foreground = colors[6],
            background = colors[3],
            fontsize = 10,
            text=""
        ),
        widget.Clock(
            format='%I:%M %p %a %d', 
            background=colors[3]
        ),
        widget.TextBox(
                    
            fontsize = 30,
            foreground = colors[3],
            background = colors[3],
                    
        ),
        # End of the second group of  icons
        widget.TextBox(
            fontsize = 30,
            foreground = colors[4],
            background = colors[4],
        ),
        widget.TextBox(
            foreground = colors[6],
            background = colors[4],
            fontsize = 15,
            text="龍"
        ),
        
        widget.Net(
            fontsize = 10,
            background = colors[4],
            format = 'Network: {down} ↓↑ {up}'
            
        ),

        widget.TextBox(
            fontsize = 30,
            foreground = colors[4],
            background = colors[4],
        ),
        # Beggining of the third group of icons
        widget.TextBox(
            fontsize = 30,
            foreground = colors[5],
            background = colors[5],
        ),

        widget.TextBox(
            foreground = colors[6],
            background = colors[5],
            fontsize = 15,
            text=""
        ),
        widget.CurrentLayout(
            background = colors[5]
        ),
        widget.TextBox(                  
            fontsize = 30,
            foreground = colors[5],
            background = colors[5],                  
        ),
        widget.TextBox(
            fontsize = 30,
            foreground = colors[5],
            background = colors[5],
        ),
    ]
    return widget_list

