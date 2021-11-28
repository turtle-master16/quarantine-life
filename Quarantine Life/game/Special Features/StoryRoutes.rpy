init:
    define persistent.is_route_unlocked = {
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
    zorder 50

    $ route_coordinates = {
        "start.mainstart": (283, 318, 304, 37),
        "lockdown": (679, 433, 304, 37),
        "getcaught": (1119, 512, 304, 37),
        "quarantine": (1119, 352, 304, 37),
        "newnormal": (1517, 262, 304, 37),
        "newnormal.collectandprogress": (1920, 449, 304, 37),
        "commuting": (2330, 364, 304, 37),
        "friend": (2761, 251, 304, 37),
        "home": (2792, 487, 304, 37),
        "phonemale": (3233, 139, 304, 37),
        "phonefemale": (3211, 386, 304, 37),
        "princegoingout": (3240, 605, 304, 37),
        "firstdatemale": (3619, 140, 304, 37),
        "firstdatefemale": (3668, 325, 304, 37),
        "kyle": (3701, 536, 304, 37),
        "jason.meetupjason": (4122, 44, 304, 37),
        "jsexerciseend": (4079, 186, 304, 37),
        "jillian.restaurantdate": (4122, 263, 304, 37),
        "jillian.artsncraft": (4160, 407, 304, 37),
        "kylemeet": (4121, 487, 304, 37),
        "kylehome.findhobby": (4168, 639, 304, 37)
    }

    $ called_routes = {
        "phonemale": Call("phone", male=True),
        "phonefemale": Call("phone", male=False),
        "firstdatemale": Call("firstdate", male=True),
        "firstdatefemale": Call("firstdate", male=False),
    }

    viewport id "storyroute":
        draggable True

        imagemap:
            ground "images/menu/storyroutes/bg storyroute.png"

            imagebutton:
                    idle "images/menu/storyroutes/storyroute title.png"
                    xalign 0.005
                    yalign 0.03
                    action 0

            for route in route_coordinates:
                showif not(persistent.is_route_unlocked[route]):
                    imagebutton:
                        idle "images/menu/storyroutes/lockedroute.png"
                        xpos route_coordinates[route][0]
                        ypos route_coordinates[route][1]
                        action 0
                else:
                    if route in called_routes:
                         hotspot route_coordinates[route] action [Hide("storyroute"), Hide("flapButtons"), called_routes[route]]
                    else:
                        hotspot route_coordinates[route] action [Hide("storyroute"), Hide("flapButtons"), Jump(route)]

    imagebutton:
        idle "images/misc/black close.png"
        xalign 0.99
        yalign 0.02
        action Hide("storyroute")
