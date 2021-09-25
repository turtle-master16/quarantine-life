# Date UI
transform datebg:
    on show:
        yalign -0.08
        linear 0.4 yalign 0.0
    on hide:
        yalign 0.0
        linear 0.4 yalign -0.08
transform datetext:
    on show:
        yalign -0.05
        linear 0.4 yalign 0.01
        ease 0.3 zoom 1.1
        ease 0.3 zoom 1.0
    on hide:
        yalign 0.0
        linear 0.4 yalign -0.08

screen displayDate(date=""):
    tag Date
    zorder 2
    add Image("/xtras/DateBg.png"):
        at datebg
        xanchor 0.5
        xalign 0.19
    text date:
        at datetext
        xanchor 0.5
        size 20
        color "#000"
        xalign 0.19
