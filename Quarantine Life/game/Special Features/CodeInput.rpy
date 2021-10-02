init python:
    attempt = [0, 0, 0, 0]
    def increment(ind):
        attempt[ind] = attempt[ind] + 1
        if attempt[ind] > 9:
            attempt[ind] = 0
        renpy.call("inputbox")
    def decrement(ind):
        attempt[ind] = attempt[ind] - 1
        if attempt[ind] < 0:
            attempt[ind] = 9
        renpy.call("inputbox")
    def checkAttempt():
        strAns = []
        for i in attempt:
            strAns.append(str(i))
        ans = ''.join(strAns)
        if ans == "7021":
            renpy.call("inputbox.after_attempt", True)
        else:
            renpy.call("inputbox.after_attempt", False)

screen inputbox():
    modal True
    frame:
        style "esc_coverall"
        hbox:
            style "esc_coverall"
            textbutton "Return":
                style "esc_textbutton"
                text_color "#ffffff"
                action Return(0)
            hbox:
                style "esc_codehbox"
                vbox:
                    style "esc_codevbox"
                    imagebutton:
                        idle "images/misc/arrow2.png"
                        xalign 0.5
                        action Function(increment, 0)
                    frame:
                        style "esc_codeframe"
                        text "{}".format(str(attempt[0])):
                            style "esc_number"
                    imagebutton:
                        idle im.Flip("images/misc/arrow2.png", vertical=True)
                        xalign 0.5
                        action Function(decrement, 0)
                vbox:
                    style "esc_codevbox"
                    imagebutton:
                        idle "images/misc/arrow2.png"
                        xalign 0.5
                        action Function(increment, 1)
                    frame:
                        style "esc_codeframe"
                        text "{}".format(str(attempt[1])):
                            style "esc_number"
                    imagebutton:
                        idle im.Flip("images/misc/arrow2.png", vertical=True)
                        xalign 0.5
                        action Function(decrement, 1)
                vbox:
                    style "esc_codevbox"
                    imagebutton:
                        idle "images/misc/arrow2.png"
                        xalign 0.5
                        action Function(increment, 2)
                    frame:
                        style "esc_codeframe"
                        text "{}".format(str(attempt[2])):
                            style "esc_number"
                    imagebutton:
                        idle im.Flip("images/misc/arrow2.png", vertical=True)
                        xalign 0.5
                        action Function(decrement, 2)
                vbox:
                    style "esc_codevbox"
                    imagebutton:
                        idle "images/misc/arrow2.png"
                        xalign 0.5
                        action Function(increment, 3)
                    frame:
                        style "esc_codeframe"
                        text "{}".format(str(attempt[3])):
                            style "esc_number"
                    imagebutton:
                        idle im.Flip("images/misc/arrow2.png", vertical=True)
                        xalign 0.5
                        action Function(decrement, 3)
            textbutton "Enter":
                style "esc_textbutton"
                text_color "#ffffff"
                action [Function(checkAttempt)]
