# Event Flags
default itemselected = ""
default itemchoices = {"Reset":0, "A": 1, "B": 2, "C":3, "D":4, "E":5, "F":6}
default correctans = 0 # Quiz game

label objDialogue(dia):
    # Keeps the items visible/not visible during the say screen
    call hideStuff('faceshield', 'livingroom')
    call hideStuff('bedkey', 'livingroom')
    call hideStuff('sanitizer', 'kitchen')
    call hideStuff("wallet", 'bedroom')
    call hideStuff('draweropen', 'bedroom', isState=True)
    call hideStuff('boxclosed', 'bedroom', isState=True)

    $ islist = isinstance(dia, list)
    if islist:
        while dia:
            $ renpy.say(pl, dia.pop(0))
        return
    $ renpy.say(pl, dia)
    return

label hideStuff(item, location, isState=False):
    # Hide the takeable/roomstate item when switching rooms
    # to prevent it from showing in the new room.
    if isState:
        if not(roomstatus["drawerclosed"]) and (currentRoom == ROOMS[location]):
            $ renpy.show("draweropen", at_list=[takeables['drawerclosed']], layer="master")
        else:
            $ renpy.hide("draweropen", layer="master")
        if (roomstatus["boxclosed"]) and (currentRoom == ROOMS[location]):
            $ renpy.show("boxclosed", at_list=[takeables['boxclosed']], layer="master")
        elif not(roomstatus["boxclosed"]):
            if not(onhand['facemask']):
                $ renpy.show("boxwithmask", at_list=[takeables['boxclosed']], layer="master")
                $ renpy.hide("boxclosed", layer="master")
            else:
                $ renpy.show("boxnomask", at_list=[takeables['boxclosed']], layer="master")
                $ renpy.hide("boxwithmask", layer="master")
        elif not(currentRoom==ROOMS[location]):
            $ renpy.hide("boxclosed", layer="master")
            $ renpy.hide("boxwithmask", layer="master")
            $ renpy.hide("boxnomask", layer="master")
        return
    else:
        if currentRoom == ROOMS[location]:
            if not(onhand[item]):
                if (item=="wallet") and (roomstatus['drawerclosed']):
                    return
                $ renpy.show(item, at_list=[takeables[item]])
            else:
                $ renpy.hide(item, layer="master")
        return

default takeables = {
    "faceshield":Transform(xpos=0.79, ypos=0.76, xanchor=0.5, yanchor=1.0, zoom=0.15),
    "bedkey":Transform(xpos=0.11, ypos=0.82, xanchor=0.5, yanchor=1.0, zoom=0.05),
    "wallet":Transform(xpos=0.6, ypos=0.46, yoffset=5, xanchor=0.5, yanchor=1.0, zoom=0.11),
    "sanitizer":Transform(xpos=0.68, ypos=0.34, xanchor=0.5, yanchor=1.0, zoom=0.08),
    "drawerclosed":Transform(xpos=0.54, ypos=0.54, yoffset=5,xanchor=0.5, yanchor=1.0, zoom=0.48),
    "boxclosed": Transform(xpos=0.18, ypos=0.49, xanchor=0.5, yanchor=1.0, zoom=0.26)
}

screen broomfind():
    $ broom_location = Transform(xpos=0.93, ypos=0.96, xanchor=0.5, yanchor=1.0, zoom=0.51)
    imagebutton:
        idle "clickables/broom.png"
        at broom_location
        action Return()

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

# Supermart ------------------
default mart_item_count = {
    "facemask":0,
    "toiletpaper":0,
    "redcan": 0,
    "greencan": 0,
    "orangecan": 0,
    "browncan": 0,
    "yellowcan": 0,
    "hygiene": 0,
}
screen supermarket():
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

# Work preparation ---------------
define ROOMS = {
    "livingroom":1,
    "bedroom":2,
    "kitchen":3
}
default currentRoom = ROOMS['livingroom']
default onhand = {
    "bedkey":False,
    "faceshield":False,
    "sanitizer":False,
    "facemask":False,
    "wallet":False,
}
default roomstatus = {
    "boxclosed": True,
    "drawerclosed": True
}
label inputbox():
    call hideStuff('boxclosed', 'bedroom', isState=True)
    call screen inputbox()
    return
    label .after_attempt(correct):
        if correct:
            pl "Correct!"
            $ roomstatus['boxclosed'] = False
        else:
            pl "Wrong!"
screen workprep():
    $ lvroom_items = {
        "drawerLvrm": (35, 573, 199, 141),
        "correctPlant":(854, 419, 54, 84),
        "pictureLvrm":(127, 198, 42, 158),
        "wrongPlantA":(288, 416, 57, 72),
        "wrongPlantB":(518, 324, 50, 67),
        "wrongPlantC":(733, 318, 50, 73),
        "tv":(1014, 283, 132, 218),
        "mugs":(448, 461, 102, 45),
        "sofaPartA":(252, 503, 138, 173),
        "sofaPartB":(98, 443, 159, 114),
        "window": (293, 178, 660, 123),
    }
    $ bdroom_items = {
        "bed":(91, 434, 624, 182),
        "phone":(206, 358, 63, 28),
        "dumbell":(903, 365, 178, 133),
        "books": (195, 33, 171, 121),
        "pictureBdrm": (60, 60, 64, 115),
        "drawerBdrm": (556, 284, 253, 131),
        "window": (1076, 7, 117, 397),
        "plant": (462, 53, 72, 109),
        "table": (172, 291, 138, 61),
        }
    $ kitchen_items = {
        "cans": (237, 3, 260, 97),
        "cabinet":(557, 288, 317, 207),
        "stove": (388, 189, 121, 121),
        "sanitizer": (845, 181, 45, 60),
    }
    $ object_dialogue = {
        # Living Room
        "faceshield": "Got it.",
        "tv":"Not in the mood to watch TV.",
        "pictureLvrm": "There’s something written at the corner of the frame. \n{b}7 _ _ _{/b}",
        "correctPlant": "There’s a piece of paper. 1",
        "wrongPlant": "A healthy looking plant.",
        "mugs": "Empty.",
        "sofa": "No time to relax now.",
        "window": "Nothing to see here.",
        "drawerLvrm": "There’s a key!",
        # Bedroom
        "bed": "I can sleep later",
        "plant": "The house plants are growing quite nicely",
        "books": "No time to read",
        "studyTable": "Pens, papers and box that looks like it needs a 4-digit code to unlock.",
        "studyTable2": "I got my Face mask.",
        "phone": "I have 0 new messages.",
        "dumbell": "Just some dumbells.",
        "drawerBdrm": "It’s locked.",
        "drawerhaskey": ["It's locked. I'll try using the key from the living room...",
                        "It's now open."],
        "pictureBdrm": "{b}_ _ 2 _{/b}",
        "wallet": "Here's my wallet.",
        # Kitchen
        "cans": "Nope",
        "cabinet": "It’s filled with canned goods",
        "stove": "I’m not hungry.",
        "sanitizer": "Here’s my hand sanitizer.",
    }
    if currentRoom == ROOMS["livingroom"]:
        imagemap:
            ground "images/bg/bg livingroom back.png"
            if not(onhand['faceshield']):
                imagebutton:
                    idle "clickables/faceshield.png"
                    at transform:
                        xpos 0.79 ypos 0.76 xanchor 0.5 yanchor 1.0, zoom 0.15
                    action [SetDict(onhand, "faceshield", True), Call("objDialogue", object_dialogue["faceshield"])]
            if not(onhand['bedkey']):
                imagebutton:
                    idle "clickables/bedkey.png"
                    at transform:
                        xpos 0.11 ypos 0.82 xanchor 0.5 yanchor 1.0 zoom 0.05
                    action [SetDict(onhand, "bedkey", True),
                            Call("objDialogue", object_dialogue["drawerLvrm"])]
            hotspot lvroom_items["tv"] action Call("objDialogue", object_dialogue["tv"])
            hotspot lvroom_items["pictureLvrm"] action Call("objDialogue", object_dialogue["pictureLvrm"])
            hotspot lvroom_items["correctPlant"] action Call("objDialogue", object_dialogue["correctPlant"])
            hotspot lvroom_items["wrongPlantA"] action Call("objDialogue", object_dialogue["wrongPlant"])
            hotspot lvroom_items["wrongPlantB"] action Call("objDialogue", object_dialogue["wrongPlant"])
            hotspot lvroom_items["wrongPlantC"] action Call("objDialogue", object_dialogue["wrongPlant"])
            hotspot lvroom_items["mugs"] action Call("objDialogue", object_dialogue["mugs"])
            hotspot lvroom_items["sofaPartA"] action Call("objDialogue", object_dialogue["sofa"])
            hotspot lvroom_items["sofaPartB"] action Call("objDialogue", object_dialogue["sofa"])
            hotspot lvroom_items["window"] action Call("objDialogue", object_dialogue["window"])

        imagebutton:
            idle "images/misc/arrow.png"
            yalign 0.5
            action [SetVariable("currentRoom", ROOMS["bedroom"]),
                    Call("updateDate", "May 2020, 6:00 pm, Week 1, Bedroom room, GCQ")]
        imagebutton:
            idle im.Flip("images/misc/arrow.png", horizontal=True)
            xalign 1.0
            yalign 0.5
            action [SetVariable("currentRoom", ROOMS["kitchen"]),
                    Call("updateDate", "May 2020, 6:00 pm, Week 1, Kitchen, GCQ")]
    elif currentRoom == ROOMS['bedroom']:
        imagemap:
            ground "images/bg/bg bedroom back.png"
            hotspot bdroom_items["bed"] action Call("objDialogue", object_dialogue["bed"])
            hotspot bdroom_items["pictureBdrm"] action Call("objDialogue", object_dialogue["pictureBdrm"])
            hotspot bdroom_items["dumbell"] action Call("objDialogue", object_dialogue["dumbell"])
            hotspot bdroom_items["phone"] action Call("objDialogue", object_dialogue["phone"])
            hotspot bdroom_items["window"] action Call("objDialogue", object_dialogue["window"])
            hotspot bdroom_items["plant"] action Call("objDialogue", object_dialogue["plant"])
            hotspot bdroom_items["books"] action Call("objDialogue", object_dialogue["books"])
            if roomstatus['boxclosed']:
                imagebutton:
                    idle "clickables/boxclosed.png"
                    at takeables['boxclosed']
                    action [Call("inputbox"),
                            Call("objDialogue", object_dialogue["studyTable"])]
            elif not(roomstatus['boxclosed']) and not(onhand['facemask']):
                imagebutton:
                    idle "clickables/boxwithmask.png"
                    at transform:
                        xpos 0.18 ypos 0.49 xanchor 0.5 yanchor 1.0 zoom 0.26
                    action [SetDict(onhand, 'facemask' ,True),
                            Call("objDialogue", object_dialogue["studyTable2"])]
            elif onhand['facemask']:
                add Image("clickables/boxnomask.png"):
                    xpos 0.18 ypos 0.49 xanchor 0.5 yanchor 1.0 zoom 0.26
            if roomstatus['drawerclosed']:
                if onhand['bedkey']:
                    hotspot bdroom_items["drawerBdrm"] action [SetDict(roomstatus, "drawerclosed", False),
                                                               Call("objDialogue", object_dialogue["drawerhaskey"])]
                else:
                    hotspot bdroom_items["drawerBdrm"] action Call("objDialogue", object_dialogue["drawerBdrm"])
            elif not(roomstatus['drawerclosed']):
                add Image("clickables/draweropen.png"):
                    xpos 0.54 ypos 0.54 yoffset 5 xanchor 0.5 yanchor 1.0 zoom 0.48
                if not(onhand['wallet']):
                    imagebutton:
                        idle "clickables/wallet.png"
                        at transform:
                            xpos 0.6 ypos 0.46 yoffset 5 xanchor 0.5 yanchor 1.0 zoom 0.11
                        action [SetDict(onhand, "wallet", True),
                                Call("objDialogue", object_dialogue["wallet"])]
        imagebutton:
            idle im.Flip("images/misc/arrow.png", horizontal=True)
            xalign 1.0
            yalign 0.5
            action [SetVariable("currentRoom", ROOMS["livingroom"]),
                    Call("updateDate", "May 2020, 6:00 pm, Week 1, Living room, GCQ")]
    elif currentRoom == ROOMS['kitchen']:
        imagemap:
            ground "images/bg/bg kitchen.png"
            hotspot kitchen_items["cans"] action Call("objDialogue", object_dialogue["cans"])
            hotspot kitchen_items["cabinet"] action Call("objDialogue", object_dialogue["cabinet"])
            hotspot kitchen_items["stove"] action Call("objDialogue", object_dialogue["stove"])
            if not(onhand['sanitizer']):
                hotspot kitchen_items["sanitizer"] action [SetDict(onhand, "sanitizer", True),
                                                           Call("objDialogue", object_dialogue["sanitizer"])]
                add Image("clickables/sanitizer.png"):
                    xpos 0.68 ypos 0.34 xanchor 0.5 yanchor 1.0 zoom 0.08
        imagebutton:
            idle "images/misc/arrow.png"
            yalign 0.5
            action [SetVariable("currentRoom", ROOMS["livingroom"]),
                    Call("updateDate", "May 2020, 6:00 pm, Week 1, Living room, GCQ")]
