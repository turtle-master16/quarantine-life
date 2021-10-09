image notify:
    "images/misc/notify.png"

transform t_notify:
    xpos 0.5
    ypos 0.0
    xanchor 0.5
    yanchor 0.0
    zoom 1.4
    on show:
        yoffset -80
        linear 1.0 yoffset 0
    on hide:
        pause 2.0
        yoffset 0
        linear 1.0 yoffset -85

screen notify():
    layer "screens"
    zorder 50
    add "images/misc/notify.png" at t_notify
    timer 2.0 action Hide("notify")
