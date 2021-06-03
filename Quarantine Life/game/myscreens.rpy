# Styles
init 5:
    style esc_codeframe:
        xalign 0.5
        yalign 0.5
        xsize 50
        ysize 70
    style esc_coverall:
        xalign 0.5
        yalign 0.5
        xfill True
        yfill True
    style esc_textbutton:
        xalign 0.5
        yalign 0.5
    style esc_codehbox:
        spacing 20
        xalign 0.5
        yfill True
    style esc_codevbox:
        spacing 30
        yalign 0.5
    style esc_number:
        xalign 0.5
        yalign 0.5
        size 40
# Activity Pick ------------------
screen livingroomact():
    $ ret = 2
    $ lvroom_items = {
        "tv":(986, 296, 118, 234),
        "mat":(412, 608, 441, 83),
        "mugs":(448, 461, 102, 45),
        "couch":(94, 500, 302, 185),
        "mirror":(127, 198, 42, 158),
        "window": (296, 181, 655, 208)
    }
    imagemap:
        ground "images/bg/bg livingroom back.png"
        hotspot lvroom_items["tv"] action [SetVariable("itemselected", itemchoices["A"]), Jump("livingroomact")]
        hotspot lvroom_items["mat"] action Call("livingroomact.misc_item_dialog", 1)
        hotspot lvroom_items["mugs"] action Call("livingroomact.misc_item_dialog", 2)
        hotspot lvroom_items["couch"] action Call("livingroomact.misc_item_dialog", 3)
        hotspot lvroom_items["mirror"] action Call("livingroomact.misc_item_dialog", 4)
        hotspot lvroom_items["window"] action Call("livingroomact.misc_item_dialog", 5)

    imagebutton:
        idle "images/misc/arrow.png"
        yalign 0.5
        action [SetVariable("itemselected", 2), Jump("livingroomact")]

screen bedroomact():
    $ ret = 4
    $ bdroom_items = {
        "bed":(91, 434, 624, 182),
        "phone":(206, 358, 63, 28),
        "exercise":(903, 365, 178, 133),
        "books": (209, 48, 145, 105),
        "mirror": (60, 60, 64, 115),
        "drawer": (556, 284, 253, 131),
        }
    imagemap:
        ground "images/bg/bg bedroom back.png"
        hotspot bdroom_items["bed"] action [SetVariable("itemselected", itemchoices["A"]), Jump("bedroomact")]
        hotspot bdroom_items["phone"] action [SetVariable("itemselected", itemchoices["B"]), Jump("bedroomact")]
        hotspot bdroom_items["exercise"] action [SetVariable("itemselected", itemchoices["C"]), Jump("bedroomact")]
        hotspot bdroom_items["books"] action Call("bedroomact.misc_item_dialog", 1)
        hotspot bdroom_items["mirror"] action Call("bedroomact.misc_item_dialog", 2)
        hotspot bdroom_items["drawer"] action Call("bedroomact.misc_item_dialog", 3)
    imagebutton:
        idle im.Flip("images/misc/arrow.png", horizontal=True)
        xalign 1.0
        yalign 0.5
        action [SetVariable("itemselected", 4), Jump("bedroomact")]

# Escape Room ------------------------
screen escaperoom():
    layer "background"
    $ items = {
    "books":(11, 79, 160, 167),
    "door":(1021, 3, 74, 494),
    "window":(358, 1, 205, 299),
    "pot": (309, 187, 50, 105),
    "dumbell":(419, 340, 92, 92),
    "phone":(369, 497, 113, 26),
    "drawer":(239, 299, 171, 166),
    "sidetable":(1049, 522, 228, 194),
    "bed":(572, 404, 425, 312),
    }
    imagemap:
        ground "images/bg/bg bedroom left evening.png"
        hotspot items["books"] action [SetVariable("itemselected", itemchoices["A"]), Jump("escaperoom")]
        hotspot items["door"] action [SetVariable("itemselected", itemchoices["B"]), Jump("escaperoom")]
        hotspot items["pot"] action Call("escaperoom.misc_item_dialog", 1)
        hotspot items["dumbell"] action Call("escaperoom.misc_item_dialog", 2)
        hotspot items["phone"] action Call("escaperoom.misc_item_dialog", 3)
        hotspot items["drawer"] action Call("escaperoom.misc_item_dialog", 4)
        hotspot items["window"] action Call("escaperoom.misc_item_dialog", 5)
        hotspot items["sidetable"] action Call("escaperoom.misc_item_dialog", 6)
        hotspot items["bed"] action Call("escaperoom.misc_item_dialog", 7)

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

# Supermarket Game
screen supermarket:
    layer "background"
    $ mart_items = {
        "facemask":(709, 404, 502, 314),
        "toiletpaper":(824, 180, 137, 36),
        "toiletpaper2":(990, 280, 216, 73),
        "redcan":(0, 343, 195, 25),
        "redcan2": (241, 361, 654, 21),
        "greencan": (1, 414, 198, 60),
        "greencan2": (234, 421, 455, 28),
        "orangecan":(462, 486, 217, 26),
        "browncan":(1, 218, 199, 70),
        "yellowcan":(240, 285, 655, 28),
        "hygiene":(212, 495, 231, 221),
        "hygiene2":(88, 522, 97, 196),
        "hygiene3":(10, 579, 67, 139),
    }
    imagemap:
        ground "images/bg/bg supermarket.png"
        hotspot mart_items["facemask"] action Call("supermarket.item_take", 1)
        hotspot mart_items["toiletpaper"] action Call("supermarket.item_take", 2)
        hotspot mart_items["toiletpaper2"] action Call("supermarket.item_take", 2)
        hotspot mart_items["redcan"] action Call("supermarket.item_take", 3)
        hotspot mart_items["redcan2"] action Call("supermarket.item_take", 3)
        hotspot mart_items["greencan"] action Call("supermarket.item_take", 4)
        hotspot mart_items["greencan2"] action Call("supermarket.item_take", 4)
        hotspot mart_items["orangecan"] action Call("supermarket.item_take", 5)
        hotspot mart_items["browncan"] action Call("supermarket.item_take", 6)
        hotspot mart_items["yellowcan"] action Call("supermarket.item_take", 7)
        hotspot mart_items["hygiene"] action Call("supermarket.item_take", 8)
        hotspot mart_items["hygiene2"] action Call("supermarket.item_take", 8)
        hotspot mart_items["hygiene3"] action Call("supermarket.item_take", 8)

    imagebutton:
        idle im.Flip("images/misc/arrow.png", horizontal=True)
        xalign 1.0
        yalign 0.5
        action Call("supermarket.maingame", True)

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

# Test mode
screen testmode():
    vbox:
        text "Welcome to route test mode!":
            xalign 0.5
            xfill True
            size 30
        viewport id "vp":
            draggable True
            hbox:
                spacing 20
                vbox: #Home
                    xalign 0.5
                    yoffset 20
                    spacing 10
                    text "{b}1. Home{/b}" xalign 0.5
                    textbutton "(Start)" action Jump('start.mainstart') xalign 0.5
                    textbutton "(COVID News)" action Jump('news') xalign 0.5
                    textbutton "{color=#f00}1a.{/color}<-(Lockdown)->{color=#f2f542}Proceed{/color}" action Jump('lockdown') xalign 0.5
                    hbox:
                        vbox:
                            text "{color=#f00}{b}1a.{/b}{/color}" xalign 0.5
                            textbutton "(Arrested End)" action Jump('getcaught') xalign 0.5
                        text "OR"
                        vbox:
                            textbutton "(Quarantine)" action Jump('quarantine') xalign 0.5
                            textbutton "(New Normal)" action Jump('newnormal') xalign 0.5
                            textbutton "(Lv_Rm Activities({color=#f2f542}2.{/color}))" action Jump('livingroomact') xalign 0.5
                vbox: #Work
                    xalign 0.5
                    yoffset 20
                    spacing 10
                    text "{color=#f2f542}{b}2. Work{/b}{/color}" xalign 0.5
                    textbutton "(Commute to work)" action Jump('commuting') xalign 0.5
                    textbutton "{color=#42bff5}3a.{/color}<-(Office)->{color=#427bf5}3b.{/color}" action Jump('office') xalign 0.5
                vbox: #Home2
                    xalign 0.5
                    yoffset 20
                    spacing 10
                    text "{color=#42bff5}{b}3a. Home (After Work){/b}{/color}" xalign 0.5 layout "nobreak"
                    textbutton "(Home)" action Jump('home') xalign 0.5
                    textbutton "(Supermarket)" action Jump('supermarket') xalign 0.5
                    textbutton "(Kitchen)" action Jump('kitchen') xalign 0.5
                    textbutton "{color=#7242f5}3aa.{/color}<-(Project)->{color=#7242f5}3ab.{/color}" action Jump('project') xalign 0.5 text_layout "nobreak"
                    hbox:
                        vbox:
                            xalign 0.5
                            yoffset 20
                            text "{color=#7242f5}{b}3aa. {/b}{/color}" xalign 0.5
                            textbutton "(Prince End A)" action Jump('bros') xalign 0.5
                        text "OR"
                        vbox:
                            xalign 0.5
                            yoffset 20
                            text "{color=#7242f5}{b}3ab. {/b}{/color}" xalign 0.5
                            textbutton "(Prince End B)" action Jump('falsealarm') xalign 0.5 text_layout "nobreak"
                vbox: #Friend
                    xalign 0.5
                    yoffset 20
                    spacing 10
                    text "{color=#427bf5}{b}3b. Friend Route{/b}{/color}" xalign 0.5 layout "nobreak"
                    textbutton "3ba.<-(Restaurant)->3bb." action Jump('restaurant') xalign 0.5 text_layout "nobreak"
                    hbox:
                        vbox:
                            xalign 0.5
                            yoffset 20
                            spacing 10
                            text "{color=#228b22}{b}3ba. Kyle Route{/b}{/color}" xalign 0.5 layout "nobreak"
                            textbutton "(Kyle)" action Jump('kyle') xalign 0.5
                            textbutton "Kyle Meet<-(Kyle Home)->Kyle Refuse" action Jump('kylehome') xalign 0.5 text_layout "nobreak"
                            hbox:
                                xalign 0.5
                                spacing 20
                                vbox:
                                    textbutton "(Kyle Meet)" action Jump('kylemeet') xalign 0.5 text_layout "nobreak"
                                    textbutton "(Hospital)" action Jump('hospital') xalign 0.5
                                    textbutton "(Player End 1)" action Jump('mcend') xalign 0.5 text_layout "nobreak"
                                text "OR"
                                vbox:
                                    textbutton "(Player End 2)" action Jump('kylehome.mcend2') xalign 0.5 text_layout "nobreak"
                        vbox:
                            xalign 0.5
                            yoffset 20
                            spacing 10
                            text "{b}3bb. Date Route{/b}" xalign 0.5 layout "nobreak"
                            textbutton "{color=#d2691e}Jason{/color}<-(Date Search)->{color=#add8e6}Jillian{/color}" action Jump('datesearch') xalign 0.5 text_layout "nobreak"
                vbox: #Dates
                    xalign 0.5
                    yoffset 20
                    spacing 10
                    text "{color=#d2691e}{b}Jason{/b}{/color}" xalign 0.5 layout "nobreak"
                    textbutton "{color=#228b22}Kyle Route{/color}<-(Jason Start)->{color=#d2691e}Proceed{/color}" action Jump('phone') xalign 0.5 text_layout "nobreak"
                    hbox:
                        xalign 0.5
                        xanchor 0.5
                        vbox:
                            xalign 0.5
                            xsize 520
                            textbutton "{color=#228b22}(Go to 3ba. Kyle Route){/color}" action Jump('kyle') xalign 0.5 text_layout "nobreak"
                        text "OR"  xalign 0.5
                        vbox:
                            xalign 0.5
                            xsize 520
                            textbutton "(Post Date Search Jason)" action Jump('postdatesearch') xalign 0.5 text_layout "nobreak"
                            textbutton "(First Date Jason)" action Jump('firstdate') xalign 0.5 text_layout "nobreak"
                            textbutton "Js End 1<-(Jason Casual)-> Js End 2" action Jump('jason') xalign 0.5 text_layout "nobreak"
                            hbox:
                                xalign 0.5
                                spacing 50
                                textbutton "(Js End 1)" action Jump('jsexerciseend') xalign 0.5 text_layout "nobreak"
                                text "OR"
                                textbutton "(Js End 2)" action Jump('jsend') xalign 0.5 text_layout "nobreak"
                    text "{color=#add8e6}{b}Jillian{/b}{/color}" xalign 0.5 layout "nobreak"
                    textbutton "(Jillian Start)" action Call('phone', False) xalign 0.5 text_layout "nobreak"
                    textbutton "(Post Date Search Jillian)" action Call('postdatesearch', False) xalign 0.5 text_layout "nobreak"
                    textbutton "{color=#228b22}Kyle Route{/color}<-(First Date Jillian)->{color=#add8e6}Proceed{/color}" action Call('firstdate', False) xalign 0.5 text_layout "nobreak"
                    hbox:
                        xalign 0.5
                        xanchor 0.5
                        vbox:
                            xalign 0.5
                            xsize 400
                            textbutton "{color=#228b22}(Go to 3ba. Kyle Route){/color}" action Jump('kyle') xalign 0.5 text_layout "nobreak"
                        text "OR" xalign 0.5 xsize 400
                        vbox:
                            xalign 0.5
                            xsize 400
                            textbutton "(Jilllian Casual)" action Jump('jillian') xalign 0.5 text_layout "nobreak"
                            textbutton "(Jillian Ask out)" action Jump('jlaskout') xalign 0.5 text_layout "nobreak"
                            textbutton "(Jillian Date)" action Jump('jldate') xalign 0.5 text_layout "nobreak"
                            textbutton "(Jillian End)" action Jump('jlend') xalign 0.5 text_layout "nobreak"

screen returnbutton:
    zorder 2
    imagebutton:
        idle "images/misc/return.png"
        xalign 1.0
        yalign 1.0
        action Call("start", retmode=True)
