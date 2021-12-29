init:
    $ current_achievement_sidebar = 1
    $ current_achievement_page = ''

    define persistent.is_achievement_unlocked = {
        "minimum public health standard": False,
        "ecq": False,
        "mecq": False,
        "gcq": False,
        "flexible learning": False,
        "public transportation": False,
        "company shuttle": False,
        "food establishment operation": False,
        "grocery shopping": False,
        "online shopping": False,
        "quarantine age restriction": False,
        "restaurant operation": False,
        "home work out": False,
        "what to do if someone is sick": False,
        "covid symptoms": False,
        "prevent the spread of covid19": False,
        "how to properly wear a mask": False
    }

init python:
    def showAchievementOverlay(achievement):
        if persistent.is_achievement_unlocked[achievement]:
            return

        persistent.is_achievement_unlocked[achievement] = True
        renpy.show_screen("achievementoverlay", achievement=achievement)
        renpy.with_statement(Dissolve(1.0))
        renpy.pause(1.0)
        renpy.hide_screen("achievementoverlay")
        renpy.with_statement(Dissolve(1.5))
        renpy.pause(1.5)
        renpy.save_persistent()

transform popupzoom:
    zoom 1.3
    xalign 0.5
    yalign 0.9

screen achievementoverlay(achievement):
    add Solid("#F9B83455")

    if achievement == "minimum public health standard":
        imagebutton:
            idle "images/menu/achievements/achievement popups/Minimum Public Health Standard.png"
            at popupzoom
            action 0

    elif achievement == "ecq":
        imagebutton:
            idle "images/menu/achievements/achievement popups/Enhanced Community Quarantine.png"
            at popupzoom
            action 0

    elif achievement == "mecq":
        imagebutton:
            idle "images/menu/achievements/achievement popups/Modified Enhanced Community Quarantine.png"
            at popupzoom
            action 0

    elif achievement == "gcq":
        imagebutton:
            idle "images/menu/achievements/achievement popups/General Community Quarantine.png"
            at popupzoom
            action 0

    elif achievement == "flexible learning":
        imagebutton:
            idle "images/menu/achievements/achievement popups/Flexible Learning.png"
            at popupzoom
            action 0

    elif achievement == "public transportation":
        imagebutton:
            idle "images/menu/achievements/achievement popups/Public Transportation.png"
            at popupzoom
            action 0

    elif achievement == "company shuttle":
        imagebutton:
            idle "images/menu/achievements/achievement popups/Company Shuttle.png"
            at popupzoom
            action 0

    elif achievement == "food establishment operation":
        imagebutton:
            idle "images/menu/achievements/achievement popups/Food Establishment Operation.png"
            at popupzoom
            action 0

    elif achievement == "grocery shopping":
        imagebutton:
            idle "images/menu/achievements/achievement popups/Grocery Shopping.png"
            at popupzoom
            action 0

    elif achievement == "online shopping":
        imagebutton:
            idle "images/menu/achievements/achievement popups/Online Shopping.png"
            at popupzoom
            action 0

    elif achievement == "quarantine age restriction":
        imagebutton:
            idle "images/menu/achievements/achievement popups/Quarantine Age Restriction.png"
            at popupzoom
            action 0

    elif achievement == "restaurant operation":
        imagebutton:
            idle "images/menu/achievements/achievement popups/Restaurant Operation.png"
            at popupzoom
            action 0

    elif achievement == "home work out":
        imagebutton:
            idle "images/menu/achievements/achievement popups/Home Work Out.png"
            at popupzoom
            action 0

    elif achievement == "what to do if someone is sick":
        imagebutton:
            idle "images/menu/achievements/achievement popups/What To Do If Someone Is Sick.png"
            at popupzoom
            action 0

    elif achievement == "covid symptoms":
        imagebutton:
            idle "images/menu/achievements/achievement popups/COVID-19 Symptoms.png"
            at popupzoom
            action 0

    elif achievement == "prevent the spread of covid19":
        imagebutton:
            idle "images/menu/achievements/achievement popups/Prevent the Spread of COVID-19.png"
            at popupzoom
            action 0

    elif achievement == "how to properly wear a mask":
        imagebutton:
            idle "images/menu/achievements/achievement popups/How to Properly Wear a Mask.png"
            at popupzoom
            action 0

screen achievements:
    modal True
    add Solid("#43403edd")
    zorder 50

    imagebutton:
        idle "images/misc/close.png"
        xalign 0.975
        yalign 0.05
        action Hide("achievements")

    imagebutton:
        idle "images/menu/achievements/achievement title.png"
        xalign 0.035
        yalign 0.06
        action 0

    showif current_achievement_sidebar == 1:
        imagemap:
            ground "images/menu/achievements/achievement sidebar/list 1.png"
            xalign 0.04
            yalign 0.54

            showif not(persistent.is_achievement_unlocked["minimum public health standard"]):
                imagebutton:
                    idle "images/menu/achievements/achievement sidebar/list lock.png"
                    yalign 0.01
                    action 0
            else:
                hotspot (3,2,379,84) action SetVariable("current_achievement_page", "minimum public health standard pt 1")

            showif not(persistent.is_achievement_unlocked["ecq"]):
                imagebutton:
                    idle "images/menu/achievements/achievement sidebar/list lock.png"
                    yalign 0.25
                    action 0
            else:
                hotspot (3,99,380,88) action SetVariable("current_achievement_page", "ecq")

            showif not(persistent.is_achievement_unlocked["mecq"]):
                imagebutton:
                    idle "images/menu/achievements/achievement sidebar/list lock.png"
                    yalign 0.5
                    action 0
            else:
                hotspot (1,200,381,85) action SetVariable("current_achievement_page", "mecq")

            showif not(persistent.is_achievement_unlocked["gcq"]):
                imagebutton:
                    idle "images/menu/achievements/achievement sidebar/list lock.png"
                    yalign 0.75
                    action 0
            else:
                hotspot (3,299,380,85) action SetVariable("current_achievement_page", "gcq")

            showif not(persistent.is_achievement_unlocked["flexible learning"]):
                imagebutton:
                    idle "images/menu/achievements/achievement sidebar/list lock.png"
                    yalign 0.99
                    action 0
            else:
                hotspot (2,399,381,88) action SetVariable("current_achievement_page", "flexible learning")

    elif current_achievement_sidebar == 2:
        imagemap:
            ground "images/menu/achievements/achievement sidebar/list 2.png"
            xalign 0.04
            yalign 0.54

            showif not(persistent.is_achievement_unlocked["public transportation"]):
                imagebutton:
                        idle "images/menu/achievements/achievement sidebar/list lock.png"
                        yalign 0.01
                        action 0
            else:
                hotspot (1,0,381,86) action SetVariable("current_achievement_page", "public transportation pt 1")

            showif not(persistent.is_achievement_unlocked["company shuttle"]):
                imagebutton:
                    idle "images/menu/achievements/achievement sidebar/list lock.png"
                    yalign 0.25
                    action 0
            else:
                hotspot (1,99,382,88) action SetVariable("current_achievement_page", "company shuttle")

            showif not(persistent.is_achievement_unlocked["food establishment operation"]):
                imagebutton:
                    idle "images/menu/achievements/achievement sidebar/list lock.png"
                    yalign 0.5
                    action 0
            else:
                hotspot (2,198,379,86) action SetVariable("current_achievement_page", "food establishment operation")

            showif not(persistent.is_achievement_unlocked["grocery shopping"]):
                imagebutton:
                    idle "images/menu/achievements/achievement sidebar/list lock.png"
                    yalign 0.75
                    action 0
            else:
                hotspot (2,297,381,88) action SetVariable("current_achievement_page", "grocery shopping")

            showif not(persistent.is_achievement_unlocked["online shopping"]):
                imagebutton:
                        idle "images/menu/achievements/achievement sidebar/list lock.png"
                        yalign 0.99
                        action 0
            else:
                hotspot (3,400,379,87) action SetVariable("current_achievement_page", "online shopping")

    elif current_achievement_sidebar == 3:
        imagemap:
            ground "images/menu/achievements/achievement sidebar/list 3.png"
            xalign 0.04
            yalign 0.54

            showif not(persistent.is_achievement_unlocked["quarantine age restriction"]):
                imagebutton:
                    idle "images/menu/achievements/achievement sidebar/list lock.png"
                    yalign 0.01
                    action 0
            else:
                hotspot (2,0,384,85) action SetVariable("current_achievement_page", "quarantine age restriction")

            showif not(persistent.is_achievement_unlocked["restaurant operation"]):
                imagebutton:
                    idle "images/menu/achievements/achievement sidebar/list lock.png"
                    yalign 0.25
                    action 0
            else:
                hotspot (2,99,382,85) action SetVariable("current_achievement_page", "restaurant operation pt 1")

            showif not(persistent.is_achievement_unlocked["home work out"]):
                imagebutton:
                    idle "images/menu/achievements/achievement sidebar/list lock.png"
                    yalign 0.5
                    action 0
            else:
                hotspot (1,197,382,86) action SetVariable("current_achievement_page", "home work out pt 1")

            showif not(persistent.is_achievement_unlocked["what to do if someone is sick"]):
                imagebutton:
                    idle "images/menu/achievements/achievement sidebar/list lock.png"
                    yalign 0.75
                    action 0
            else:
                hotspot (2,295,380,86) action SetVariable("current_achievement_page", "what to do if someone is sick pt 1")

            showif not(persistent.is_achievement_unlocked["covid symptoms"]):
                imagebutton:
                    idle "images/menu/achievements/achievement sidebar/list lock.png"
                    yalign 0.99
                    action 0
            else:
                hotspot (1,395,382,88) action SetVariable("current_achievement_page", "covid symptoms")

    elif current_achievement_sidebar == 4:
        imagemap:
            ground "images/menu/achievements/achievement sidebar/list 4.png"
            xalign 0.04
            yalign 0.24

            showif not(persistent.is_achievement_unlocked["prevent the spread of covid19"]):
                imagebutton:
                    idle "images/menu/achievements/achievement sidebar/list lock.png"
                    yalign 0.01
                    action 0
            else:
                hotspot (2,0,381,86) action SetVariable("current_achievement_page", "prevent the spread of covid19 pt 1")

            showif not(persistent.is_achievement_unlocked["how to properly wear a mask"]):
                imagebutton:
                    idle "images/menu/achievements/achievement sidebar/list lock.png"
                    yalign 0.99
                    action 0
            else:
                hotspot (0,99,382,86) action SetVariable("current_achievement_page", "how to properly wear a mask pt 1")

    showif current_achievement_sidebar == 1:
        imagebutton:
            idle "images/menu/achievements/sidebar inactive prev btn.png"
            action 0
            xalign 0.248
            yalign 0.93
    else:
        imagebutton:
            idle "images/menu/achievements/sidebar prev btn.png"
            action SetVariable("current_achievement_sidebar", If(current_achievement_sidebar>1, current_achievement_sidebar-1, 1))
            xalign 0.248
            yalign 0.93

    showif current_achievement_sidebar == 4:
        imagebutton:
                idle "images/menu/achievements/sidebar inactive next btn.png"
                action 0
                xalign 0.298
                yalign 0.928
    else:
        imagebutton:
            idle "images/menu/achievements/sidebar next btn.png"
            action SetVariable("current_achievement_sidebar", If(current_achievement_sidebar<4, current_achievement_sidebar+1, 4))
            xalign 0.298
            yalign 0.928

    showif current_achievement_page == 'minimum public health standard pt 1':
        imagemap:
            ground "images/menu/achievements/pages/minimum public health standard - pt 1.png"
            xalign 0.9
            yalign 0.83

            imagebutton:
                idle "images/menu/achievements/page next btn.png"
                action SetVariable("current_achievement_page", "minimum public health standard pt 2")
                xalign 0.93
                yalign 0.96

    elif current_achievement_page == 'minimum public health standard pt 2':
        imagemap:
            ground "images/menu/achievements/pages/minimum public health standard - pt 2.png"
            xalign 0.9
            yalign 0.83

            imagebutton:
                idle "images/menu/achievements/page prev btn.png"
                action SetVariable("current_achievement_page", "minimum public health standard pt 1")
                xalign 0.1
                yalign 0.959

    elif current_achievement_page == 'ecq':
        imagemap:
            ground "images/menu/achievements/pages/ECQ.png"
            xalign 0.9
            yalign 0.83

    elif current_achievement_page == 'mecq':
        imagemap:
            ground "images/menu/achievements/pages/MECQ.png"
            xalign 0.9
            yalign 0.83

    elif current_achievement_page == 'gcq':
        imagemap:
            ground "images/menu/achievements/pages/GCQ.png"
            xalign 0.9
            yalign 0.83

    elif current_achievement_page == 'flexible learning':
        imagemap:
            ground "images/menu/achievements/pages/flexible learning.png"
            xalign 0.9
            yalign 0.83

    elif current_achievement_page == 'public transportation pt 1':
        imagemap:
            ground "images/menu/achievements/pages/public transportation pt 1.png"
            xalign 0.9
            yalign 0.83

            imagebutton:
                idle "images/menu/achievements/page next btn.png"
                action SetVariable("current_achievement_page", "public transportation pt 2")
                xalign 0.93
                yalign 0.96

    elif current_achievement_page == 'public transportation pt 2':
        imagemap:
            ground "images/menu/achievements/pages/public transportation pt 2.png"
            xalign 0.9
            yalign 0.83

            imagebutton:
                idle "images/menu/achievements/page prev btn.png"
                action SetVariable("current_achievement_page", "public transportation pt 1")
                xalign 0.1
                yalign 0.959

    elif current_achievement_page == 'company shuttle':
        imagemap:
            ground "images/menu/achievements/pages/company shuttles.png"
            xalign 0.9
            yalign 0.83

    elif current_achievement_page == 'food establishment operation':
        imagemap:
            ground "images/menu/achievements/pages/food establishment operation.png"
            xalign 0.9
            yalign 0.83

    elif current_achievement_page == 'grocery shopping':
        imagemap:
            ground "images/menu/achievements/pages/grocery shopping.png"
            xalign 0.9
            yalign 0.83

    elif current_achievement_page == 'online shopping':
        imagemap:
            ground "images/menu/achievements/pages/online shopping.png"
            xalign 0.9
            yalign 0.83

    elif current_achievement_page == 'quarantine age restriction':
        imagemap:
            ground "images/menu/achievements/pages/quarantine age restriction.png"
            xalign 0.9
            yalign 0.83

    elif current_achievement_page == 'restaurant operation pt 1':
        imagemap:
            ground "images/menu/achievements/pages/restaurant operation pt 1.png"
            xalign 0.9
            yalign 0.83

            imagebutton:
                idle "images/menu/achievements/page next btn.png"
                action SetVariable("current_achievement_page", "restaurant operation pt 2")
                xalign 0.93
                yalign 0.96

    elif current_achievement_page == 'restaurant operation pt 2':
        imagemap:
            ground "images/menu/achievements/pages/restaurant operation pt 2.png"
            xalign 0.9
            yalign 0.83

            imagebutton:
                idle "images/menu/achievements/page prev btn.png"
                action SetVariable("current_achievement_page", "restaurant operation pt 1")
                xalign 0.1
                yalign 0.959

    elif current_achievement_page == 'home work out pt 1':
        imagemap:
            ground "images/menu/achievements/pages/home work out pt 1.png"
            xalign 0.9
            yalign 0.83

            imagebutton:
                idle "images/menu/achievements/page next btn.png"
                action SetVariable("current_achievement_page", "home work out pt 2")
                xalign 0.93
                yalign 0.96

    elif current_achievement_page == 'home work out pt 2':
        imagemap:
            ground "images/menu/achievements/pages/home work out pt 2.png"
            xalign 0.9
            yalign 0.83

            imagebutton:
                idle "images/menu/achievements/page prev btn.png"
                action SetVariable("current_achievement_page", "home work out pt 1")
                xalign 0.1
                yalign 0.959

    elif current_achievement_page == 'what to do if someone is sick pt 1':
        imagemap:
            ground "images/menu/achievements/pages/What To Do If Someone Is Sick pt 1.png"
            xalign 0.9
            yalign 0.83

            imagebutton:
                idle "images/menu/achievements/page next btn.png"
                action SetVariable("current_achievement_page", "what to do if someone is sick pt 2")
                xalign 0.93
                yalign 0.96

    elif current_achievement_page == 'what to do if someone is sick pt 2':
        imagemap:
            ground "images/menu/achievements/pages/What To Do If Someone Is Sick pt 2.png"
            xalign 0.9
            yalign 0.83

            imagebutton:
                idle "images/menu/achievements/page prev btn.png"
                action SetVariable("current_achievement_page", "what to do if someone is sick pt 1")
                xalign 0.1
                yalign 0.959

            imagebutton:
                idle "images/menu/achievements/page next btn.png"
                action SetVariable("current_achievement_page", "what to do if someone is sick pt 3")
                xalign 0.93
                yalign 0.96

    elif current_achievement_page == 'what to do if someone is sick pt 3':
        imagemap:
            ground "images/menu/achievements/pages/What To Do If Someone Is Sick pt 3.png"
            xalign 0.9
            yalign 0.83

            imagebutton:
                idle "images/menu/achievements/page prev btn.png"
                action SetVariable("current_achievement_page", "what to do if someone is sick pt 2")
                xalign 0.1
                yalign 0.959

            imagebutton:
                idle "images/menu/achievements/page next btn.png"
                action SetVariable("current_achievement_page", "what to do if someone is sick pt 4")
                xalign 0.93
                yalign 0.96

    elif current_achievement_page == 'what to do if someone is sick pt 4':
        imagemap:
            ground "images/menu/achievements/pages/What To Do If Someone Is Sick pt 4.png"
            xalign 0.9
            yalign 0.83

            imagebutton:
                idle "images/menu/achievements/page prev btn.png"
                action SetVariable("current_achievement_page", "what to do if someone is sick pt 3")
                xalign 0.1
                yalign 0.959

    elif current_achievement_page == 'covid symptoms':
        imagemap:
            ground "images/menu/achievements/pages/covid-19 symptoms.png"
            xalign 0.9
            yalign 0.83

    elif current_achievement_page == 'prevent the spread of covid19 pt 1':
        imagemap:
            ground "images/menu/achievements/pages/Prevent the Spread of COVID-19 pt 1.png"
            xalign 1.048
            yalign 0.83

            imagebutton:
                idle "images/menu/achievements/page next btn.png"
                action SetVariable("current_achievement_page", "prevent the spread of covid19 pt 2")
                xalign 0.835
                yalign 0.96

    elif current_achievement_page == 'prevent the spread of covid19 pt 2':
        imagemap:
            ground "images/menu/achievements/pages/Prevent the Spread of COVID-19 pt 2.png"
            xalign 0.9
            yalign 0.83

            imagebutton:
                    idle "images/menu/achievements/page prev btn.png"
                    action SetVariable("current_achievement_page", "prevent the spread of covid19 pt 1")
                    xalign 0.1
                    yalign 0.959

            imagebutton:
                    idle "images/menu/achievements/page next btn.png"
                    action SetVariable("current_achievement_page", "prevent the spread of covid19 pt 3")
                    xalign 0.93
                    yalign 0.96

    elif current_achievement_page == 'prevent the spread of covid19 pt 3':
        imagemap:
            ground "images/menu/achievements/pages/Prevent the Spread of COVID-19 pt 3.png"
            xalign 1.048
            yalign 0.83

            imagebutton:
                    idle "images/menu/achievements/page prev btn.png"
                    action SetVariable("current_achievement_page", "prevent the spread of covid19 pt 2")
                    xalign 0.1
                    yalign 0.959

    elif current_achievement_page == 'how to properly wear a mask pt 1':
        imagemap:
            ground "images/menu/achievements/pages/How to Properly Wear a Mask pt 1.png"
            xalign 0.9
            yalign 0.83

            imagebutton:
                idle "images/menu/achievements/page next btn.png"
                action SetVariable("current_achievement_page", "how to properly wear a mask pt 2")
                xalign 0.93
                yalign 0.96

    elif current_achievement_page == 'how to properly wear a mask pt 2':
        imagemap:
            ground "images/menu/achievements/pages/How to Properly Wear a Mask pt 2.png"
            xalign 0.9
            yalign 0.83

            imagebutton:
                idle "images/menu/achievements/page prev btn.png"
                action SetVariable("current_achievement_page", "how to properly wear a mask pt 1")
                xalign 0.1
                yalign 0.959
