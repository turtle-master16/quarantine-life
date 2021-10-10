"""
    Stuff in this file are stuff shared by all the Point N' Click Screens
"""

define instructions = {
    "supermarket":
"""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.
""",
    "workprep":
"Hello world"
}
# Conditional Variables (For phone function)
default itemselected = ""
default itemchoices = {"Reset":0, "A": 1, "B": 2, "C":3, "D":4, "E":5, "F":6}
#--------------------

# For room switching
define ROOMS = {
    "livingroom":1,
    "bedroom":2,
    "kitchen":3
}
default currentRoom = ROOMS['livingroom']
default currentScreen = "" # Tells which minigame is on screen at the moment

label hideStuff():
    # Hide the takeable/roomstate item when switching rooms
    # to prevent it from showing in the new room.
    python:
        location = {
            ROOMS['livingroom']: ["faceshield", "bedkey"],
            ROOMS['bedroom']: ["wallet", "facemask"],
            ROOMS['kitchen']: ["sanitizer"],
        }
        left_side = {
            "facemask":"bedleft",
            "bedkey":"livingleft"
        }
        right_side = {
            "faceshield":"livingright",
            "wallet":"bedright",
            "sanitizer":"kitchenright"
        }

        for item in location[currentRoom]:
            if item == "facemask":
                if not(roomstatus['boxclosed']):
                    renpy.show("bedleft", at_list=[left_corner])
                continue
            elif item == "wallet":
                if not(roomstatus['drawerclosed']):
                    renpy.show("bedright", at_list=[right_corner])
                continue
            if item in left_side:
                if not(onhand[item]):
                    renpy.show(left_side[item], at_list=[left_corner])
                continue
            elif item in right_side:
                if not(onhand[item]):
                    renpy.show(right_side[item], at_list=[right_corner])
    return
# ------------------

label objDialogue(dia, from_inputbox=False):
    # Keeps the items visible/not visible while in this label
    call hideStuff()

    $ islist = isinstance(dia, list)
    if islist:
        while dia:
            $ renpy.say(pl, dia.pop(0))
        return
    $ renpy.say(pl, dia)
    if from_inputbox:
        call inputbox()
    return

# A button that shows instructions/guides when clicked
# Pass a string/list of strings for the screen/s to use
screen flapButton(screens_to_show):
    zorder 1
    if isinstance(screens_to_show, list):
        $ xoff = 0
        for scrn in screens_to_show:
            if isinstance(scrn, tuple):
                imagebutton:
                    idle Solid("#fff")
                    at t_flapButton
                    xsize 75
                    ysize 75
                    xalign 0.8
                    xoffset xoff
                    xanchor 0.5
                    action [Hide("flapButton"), ShowTransient(scrn[0], **scrn[1])]
            else:
                imagebutton:
                    idle Solid("#fff")
                    at t_flapButton
                    xsize 75
                    ysize 75
                    xalign 0.8
                    xoffset xoff
                    xanchor 0.5
                    action [Hide("flapButton"), ShowTransient(scrn)]
            $ xoff += 85
    else:
        imagebutton:
            idle Solid("#fff")
            at t_flapButton
            xsize 75
            ysize 75
            xpos 0.8
            xanchor 0.5
            action [Hide("flapButton"), ShowTransient(screens_to_show)]

screen instruction():
    modal True
    zorder 2
    frame:
        at t_instructions
        background Solid("#fff")
        xpos 0.5
        ypos 0.5
        xanchor 0.5
        yanchor 0.5
        vbox:
            text "INSTRUCTIONS":
                size 30
                xalign 0.5
                color "#000"
            null height 20
            text "{}".format(instructions[currentScreen]):
                color "#000"
            null height 20
            textbutton "Tap here to close":
                text_color "#000"
                xalign 0.5
                action [Hide("instruction"), Function(showFlapButtons)]

screen workitem_list:
    modal True
    zorder 2
    add Image("images/misc/paper.png"):
        at transform:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.5
            zoom 3.4
            on show:
                yoffset 700
                linear 0.5 yoffset 0
            on hide:
                yoffset 0
                linear 0.5 yoffset 700
    vbox:
        xanchor 0.5
        yanchor 0.5
        xoffset 12
        xpos 0.5
        ypos 0.4
        at transform:
            on show:
                yoffset 700
                linear 0.5 yoffset 0
            on hide:
                yoffset 0
                linear 0.5 yoffset 700
        text "ITEM CHECKLIST":
            xpos 0.5
            xanchor 0.5
            color "#000"
        null height 20
        $ items_needed = [item for item in onhand if not(item == 'bedkey')]
        for item in items_needed:
            $ it_cap = item.capitalize()
            showif onhand[item]:
                text "{s}[it_cap]{/s}":
                    xpos 0.5
                    xanchor 0.5
                    color "#000"
            else:
                text "[it_cap]":
                    xpos 0.5
                    xanchor 0.5
                    color "#000"
            null height 15

        null height 20

        textbutton "Tap to close":
            xpos 0.5
            xanchor 0.5
            text_color "#000"
            action [Hide("workitem_list"), Function(showFlapButtons)]

init python:
    def showFlapButtons():
        if currentScreen == "supermarket":
            img_dict = {"img":"images/misc/grocerylist.png"}
            renpy.show_screen("flapButton", screens_to_show=["instruction",
                                                            "price_list",
                                                            ("flyingImage", img_dict)
                                                            ], _transient=True)
        elif currentScreen == "workprep":
            renpy.show_screen("flapButton", screens_to_show=["instruction",
                                                             "workitem_list"
                                                            ], _transient=True)
