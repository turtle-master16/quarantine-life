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
    xanchor 0.0
    yanchor 1.0
    xpos 0.0
    ypos 1.0

transform right_corner:
    xanchor 1.0
    yanchor 1.0
    xpos 1.0
    ypos 1.0
