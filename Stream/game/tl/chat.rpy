style chatbox:
    xsize 400
    ysize 600
    xalign 0.95
    yalign 0.5
    background Frame("background_chat.png")
screen chatTitle(dialogue=["hello"]):
    frame:
        style "chatbox"
        text "CHAT" xalign 0.5 yalign 0.05
        for d in dialogue:
            textbutton "[d]" xalign 0.2 yalign 0.95
