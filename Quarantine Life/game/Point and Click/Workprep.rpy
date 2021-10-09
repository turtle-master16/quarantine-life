# Work preparation ---------------
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
default takeables = {
    "faceshield":Transform(xpos=0.79, ypos=0.76, xanchor=0.5, yanchor=1.0, zoom=0.15),
    "bedkey":Transform(xpos=0.11, ypos=0.82, xanchor=0.5, yanchor=1.0, zoom=0.05),
    "wallet":Transform(xpos=0.6, ypos=0.46, yoffset=5, xanchor=0.5, yanchor=1.0, zoom=0.11),
    "sanitizer":Transform(xpos=0.68, ypos=0.34, xanchor=0.5, yanchor=1.0, zoom=0.08),
    "drawerclosed":Transform(xpos=0.54, ypos=0.54, yoffset=5,xanchor=0.5, yanchor=1.0, zoom=0.48),
    "boxclosed": Transform(xpos=0.18, ypos=0.49, xanchor=0.5, yanchor=1.0, zoom=0.26),
    "boxnomask": Transform(xpos=0.18, xoffset=2, ypos=0.49, xanchor=0.5, yanchor=1.0, zoom=0.26)
}

label inputbox():
    call hideStuff('boxclosed', 'bedroom', isState=True)
    call screen inputbox()
    return
    label .after_attempt(correct):
        if correct:
            pl "I unlocked it..."
            $ roomstatus['boxclosed'] = False
        else:
            pl "Seems like the code is wrong..."
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
        "phone":(206, 364, 75, 32),
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
                    action [Call("objDialogue", object_dialogue["studyTable"], True),
                            Call("inputbox")]
            elif not(roomstatus['boxclosed']) and not(onhand['facemask']):
                imagebutton:
                    idle "clickables/boxwithmask.png"
                    at transform:
                        xpos 0.18 ypos 0.49 xanchor 0.5 yanchor 1.0 zoom 0.26
                    action [SetDict(onhand, 'facemask' ,True),
                            Call("objDialogue", object_dialogue["studyTable2"])]
            elif onhand['facemask']:
                add Image("clickables/boxnomask.png"):
                    at takeables['boxnomask']
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
