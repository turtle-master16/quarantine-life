init:
    $ current_dialogevent_page = 1

    define persistent.is_dialog_unchecked = {
        "mandatoryhomequarantine.notstayinghome": False,
        "mandatoryhomequarantine.nowork": False,
        "mandatoryhomequarantine.remainpositive": False,
        "convowithcoworker.heyian": False,
        "convowithcoworker.imbusy": False,
        "convowithcoworker.stayaway": False,
        "greetingyourcoworker.illjoin": False,
        "greetingyourcoworker.nexttime": False,
        "invitationfromcoworker.soundsgood": False,
        "invitationfromcoworker.icant": False,
        "genderpreference.men": False,
        "genderpreference.women": False,
        "meetupwithjason.notsure": False,
        "meetupwithjason.soundsgood": False,
        "talkingtojillian.whatswrong": False,
        "talkingtojillian.pickupline": False,
        "hangoutwithjillian.askherout": False,
        "hangoutwithjillian.dontaskherout": False,
        "reconnectingfriend.hangout": False,
        "reconnectingfriend.stayhome": False
    }

screen dialogevents:
    modal True
    add Solid("#595171dd")
    zorder 50

    imagebutton:
            idle "images/misc/close.png"
            xalign 0.975
            yalign 0.05
            action Hide("dialogevents")

    frame:
        at t_dialogevents_notebook
        background "images/menu/dialogevents/notebook bg.png"

        showif current_dialogevent_page == 1:
            imagemap:
                at t_dialogevents_pages
                ground "images/menu/dialogevents/pages/page 1.png"

                imagebutton:
                        idle "images/menu/dialogevents/nextpage btn.png"
                        at t_dialogevents_nextpage
                        action SetVariable("current_dialogevent_page", 2)

                showif not(persistent.is_dialog_unchecked["mandatoryhomequarantine.notstayinghome"]):
                    imagebutton:
                        idle "images/menu/dialogevents/uncheckedbox.png"
                        xalign 0.24
                        yalign 0.165
                        action 0

                showif not(persistent.is_dialog_unchecked["mandatoryhomequarantine.nowork"]):
                    imagebutton:
                        idle "images/menu/dialogevents/uncheckedbox.png"
                        xalign 0.24
                        yalign 0.27
                        action 0

                showif not(persistent.is_dialog_unchecked["mandatoryhomequarantine.remainpositive"]):
                    imagebutton:
                        idle "images/menu/dialogevents/uncheckedbox.png"
                        xalign 0.24
                        yalign 0.385
                        action 0

                showif not(persistent.is_dialog_unchecked["convowithcoworker.heyian"]):
                    imagebutton:
                        idle "images/menu/dialogevents/uncheckedbox.png"
                        xalign 0.24
                        yalign 0.6
                        action 0

                showif not(persistent.is_dialog_unchecked["convowithcoworker.imbusy"]):
                    imagebutton:
                        idle "images/menu/dialogevents/uncheckedbox.png"
                        xalign 0.24
                        yalign 0.71
                        action 0

                showif not(persistent.is_dialog_unchecked["convowithcoworker.stayaway"]):
                    imagebutton:
                        idle "images/menu/dialogevents/uncheckedbox.png"
                        xalign 0.24
                        yalign 0.82
                        action 0

        elif current_dialogevent_page == 2:
            imagemap:
                at t_dialogevents_pages
                ground "images/menu/dialogevents/pages/page 2.png"

                imagebutton:
                    idle "images/menu/dialogevents/previouspage btn.png"
                    at t_dialogevents_previouspage
                    action SetVariable("current_dialogevent_page", 1)

                imagebutton:
                    idle "images/menu/dialogevents/nextpage btn.png"
                    at t_dialogevents_nextpage
                    action SetVariable("current_dialogevent_page", 3)

                showif not(persistent.is_dialog_unchecked["greetingyourcoworker.illjoin"]):
                    imagebutton:
                        idle "images/menu/dialogevents/uncheckedbox.png"
                        xalign 0.24
                        yalign 0.165
                        action 0

                showif not(persistent.is_dialog_unchecked["greetingyourcoworker.nexttime"]):
                    imagebutton:
                        idle "images/menu/dialogevents/uncheckedbox.png"
                        xalign 0.24
                        yalign 0.27
                        action 0

                showif not(persistent.is_dialog_unchecked["invitationfromcoworker.soundsgood"]):
                    imagebutton:
                        idle "images/menu/dialogevents/uncheckedbox.png"
                        xalign 0.24
                        yalign 0.47
                        action 0

                showif not(persistent.is_dialog_unchecked["invitationfromcoworker.icant"]):
                    imagebutton:
                        idle "images/menu/dialogevents/uncheckedbox.png"
                        xalign 0.24
                        yalign 0.58
                        action 0

        elif current_dialogevent_page == 3:
            imagemap:
                at t_dialogevents_pages
                ground "images/menu/dialogevents/pages/page 3.png"

                imagebutton:
                    idle "images/menu/dialogevents/previouspage btn.png"
                    at t_dialogevents_previouspage
                    action SetVariable("current_dialogevent_page", 2)

                imagebutton:
                    idle "images/menu/dialogevents/nextpage btn.png"
                    at t_dialogevents_nextpage
                    action SetVariable("current_dialogevent_page", 4)

                showif not(persistent.is_dialog_unchecked["genderpreference.men"]):
                    imagebutton:
                        idle "images/menu/dialogevents/uncheckedbox.png"
                        xalign 0.24
                        yalign 0.165
                        action 0

                showif not(persistent.is_dialog_unchecked["genderpreference.women"]):
                    imagebutton:
                        idle "images/menu/dialogevents/uncheckedbox.png"
                        xalign 0.24
                        yalign 0.27
                        action 0

                showif not(persistent.is_dialog_unchecked["meetupwithjason.notsure"]):
                    imagebutton:
                        idle "images/menu/dialogevents/uncheckedbox.png"
                        xalign 0.24
                        yalign 0.47
                        action 0

                showif not(persistent.is_dialog_unchecked["meetupwithjason.soundsgood"]):
                    imagebutton:
                        idle "images/menu/dialogevents/uncheckedbox.png"
                        xalign 0.24
                        yalign 0.58
                        action 0

        elif current_dialogevent_page == 4:
            imagemap:
                at t_dialogevents_pages
                ground "images/menu/dialogevents/pages/page 4.png"

                imagebutton:
                    idle "images/menu/dialogevents/previouspage btn.png"
                    at t_dialogevents_previouspage
                    action SetVariable("current_dialogevent_page", 3)

                imagebutton:
                    idle "images/menu/dialogevents/nextpage btn.png"
                    at t_dialogevents_nextpage
                    action SetVariable("current_dialogevent_page", 5)

                showif not(persistent.is_dialog_unchecked["talkingtojillian.whatswrong"]):
                    imagebutton:
                        idle "images/menu/dialogevents/uncheckedbox.png"
                        xalign 0.24
                        yalign 0.165
                        action 0

                showif not(persistent.is_dialog_unchecked["talkingtojillian.pickupline"]):
                    imagebutton:
                        idle "images/menu/dialogevents/uncheckedbox.png"
                        xalign 0.24
                        yalign 0.27
                        action 0

                showif not(persistent.is_dialog_unchecked["hangoutwithjillian.askherout"]):
                    imagebutton:
                        idle "images/menu/dialogevents/uncheckedbox.png"
                        xalign 0.24
                        yalign 0.47
                        action 0

                showif not(persistent.is_dialog_unchecked["hangoutwithjillian.dontaskherout"]):
                    imagebutton:
                        idle "images/menu/dialogevents/uncheckedbox.png"
                        xalign 0.24
                        yalign 0.58
                        action 0

        elif current_dialogevent_page == 5:
            imagemap:
                at t_dialogevents_pages
                ground "images/menu/dialogevents/pages/page 5.png"

                imagebutton:
                    idle "images/menu/dialogevents/previouspage btn.png"
                    at t_dialogevents_previouspage
                    action SetVariable("current_dialogevent_page", 4)

                showif not(persistent.is_dialog_unchecked["reconnectingfriend.hangout"]):
                    imagebutton:
                        idle "images/menu/dialogevents/uncheckedbox.png"
                        xalign 0.24
                        yalign 0.165
                        action 0

                showif not(persistent.is_dialog_unchecked["reconnectingfriend.stayhome"]):
                    imagebutton:
                        idle "images/menu/dialogevents/uncheckedbox.png"
                        xalign 0.24
                        yalign 0.27
                        action 0


transform t_dialogevents_notebook:
    xpos 0.15
    ypos 0.01

transform t_dialogevents_pages:
    xpos 0.027
    ypos 0.09

transform t_dialogevents_previouspage:
    xalign 0.12
    yalign 0.95

transform t_dialogevents_nextpage:
    xalign 0.93
    yalign 0.95
