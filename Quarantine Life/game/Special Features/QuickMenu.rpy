screen quickMenu:
    zorder 1
    layer "screens"
    frame:
        background "gui/quick/quickcontain.png"
        at transform:
            xanchor 0.5
            yanchor 0.0
            xpos 0.03
            ypos 0.15
            yoffset -10
            on show:
                alpha 0.0
                linear 0.3 alpha 1.0
        vbox:
            xanchor 0.5
            yanchor 0.5
            xpos 0.8
            ypos 0.6
            imagebutton:
                idle "gui/quick/menu.png"
                action ShowMenu()
            imagebutton:
                idle "gui/quick/notebook.png"
                at transform:
                    yoffset 30
                action Show("achievements")
            imagebutton:
                idle "gui/quick/dialogevents.png"
                at transform:
                    xoffset -10
                    yoffset 60
                action Show("dialogevents")
            imagebutton:
                idle "gui/quick/storyroute.png"
                at transform:
                    xoffset -12
                    yoffset 90
                action Show("storyroute")
            imagebutton:
                idle "gui/quick/quicktoggle.png"
                at transform:
                    xoffset 2
                    yoffset 120
                    zoom 1.5
                    rotate 180
                action [Hide("quickMenu"), Show("quickToggle")]

screen quickToggle:
    zorder 1
    layer "screens"
    imagebutton:
        idle "gui/quick/quickclose.png"
        xpos 0.00
        ypos 0.15
        at transform:
            on show:
                alpha 0.0
                linear 0.3 alpha 1.0
        action [Hide("quickToggle"), Show("quickMenu")]
