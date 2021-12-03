# Activity Pick ------------------
screen findActivity():
    $ renpy.choice_for_skipping()
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
            ground "clickables/lvroom_frm7.png"
            hotspot lvroom_items["tv"] action Return('tv')
        imagebutton:
            idle "images/misc/inactive_arrow.png"
            hover "images/misc/arrow.png"
            yalign 0.5
            action [SetVariable("currentRoom" ,ROOMS['bedroom']),
                    Show("patientOverlay", date="April 2020, Week 1|09:00 AM|ECQ", status="happy")]
    elif currentRoom == ROOMS['bedroom']:
        imagemap:
            ground "clickables/bedroom_frm7.png"
            hotspot bdroom_items["phone"] action Return('phone')
            hotspot bdroom_items["dumbells"] action Return('dumbells')
            hotspot bdroom_items["bed"] action Return('bed')
        imagebutton:
            idle im.Flip("images/misc/inactive_arrow.png", horizontal=True)
            hover im.Flip("images/misc/arrow.png", horizontal=True)
            xalign 1.0
            yalign 0.5
            action [SetVariable("currentRoom" ,ROOMS['livingroom']),
                    Show("patientOverlay", date="April 2020, Week 1|09:00 AM|ECQ", status="happy")]

    use spark_toggle
