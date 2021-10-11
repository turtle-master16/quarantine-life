"""
    Stuff in this file are stuff shared by all the Point N' Click Screens
"""

define instructions = {
    "supermarket":
"""Get all the required items from the list (which can be viewed with the list
button on the lower left corner of the screen) and use your remaining budget for
buying extra items of your choice. The total cost of the required items and the
extra items should be EXACTLY ₱200.

Get items by tapping the item you want. After tapping, you will be asked to
choose how many of that item you would want to take or return one piece of that
item if you have any. You can use the ₱ button on the lower left part of
the screen to see the price of each item, how many items you have on hand, and
total cost of your items on hand.

Click on the cash register button on the lower right corner if you are done shopping.
""",
    "workprep":
"""Get all the items on the item checklist on the lower left corner of the screen.
Tap on objects to interact with them. Tap the arrows on the left or right side
of the screen to go to the other rooms. The item checklist will indicate which
items you already have and items still missing.

Click on the "i" button on the top right corner to review this instruction.
"""
}
# Conditional Variables
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

screen flyingImage(**kwargs):
    modal True
    zorder 1
    # Pass a dictionary with 'img' key with the value of the image to show
    imagebutton:
        idle kwargs.get('img')
        at t_flyingimage
        action [Hide("flyingImage"), Function(showFlapButtons)]

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
    if currentRoom == ROOMS['livingroom']:
        scene bg livingroom back
    elif currentRoom == ROOMS['bedroom']:
        scene bg bedroom back
    elif currentRoom == ROOMS['kitchen']:
        scene bg kitchen

    $ print currentRoom
    call hideStuff()
    $ print currentRoom

    $ islist = isinstance(dia, list)
    if islist:
        while dia:
            $ renpy.say(pl, dia.pop(0))
        return
    $ renpy.say(pl, dia)

    call hideStuff()

    if from_inputbox:
        call inputbox()
    return

# A button that shows instructions/guides when clicked
# Pass a string/list of strings for the screen/s to use
screen flapButton(screens_to_show, img_to_use):
    zorder 1
    if isinstance(screens_to_show, list):
        $ xoff = 0
        for scrn in screens_to_show:
            $ screen_index = screens_to_show.index(scrn)
            if isinstance(scrn, tuple):
                imagebutton:
                    idle img_to_use[screen_index]
                    at t_flapButton
                    xalign 0.04
                    xoffset xoff
                    xanchor 0.5
                    action [Hide("flapButton"), Show(scrn[0], **scrn[1])]
            else:
                if scrn == "instruction":
                    imagebutton:
                        idle img_to_use[screen_index]
                        xalign 0.96
                        yalign 0.06
                        xanchor 0.5
                        yanchor 0.5
                        at transform:
                            zoom 0.2
                            on show:
                                yoffset -100
                                linear 0.3 yoffset 0
                            on hide:
                                linear 0.3 yoffset -100
                        action [Hide("flapButton"), Show(scrn)]
                    $ xoff -= 110
                else:
                    imagebutton:
                        idle img_to_use[screen_index]
                        at t_flapButton
                        xalign 0.05
                        xoffset xoff
                        xanchor 0.5
                        action [Hide("flapButton"), Show(scrn)]
            $ xoff += 110
    else:
        imagebutton:
            idle Solid("#fff")
            at t_flapButton
            xsize 75
            ysize 75
            xpos 0.8
            xanchor 0.5
            action [Hide("flapButton"), Show(screens_to_show)]

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

init python:
    img_dict = {"img":"images/misc/grocerylist.png"}

    img_set = {
        "supermarket": (
            "images/misc/flapinstruction.png",
            "images/misc/flapgrocery.png",
            "images/misc/flapgrocerylist.png"
        ),
        "workprep": (
            "images/misc/flapinstruction.png",
            "images/misc/flapcheck.png"
        )
    }

    screen_set = {
        "supermarket": [
            "instruction",
            "price_list",
            ("flyingImage", img_dict)
        ],
        "workprep":[
            "instruction",
            "workitem_list",
        ]
    }

    def showFlapButtons():
        if currentScreen == "supermarket":
            img_dict = {"img":"images/misc/grocerylist.png"}
            renpy.show_screen("flapButton", screens_to_show=screen_set["supermarket"],
                                            img_to_use=img_set["supermarket"],
                                            _transient=True)
        elif currentScreen == "workprep":
            renpy.show_screen("flapButton", screens_to_show=screen_set["workprep"],
                                            img_to_use=img_set["workprep"],
                                            _transient=True)


transform t_flapButton:
    yanchor 1.0
    zoom 0.3
    on show:
        ypos 1.0
        yoffset 130
        linear 0.3 yoffset 0
    on hide:
        linear 0.3 yoffset 130

transform t_instructions:
    on show:
        yoffset 700
        linear 0.6 yoffset 0
    on hide:
        linear 0.6 yoffset 700

transform t_flyingimage:
    xanchor 0.5
    yanchor 0.5
    xpos 0.5
    ypos 0.5
    on show:
        yoffset 700
        linear 0.5 yoffset 0
    on hide:
        yoffset 0
        linear 0.5 yoffset 700
