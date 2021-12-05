init python:

    ansA=ansB=ansC=ansD= 0

    def checkAttempt():
        answer = "{}{}{}{}".format(ansA, ansB, ansC, ansD)
        if answer == "7021":
            renpy.call("inputbox.after_attempt", True)
        else:
            renpy.call("inputbox.after_attempt", False)

    # Use this if a particular screen just can't hide properly with renpy.hidescreen()
    def xTraHide(scr):
        while renpy.get_screen(scr):
            renpy.hide_screen(scr)

screen inputboxB:
    modal True
    zorder 50
    $ renpy.hide_screen("ui_start")
    imagemap:
        xalign .5 yalign .4
        at transform:
            alpha 0.75
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
            xalign 0.5 yalign 0.5
            xoffset -5 spacing 111
            text "{{b}}{}{{/b}}".format(ansA) color "#fff" size 50
            text "{{b}}{}{{/b}}".format(ansB) color "#fff" size 50
            text "{{b}}{}{{/b}}".format(ansC) color "#fff" size 50
            text "{{b}}{}{{/b}}".format(ansD) color "#fff" size 50

        imagebutton:
            idle "images/misc/white close.png"
            xalign 0.99 yalign 0.02
            action [Hide("inputboxB"), Show("ui_start")]

        imagebutton:
            xalign .5 yalign 1.3
            at transform:
                zoom 0.7
            idle "images/misc/enter_code.png"
            action [Hide("inputboxB"), Show("ui_start"), Function(checkAttempt)]

transform inv:
    alpha 0.0
