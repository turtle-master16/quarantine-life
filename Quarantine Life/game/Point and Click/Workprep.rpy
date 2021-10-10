# Work preparation ---------------
init python:
    def readyForWork():
        for item in onhand:
            if onhand[item] == "bedkey":
                continue
            if not(onhand[item]):
                return False
        return True
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
    call hideStuff()
    call screen inputbox()
    return
    label .after_attempt(correct):
        if correct:
            pl "I unlocked it..."
            $ roomstatus['boxclosed'] = False
        else:
            pl "Seems like the code is wrong..."

screen workprep():
    layer "screens"
    if currentRoom == ROOMS["livingroom"]:
        imagemap:
            ground "images/bg/bg livingroom back.png"
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

        if not(onhand['faceshield']):
            imagemap:
                at right_corner
                ground "images/clickables/livingright.png"
                hotspot (110, 183, 78, 196) action Call("objDialogue", object_dialogue["pictureLvrm"])
                hotspot (20, 488, 77, 73) action [SetDict(onhand, "faceshield", True),
                                                  Call("objDialogue", object_dialogue["faceshield"])]
        if not(onhand['bedkey']):
            imagemap:
                at left_corner
                ground "images/clickables/livingleft.png"
                hotspot (82, 269, 148, 203) action Call("objDialogue", object_dialogue["tv"])
                hotspot (97, 553, 84, 49) action [SetDict(onhand, "bedkey", True),
                                                  Call("objDialogue", object_dialogue["drawerLvrm"])]

        imagebutton:
            idle "images/misc/arrow.png"
            yalign 0.5
            action [SetVariable("currentRoom", ROOMS["bedroom"]),
                    Call("updateDate", "June 2020, Week 2 | 06:00 PM, Bedroom | GCQ")]
        imagebutton:
            idle im.Flip("images/misc/arrow.png", horizontal=True)
            xalign 1.0
            yalign 0.5
            action [SetVariable("currentRoom", ROOMS["kitchen"]),
                    Call("updateDate", "June 2020, Week 2 | 06:00 PM, Kitchen | GCQ")]

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
                if onhand['wallet']:
                    hotspot (182, 228, 103, 113) action Call("objDialogue", object_dialogue["studyTable3"])

                elif not(onhand['wallet']):
                    hotspot (182, 228, 103, 113) action Call("objDialogue", object_dialogue["studyTable"], from_inputbox=True)

            if roomstatus['drawerclosed']:
                if onhand['bedkey']:
                    if onhand['facemask']:
                        hotspot bdroom_items["drawerBdrm"] action Call("objDialogue", object_dialogue["facemask2"])
                    elif not(onhand['facemask']):
                        hotspot bdroom_items["drawerBdrm"] action [SetDict(roomstatus, "drawerclosed", False),
                                                                   Call("objDialogue", object_dialogue["drawerhaskey"])]
                elif not(onhand['bedkey']):
                    hotspot bdroom_items["drawerBdrm"] action Call("objDialogue", object_dialogue["drawerBdrm"])

        if not(roomstatus['drawerclosed']) and not(onhand['facemask']):
            imagemap:
                at right_corner
                ground "images/clickables/bedright.png"
                hotspot (478,372,155,106) action Call("objDialogue", object_dialogue["dumbell"])
                hotspot (646,0,77,344) action Call("objDialogue", object_dialogue["window"])
                hotspot (119,287,246,119) action [SetDict(onhand, "facemask", True),
                                                  SetDict(roomstatus, "drawerclosed", True),
                                                  Call("objDialogue", object_dialogue["facemask"])]
        if not(roomstatus['boxclosed']) and not(onhand['wallet']):
            imagemap:
                at left_corner
                ground "images/clickables/bedleft.png"
                hotspot (56,56,68,122) action Call("objDialogue", object_dialogue["pictureBdrm"])
                hotspot (201,47,173,115) action Call("objDialogue", object_dialogue["books"])
                hotspot (182,222,140,116) action [SetDict(onhand, "wallet", True),
                                                  SetDict(roomstatus, "boxclosed", True),
                                                  Call("objDialogue", object_dialogue["studyTable2"])]
                hotspot (203,358,63,29) action Call("objDialogue", object_dialogue["phone"])
                hotspot (105,419,332,131) action Call("objDialogue", object_dialogue["bed"])

        imagebutton:
            idle im.Flip("images/misc/arrow.png", horizontal=True)
            xalign 1.0
            yalign 0.5
            action [SetVariable("currentRoom", ROOMS["livingroom"]),
                    Call("updateDate", "June 2020, Week 2 | 06:00 PM, Living Room | GCQ")]

    elif currentRoom == ROOMS['kitchen']:
        imagemap:
            ground "images/bg/bg kitchen.png"
            hotspot kitchen_items["cans"] action Call("objDialogue", object_dialogue["cans"])
            hotspot kitchen_items["cabinet"] action Call("objDialogue", object_dialogue["cabinet"])
            hotspot kitchen_items["stove"] action Call("objDialogue", object_dialogue["stove"])

        if not(onhand['sanitizer']):
            imagemap:
                at right_corner
                ground "images/clickables/kitchenright.png"
                hotspot (11, 181, 34, 63) action [SetDict(onhand, "sanitizer", True),
                                                  Call("objDialogue", object_dialogue["sanitizer"])]

        imagebutton:
            idle "images/misc/arrow.png"
            yalign 0.5
            action [SetVariable("currentRoom", ROOMS["livingroom"]),
                    Call("updateDate", "June 2020, Week 2 | 06:00 PM, Living Room | GCQ")]
