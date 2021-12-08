init:
    $ current_bgm_timestamp = 0.0
    $ ending_choices = {
        "quarantine violator": [],
        "safety is priority": [],
        "lets meet up": [],
        "an exercise date": [],
        "arts n craft": [],
        "a virtual lunch date": [],
        "reconnect with a friend": [],
        "trying a new hobby": []
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

label endingScenes(ending_name):
    scene black onlayer background
    $ renpy.choice_for_skipping()
    $ resetBgmTimeStamp()

    $ renpy.hide_screen("patientOverlay")
    $ renpy.hide_screen("ui_start")
    $ renpy.hide_screen("quickMenu")
    $ renpy.hide_screen("quickToggle")

    $ renpy.music.play("audio/bgm/ending song.mp3", loop=True, fadein=5.0)

    $ renpy.show("bg {}".format(ending_name), layer="background")
    $_dismiss_pause = False
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

    $ playAfterTimestamp(28.0)
    hide kitchen_endscene onlayer background
    show bedroom_endscene onlayer background:
        yalign 0.5
        linear 4.0 xalign 0.4

    $ playAfterTimestamp(32.0)
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

    $ playAfterTimestamp(44.5)
    hide livingroom_endscene onlayer background
    show bg living room ending onlayer background:
        xalign 0.4
        yalign 0.5
        linear 2.0 xalign 0.2

    $ playAfterTimestamp(46.5)
    hide bg living room ending onlayer background
    show front_endscene onlayer background:
        yalign 0.5

    $ playAfterTimestamp(54.5)
    hide front_endscene onlayer background
    show bg front house 2 ending onlayer background:
        xalign 1.1
        yalign 0.5
        linear 1.5 xalign 0.9

    $ playAfterTimestamp(56.0)
    hide front_endscene onlayer background
    show bg front house ending onlayer background:
        xalign 1.1
        yalign 0.5
        linear 1.0 xalign 1.0

    $ playAfterTimestamp(57.0)
    hide bg front house ending onlayer background
    $ dissolveAfterTimestamp(57.5)

    $ playAfterTimestamp(57.5)
    show bg main ending onlayer background:
        xalign 0.5
        yanchor 0.74
        easein 38.0 yanchor 0.05
    $ dissolveAfterTimestamp(60.0)

    $ playAfterTimestamp(94.5)
    hide screen skipEndingScenes
    $ dissolveAfterTimestamp(95.0)

    $ playAfterTimestamp(96.0)

    label .savePoint:
        $ renpy.music.play("audio/bgm/good end.mp3", loop=True, fadein=5.0, if_changed=True)
        show bg main ending onlayer background:
            xalign 0.5
            yanchor 0.05

        label .repick:
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
        xalign 1.02 yalign 0.94
        at double
        action Show("confirm", message="Skip the ending scenes?", yes_action=[Hide("confirm"), Hide("skipEndingScenes"), Jump("endingScenes.savePoint")], no_action=Hide("confirm"))
