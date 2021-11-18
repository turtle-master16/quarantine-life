init python:
    img_set = {
        "supermarket": (
            "images/misc/flapgrocery.png",
            "images/misc/flapgrocerylist.png"
        ),
        "workprep": (
            "images/misc/flapcheck.png",
        )
    }

    screen_set = {
        "supermarket": [
            "price_list",
            ("flyingImage", "images/misc/grocerylist.png"),
        ],
        "workprep":[
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
        renpy.show_screen("flap_instruction", _transient=True)

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

# Displays buttons that shows instructions/guides when clicked
# Pass a list of strings with the names of the screens to use
screen flapButton(screens_to_show, img_to_use):
    zorder 1
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
                action [Hide("flapButton"), Show(scrn[0], img_to_use=scrn[1])]
        else:
            imagebutton:
                idle img_to_use[screen_index]
                at t_flapButton
                xalign 0.05
                xoffset xoff
                xanchor 0.5
                action [Hide("flapButton"), Show(scrn)]
        $ xoff += 110

screen instruction():
    modal True
    zorder 2
    frame:
        at t_instructions
        background Solid("#fff")
        xalign 0.5
        yalign 0.5
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

screen flap_instruction():
    zorder 1
    imagebutton:
        idle "images/misc/flapinstruction.png"
        at t_flapInstructions
        action [Hide("flapButton"), Hide("flap_instruction"), Show("instruction")]

screen flyingImage(img_to_use):
    modal True
    zorder 1
    imagebutton:
        idle img_to_use
        at t_flyingimage
        action [Hide("flyingImage"), Function(showFlapButtons)]


transform t_flapInstructions:
    xalign 0.96
    yalign 0.06
    xanchor 0.5
    yanchor 0.5
    zoom 0.2
    on show:
        yoffset -100
        linear 0.3 yoffset 0
    on hide:
        linear 0.3 yoffset -100

transform t_instructions:
    on show:
        yoffset 700
        linear 0.6 yoffset 0
    on hide:
        linear 0.6 yoffset 700

transform t_flyingimage:
    xalign 0.5
    yalign 0.5
    on show:
        yoffset 700
        linear 0.5 yoffset 0
    on hide:
        yoffset 0
        linear 0.5 yoffset 700
