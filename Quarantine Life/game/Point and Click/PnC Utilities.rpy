init python:
    # Used at the end of minigames/Use of story route
    def hideGameScreens():
        renpy.hide_screen("spark_toggle")
        renpy.hide_screen("spk")
        renpy.hide_screen("phone_message")
        xTraHide("workprep_ui")
        renpy.hide_screen("supermarket_ui")
        renpy.hide_screen("storyroute")
        renpy.hide_screen("confirm")
        globals()['quickMenuHide'] = False
        globals()['currentScreen'] = None
        globals()['currentRoom'] = ROOMS["livingroom"]
        return

    def minigame_end():
        persistent.minigame_completed[currentScreen] = True
        curScr = currentScreen
        hideGameScreens()
        if not(renpy.is_skipping()):
            renpy.show_screen("notify", img="images/misc/taskpopups/taskcomplete.png")
        renpy.jump(post_minigame_label_jump_to[curScr])
        return

# For room switching
define ROOMS = {
    "livingroom":1,
    "bedroom":2,
    "kitchen":3
}
default currentRoom = ROOMS['livingroom']
default currentScreen = None # Tells which minigame is on screen at the moment

label hideStuff():
    # (Mainly for workprep minigame)
    # Hide the takeable/roomstate item when switching rooms
    # to prevent it from showing in the new room.
    python:
        location = {
            ROOMS['livingroom']: ["faceshield", "bedkey"],
            ROOMS['bedroom']:    ["wallet", "facemask"],
            ROOMS['kitchen']:    ["sanitizer"],
        }
        left_side = {
            "facemask": "bedleft",
            "bedkey":   "livingleft"
        }
        right_side = {
            "faceshield": "livingright",
            "wallet":     "bedright",
            "sanitizer":  "kitchenright"
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

# Calls the say screen when an hotspot/imgbtn is clicked
label objDialogue(dia, from_inputbox=False):
    # Keeps the items visible/not visible while in this label
    show screen ui_start
    if currentScreen == "workprep":
        if currentRoom == ROOMS['livingroom']:
            scene livingroom_workprep
        elif currentRoom == ROOMS['bedroom']:
            scene bedroom_workprep
        elif currentRoom == ROOMS['kitchen']:
            scene kitchen_workprep

    if currentScreen == "broomfind":
        scene lvroom_frm7
        show broom at right_corner
        $ onhand["bedkey"] = True
        $ onhand["faceshield"] = True

    call hideStuff()

    $ islist = isinstance(dia, list)
    if islist:
        while dia:
            $ renpy.say(pl, dia.pop(0))
        return
    $ renpy.say(pl, dia)

    call hideStuff()

    if from_inputbox:
        show screen inputbox(_transient=True)
    return

# Initialize the minigame
label initMinigame(name):

    $ renpy.call("resetItems") # Start game from scratch

    $ currentScreen = name

    $ quickMenuHide = True

    $ taskpopout = "images/misc/taskpopups/{}.png".format(name)

    if renpy.is_skipping():
        if persistent.skip_complete_games and persistent.minigame_completed[currentScreen]:
            $ minigame_end()
        else:
            show screen notify(img=taskpopout)
            $ renpy.choice_for_skipping()
            $ Skip(fast=False, confirm=False) # Stop skip
            $ config.skipping = False
    else:
        show screen notify(img=taskpopout)

    $ renpy.jump(name) # Start minigame

    return

# Reset the state of minigames in order to prevent the Minigames from
# breaking after loading a save state or use of story routes
label resetItems():
    python:
        # For workprep
        currentScreen = None
        currentRoom = ROOMS["livingroom"]
        for item in onhand:
            onhand[item] = False
        ansA=ansB=ansC=ansD = 0

        # For supermarket
        currentItemCost = 0
        for item in shopItems:
            shopItems[item].onhand = 0

        # For quiz game
        correctans = 0
        currentQuestion = 1
    return
