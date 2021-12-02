screen quickMenu:
    zorder 20
    layer "screens"
    imagebutton:
        idle "gui/quick/navigation_open.png"
        at transform:
            xalign 1.0
            yalign 0.3
            alpha 1.0
            on show:
                xalign 1.09
                linear 0.2 xalign 1.0
            on hide:
                xalign 1.0
                linear 0.2 xalign 1.09
                linear 0.1 alpha 0.0
        action [Hide("quickMenu"), Show("quickToggle")]
    vbox:
        at transform:
            xalign 0.995
            yalign 0.24
            on show:
                xalign 1.2
                linear 0.3 xalign 0.995
            on hide:
                xalign 0.995
                linear 0.8 xalign 1.2
        imagebutton:
            idle "gui/quick/achievement_icon.png"
            at transform:
                yoffset 30
            action Show("achievements")
        imagebutton:
            idle "gui/quick/narrative_icon.png"
            at transform:
                xoffset -5
                yoffset 60
            action Show("dialogevents")
        imagebutton:
            idle "gui/quick/timeline_icon.png"
            at transform:
                xoffset -7
                yoffset 90
            action Show("storyroute")

screen quickToggle:
    zorder 20
    layer "screens"
    $ isMenuOpen = renpy.get_screen("quickMenu")
    if not(isMenuOpen):
        imagebutton:
            idle "gui/quick/inactive_navigation_close.png"
            hover "gui/quick/navigation_close.png"
            xalign 1.0
            yalign 0.3
            at transform:
                on show:
                    alpha 0.0
                    linear 0.2 alpha 0.7
            action [Hide("quickToggle"), Show("quickMenu")]
