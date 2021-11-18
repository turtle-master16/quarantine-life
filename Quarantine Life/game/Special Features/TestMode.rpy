# Styles
init 5:
    style esc_codeframe:
        xalign 0.5
        yalign 0.5
        xsize 50
        ysize 70
    style esc_coverall:
        xalign 0.5
        yalign 0.5
        xfill True
        yfill True
    style esc_textbutton:
        xalign 0.5
        yalign 0.5
    style esc_codehbox:
        spacing 20
        xalign 0.5
        yfill True
    style esc_codevbox:
        spacing 30
        yalign 0.5
    style esc_number:
        xalign 0.5
        yalign 0.5
        size 40

# Test mode
screen testmode():
    use quickMenu
    vbox:
        # textbutton "Unlock Routes":
        #     text_color "#fff"
        #     action Call("unlockRoutes")
        # textbutton "Unlock Achivements":
        #     text_color "#fff"
        #     action Call("unlockAch")
        # textbutton "Check all Dialog Events":
        #     text_color "#fff"
        #     action Call("checkEvents")
        textbutton "Reset Persistent Data":
            text_color "#fff"
            action persistent._clear()
        # textbutton "Start Game":
        #     text_color "#fff"
        #     action Jump("start.mainstart")
