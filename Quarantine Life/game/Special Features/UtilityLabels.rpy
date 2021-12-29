default currentRoute = ""
default quickMenuHide = False
define persistent.skip_complete_games = False

init python:
    def setPersistent(route):
        persistent.is_route_unlocked[route] = True
        globals()['currentRoute'] = route

label timeskip(img="black", mes=None):
    hide screen patientOverlay
    hide screen quickMenu
    hide screen quickToggle
    hide screen displayDate
    window hide
    $ renpy.scene('middle')
    $ renpy.scene('background')
    show black onlayer background
    if mes:
        $ renpy.with_statement(wipeleft)
        centered "[mes]"
        $ renpy.scene('background')
        $ renpy.show(img, layer='background')
        $ renpy.with_statement(wiperight)
    else:
        $ renpy.with_statement(wipeleftlong)
        $ renpy.scene('background')
        $ renpy.show(img, layer='background')
        $ renpy.with_statement(wiperightlong)
    show screen ui_start
    return

label ending_reached(end_type=""):
    $ renpy.hide_screen("patientOverlay")
    $ renpy.hide_screen("ui_start")

    $ music_to_use = {
        "bad":  "audio/bgm/bad end.mp3",
        "good": "audio/bgm/good end.mp3",
    }
    $ renpy.music.play(music_to_use[end_type], loop=True, fadeout=2, fadein=2, if_changed=True)

    scene black onlayer background
    with dissolve

    $ end_type_cap = end_type.capitalize()
    $ quickMenuHide = True
    if end_type == "bad":
        centered "{color=#F00}{b}[end_type_cap] End{/b}{/color}"
    elif end_type == "good":
        centered "{color=#0F0}{b}[end_type_cap] End{/b}{/color}"

    $ renpy.hide_screen("quick_menu")

    $ quickMenuHide = False

    label .repick:
        menu:
            "Choose another route":
                show screen storyroute
                jump ending_reached.repick

            "Return to starting point":
                jump start.mainstart

            "Return to main menu":
                stop sound fadeout 0.2
                jump proceed

screen skip_stopper:
    zorder 100
    if renpy.is_skipping():
        add Solid("#ffc50033")
        imagebutton:
            idle "gui/quick/skip_stopper.png"
            at delayed_blink(0.0, 1.0)
            xalign 0.5 yalign 0.5
            action Skip() alternate Skip(fast=True, confirm=True)
