image notify:
    "images/misc/notify.png"

transform t_notify:
    xpos 0.5
    ypos 0.0
    xanchor 0.5
    yanchor 0.0
    zoom 1.0
    on show:
        yoffset -80
        linear 1.0 yoffset 0
    on hide:
        pause 2.0
        yoffset 0
        linear 1.0 yoffset -120

screen notify(img):
    layer "screens"
    zorder 50
    add img at t_notify
    timer 1.5 action Hide("notify")
