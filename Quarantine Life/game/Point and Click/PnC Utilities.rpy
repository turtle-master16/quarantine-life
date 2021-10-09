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

label hideStuff(item, room, isState=False):
    # Hide the takeable/roomstate item when switching rooms
    # to prevent it from showing in the new room.
    if isState:
        if not(roomstatus["drawerclosed"]) and (currentRoom == ROOMS[room]):
            $ renpy.show("draweropen", at_list=[workprep_item_placement['drawerclosed']], layer="master")
        else:
            $ renpy.hide("draweropen", layer="master")
        if (roomstatus["boxclosed"]) and (currentRoom == ROOMS[room]):
            $ renpy.show("boxclosed", at_list=[workprep_item_placement['boxclosed']], layer="master")
        elif not(roomstatus["boxclosed"]) and (currentRoom == ROOMS[room]):
            if not(onhand['facemask']):
                $ renpy.show("boxwithmask", at_list=[workprep_item_placement['boxclosed']], layer="master")
                $ renpy.hide("boxclosed", layer="master")
            else:
                $ renpy.show("boxnomask", at_list=[workprep_item_placement['boxnomask']], layer="master")
                $ renpy.hide("boxwithmask", layer="master")
        return
    else:
        if currentRoom == ROOMS[room]:
            if not(onhand[item]):
                if (item=="wallet") and (roomstatus['drawerclosed']):
                    return
                $ renpy.show(item, at_list=[workprep_item_placement[item]])
            else:
                $ renpy.hide(item, layer="master")
        return
# ------------------

label objDialogue(dia, from_inputbox=False):
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
    if from_inputbox:
        call inputbox()
    return

# A button that shows instructions/guides when clicked
# Pass a string/list of strings for the screen/s to use
screen flapButton(screen_to_show, args={}):
    zorder 1
    $ islist = isinstance(screen_to_show, list)
    if islist:
        $ xoff = 0
        for scrn in screen_to_show:
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
            action [Hide("flapButton"), ShowTransient(screen_to_show)]

screen instruction:
    modal True
    zorder 1
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
    def showFlapButtons():
        if currentScreen == "supermarket":
            renpy.show_screen("flapButton", screen_to_show=["instruction", "price_list"], _transient=True)