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
    $ renpy.hide_screen("displayDate")
    $ renpy.show_screen("returnbutton")
    vbox:
        text "Welcome to route test mode!":
            xalign 0.5
            xfill True
            size 30
        viewport id "vp":
            draggable True
            hbox:
                spacing 20
                vbox: #Home
                    xalign 0.5
                    yoffset 20
                    spacing 10
                    text "{b}1. Home{/b}" xalign 0.5
                    textbutton "(Start)" action Jump('start.mainstart') xalign 0.5
                    textbutton "(COVID News)" action Jump('news') xalign 0.5
                    textbutton "{color=#f00}1a.{/color}<-(Lockdown)->{color=#f2f542}Proceed{/color}" action Jump('lockdown') xalign 0.5
                    hbox:
                        vbox:
                            text "{color=#f00}{b}1a.{/b}{/color}" xalign 0.5
                            textbutton "(Arrested End)" action Jump('getcaught') xalign 0.5
                        text "OR"
                        vbox:
                            textbutton "(Quarantine)" action Jump('quarantine') xalign 0.5
                            textbutton "(New Normal)" action Jump('newnormal') xalign 0.5
                            textbutton "(Lv_Rm Activities({color=#f2f542}2.{/color}))" action Jump('livingroomact') xalign 0.5
                vbox: #Work
                    xalign 0.5
                    yoffset 20
                    spacing 10
                    text "{color=#f2f542}{b}2. Work{/b}{/color}" xalign 0.5
                    textbutton "(Commute to work)" action Jump('commuting') xalign 0.5
                    textbutton "{color=#42bff5}3a.{/color}<-(Office)->{color=#427bf5}3b.{/color}" action Jump('office') xalign 0.5
                vbox: #Home2
                    xalign 0.5
                    yoffset 20
                    spacing 10
                    text "{color=#42bff5}{b}3a. Home (After Work){/b}{/color}" xalign 0.5 layout "nobreak"
                    textbutton "(Home)" action Jump('home') xalign 0.5
                    textbutton "(Supermarket)" action Jump('supermarket') xalign 0.5
                    textbutton "(Kitchen)" action Jump('kitchen') xalign 0.5
                    textbutton "{color=#7242f5}3aa.{/color}<-(Project)->{color=#7242f5}3ab.{/color}" action Jump('project') xalign 0.5 text_layout "nobreak"
                    hbox:
                        vbox:
                            xalign 0.5
                            yoffset 20
                            text "{color=#7242f5}{b}3aa. {/b}{/color}" xalign 0.5
                            textbutton "(Prince End A)" action Jump('bros') xalign 0.5
                        text "OR"
                        vbox:
                            xalign 0.5
                            yoffset 20
                            text "{color=#7242f5}{b}3ab. {/b}{/color}" xalign 0.5
                            textbutton "(Prince End B)" action Jump('falsealarm') xalign 0.5 text_layout "nobreak"
                vbox: #Friend
                    xalign 0.5
                    yoffset 20
                    spacing 10
                    text "{color=#427bf5}{b}3b. Friend Route{/b}{/color}" xalign 0.5 layout "nobreak"
                    textbutton "3ba.<-(Restaurant)->3bb." action Jump('restaurant') xalign 0.5 text_layout "nobreak"
                    hbox:
                        vbox:
                            xalign 0.5
                            yoffset 20
                            spacing 10
                            text "{color=#228b22}{b}3ba. Kyle Route{/b}{/color}" xalign 0.5 layout "nobreak"
                            textbutton "(Kyle)" action Jump('kyle') xalign 0.5
                            textbutton "Kyle Meet<-(Kyle Home)->Kyle Refuse" action Jump('kylehome') xalign 0.5 text_layout "nobreak"
                            hbox:
                                xalign 0.5
                                spacing 20
                                vbox:
                                    textbutton "(Kyle Meet)" action Jump('kylemeet') xalign 0.5 text_layout "nobreak"
                                    textbutton "(Hospital)" action Jump('hospital') xalign 0.5
                                    textbutton "(Player End 1)" action Jump('mcend') xalign 0.5 text_layout "nobreak"
                                text "OR"
                                vbox:
                                    textbutton "(Player End 2)" action Jump('kylehome.mcend2') xalign 0.5 text_layout "nobreak"
                        vbox:
                            xalign 0.5
                            yoffset 20
                            spacing 10
                            text "{b}3bb. Date Route{/b}" xalign 0.5 layout "nobreak"
                            textbutton "{color=#d2691e}Jason{/color}<-(Date Search)->{color=#add8e6}Jillian{/color}" action Jump('datesearch') xalign 0.5 text_layout "nobreak"
                vbox: #Dates
                    xalign 0.5
                    yoffset 20
                    spacing 10
                    text "{color=#d2691e}{b}Jason{/b}{/color}" xalign 0.5 layout "nobreak"
                    textbutton "{color=#228b22}Kyle Route{/color}<-(Jason Start)->{color=#d2691e}Proceed{/color}" action Jump('phone') xalign 0.5 text_layout "nobreak"
                    hbox:
                        xalign 0.5
                        xanchor 0.5
                        vbox:
                            xalign 0.5
                            xsize 520
                            textbutton "{color=#228b22}(Go to 3ba. Kyle Route){/color}" action Jump('kyle') xalign 0.5 text_layout "nobreak"
                        text "OR"  xalign 0.5
                        vbox:
                            xalign 0.5
                            xsize 520
                            textbutton "(Post Date Search Jason)" action Jump('postdatesearch') xalign 0.5 text_layout "nobreak"
                            textbutton "(First Date Jason)" action Jump('firstdate') xalign 0.5 text_layout "nobreak"
                            textbutton "Js End 1<-(Jason Casual)-> Js End 2" action Jump('jason') xalign 0.5 text_layout "nobreak"
                            hbox:
                                xalign 0.5
                                spacing 50
                                textbutton "(Js End 1)" action Jump('jsexerciseend') xalign 0.5 text_layout "nobreak"
                                text "OR"
                                textbutton "(Js End 2)" action Jump('jsend') xalign 0.5 text_layout "nobreak"
                    text "{color=#add8e6}{b}Jillian{/b}{/color}" xalign 0.5 layout "nobreak"
                    textbutton "(Jillian Start)" action Call('phone', False) xalign 0.5 text_layout "nobreak"
                    textbutton "(Post Date Search Jillian)" action Call('postdatesearch', False) xalign 0.5 text_layout "nobreak"
                    textbutton "{color=#228b22}Kyle Route{/color}<-(First Date Jillian)->{color=#add8e6}Proceed{/color}" action Call('firstdate', False) xalign 0.5 text_layout "nobreak"
                    hbox:
                        xalign 0.5
                        xanchor 0.5
                        vbox:
                            xalign 0.5
                            xsize 400
                            textbutton "{color=#228b22}(Go to 3ba. Kyle Route){/color}" action Jump('kyle') xalign 0.5 text_layout "nobreak"
                        text "OR" xalign 0.5 xsize 400
                        vbox:
                            xalign 0.5
                            xsize 400
                            textbutton "(Jilllian Casual)" action Jump('jillian') xalign 0.5 text_layout "nobreak"
                            textbutton "(Jillian Ask out)" action Jump('jlaskout') xalign 0.5 text_layout "nobreak"
                            textbutton "(Jillian Date)" action Jump('jldate') xalign 0.5 text_layout "nobreak"
                            textbutton "(Jillian End)" action Jump('jlend') xalign 0.5 text_layout "nobreak"

screen returnbutton:
    zorder 3
    imagebutton:
        idle "images/misc/return.png"
        xalign 1.0
        yalign 1.0
        # action Call("start", retmode=True)
        action If(renpy.get_screen("dialogevents"), true=Hide("dialogevents"), false=Show("dialogevents", _zorder=1))
    imagebutton:
        idle "images/misc/return.png"
        xalign 0
        yalign 0
        # action Call("start", retmode=True)
        action If(renpy.get_screen("storyroute"), true=Hide("storyroute"), false=Show("storyroute", _zorder=1))
    imagebutton:
        idle "images/misc/return.png"
        xalign 0
        yalign 1.0
        # action Call("start", retmode=True)
        action If(renpy.get_screen("achievements"), true=Hide("achievements"), false=Show("achievements", _zorder=1))
