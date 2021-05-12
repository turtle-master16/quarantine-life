init python:
    class phone_convo:
        def __init__(self, people, con, split=None):
            self.people = people
            self.con = con
            self.split = split
            self.sent = []
            self.typing = ""
            self.speaker = None
            self.speaking = None
            self.msg = None
            self.wait = 0
            self.choose = None
        def set_msg(self, m):
            self.msg = m
            self.choose = None

        def append_split(self, route):
            if isinstance(self.split, list):
                for ii, i in enumerate(self.split[route]):
                    if ii > 1:
                        self.con.append(i)


        def tick(self):
            if self.wait > 0:
                self.wait -= 0.5
            else:
                if self.msg is None:
                    self.msg = self.con.pop(0)
                    self.wait = 1.0
                    if isinstance(self.msg, (int, long)):
                        self.speaker = self.msg
                        self.speaking = self.msg
                        self.msg = None
                    elif isinstance(self.msg, list):
                        self.choose = self.msg
                elif self.choose:
                    pass
                else:
                    if self.typing == self.msg:
                        if self.speaker is not None:
                            self.sent.append([self.speaker,[self.msg]])
                            self.speaker = None
                            self.msg = None
                            Hide("phone")()
                            Show("phone",c = self)()
                            # Scroll("phone_vp", "vertical increase", 1000)()

                        else:
                            self.sent[-1][1].append(self.msg)
                            self.msg = None
                            Hide("phone")()
                            Show("phone", c = self)()
                            # Scroll("phone_vp", "vertical increase", 1000)()
                        self.typing = ""
                    else:
                        self.typing += str(self.msg[len(self.typing)])



screen phone(c):
    modal True
    default last = 100
    # text str(c.typing) align 0.0,0.0
    if len(c.con) or c.msg:
        timer .1 repeat True action Function(c.tick)
    style_prefix "phone"
    frame:
        xysize(650,700) padding(0,0) background "#222" align .5,.5
        frame:
            ysize 80 xfill True yalign 0.0 background "#333b"
            text c.people[1][0]
        frame:
            xysize 580,70 align .5,1.0 yoffset -10 background "#333b"
            if c.speaking == 0:
                text c.typing
            else:
                if c.wait > 0:
                    pass
                else:
                    text "{} is typing...".format(c.people[1][0]) size 15 yoffset -50 xalign 0.0
        frame:
            background None padding (30,80,30,110) yfill True
            viewport id "phone_vp":
                draggable True scrollbars None yinitial 1.0
                xfill False
                yfill False
                yalign 1.0
                frame:
                    padding(0,0) background None
                    vbox:
                        xfill True spacing 4
                        for i in c.sent:
                            if i[0] == 0:
                                for iii,ii in enumerate(i[1]):
                                    if iii == 0:
                                        hbox:
                                            xalign 1.0 spacing 0
                                            frame:
                                                style "phone_right" xoffset 64
                                                text ii color "#000"
                                            add c.people[i[0]] yalign 0.0
                                    else:
                                        frame:
                                            xalign 1.0
                                            style "phone_right_1"
                                            text ii color "#000"
                            else:
                                for iii,ii in enumerate(i[1]):
                                    if iii == 0:
                                        hbox:
                                            xalign 0.0 spacing 0
                                            add c.people[i[0]] yalign 0.0
                                            frame:
                                                style "phone_left" xoffset -64
                                                text ii color "#000"
                                    else:
                                        frame:
                                            xalign 0.0
                                            style "phone_left_1"
                                            text ii color "#000"

    if c.choose:
        vbox:
            align .5,.5 spacing 10
            for i in c.choose:
                button:
                    xsize 580 align .5,.5 background "#ffa500" padding 10,20
                    text i align .5,.5
                    action [Function(c.set_msg, i), Function(c.append_split, c.choose.index(i))]
style phone_text:
    size 22
    yalign .5

style phone_right:
    background Frame(im.Flip("phone/frm0.png",True), 10,20,76,10)
    padding(32,12,96,12)
    yminimum 64

style phone_left:
    background Frame("phone/frm0.png", 76,20,10,10)
    padding(96,12,32,12)
    yminimum 64

style phone_right_1:
    background Frame(im.Flip("phone/frm1.png",True), 10,20,76,10)
    padding(32,12,96,12)
    yminimum 64

style phone_left_1:
    background Frame("phone/frm1.png", 76,20,10,10)
    padding(96,12,32,12)
    yminimum 64

default phone_conv_2 = phone_convo(
    # Names
    [
        ["[player_name]", "phone/img1.png"],
        ["Jason", "phone/jason.png"],
    ],
    # Main Dialogue
    [
        1,
        "Hi",
        0,
        ["Hi", "I like your hair", "Hit him with a pickup line"],
    ],
    # Choice Dialogue
    [
        # Route A
        [
            0,
            "Hi. It’s very nice to meet you.",
            1,
            "Hi. It’s very nice to meet you as well.",
        ],
        # Route B
        [
            0,
            "Your hair, it looks good. I like it.",
            1,
            "My Hair?",
            0,
            "Yeah. From your profile picture, it really suits you.",
            1,
            "Oh. Haha. Thank you, I appreciate the compliment.",
        ],
        # Route C
        [
            0,
            "Happy Mother's Day!",
            1,
            "Mais...",
        ],
    ]
)
