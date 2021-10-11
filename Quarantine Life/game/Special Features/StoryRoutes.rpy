init:
    $ is_route_unlocked = {
        "start.mainstart": False,
        "lockdown": False,
        "getcaught": False,
        "quarantine": False,
        "newnormal": False,
        "newnormal.collectandprogress": False,
        "commuting": False,
        "friend": False,
        "home": False,
        "phonemale": False,
        "phonefemale": False,
        "princegoingout": False,
        "firstdatemale": False,
        "firstdatefemale": False,
        "kyle": False,
        "jason.meetupjason": False,
        "jsexerciseend": False,
        "jillian.restaurantdate": False,
        "jillian.artsncraft": False,
        "kylemeet": False,
        "kylehome.findhobby": False
    }

screen storyroute:
    $ route_coordinates = {
        "start.mainstart": (66, 377, 306, 51),
        "lockdown": (459, 378, 306, 47),
        "getcaught": (935, 339, 306, 45),
        "quarantine": (935, 450, 306, 47),
        "newnormal": (1360, 497, 307, 46),
        "newnormal.collectandprogress": (1750, 388, 306, 49),
        "commuting": (2142, 421, 303, 50),
        "friend": (2530, 347, 307, 45),
        "home": (2530, 567, 306, 46),
        "phonemale": (2944, 287, 306, 47),
        "phonefemale": (2999, 483, 307, 48),
        "princegoingout": (2913, 654, 309, 48),
        "firstdatemale": (3363, 211, 307, 49),
        "firstdatefemale": (3407, 430, 310, 49),
        "kyle": (3472, 654, 306, 47),
        "jason.meetupjason": (3880, 96, 311, 49),
        "jsexerciseend": (3840, 256, 309, 49),
        "jillian.restaurantdate": (3883, 358, 306, 49),
        "jillian.artsncraft": (3981, 531, 304, 44),
        "kylemeet": (3957, 611, 307, 47),
        "kylehome.findhobby": (3898, 769, 307, 46)
    }

    viewport id "storyroute":
        draggable True

        imagemap:
            ground "images/menu/storyroutes/bg storyroute.png"

            showif not(is_route_unlocked["start.mainstart"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.0165
                    yalign 0.445
                    action 0
            else:
                hotspot route_coordinates["start.mainstart"] action [Hide("storyroute"), Jump("start.mainstart")]

            showif not(is_route_unlocked["lockdown"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.114
                    yalign 0.445
                    action 0
            else:
                hotspot route_coordinates["lockdown"] action [Hide("storyroute"), Jump("lockdown")]

            showif not(is_route_unlocked["getcaught"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.2305
                    yalign 0.4
                    action 0
            else:
                hotspot route_coordinates["getcaught"] action [Hide("storyroute"), Jump("getcaught")]

            showif not(is_route_unlocked["quarantine"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.2305
                    yalign 0.53
                    action 0
            else:
                hotspot route_coordinates["quarantine"] action [Hide("storyroute"), Jump("quarantine")]

            showif not(is_route_unlocked["newnormal"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.335
                    yalign 0.583
                    action 0
            else:
                hotspot route_coordinates["newnormal"] action [Hide("storyroute"), Jump("newnormal")]

            showif not(is_route_unlocked["newnormal.collectandprogress"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.4311
                    yalign 0.456
                    action 0
            else:
                hotspot route_coordinates["newnormal.collectandprogress"] action [Hide("storyroute"), Jump("newnormal.collectandprogress")]

            showif not(is_route_unlocked["commuting"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.5275
                    yalign 0.499
                    action 0
            else:
                hotspot route_coordinates["commuting"] action [Hide("storyroute"), Jump("newnormal.collectandprogress")]

            showif not(is_route_unlocked["friend"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.6243
                    yalign 0.41
                    action 0
            else:
                hotspot route_coordinates["friend"] action [Hide("storyroute"), Jump("friend")]

            showif not(is_route_unlocked["home"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.6243
                    yalign 0.665
                    action 0
            else:
                hotspot route_coordinates["home"] action [Hide("storyroute"), Jump("home")]

            showif not(is_route_unlocked["phonemale"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.7255
                    yalign 0.339
                    action 0
            else:
                hotspot route_coordinates["phonemale"] action [Hide("storyroute"), Call("phone", male=True)]

            showif not(is_route_unlocked["phonefemale"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.74
                    yalign 0.568
                    action 0
            else:
                hotspot route_coordinates["phonefemale"] action [Hide("storyroute"), Call("phone", male=False)]

            showif not(is_route_unlocked["princegoingout"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.7178
                    yalign 0.769
                    action 0
            else:
                hotspot route_coordinates["princegoingout"] action [Hide("storyroute"), Jump("princegoingout")]

            showif not(is_route_unlocked["firstdatemale"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.829
                    yalign 0.248
                    action 0
            else:
                hotspot route_coordinates["firstdatemale"] action [Hide("storyroute"), Call("firstdate", male=True)]

            showif not(is_route_unlocked["firstdatefemale"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.8396
                    yalign 0.508
                    action 0
            else:
                hotspot route_coordinates["firstdatefemale"] action [Hide("storyroute"), Call("firstdate", male=False)]

            showif not(is_route_unlocked["kyle"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.8552
                    yalign 0.767
                    action 0
            else:
                hotspot route_coordinates["kyle"] action [Hide("storyroute"), Jump("kyle")]

            showif not(is_route_unlocked["jason.meetupjason"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.9575
                    yalign 0.117
                    action 0
            else:
                hotspot route_coordinates["jason.meetupjason"] action [Hide("storyroute"), Jump("jason.meetupjason")]

            showif not(is_route_unlocked["jsexerciseend"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.9456
                    yalign 0.303
                    action 0
            else:
                hotspot route_coordinates["jsexerciseend"] action [Hide("storyroute"), Jump("jsexerciseend")]

            showif not(is_route_unlocked["jillian.restaurantdate"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.9571
                    yalign 0.425
                    action 0
            else:
                hotspot route_coordinates["jillian.restaurantdate"] action [Hide("storyroute"), Jump("jillian.restaurantdate")]

            showif not(is_route_unlocked["jillian.artsncraft"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.9817
                    yalign 0.625
                    action 0
            else:
                hotspot route_coordinates["jillian.artsncraft"] action [Hide("storyroute"), Jump("jillian.artsncraft")]

            showif not(is_route_unlocked["kylemeet"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.9755
                    yalign 0.721
                    action 0
            else:
                hotspot route_coordinates["kylemeet"] action [Hide("storyroute"), Jump("kylemeet")]

            showif not(is_route_unlocked["kylehome.findhobby"]):
                imagebutton:
                    idle "images/menu/storyroutes/lockedroute.png"
                    xalign 0.96
                    yalign 0.904
                    action 0
            else:
                hotspot route_coordinates["kylehome.findhobby"] action [Hide("storyroute"), Jump("kylehome.findhobby")]
