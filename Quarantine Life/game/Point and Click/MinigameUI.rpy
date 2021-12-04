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

define persistent.minigame_completed = {
    "broomfind":    False,
    "findActivity": False,
    "workprep":     False,
    "supermarket":  False,
}
define post_minigame_label_jump_to = {
    "broomfind":    "post_broomfind",
    "findActivity": "newnormal",
    "workprep":     "workprep.post_workprep",
    "supermarket":  "supermarket.post_supermarket",
}

screen spark_toggle:
    zorder 5
    if not(currentScreen == ""):
        imagebutton:
            idle "spark_toggle"
            at transform:
                xalign 0.5
                yalign 0.96
                zoom 0.6
                on show:
                    alpha 0.0
                    linear 0.3 alpha 1.0
                on hide:
                    alpha 1.0
                    linear 0.3 alpha 0.0

            action ToggleScreen("spk")

default current_page = -1

# When current page is -1, it's currently at the objective page (first page of
# instruction)
screen instruction:
    zorder 30
    modal True
    $ i = instruct_data[currentScreen]
    $ isSkipAvailable = persistent.minigame_completed[currentScreen]
    $ last_page = i.pages if isSkipAvailable else i.pages - 1
    imagebutton:
        idle "black"
        action [If(current_page == last_page, [Hide("instruction"), SetVariable("current_page", -1)],
                                              SetVariable("current_page", current_page + 1))]

    frame:
        at transform:
            xalign 0.5 yalign 0.30 zoom 0.7

        if current_page <= 0:
            add i.bg alpha 1.0
        else:
            add i.bg alpha 0.5

        add "gui/quick/settings_icon.png":
            xalign 0.99 yalign 0.03 alpha 0.5

        for e in i.btn_set:
            if not(isinstance(e, str)):             # Only display e if it's not a string (string logic is after loop)
                if e == i.btn_set[current_page] and current_page > -1:
                    add e.img:                      # Emphasize the current element (based on current page)
                        at transform:
                            xalign e.xalign
                            yalign e.yalign
                            zoom e.zoom
                            alpha 1.0
                else:
                    # If e is a menu element or e is the skip element but it's unavailable, hide it
                    if e.isMenu or (not(isSkipAvailable) and e == general_btns["skip"]):
                        add e.img:
                            at transform:
                                xalign e.xalign
                                yalign e.yalign
                                zoom e.zoom
                                alpha 0.0
                    else:                           # Fade the rest of the elements
                        add e.img:
                            at transform:
                                xalign e.xalign
                                yalign e.yalign
                                zoom e.zoom
                                alpha 0.2

    if current_page == -1:                               # Objective
        text "{{b}}Objective: {}{{/b}}".format(i.objective):
            xalign 0.5 ycenter 0.90
            xsize 0.8 text_align 0.5
    else:
        if isinstance(i.btn_set[current_page], str):     # Text Instruction (No emphasized element)
            text "{{b}}{}{{/b}}".format(i.btn_set[current_page]):
                xalign 0.5 ycenter 0.90
                xsize 0.8 text_align 0.5
        else:                                            # If it is a InstructionElement Object, get it's desc field
            text "{{b}}{}{{/b}}".format(i.btn_set[current_page].desc):
                xalign 0.5 ycenter 0.90
                xsize 0.8 text_align 0.5

screen supermarket_ui:
    imagebutton:
        idle "images/supermarket/inactive_basket_btn.png"
        hover "images/supermarket/basket_btn.png"
        xalign 0.98
        yalign 0.95
        action ShowTransient("basketMenu")
    imagebutton:
        idle "images/supermarket/groceryList_icon.png"
        xalign 0.83
        yalign 0.95
        at third
        action ShowTransient("fly_in_image", img="images/supermarket/grocery_list.png")

screen workprep_ui:
    imagebutton:
        idle "images/misc/flapcheck.png"
        xalign 0.8
        yalign 1.0
        at transform:
            zoom 0.3
        action ShowTransient("workitem_list")

screen ui_start:
    zorder 20
    imagebutton:
        idle "gui/quick/settings_icon.png"
        xalign 0.99 yalign 0.03
        action ShowMenu("preferences")
    if not(currentScreen == ""):
        imagebutton:
            idle "gui/quick/instructions_icon.png"
            xalign 0.9 yalign 0.03
            action [ShowTransient("instruction"), Hide("spark_toggle")]
        if persistent.minigame_completed[currentScreen]:
            imagebutton:
                idle "gui/quick/skipGame_btn.png"
                xalign 0.84 yalign 0.00
                action Show("confirm", message="Do you want to skip this minigame?", yes_action=Function(minigame_end), no_action=Hide("confirm"))
    use skip_stopper
    use quickToggle

transform t_flyingimage:
    xalign 0.5
    yalign 0.5
    on show:
        yoffset 700
        linear 0.5 yoffset 0
    on hide:
        yoffset 0
        linear 0.5 yoffset 700

screen fly_in_image(img):
    zorder 2
    modal True
    add Solid("#61564388")

    imagebutton:
        idle img
        at t_flyingimage
        action Hide("fly_in_image")
