init python:
    import random
    class ClickableItems:
        def __init__(self, dialogue, hspot, xoff=0, yoff=0):
            self.dialogue = dialogue
            self.hspot = hspot
            self.is_grouped = isinstance(hspot, list)
            if not(self.is_grouped):
                self.sparklepos = getRectCenter(hspot)
                self.sparklepos[0] += xoff
                self.sparklepos[1] += yoff
            else:
                self.sparklepos = [getRectCenter(hs) for hs in hspot]
        def sayDialogue(self):
            renpy.call("objDialogue", dia=self.dialogue)

    def getRectCenter(rect):
        return [int(rect[0] + rect[2] * 0.5), int(rect[1] + rect[3] * 0.5)]

screen spk:
    if currentRoom == ROOMS["livingroom"]:
        for item in lvroom_itemsC:
            if lvroom_itemsC[item].is_grouped:
                for cent in lvroom_itemsC[item].sparklepos:
                    add "spark":
                        pos cent
            else:
                add "spark":
                    pos lvroom_itemsC[item].sparklepos
            if not(onhand["faceshield"]):
                add "spark":
                    pos lvroom_itemsC["tv"].sparklepos
                add "spark":
                    pos (991, 514)
            if not(onhand["bedkey"]):
                for item2 in lvroom_left:
                    add "spark":
                        pos lvroom_left[item2].sparklepos
    elif currentRoom == ROOMS["kitchen"]:
        for item in kitchen_items:
            if kitchen_items[item].is_grouped:
                for cent in kitchen_items[item].sparklepos:
                    add "spark":
                        pos cent
            else:
                if not(item == "sanitizer") or not(onhand["sanitizer"]):
                    add "spark":
                        pos kitchen_items[item].sparklepos
    elif currentRoom == ROOMS["bedroom"]:
        for item in bdroom_items:
            add "spark":
                pos bdroom_items[item].sparklepos
        add "spark":
            pos (250, 300)


# WORKPREP -------------------------------------------------------
default lvroom_itemsC = {
    "drawerLvrm":    ClickableItems(dialogue=object_dialogue['drawerLvrm'],   hspot=(35, 573, 199, 141)),
    "correctPlant":  ClickableItems(dialogue=object_dialogue['correctPlant'], hspot=(854, 419, 54, 84)),
    "pictureLvrm":   ClickableItems(dialogue=object_dialogue['pictureLvrm'],  hspot=(127, 198, 42, 158), yoff=-80),
    "wrongPlant":    ClickableItems(dialogue=object_dialogue['wrongPlant'],   hspot=[(288, 416, 57, 72),
                                                                                    (518, 324, 50, 67),
                                                                                    (733, 318, 50, 73)]),
    "tv":            ClickableItems(dialogue=object_dialogue['tv'],           hspot=(1014, 283, 132, 218)),
    "mugs":          ClickableItems(dialogue=object_dialogue['mugs'],         hspot=(448, 461, 102, 45)),
    "sofa":          ClickableItems(dialogue=object_dialogue['sofa'],         hspot=(242, 501, 151, 183)),
    "window":        ClickableItems(dialogue=object_dialogue['window'],       hspot=(293, 178, 660, 123)),
}
default lvroom_right = {
    "tv":            ClickableItems(dialogue=object_dialogue['tv'],           hspot=(84, 277, 131, 205)),
    "faceshield":    ClickableItems(dialogue=object_dialogue['faceshield'],   hspot=(21, 489, 73, 49)),
}
default lvroom_left = {
    "drawerLvrm":    ClickableItems(dialogue=object_dialogue['drawerLvrm'],   hspot=(97, 553, 84, 49)),
}
define bdroom_items = {
    "bed":        ClickableItems(dialogue=object_dialogue['bed'],         hspot=(91, 434, 624, 182)),
    "phone":      ClickableItems(dialogue=object_dialogue['phone'],       hspot=(206, 364, 75, 32)),
    "dumbell":    ClickableItems(dialogue=object_dialogue['dumbell'],     hspot=(903, 365, 178, 133)),
    "books":      ClickableItems(dialogue=object_dialogue['books'],       hspot=(195, 33, 171, 121), yoff=20),
    "pictureBdrm":ClickableItems(dialogue=object_dialogue['pictureBdrm'], hspot=(60, 60, 64, 115)),
    "drawerBdrm": ClickableItems(dialogue=object_dialogue['drawerBdrm'],  hspot=(556, 284, 253, 131)),
    "window":     ClickableItems(dialogue=object_dialogue['window'],      hspot=(1076, 7, 117, 397)),
    "plant":      ClickableItems(dialogue=object_dialogue['plant'],       hspot=(462, 53, 72, 109)),
}
define kitchen_items = {
    "cans":       ClickableItems(dialogue=object_dialogue['cans'],      hspot=(237, 3, 260, 97), xoff=80),
    "cabinet":    ClickableItems(dialogue=object_dialogue['cabinet'],   hspot=(557, 288, 317, 207)),
    "stove":      ClickableItems(dialogue=object_dialogue['stove'],     hspot=(388, 189, 121, 121)),
    "sanitizer":  ClickableItems(dialogue=object_dialogue['sanitizer'], hspot=(845, 181, 45, 60)),
}

# SUPERMARKET --------------------
define mart_items = {
    "redcan":      (1,290,273,79),
    "redcan2":     (330,344,525,38),
    "yellowcan":   (332,282,527,37),
    "orangecan":   (1,525,231,164),
    "orangecan2":  (378,479,84,23),
    "orangecan3":  (688,478,101,24),
    "greencan":    (388,410,401,40),
    "greencan2":   (1,416,224,75),
    "browncan":    (0,132,258,133),
    "toiletroll":  (1069,282,163,78),
    "toiletroll2": (880,138,365,121),
    "facemask":    (808,416,462,242),
    "hygiene":     (494, 476, 179, 240),
    "hygiene2":    (355, 516, 139, 203),
}
