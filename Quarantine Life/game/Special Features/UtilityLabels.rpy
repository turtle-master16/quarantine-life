label timeskip(img="black", mes=None):
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

label updateDate(date=""):
    # Use this to update the top right date display
    # How to Use: call updateDate("Date")
    $ datescreenon = renpy.get_screen("displayDate")
    if datescreenon:
            $ renpy.hide_screen("displayDate")
            $ renpy.pause(0.4)
    $ renpy.show_screen("displayDate", date)
