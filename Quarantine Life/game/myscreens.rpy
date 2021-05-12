# Activity Pick ------------------
screen livingroomact():
    $ ret = 2
    $ items = {"tv":(986, 296, 118, 234)}
    imagemap:
        ground "images/bg/bg livingroom back.png"
        hotspot items["tv"] action [SetVariable("itemselected", itemchoices["A"]), Jump("livingroomact")]

    imagebutton:
        idle "images/misc/arrow.png"
        yalign 0.5
        action [SetVariable("itemselected", 2), Jump("livingroomact")]

screen bedroomact():
    $ ret = 4
    $ items = {"bed":(91, 434, 624, 182), "phone":(206, 358, 63, 28), "exercise":(903, 365, 178, 133)}
    imagemap:
        ground "images/bg/bg bedroom back.png"
        hotspot items["bed"] action [SetVariable("itemselected", itemchoices["A"]), Jump("bedroomact")]
        hotspot items["phone"] action [SetVariable("itemselected", itemchoices["B"]), Jump("bedroomact")]
        hotspot items["exercise"] action [SetVariable("itemselected", itemchoices["C"]), Jump("bedroomact")]
    imagebutton:
        idle im.Flip("images/misc/arrow.png", horizontal=True)
        xalign 1.0
        yalign 0.5
        action [SetVariable("itemselected", 4), Jump("bedroomact")]

# Escape Room ------------------------
screen escaperoom():
    layer "background"
    $ items = {"books":(11, 79, 160, 167), "door":(1021, 3, 74, 494), "note":(302, 183, 83, 115)}
    imagemap:
        ground "images/bg/bg bedroom left evening c.png"
        hotspot items["books"] action [SetVariable("itemselected", itemchoices["A"]), Jump("escaperoom")]
        hotspot items["door"] action [SetVariable("itemselected", itemchoices["B"]), Jump("escaperoom")]
        hotspot items["note"] action [SetVariable("itemselected", itemchoices["C"]), Jump("escaperoom")]

default codeinput = {"A":0, "B":0, "C":0, "D":0}
default trialanswer = ""

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
        background "images/bg/bg bedroom left evening.png"
        xalign 0.5
        yalign 0.5
        xfill True
        yfill True
        hbox :
            xfill True
            yfill True
            xalign 0.5
            yalign 0.5
            textbutton "Return":
                xalign 0.5
                yalign 0.5
                text_color "#ffffff"
                action [SetVariable("itemselected", itemchoices["Reset"]), Hide("crypticbox"), Show("escaperoom")]
            hbox:
                spacing 20
                xalign 0.5
                yfill True
                vbox:
                    spacing 30
                    yalign 0.5
                    imagebutton:
                        idle "images/misc/arrow2.png"
                        xalign 0.5
                        action Call("updateDict", k="A")
                    frame:
                        xalign 0.5
                        yalign 0.5
                        xsize 50
                        ysize 70
                        text "{}".format(codeinput['A']):
                            xalign 0.5
                            yalign 0.5
                            size 40
                    imagebutton:
                        idle im.Flip("images/misc/arrow2.png", vertical=True)
                        xalign 0.5
                        action Call("updateDict", k="A", op=1)
                vbox:
                    spacing 30
                    yalign 0.5
                    imagebutton:
                        idle "images/misc/arrow2.png"
                        xalign 0.5
                        action Call("updateDict", k="B")
                    frame:
                        xalign 0.5
                        yalign 0.5
                        xsize 50
                        ysize 70
                        text "{}".format(codeinput['B']):
                            xalign 0.5
                            yalign 0.5
                            size 40
                    imagebutton:
                        idle im.Flip("images/misc/arrow2.png", vertical=True)
                        xalign 0.5
                        action Call("updateDict", k="B", op=1)
                vbox:
                    spacing 30
                    yalign 0.5
                    imagebutton:
                        idle "images/misc/arrow2.png"
                        xalign 0.5
                        action Call("updateDict", k="C")
                    frame:
                        xalign 0.5
                        yalign 0.5
                        xsize 50
                        ysize 70
                        text "{}".format(codeinput['C']):
                            xalign 0.5
                            yalign 0.5
                            size 40
                    imagebutton:
                        idle im.Flip("images/misc/arrow2.png", vertical=True)
                        xalign 0.5
                        action Call("updateDict", k="C", op=1)
                vbox:
                    spacing 30
                    yalign 0.5
                    imagebutton:
                        idle "images/misc/arrow2.png"
                        xalign 0.5
                        action Call("updateDict", k="D")
                    frame:
                        xalign 0.5
                        yalign 0.5
                        xsize 50
                        ysize 70
                        text "{}".format(codeinput['D']):
                            xalign 0.5
                            yalign 0.5
                            size 40
                    imagebutton:
                        idle im.Flip("images/misc/arrow2.png", vertical=True)
                        xalign 0.5
                        action Call("updateDict", k="D", op=1)
            textbutton "Enter":
                xalign 0.5
                yalign 0.5
                text_color "#ffffff"
                action Call("checkinput")

init:
    python:
        # This function will run a countdown of the given length. It will
        # be white until 5 seconds are left, and then red until 0 seconds are
        # left, and then will blink 0.0 when time is up.
        def countdown(st, at, length=0.0):

            remaining = length - st

            if remaining > 2.0:
                return Text("%.1f" % remaining, color="#fff", size=30), .1
            elif remaining > 0.0:
                return Text("%.1f" % remaining, color="#f00", size=30), .1
            else:
                return anim.Blink(Text("0.0", color="#f00", size=30)), None

    # Show a countdown for 10 seconds.
    image countdown = DynamicDisplayable(countdown, length=120.0)

screen escapetimer():
    layer "middle"
    add "countdown"
    timer 120.0 action [Call("timeout"), Hide("escapetimer")]
# Utility Labels ---------------------------
label timeout:
    scene black onlayer background
    centered "JUMPSCARE!"
    scene bg bedroom left onlayer background
    with dissolve

    with vpunch
    pl "Ahhhh!"

    pl "That nightmare scared the living daylights out of me..."

    show prince whatever onlayer middle
    with dissolve

    pr "Why are you screaming so early in the morning?"

    pr "You're going to wake up the neighbors."

    pl "I had a terrible nightmare."

    jump newnormal

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

        plt "(I got it! Time to open the door.)"

        window hide

    else:
        plt "(Tsk! It's wrong)"

        plt "(Maybe I should look for more clues)"

        window hide

    jump escaperoom
