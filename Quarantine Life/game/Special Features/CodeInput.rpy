init python:

    ansA=ansB=ansC=ansD= 0

    def checkAttempt():
        renpy.show_screen("ui_start")
        answer = "{}{}{}{}".format(ansA, ansB, ansC, ansD)
        if answer == "7021":
            renpy.call("inputbox", True)
        else:
            renpy.call("inputbox", False)

    # Use this if a particular screen JUST can't hide properly with renpy.hide_screen()
    def xTraHide(scr):
        while renpy.get_screen(scr):
            renpy.hide_screen(scr)

screen inputbox:
    modal True
    add Solid("#00000088")
    zorder 10
    imagemap:
        xalign .5 yalign .4
        at transform:
            alpha 0.5
        ground "images/misc/safe_bg.png"
        hotspot (66, 8, 111, 165)    action  If(ansA < 9,  SetVariable("ansA", ansA + 1), SetVariable("ansA", 0)) at inv
        hotspot (208, 9, 108, 166)   action  If(ansB < 9,  SetVariable("ansB", ansB + 1), SetVariable("ansB", 0)) at inv
        hotspot (355, 11, 109, 163)  action  If(ansC < 9,  SetVariable("ansC", ansC + 1), SetVariable("ansC", 0)) at inv
        hotspot (496, 13, 111, 159)  action  If(ansD < 9,  SetVariable("ansD", ansD + 1), SetVariable("ansD", 0)) at inv
        hotspot (64, 218, 117, 159)  action  If(ansA > 0,  SetVariable("ansA", ansA - 1), SetVariable("ansA", 9)) at inv
        hotspot (211, 221, 108, 156) action  If(ansB > 0,  SetVariable("ansB", ansB - 1), SetVariable("ansB", 9)) at inv
        hotspot (354, 223, 114, 153) action  If(ansC > 0,  SetVariable("ansC", ansC - 1), SetVariable("ansC", 9)) at inv
        hotspot (492, 225, 113, 151) action  If(ansD > 0,  SetVariable("ansD", ansD - 1), SetVariable("ansD", 9)) at inv
    fixed:
        xalign .5 yalign .4
        xsize 691 ysize 385
        add "images/misc/safe_num.png":
            xalign .5 yalign .5
        hbox:
            xalign 0.52 yalign 0.5
            xoffset 0 spacing 113
            text "{{b}}{}{{/b}}".format(ansA) color "#fff" size 50
            text "{{b}}{}{{/b}}".format(ansB) color "#fff" size 50
            text "{{b}}{}{{/b}}".format(ansC) color "#fff" size 50
            text "{{b}}{}{{/b}}".format(ansD) color "#fff" size 50

        imagebutton:
            idle "images/misc/close.png"
            xalign 0.97 yalign 0.03
            action [Hide("inputbox"), Show("ui_start")]

        imagebutton:
            xalign .5 yalign 1.13
            at transform:
                zoom 0.7
            idle "images/misc/enter_code.png"
            action [Hide("inputbox"), Function(checkAttempt)]

transform inv:
    alpha 0.0
