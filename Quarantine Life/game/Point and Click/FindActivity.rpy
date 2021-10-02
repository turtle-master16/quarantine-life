# Since it's a 'short' screen, I mixed it in with find activity screen
screen broomfind():
    $ broom_location = Transform(xpos=0.93, ypos=0.96, xanchor=0.5, yanchor=1.0, zoom=0.51)
    imagebutton:
        idle "clickables/broom.png"
        at broom_location
        action Return()

# Activity Pick ------------------
screen findActivity():
    layer "background"
    $ lvroom_items = {
        "tv":(986, 296, 118, 234),
    }
    $ bdroom_items = {
        "phone":(195, 338, 80, 52),
        "dumbells": (918, 374, 158, 121),
        "bed": (64, 424, 632, 157),
    }
    if currentRoom == ROOMS['livingroom']:
        imagemap:
            ground "images/bg/bg livingroom back.png"
            hotspot lvroom_items["tv"] action Return('tv')
        imagebutton:
            idle "images/misc/arrow.png"
            yalign 0.5
            action [SetVariable("currentRoom" ,ROOMS['bedroom']),
                    Call("updateDate", "April 2020, 9:00 am, Week 1, Bedroom, ECQ")]
    elif currentRoom == ROOMS['bedroom']:
        imagemap:
            ground "images/bg/bg bedroom back.png"
            hotspot bdroom_items["phone"] action Return('phone')
            hotspot bdroom_items["dumbells"] action Return('dumbells')
            hotspot bdroom_items["bed"] action Return('bed')
        imagebutton:
            idle im.Flip("images/misc/arrow.png", horizontal=True)
            xalign 1.0
            yalign 0.5
            action [SetVariable("currentRoom" ,ROOMS['livingroom']),
                    Call("updateDate", "April 2020, 9:00 am, Week 1, Living room, ECQ")]
