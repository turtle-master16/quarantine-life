default codeinput = {"A":0, "B":0, "C":0, "D":0}

screen crypticbox():
    modal True
    layer "background"
    python:
        for k, v in codeinput.items():
            if v > 9:
                codeinput[k] = 0
            elif v < 0:
                codeinput[k] = 9
    frame:
        style "esc_coverall"
        background "images/bg/bg bedroom left evening.png"

        hbox:
            style "esc_coverall"

            textbutton "Return":
                style "esc_textbutton"
                text_color "#ffffff"
                action [SetVariable("itemselected", itemchoices["Reset"]), SetVariable("screenon", False), Hide("crypticbox"), Jump("escaperoom")]
            hbox:
                style "esc_codehbox"

                vbox:
                    style "esc_codevbox"
                    imagebutton:
                        idle "images/misc/arrow2.png"
                        xalign 0.5
                        action Call("updateDict", k="A")
                    frame:
                        style "esc_codeframe"
                        text "{}".format(codeinput['A']):
                            style "esc_number"
                    imagebutton:
                        idle im.Flip("images/misc/arrow2.png", vertical=True)
                        xalign 0.5
                        action Call("updateDict", k="A", op=1)
                vbox:
                    style "esc_codevbox"
                    imagebutton:
                        idle "images/misc/arrow2.png"
                        xalign 0.5
                        action Call("updateDict", k="B")
                    frame:
                        style "esc_codeframe"
                        text "{}".format(codeinput['B']):
                            style "esc_number"
                    imagebutton:
                        idle im.Flip("images/misc/arrow2.png", vertical=True)
                        xalign 0.5
                        action Call("updateDict", k="B", op=1)
                vbox:
                    style "esc_codevbox"
                    imagebutton:
                        idle "images/misc/arrow2.png"
                        xalign 0.5
                        action Call("updateDict", k="C")
                    frame:
                        style "esc_codeframe"
                        text "{}".format(codeinput['C']):
                            style "esc_number"
                    imagebutton:
                        idle im.Flip("images/misc/arrow2.png", vertical=True)
                        xalign 0.5
                        action Call("updateDict", k="C", op=1)
                vbox:
                    style "esc_codevbox"
                    imagebutton:
                        idle "images/misc/arrow2.png"
                        xalign 0.5
                        action Call("updateDict", k="D")
                    frame:
                        style "esc_codeframe"
                        text "{}".format(codeinput['D']):
                            style "esc_number"
                    imagebutton:
                        idle im.Flip("images/misc/arrow2.png", vertical=True)
                        xalign 0.5
                        action Call("updateDict", k="D", op=1)
            textbutton "Enter":
                style "esc_textbutton"
                text_color "#ffffff"
                action Call("checkinput")

init:
    python:
        def countdown(st, at, length=0.0):

            remaining = length - st

            if remaining > 2.0:
                return Text("%.1f" % remaining, color="#000", size=35), .1
            elif remaining > 0.0:
                return Text("%.1f" % remaining, color="#f00", size=35), .1
            else:
                return anim.Blink(Text("0.0", color="#f00", size=35)), None

    image countdown = DynamicDisplayable(countdown, length=60.0)

screen escapetimer(game="escape"):
    layer "background"
    zorder 2
    add "countdown":
        xoffset 5
    timer 60.0 action [Call("timeout", game), Hide("escapetimer")]

# Utility Labels & Screens ---------------------------
label timeout(game="escape"):
    if game == "escape":
        scene black onlayer background
        centered "JUMPSCARE!"
        scene bg bedroom left onlayer background
        with dissolve

        $ renpy.block_rollback()

        plt "(Ahh! What a terrible nightmare. I’m glad that’s over.)"

        call newnormal(True)
    else:
        $ renpy.block_rollback()

        plt "(I should check out these now, or I'll arrive home late. I need to catch dinner)"

        jump supermarket.results

label updateDict(k=None, op=0):
    python:
        if not k == None:
            if op==0:
                codeinput[k] = codeinput[k] + 1
            elif op==1:
                codeinput[k] = codeinput[k] - 1
    jump escaperoom

label checkinput:
    python:
        templist = ["0", "0", "0", "0"]
        trialanswer = ""
        for k, v in codeinput.items():
            if k == "A":
                templist[0] = str(v)
            elif k == "B":
                templist[1] = str(v)
            elif k == "C":
                templist[2] = str(v)
            elif k == "D":
                templist[3] = str(v)
        trialanswer = trialanswer.join(templist)

    if trialanswer == "7021":
        $ haskey = True

        plt "(Sweet. It’s the key, I can finally get out of here.)"

        window hide

    else:
        plt "(Seems like the code is wrong)"

        plt "(Maybe I should look for more hints)"

        window hide

    jump escaperoom
