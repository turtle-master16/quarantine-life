# Sprite Transforms
transform moveright:
    linear 0.5 xpos 0.85
transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -20
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0

# Phone Transforms
transform phone_pickup:
    subpixel True xpos 0.5 ypos 1.03 xanchor 0.5 yanchor 1.0 rotate None
    parallel:
        ypos 2.0
        linear 0.6 ypos 1.0

transform phone_hide:
    ypos 1.03
    linear 1.0 ypos 2.0
transform phone_message_bubble_tip:
    xoffset 10
    yoffset 1
transform phone_message_bubble_tip2:
    xoffset 165
    yoffset 1
transform scrolling_out_message:
    easeout 0.1 yoffset -30 alpha 0
transform incoming_message:
    xoffset -32
    yoffset 100
    alpha 0
    parallel:
        easein 0.1 alpha 1
    parallel:
        easein 0.2 yoffset 0

    on hide:
        scrolling_out_message
transform dissolve2:
    parallel:
        alpha -0.01
        linear 0.8 alpha 1.3

# Used in timer countdown
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

# Cropped images positioning convenience
transform left_corner:
    xalign 0.0
    yalign 1.0

transform right_corner:
    xalign 1.0
    yalign 1.0

# Hide and Show animations for UI stuff
transform t_flapButton:
    yanchor 1.0
    zoom 0.3
    on show:
        ypos 1.0
        yoffset 130
        linear 0.3 yoffset 0
    on hide:
        linear 0.3 yoffset 130

transform t_price_list:
    on show:
        yoffset 700
        linear 0.8 yoffset 0
    on hide:
        yoffset 0
        linear 0.8 yoffset 700

transform double:
    zoom 2.0

transform third:
    zoom 1.3
