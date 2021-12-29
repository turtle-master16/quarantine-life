screen quickMenu:
    zorder 20
    layer "screens"
    imagebutton:
        idle "gui/quick/navigation_open.png"
        xalign 0.999
        yalign 0.4
        if currentRoom == ROOMS["kitchen"]:
            at slide2
        else:
            at slide1
        action [Hide("quickMenu"), Show("quickToggle")]
    vbox:
        xalign 0.999
        yalign 0.33
        spacing 15
        if not(currentRoom == ROOMS["kitchen"]):
            at slide3
        else:
            at slide4
        imagebutton:
            idle "gui/quick/achievement_icon.png"
            action Show("achievements")
        imagebutton:
            idle "gui/quick/narrative_icon.png"
            action Show("dialogevents")
        imagebutton:
            idle "gui/quick/timeline_icon.png"
            action Show("storyroute")

screen quickToggle:
    zorder 20
    layer "screens"
    $ isMenuOpen = renpy.get_screen("quickMenu")
    if not(isMenuOpen):
        if currentRoom == ROOMS["kitchen"]:
            imagebutton:
                idle "gui/quick/inactive_navigation_close.png"
                hover "gui/quick/navigation_close.png"
                xalign 0.0
                yalign 0.4
                at transform:
                    xzoom -1.0
                    on show:
                        alpha 0.0
                        linear 0.2 alpha 0.7
                action [Hide("quickToggle"), Show("quickMenu")]
        else:
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

transform slide1:
    yalign 0.3
    on show:
        xalign 1.09
        linear 0.2 xalign 1.0
    on hide:
        xalign 1.0
        linear 0.2 xalign 1.09
        linear 0.1 alpha 0.0

transform slide2:
    yalign 0.4
    xzoom -1.0
    on show:
        xalign -0.09
        linear 0.2 xalign 0.00
    on hide:
        xalign 0.0
        linear 0.2 xalign -0.09
        linear 0.1 alpha 0.0

transform slide3:
    on show:
        xalign 1.2
        linear 0.3 xalign 0.999
    on hide:
        xalign 0.999
        linear 0.8 xalign 1.2

transform slide4:
    yalign 0.4
    on show:
        xalign -0.8
        linear 0.3 xalign 0.001
    on hide:
        xalign 0.001
        linear 0.8 xalign -0.8
