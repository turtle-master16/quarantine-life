label timeskip(img="black", mes=None):
    hide screen patientOverlay
    hide screen quickMenu
    hide screen quickToggle
    $ renpy.scene('middle')
    $ renpy.scene('background')
    show black onlayer background
    hide screen displayDate
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

screen rback:
    textbutton "Back":
        xalign 0.5
        yalign 0.9
        action Rollback()
