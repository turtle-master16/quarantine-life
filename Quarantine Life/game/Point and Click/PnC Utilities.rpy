"""
    Stuff in this file are stuff shared by all the Point N' Click Screens
"""
# Conditional Variables
default itemselected = ""
default itemchoices = {"Reset":0, "A": 1, "B": 2, "C":3, "D":4, "E":5, "F":6}
default correctans = 0 # Quiz game
#--------------------

# For room switching
define ROOMS = {
    "livingroom":1,
    "bedroom":2,
    "kitchen":3
}
default currentRoom = ROOMS['livingroom']

label hideStuff(item, location, isState=False):
    # Hide the takeable/roomstate item when switching rooms
    # to prevent it from showing in the new room.
    if isState:
        if not(roomstatus["drawerclosed"]) and (currentRoom == ROOMS[location]):
            $ renpy.show("draweropen", at_list=[takeables['drawerclosed']], layer="master")
        else:
            $ renpy.hide("draweropen", layer="master")
        if (roomstatus["boxclosed"]) and (currentRoom == ROOMS[location]):
            $ renpy.show("boxclosed", at_list=[takeables['boxclosed']], layer="master")
        elif not(roomstatus["boxclosed"]) and (currentRoom == ROOMS[location]):
            if not(onhand['facemask']):
                $ renpy.show("boxwithmask", at_list=[takeables['boxclosed']], layer="master")
                $ renpy.hide("boxclosed", layer="master")
            else:
                $ renpy.show("boxnomask", at_list=[takeables['boxnomask']], layer="master")
                $ renpy.hide("boxwithmask", layer="master")
        return
    else:
        if currentRoom == ROOMS[location]:
            if not(onhand[item]):
                if (item=="wallet") and (roomstatus['drawerclosed']):
                    return
                $ renpy.show(item, at_list=[takeables[item]])
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
