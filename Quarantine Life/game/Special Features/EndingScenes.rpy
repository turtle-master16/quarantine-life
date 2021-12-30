init:
    $ current_bgm_timestamp = 0.0
    $ ending_choices = {
        "quarantine violator": [
            "told Carla that you will not be staying at home during the quarantine."
        ],
        "safety is priority": [
            "told Carla that you will be staying at home during the quarantine.",
            "turned down Ian's invitation to hang out."
        ],
        "lets meet up": [
            "told Carla that you will be staying at home during the quarantine.",
            "went out to eat with your coworkers.",
            "accepted Jason's invitation to meet up."
        ],
        "an exercise date": [
            "told Carla that you will be staying at home during the quarantine.",
            "went out to eat with your coworkers.",
            "did not accept Jason's invitation to meet up."
        ],
        "arts n craft": [
            "told Carla that you will be staying at home during the quarantine.",
            "went out to eat with your coworkers.",
            "did not invite Jillian to go out."
        ],
        "a virtual lunch date": [
            "told Carla that you will be staying at home during the quarantine.",
            "went out to eat with your coworkers.",
            "invited Jillian to go out."
        ],
        "reconnect with a friend": [
            "told Carla that you will be staying at home during the quarantine.",
            "went out to eat with your coworkers.",
            "accepted Kyle's invitation to hang out."
        ],
        "trying a new hobby": [
            "told Carla that you will be staying at home during the quarantine.",
            "went out to eat with your coworkers.",
            "did not accept Kyle's invitation to hang out."
        ]
    }

init python:
    def playAfterTimestamp(timestamp):
        global current_bgm_timestamp
        pauseDuration = timestamp - current_bgm_timestamp
        renpy.pause(pauseDuration, hard="True")
        current_bgm_timestamp = timestamp

    def dissolveAfterTimestamp(timestamp):
        global current_bgm_timestamp
        dissolveDuration = timestamp - current_bgm_timestamp
        renpy.with_statement(Dissolve(dissolveDuration))
        current_bgm_timestamp = timestamp

    def resetBgmTimeStamp():
        global current_bgm_timestamp
        current_bgm_timestamp = 0.0

    print(persistent.userDeviceID)

label endingScenes(ending_name):
    $_dismiss_pause = False
    $ renpy.choice_for_skipping()

    $ renpy.hide_screen("patientOverlay")
    $ renpy.hide_screen("ui_start")
    $ renpy.hide_screen("quickMenu")
    $ renpy.hide_screen("quickToggle")
    window hide

    show screen plainWhite
    with Dissolve(0.6)

    $ getLatestTraversedEndingRecords()

    $ resetBgmTimeStamp()
    $ renpy.music.play("audio/bgm/ending song.mp3", loop=True, fadein=5.0)

    hide screen plainWhite
    scene black onlayer background
    $ renpy.show("bg {}".format(ending_name), layer="background")
    $ dissolveAfterTimestamp(3.0)

    $ playAfterTimestamp(5.5)
    $ renpy.hide("bg {}".format(ending_name), layer="background")

    if ending_name == "quarantine violator" or ending_name == "reconnect with a friend":
        show screen endingCategory(category="Bad")
    else:
        show screen endingCategory(category="Good")
    $ dissolveAfterTimestamp(10.5)

    $ playAfterTimestamp(11.0)
    hide screen endingCategory
    show screen plainWhite
    $ dissolveAfterTimestamp(16.9)
    $_dismiss_pause = True

    $ playAfterTimestamp(16.9)

    show screen skipEndingScenes

    hide screen plainWhite
    show bg kitchen ending onlayer background:
        yalign 0.5
        linear 1.1 xalign 0.25

    $ playAfterTimestamp(18.0)
    hide bg kitchen ending onlayer background
    show kitchen_endscene onlayer background:
        xpos -0.07
        yalign 0.5
        linear 10.0 xpos 0.0001

    $ playAfterTimestamp(19.0)
    $ renpy.show_screen("credits1")
    $ dissolveAfterTimestamp(19.5)
    $ playAfterTimestamp(23.0)
    $ renpy.hide_screen("credits1")
    $ dissolveAfterTimestamp(23.5)

    if not (ending_name == "quarantine violator" or ending_name == "safety is priority"):
        $ playAfterTimestamp(24.5)
        $ renpy.show_screen("endingSummary", summary="You and {} of players {}".format(
            getEndingTraversePercentage("quarantine violator", reverse=True),
            ending_choices[ending_name][0])
        )
        $ dissolveAfterTimestamp(25.0)

    $ playAfterTimestamp(28.0)
    $ renpy.hide_screen("endingSummary")
    hide kitchen_endscene onlayer background
    show bedroom_endscene onlayer background:
        yalign 0.5
        linear 4.0 xalign 0.4

    if ending_name == "safety is priority":
        $ playAfterTimestamp(28.5)
        $ renpy.show_screen("endingSummary", summary="You and {} of players {}".format(
            getEndingTraversePercentage("quarantine violator", reverse=True),
            ending_choices[ending_name][0])
        )
        $ dissolveAfterTimestamp(29.0)
    elif ending_name != "quarantine violator":
        $ playAfterTimestamp(28.5)
        $ renpy.show_screen("endingSummary", summary="You and {} of players {}".format(
            getEndingTraversePercentage("safety is priority", reverse=True),
            ending_choices[ending_name][1])
        )
        $ dissolveAfterTimestamp(29.0)

    $ playAfterTimestamp(32.0)
    $ renpy.hide_screen("endingSummary")
    hide bedroom_endscene onlayer background
    show bg bedroom ending onlayer background:
        xalign 0
        yalign 0.5
        linear 1.5 xalign 0.2

    $ playAfterTimestamp(33.5)
    hide bg bedroom ending onlayer background
    show livingroom_endscene onlayer background:
        yalign 0.5
        linear 11.0 xalign 0.75

    $ playAfterTimestamp(34.5)
    $ renpy.show_screen("credits2")
    $ dissolveAfterTimestamp(35.0)
    $ playAfterTimestamp(37.0)
    $ renpy.hide_screen("credits2")
    $ dissolveAfterTimestamp(37.5)

    $ playAfterTimestamp(38.0)
    $ renpy.show_screen("credits3")
    $ dissolveAfterTimestamp(38.5)
    $ playAfterTimestamp(40.0)
    $ renpy.hide_screen("credits3")
    $ dissolveAfterTimestamp(40.5)

    if ending_name == "quarantine violator":
        $ playAfterTimestamp(41.0)
        $ renpy.show_screen("endingSummary", summary="You and {} of players {}".format(
            getEndingTraversePercentage("quarantine violator"),
            ending_choices[ending_name][0])
        )
        $ dissolveAfterTimestamp(41.5)
    elif ending_name == "safety is priority":
        $ playAfterTimestamp(41.0)
        $ renpy.show_screen("endingSummary", summary="You and {} of players {}".format(
            getEndingTraversePercentage("safety is priority"),
            ending_choices[ending_name][1])
        )
        $ dissolveAfterTimestamp(41.5)
    else:
        $ playAfterTimestamp(41.0)
        $ renpy.show_screen("endingSummary", summary="You and {} of players {}".format(
            getEndingTraversePercentage(ending_name),
            ending_choices[ending_name][2])
        )
        $ dissolveAfterTimestamp(41.5)

    $ playAfterTimestamp(44.5)
    $ renpy.hide_screen("endingSummary")
    hide livingroom_endscene onlayer background
    show bg living room ending onlayer background:
        xalign 0.4
        yalign 0.5
        linear 2.0 xalign 0.2

    $ playAfterTimestamp(46.0)
    hide bg living room ending onlayer background
    show front_endscene onlayer background:
        yalign 0.5

    $ playAfterTimestamp(51.0)
    $ renpy.show_screen("endingSummary", summary="You and {} of players reached this ending.".format(getEndingTraversePercentage(ending_name)))
    $ dissolveAfterTimestamp(51.5)

    $ playAfterTimestamp(54.5)
    $ renpy.hide_screen("endingSummary")
    hide front_endscene onlayer background
    show bg front house 2 ending onlayer background:
        xalign 1.1
        yalign 0.5
        linear 1.5 xalign 0.9

    $ playAfterTimestamp(55.0)
    $ renpy.show_screen("credits4")
    $ dissolveAfterTimestamp(55.5)

    $ playAfterTimestamp(56.0)
    hide front_endscene onlayer background
    show bg front house ending onlayer background:
        xalign 1.1
        yalign 0.5
        linear 1.0 xalign 1.0

    $ playAfterTimestamp(57.0)
    hide bg front house ending onlayer background
    $ renpy.hide_screen("credits4")
    $ dissolveAfterTimestamp(57.5)

    $ playAfterTimestamp(57.5)
    show bg main ending onlayer background:
        xalign 0.5
        yanchor 0.74
        easein 38.0 yanchor 0.05
    $ renpy.show_screen("credits5")
    $ dissolveAfterTimestamp(60.0)

    $ playAfterTimestamp(63.0)
    $ renpy.hide_screen("credits5")
    $ dissolveAfterTimestamp(64.0)

    $ playAfterTimestamp(65.0)
    $ renpy.show_screen("credits6")
    $ dissolveAfterTimestamp(66.0)
    $ playAfterTimestamp(72.0)
    $ renpy.hide_screen("credits6")
    $ dissolveAfterTimestamp(73.0)

    $ playAfterTimestamp(74.0)
    $ renpy.show_screen("credits7")
    $ dissolveAfterTimestamp(75.0)
    $ playAfterTimestamp(81.0)
    $ renpy.hide_screen("credits7")
    $ dissolveAfterTimestamp(82.0)

    $ playAfterTimestamp(83.0)
    $ renpy.show_screen("credits8")
    $ dissolveAfterTimestamp(84.0)
    $ playAfterTimestamp(90.0)
    $ renpy.hide_screen("credits8")
    $ dissolveAfterTimestamp(91.0)

    $ playAfterTimestamp(94.5)
    hide screen skipEndingScenes
    $ dissolveAfterTimestamp(95.0)

    $ playAfterTimestamp(96.0)

    label .savePoint:
        $ renpy.music.play("audio/bgm/ending song.mp3", loop=True, fadein=5.0)
        scene black onlayer background
        $ renpy.hide_screen("endingSummary")
        $ renpy.hide_screen("credits1")
        $ renpy.hide_screen("credits2")
        $ renpy.hide_screen("credits3")
        $ renpy.hide_screen("credits4")
        $ renpy.hide_screen("credits5")
        show bg main ending onlayer background:
            xalign 0.5
            yalign 0
            yanchor 0.05

        $ saveLatestTraversedEndingRecords()

        label .repick:
            $ renpy.block_rollback()
            $ persistent.fromEnd = True
            menu:
                with dissolve
                "Choose another route":
                    show screen storyroute
                    jump ending_reached.repick

                "Return to starting point":
                    jump start.mainstart

                "Return to main menu":
                    stop sound fadeout 0.2
                    jump proceed

screen endingCategory(category):
    text "{} End".format(category):
        xalign 0.5
        yalign 0.5
        size 100 color "#fff"

screen plainWhite:
    add Solid("#eeeeeeff")

screen skipEndingScenes:
    imagebutton:
        idle "gui/quick/inactive_skipEndings_btn.png"
        hover "gui/quick/skipEndings_btn.png"
        xalign 1.0 yalign 0.94
        at half
        action Show("confirm", message="Skip the ending scenes?", yes_action=[Hide("confirm"), Hide("skipEndingScenes"), Jump("endingScenes.savePoint")], no_action=Hide("confirm"))

screen endingSummary(summary):
    add Solid("#00000055")

    text "{}".format(summary):
        xalign 0.5
        yalign 0.5
        color "#ddd"
        size 40
        justify True
        text_align 0.5

screen credits1:
    add Solid("#00000055")

    text "Sound Effects":
        xalign 0.5
        yalign 0.28
        color "#fff"
        size 40
        justify True
        text_align 0.5

    hbox:
        vbox:
            xsize 600
            xpos 20

            vbox:
                xalign 0.5
                ysize 120
                ypos 252

                text "Furatto kibun@ furi":
                    style "style_credit_title"
                    yalign 0.5
                text "Courtesy of BGM DOVA-SYNDROME OFFICIAL ({a=https://www.youtube.com/channel/UCq15_9MvmxT1r2-LLjtkokg}Youtube Channel{/a})":
                    style "style_credit_desc"

            vbox:
                xalign 0.5
                ysize 120
                ypos 259

                text "Male Deep Breathing":
                    style "style_credit_title"
                    yalign 0.95
                text "Courtesy of Game Sounds (Youtube Channel)":
                    style "style_credit_desc"

        vbox:
            xsize 600
            xpos 60

            vbox:
                xalign 0.5
                ysize 120
                ypos 235

                text "Closing Door Sound Effect":
                    style "style_credit_title"
                    yalign 0.95
                text "Courtesy of Blue Ingo (Youtube Channel)":
                    style "style_credit_desc"

            vbox:
                xalign 0.5
                ysize 120
                ypos 275

                text "Door Rattle Sound":
                    style "style_credit_title"
                    yalign 0.95
                text "Courtesy of SR BEST SOUND EFFECTS (Youtube Channel)":
                    style "style_credit_desc"

screen credits2:
    add Solid("#00000055")

    text "Sound Effects":
        xalign 0.5
        yalign 0.28
        color "#fff"
        size 40
        justify True
        text_align 0.5

    hbox:
        vbox:
            xsize 600
            xpos 20

            vbox:
                xalign 0.5
                ysize 120
                ypos 252

                text "Eating Sound Effect":
                    style "style_credit_title"
                    yalign 0.5
                text "Courtesy of n Beats (Youtube Channel)":
                    style "style_credit_desc"

            vbox:
                xalign 0.5
                ysize 120
                ypos 259

                text "Foosteps Sound Effect":
                    style "style_credit_title"
                    yalign 0.95
                text "Courtesy of DJ Sound FX (Youtube Channel)":
                    style "style_credit_desc"

        vbox:
            xsize 600
            xpos 60

            vbox:
                xalign 0.5
                ysize 120
                ypos 265

                text "Notification Sound Effect No Copyright":
                    style "style_credit_title"
                    yalign 0.95
                text "Courtesy of Nagaty Studio (Youtube Channel)":
                    style "style_credit_desc"

            vbox:
                xalign 0.5
                ysize 120
                ypos 275

                text "Nokia Ringtone":
                    style "style_credit_title"
                    yalign 0.95
                text "Courtesy of MobilesRingtones ({a=http://www.mobileringtones.com/}http://www.mobileringtones.com/{/a})":
                    style "style_credit_desc"

screen credits3:
    add Solid("#00000055")

    text "Sound Effects":
        xalign 0.5
        yalign 0.28
        color "#fff"
        size 40
        justify True
        text_align 0.5

    hbox:
        vbox:
            xsize 600
            xpos 20

            vbox:
                xalign 0.5
                ysize 120
                ypos 254

                text "Touch Screen Sound Effects":
                    style "style_credit_title"
                    yalign 0.5
                text "Courtesy of All Sounds (Youtube Channel)":
                    style "style_credit_desc"

            vbox:
                xalign 0.5
                ysize 120
                ypos 293

                text "Phone Vibrating Sound Effect":
                    style "style_credit_title"
                    yalign 0.95
                text "Courtesy of GFX Sounds ({a=https://gfxsounds.com/}https://gfxsounds.com/{/a})":
                    style "style_credit_desc"

        vbox:
            xsize 600
            xpos 60

            vbox:
                xalign 0.5
                ysize 120
                ypos 265

                text "Running Footsteps Sound Effects All Sounds":
                    style "style_credit_title"
                    yalign 0.95
                text "Courtesy of All Sounds (Youtube Channel)":
                    style "style_credit_desc"

            vbox:
                xalign 0.5
                ysize 120
                ypos 295

                text "Suspense Scary Music - Best Dark Music":
                    style "style_credit_title"
                    yalign 0.95
                text "Courtesy of Oak Studios (Youtube Channel)":
                    style "style_credit_desc"

screen credits4:
    add Solid("#00000055")

    text "Background Music":
        xalign 0.5
        yalign 0.28
        color "#fff"
        size 40
        justify True
        text_align 0.5

    hbox:
        vbox:
            xsize 550
            xpos 70

            vbox:
                xalign 0.5
                ysize 120
                ypos 260

                text "Pacification Calm and Relaxing Piano Music":
                    style "style_credit_title"
                    yalign 0.5
                text "Courtesy of Live music, Relax, Meditation (Youtube Channel)":
                    style "style_credit_desc"

            vbox:
                xalign 0.5
                ysize 120
                ypos 293

                text "The Lounge":
                    style "style_credit_title"
                    yalign 0.95
                text "Courtesy of Bensound ({a=https://www.bensound.com/}https://www.bensound.com/{/a})":
                    style "style_credit_desc"

        vbox:
            xsize 600
            xpos 90

            vbox:
                xalign 0.5
                ysize 120
                ypos 257

                text "Inspirational Cinematic Background Music":
                    style "style_credit_title"
                    yalign 0.95
                text "Courtesy of AShamaluevMusic (Youtube Channel)":
                    style "style_credit_desc"

            vbox:
                xalign 0.5
                ysize 120
                ypos 290

                text "Lonely":
                    style "style_credit_title"
                    yalign 0.95
                text "Courtesy of AShamaluevMusic (Youtube Channel)":
                    style "style_credit_desc"

screen credits5:
    add Solid("#00000055")

    text "The Last":
        xalign 0.5
        yalign 0.40
        color "#fff"
        size 80
        justify True
        text_align 0.5

    text "Instrumental Song for Anime Opening and Background":
        xalign 0.5
        yalign 0.5
        color "#fff"
        size 40
        justify True
        text_align 0.5

    text "Courtesy of SeeeD Tribe (Youtube Channel)":
        xalign 0.5
        yalign 0.56
        color "#fff"
        size 30
        justify True
        text_align 0.5

screen credits6:
    add Solid("#00000055")

    text "Game Development":
        xalign 0.5
        yalign 0.3
        color "#fff"
        size 45
        justify True
        text_align 0.5

    text "Phone Message System for RenPy":
        style "style_credit_title"
        yalign 0.5
    text "Source: {a=https://nadianova.itch.io/phone-message-system-for-renpy}https://nadianova.itch.io/phone-message-system-for-renpy{/a}":
        yalign 0.57
        style "style_credit_desc"

screen credits7:
    add Solid("#00000055")

    text "Game Development":
        xalign 0.5
        yalign 0.3
        color "#fff"
        size 45
        justify True
        text_align 0.5

    text "3D Camera in RenPy":
        style "style_credit_title"
        yalign 0.5
    text "Source: {a=https://github.com/kyouryuukunn/renpy-ActionEditor}https://github.com/kyouryuukunn/renpy-ActionEditor{/a}":
        yalign 0.57
        style "style_credit_desc"

screen credits8:
    add Solid("#00000055")

    text "Referenced Information":
        xalign 0.5
        yalign 0.3
        color "#fff"
        size 45
        justify True
        text_align 0.5

    text "WHO & IATF Guidelines":
        style "style_credit_title"
        yalign 0.5
    text "Source: {a=https://doh.gov.ph/COVID-19/IATF-Resolutions}https://doh.gov.ph/COVID-19/IATF-Resolutions{/a}":
        yalign 0.57
        style "style_credit_desc"


style style_credit_title:
    xalign 0.5
    color "#ddd"
    size 35
    justify True
    text_align 0.5

style style_credit_desc:
    xalign 0.5
    color "#bbb"
    size 28
    justify True
    text_align 0.5
