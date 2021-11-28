transform phone_hide:
    yalign 1.0 xalign 0.5
    yoffset 100
    easein 0.3 yoffset 1300

transform delay:
    pause 0.5

# Phone Labels
label phone_start:
    window hide
    show phone at phone_pickup
    $ renpy.pause(0.2)
    return

label phone_msg:
    $ renpy.pause()
    hide screen phone_message
    $ renpy.pause(0.1)
    return

label phone_msg2:
    $ renpy.pause()
    hide screen phone_message2
    $ renpy.pause(0.1)
    return

label phone_msgi:
    $ renpy.pause()
    hide screen phone_message_image
    $ renpy.pause(0.1)
    return

label phone_after_menu:
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    return

label hide_phone_messages:
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    return

label phone_end:
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    show phone at phone_hide
    $ renpy.pause(0.2)
    return

label message(who, what, prepause=True):
    if prepause:
        $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    # if you want to change the players name to be something else than "me" you can change it here
    if who.name.lower() == "me":
        show screen phone_message2(who.name, what, _transient=True)
    else:
        show screen phone_message(who.name, what, _transient=True)
    return

label reply_message(what, skip=False):

    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    show screen phone_message3(what, _transient=True)
    return

label message_img(who, what,img):
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    show screen phone_message_image(who, what,img)
    return


label message_start(who, what):
    # if you want to change the players name to be something else than "me" you can change it here
    if who.name.lower() == "me":
        show screen phone_message2(who, what)
    else:
        show screen phone_message(who, what)
    return

label phone_call(who, emotion,  what, status=1):
    hide screen phone_call
    hide screen phone_notif
    show screen phone_call(who.name, emotion, status)
    "[who.name]" "[what]" (who_color=charcolor[who.name])
    return

label phone_notif(sprite, who):
    hide screen phone_notif
    show screen phone_notif(sprite, who)
    return

# Phone Styles
init 5:
    style phone_message_vbox:
        xalign 0.5
        yalign 0
        ypos 150
        xsize 260

    style phone_message_frame:
        background Solid("#d9398c")
        ypadding 10
        xpadding 10

    style phone_message_frame2:
        background Solid(charcolor['Player'])
        ypadding 10
        xpadding 10

    style phone_message_contents:
        spacing 10

    style phone_message is say_dialogue:
        xoffset 0
        outlines []
        xalign 1
        yalign 0

    style phone_message2 is say_dialogue:
        xoffset 0
        outlines []
        xalign 1
        yalign 0

    style phone_message_who is phone_message:
        color "#ecf0f1"
        size 21

    style phone_message_what is phone_message:
        color "#ffffff"
        size 20
    style phone_reply is default:
        size 18
        xalign 0.5
        xsize 275
        background Solid("#666")
        hover_background Solid(charcolor['Player'])
        ypadding 10
        xpadding 10

image phone_tindah = "images/phone/phone tindah.png"
image phone = "images/phone/phone.png"

screen phone_message(who, what):
    vbox at incoming_message:
        style_group "phone_message"
        ypos 0.23
        add "images/phone/bubble-tip.png" at phone_message_bubble_tip

        frame:
            style_group "phone_message"

            vbox:
                style "phone_message_contents"
                text who style "phone_message_who"
                text what style "phone_message_what"

screen phone_message2(who, what):
    vbox at incoming_message:
        style_group "phone_message"
        xoffset -384
        xalign 1.0
        ypos 0.23
        # this one adds the triangular tip for the bubble, if you change colors you change this images too
        add "images/phone/bubble-tip2.png" at phone_message_bubble_tip2

        frame:
            style_group "phone_message2"
            background Solid(charcolor[who])
            xsize 200

            vbox:
                style "phone_message_contents"
                text who style "phone_message_who"
                text what style "phone_message_what"

screen phone_message3(what):
    vbox at incoming_message:
        style_group "phone_message"
        xoffset -384
        xalign 1.0
        ypos 0.23
        # this one adds the triangular tip for the bubble, if you change colors you change this images too
        add "images/phone/bubble-tip2.png" at phone_message_bubble_tip2

        frame:
            style_group "phone_message2"
            background Solid(charcolor['Player'])#"#78E8A0")
            xsize 200

            vbox:
                style "phone_message_contents"
                ##text who style "phone_message_who"
                text what style "phone_message_what"

screen phone_reply(reply1, reply2, reply3):
    modal True
    layer "middle"
    vbox:
        at delay
        xalign 0.529
        yalign 0.65
        spacing 2

        textbutton "[reply1]" action [SetVariable('itemselected', itemchoices['A']), Return(None)] style "phone_reply"
        textbutton "[reply2]" action [SetVariable('itemselected', itemchoices['B']), Return(None)] style "phone_reply"
        textbutton "[reply3]" action [SetVariable('itemselected', itemchoices['C']), Return(None)] style "phone_reply"

# here is a new menu that has more options than two
# basically i just added one more textbutton here, and the additional labels needed in the call
# if you wish to make a menu with one or four just copy the code below and modify it a bit
screen phone_reply2(reply1, reply2):
    modal True
    layer "middle"
    vbox:
        xalign 0.529
        yalign 0.65
        spacing 2

        textbutton "[reply1]" action [SetVariable('itemselected', itemchoices['A']), Return(None)] style "phone_reply"
        textbutton "[reply2]" action [SetVariable('itemselected', itemchoices['B']), Return(None)] style "phone_reply"

screen phone_call(who, emotion, status=1):
    layer "middle"
    modal False
    default img = "images/[who]/[who] [emotion].png"
    if status == 0:
        frame at dissolve2:
            background "images/phone/bg phone vc.png"
            xalign 0.5
            yalign 0.5
            xsize 350
            ysize 422
            xoffset -1
            add img:
                xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.4

    else:
        frame:
            background "images/phone/bg phone vc.png"
            xalign 0.5
            yalign 0.5
            xsize 350
            ysize 422
            xoffset -1
            add img:
                xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.4

screen phone_notif(sprite, who):
    modal False
    layer "middle"
    frame at dissolve2:
        background "images/phone/bg phone.png"
        xalign 0.5
        yalign 0.5
        xsize 352
        ysize 422
        vbox:
            xfill True
            yfill True
            xalign 0.5
            yalign 0.5
            image sprite:
                xalign 0.5
                yalign 0.5
            text "[who]":
                xalign 0.5
                color "#000000"
            text "is Calling...":
                xalign 0.5
                color "#000000"
            hbox:
                xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0
                xalign 0.5
                yalign 0.0
                spacing 50
                yoffset -30
                image "images/phone/phone answer call.png":
                    zoom 1.2
                image "images/phone/phone end call.png":
                    zoom 1.2


style phone_reply_text:
    xalign 0.5

screen phone_message_image(who, what, img):
    vbox at incoming_message:
        style_group "phone_message"
        add "images/phone/bubble-tip.png" at phone_message_bubble_tip

        frame:
            style_group "phone_message"

            vbox:
                style "phone_message_contents"
                text who style "phone_message_who"
                text what style "phone_message_what"
                add img


############# phone code ends ############
