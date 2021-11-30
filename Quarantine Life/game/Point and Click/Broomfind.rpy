# Since it's a 'short' screen, I mixed it in with find activity screen
screen broomfind():
    $ renpy.choice_for_skipping()
    $ spr_is_on = renpy.get_screen("spk")
    $ lvroom_items = {
        "cups":   (440, 457, 113, 49),
        "lamp":   (108, 418, 69, 166),
        "mirror": (126, 201, 46, 159),
        "sofa":   (207, 508, 178, 168),
        "tv":     (1012, 286, 134, 241),
        "plant":  [(284, 416, 60, 83),
                  (503, 301, 77, 105),
                  (744, 295, 69, 107),
                  (846, 401, 72, 119)],
        "chime":  (716, 169, 54, 88),
    }
    $ item_dialogue = {
        "cups":   "I don't have time to admire cups.",
        "lamp":   "I can't sweep the floor with this.",
        "mirror": "Hey! You in the mirror, Where did you put the broom?",
        "sofa":   "Now's not the time to relax, I got a broom to find.",
        "tv":     "I really want to watch something right now, but I got some tasks to do.",
        "plant":  "These plants won't make a good broom. Unfortunately.",
        "chime":  "One of those noisy chimes.",
    }
    imagemap:
        xalign 1.0 yalign 1.0
        ground "bg/bg living room animated/6.png"
        hotspot (1177, 363, 95, 351) action [Return("broom"), Function(hideGameScreens)]
        for item in lvroom_items:
            if isinstance(lvroom_items[item], list):
                for subitem in lvroom_items[item]:
                    hotspot subitem action Call("objDialogue", dia=item_dialogue[item])
            else:
                hotspot lvroom_items[item] action Call("objDialogue", dia=item_dialogue[item])
        if spr_is_on:
            for item in lvroom_items:
                if isinstance(lvroom_items[item], list):
                    for subitem in lvroom_items[item]:
                        add "spark":
                            pos getRectCenter(subitem)
                else:
                    add "spark":
                        pos getRectCenter(lvroom_items[item])
    add "images/clickables/broom.png":
        at right_corner
    if spr_is_on:
        add "spark":
            pos getRectCenter((1160, 363, 95, 351))
