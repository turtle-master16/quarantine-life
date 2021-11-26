"""
    Stuff in this file are stuff shared by all the Point N' Click Screens
"""

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
    if currentRoom == ROOMS['livingroom']:
        scene livingroom_workprep
    elif currentRoom == ROOMS['bedroom']:
        scene bedroom_workprep
    elif currentRoom == ROOMS['kitchen']:
        scene kitchen_workprep

    call hideStuff()

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

label initMinigame(name):
    $ renpy.call("resetItems") # Start game from scratch

    $ currentScreen = name
    show screen instruction # Show instructions before start

    $ taskpopout = "images/misc/taskpopups/{}.png".format(name)
    show screen notify(img=taskpopout) # Pop out Notif

    $ renpy.choice_for_skipping()

    $ renpy.jump(name) # Start minigame

    return

# Reset the state of minigames in order to prevent the Minigames from
# breaking after loading a save state or use of story routes
label resetItems():
    python:
        # For workprep
        currentRoom = ROOMS["livingroom"]
        for item in onhand:
            onhand[item] = False
        for item in lvroom_itemsC:
            lvroom_itemsC[item].interacted = False
        for item in lvroom_right:
            lvroom_right[item].interacted = False

        # For supermarket
        currentItemCost = 0
        for item in shopItems:
            shopItems[item].onhand = 0
    return
