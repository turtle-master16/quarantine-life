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
    layer "background"
    if currentRoom == ROOMS["livingroom"]:
        imagemap:
            ground "images/bg/bg livingroom back.png"
            for item in lvroom_itemsC:
                if lvroom_itemsC[item].is_grouped:
                    for hspot in lvroom_itemsC[item].hspot:
                        hotspot hspot action Function(lvroom_itemsC[item].sayDialogue)
                else:
                    hotspot lvroom_itemsC[item].hspot action Function(lvroom_itemsC[item].sayDialogue)


        if not(onhand['faceshield']):
            imagemap:
                at right_corner
                ground "images/clickables/livingright.png"
                hotspot lvroom_right["tv"].hspot           action [SetField(lvroom_itemsC["tv"], "interacted", True), Function(lvroom_right["tv"].sayDialogue)]
                hotspot lvroom_right["faceshield"].hspot   action [SetDict(onhand, "faceshield", True), Function(lvroom_right["faceshield"].sayDialogue)]

        if not(onhand['bedkey']):
            imagemap:
                at left_corner
                ground "images/clickables/livingleft.png"
                hotspot lvroom_left["drawerLvrm"].hspot    action [SetDict(onhand, "bedkey", True),
                                                                  Call("objDialogue", object_dialogue["drawerLvrm"])]

        imagebutton:
            idle "images/misc/arrow.png"
            yalign 0.5
            action [SetVariable("currentRoom", ROOMS["bedroom"]),
                    Show("patientOverlay", date="June 2020, Week 2|11:00 AM, GCQ", status="happy")]
        imagebutton:
            idle im.Flip("images/misc/arrow.png", horizontal=True)
            xalign 1.0
            yalign 0.5
            action [SetVariable("currentRoom", ROOMS["kitchen"]),
                    Show("patientOverlay", date="June 2020, Week 2|11:00 AM, GCQ", status="happy")]

    elif currentRoom == ROOMS['bedroom']:
        imagemap:
            ground "images/bg/bg bedroom back.png"
            for item in bdroom_items:
                hotspot bdroom_items[item].hspot action Function(bdroom_items[item].sayDialogue)

            if roomstatus['boxclosed']:
                if onhand['wallet']:
                    hotspot (182, 228, 103, 113) action Call("objDialogue", object_dialogue["studyTable3"])

                elif not(onhand['wallet']):
                    hotspot (182, 228, 103, 113) action Call("objDialogue", object_dialogue["studyTable"], from_inputbox=True)

            if roomstatus['drawerclosed']:
                if onhand['bedkey']:
                    if onhand['facemask']:
                        hotspot bdroom_items["drawerBdrm"].hspot action Call("objDialogue", object_dialogue["facemask2"])
                    elif not(onhand['facemask']):
                        hotspot bdroom_items["drawerBdrm"].hspot action [SetDict(roomstatus, "drawerclosed", False),
                                                                   Call("objDialogue", object_dialogue["drawerhaskey"])]
                elif not(onhand['bedkey']):
                    hotspot bdroom_items["drawerBdrm"].hspot     action Call("objDialogue", object_dialogue["drawerBdrm"])

        if not(roomstatus['drawerclosed']) and not(onhand['facemask']):
            imagemap:
                at right_corner
                ground "images/clickables/bedright.png"
                hotspot (478,372,155,106) action Call("objDialogue", object_dialogue["dumbell"])
                hotspot (646,0,77,344)    action Call("objDialogue", object_dialogue["window"])
                hotspot (119,287,246,119) action [SetDict(onhand, "facemask", True),
                                                  SetDict(roomstatus, "drawerclosed", True),
                                                  Call("objDialogue", object_dialogue["facemask"])]

        if not(roomstatus['boxclosed']) and not(onhand['wallet']):
            imagemap:
                at left_corner
                ground "images/clickables/bedleft.png"
                hotspot (56,56,68,122)    action Call("objDialogue", object_dialogue["pictureBdrm"])
                hotspot (201,47,173,115)  action Call("objDialogue", object_dialogue["books"])
                hotspot (182,222,140,116) action [SetDict(onhand, "wallet", True),
                                                  SetDict(roomstatus, "boxclosed", True),
                                                  Call("objDialogue", object_dialogue["studyTable2"])]
                hotspot (203,358,63,29)   action Call("objDialogue", object_dialogue["phone"])
                hotspot (105,419,332,131) action Call("objDialogue", object_dialogue["bed"])

        imagebutton:
            idle im.Flip("images/misc/arrow.png", horizontal=True)
            xalign 1.0
            yalign 0.5
            action [SetVariable("currentRoom", ROOMS["livingroom"]),
                    Show("patientOverlay", date="June 2020, Week 2|11:00 AM, GCQ", status="happy")]

    elif currentRoom == ROOMS['kitchen']:
        imagemap:
            ground "images/bg/bg kitchen.png"
            for item in kitchen_items:
                if kitchen_items[item].is_grouped:
                    for hspot in kitchen_items[item].hspot:
                        hotspot hspot action Function(kitchen_items[item].sayDialogue)
                else:
                    if not(item == "sanitizer") or not(onhand["sanitizer"]):
                        hotspot kitchen_items[item].hspot action Function(kitchen_items[item].sayDialogue)

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
                    Show("patientOverlay", date="June 2020, Week 2|11:00 AM, GCQ", status="happy")]

    textbutton "Click me":
        xalign 0.9
        yalign 0.2
        action ToggleScreen("spk")

screen workitem_list():
    modal True
    zorder 1
    add Image("images/misc/paper.png"):
        at transform:
            xalign 0.5
            yalign 0.5
            zoom 3.4
            on show:
                yoffset 700
                linear 0.5 yoffset 0
            on hide:
                yoffset 0
                linear 0.5 yoffset 700
    vbox:
        xalign 0.5
        xoffset 12
        ypos 0.4
        yanchor 0.5
        at transform:
            on show:
                yoffset 700
                linear 0.5 yoffset 0
            on hide:
                yoffset 0
                linear 0.5 yoffset 700
        text "ITEM CHECKLIST":
            xalign 0.5
            color "#000"

        null height 20

        $ items_needed = [item for item in onhand if not(item == 'bedkey')]
        for item in items_needed:
            $ it_cap = item.capitalize()
            showif onhand[item]:
                text "{s}[it_cap]{/s}":
                    xalign 0.5
                    color "#000"
            else:
                text "[it_cap]":
                    xalign 0.5
                    color "#000"
            null height 15

        null height 20

        textbutton "Tap to close":
            xalign 0.5
            text_color "#000"
            action [Hide("workitem_list"), Function(showFlapButtons)]
