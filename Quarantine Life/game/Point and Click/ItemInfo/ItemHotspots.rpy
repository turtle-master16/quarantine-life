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
    if currentScreen == "supermarket":
        for item in mart_items:
            add "spark":
                pos getRectCenter(mart_items[item])

    elif currentScreen == "findActivity":
        if currentRoom == ROOMS["livingroom"]:
            add "spark":
                pos getRectCenter((986, 296, 118, 234))
        elif currentRoom == ROOMS["bedroom"]:
            add "spark":
                pos getRectCenter((195, 338, 80, 52))
            add "spark":
                pos getRectCenter((918, 374, 158, 121))
            add "spark":
                pos getRectCenter((64, 424, 632, 157))

    elif currentScreen == "workprep":
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
                        pos (1007, 420) # Hard coded sparkle
                if not(onhand["bedkey"]):
                    for item2 in lvroom_left:
                        add "spark":
                            pos (141, 579)
        elif currentRoom == ROOMS["kitchen"]:
            for item in kitchen_items:
                if kitchen_items[item].is_grouped:
                    for sparklepos in kitchen_items[item].sparklepos:
                        add "spark":
                            pos sparklepos
                else:
                    if not(item == "sanitizer") or not(onhand["sanitizer"]):
                        add "spark":
                            pos kitchen_items[item].sparklepos
                    if not(onhand['sanitizer']):
                        add "spark":
                            pos getRectCenter((1200,232,25,69)) # HArd cOdEd Spark go BrrRrr

        elif currentRoom == ROOMS["bedroom"]:
            for item in bdroom_items:
                if bdroom_items[item].is_grouped:
                    for sparklepos in bdroom_items[item].sparklepos:
                        add "spark":
                            pos sparklepos
                else:
                    add "spark":
                        pos bdroom_items[item].sparklepos
            add "spark":
                pos getRectCenter((174,188,157,150)) # HArd cOdEd Spark go BrrRrr requiem


# WORKPREP -------------------------------------------------------
default lvroom_itemsC = {
    "apple":          ClickableItems(dialogue=object_dialogue['apple'],        hspot=(624,214,46,46)),
    "bulb":           ClickableItems(dialogue=object_dialogue['bulb'],         hspot=(511,531,65,50)),
    "chime":          ClickableItems(dialogue=object_dialogue['chime'],        hspot=(750,25,30,70)),
    "correctPlant":   ClickableItems(dialogue=object_dialogue['correctPlant'], hspot=(769, 152, 67, 107)),
    "pictureLvrm":    ClickableItems(dialogue=object_dialogue['pictureLvrm'],  hspot=(74, 111, 66, 174)),
    "headphone":      ClickableItems(dialogue=object_dialogue['headphone'],    hspot=(1030,471,101,58)),
    "keyboard":       ClickableItems(dialogue=object_dialogue['keyboard'],     hspot=(768,484,44,28)),
    "lamp":           ClickableItems(dialogue=object_dialogue['lamp'],         hspot=(34,398,86,158)),
    "monitor":        ClickableItems(dialogue=object_dialogue['monitor'],      hspot=(824,396,108,120)),
    "mugs":           ClickableItems(dialogue=object_dialogue['mugs'],         hspot=(442,320,119,65)),
    "pencil":         ClickableItems(dialogue=object_dialogue['pencil'],       hspot=(138,539,38,23)),
    "screws":         ClickableItems(dialogue=object_dialogue['screws'],       hspot=(775,615,101,47)),
    "shoes":          ClickableItems(dialogue=object_dialogue['shoes'],        hspot=(1109,608,137,102)),
    "tablet":         ClickableItems(dialogue=object_dialogue['tablet'],       hspot=(765,302,47,68)),
    "trumpet":        ClickableItems(dialogue=object_dialogue['trumpet'],      hspot=(219,396,119,62)),
    "tv":             ClickableItems(dialogue=object_dialogue['tv'],           hspot=(1056,164,146,208)),
    "unit":           ClickableItems(dialogue=object_dialogue['unit'],         hspot=(649,388,87,120)),
    "wrongPlant":     ClickableItems(dialogue=object_dialogue['wrongPlant'],   hspot=[(280,278,64,98),
                                                                                     (512,152,69,104),
                                                                                     (876,278,66,103)]),
}
default lvroom_right = {
    "faceshield":    ClickableItems(dialogue=object_dialogue['faceshield'],   hspot=(21,391,73,54)),
}
default lvroom_left = {
    "drawerLvrm":    ClickableItems(dialogue=object_dialogue['drawerLvrm'],   hspot=(114,571,68,49)),
}
define bdroom_items = {
    "books":      ClickableItems(dialogue=object_dialogue['books'],       hspot=[(214,34,217,100),
                                                                                 (505,529,76,77),
                                                                                 (559,462,97,63),
                                                                                 (659,244,87,51),
                                                                                 (299,508,89,63),
                                                                                 (505,529,76,77)]),
    "drawerBdrm": ClickableItems(dialogue=object_dialogue['drawerBdrm'],  hspot=(580,306,266,144)),
    "dumbell":    ClickableItems(dialogue=object_dialogue['dumbell'],     hspot=(949,345,169,146)),
    "gameboy":    ClickableItems(dialogue=object_dialogue['gameboy'],     hspot=(428,496,62,58)),
    "lampB":    ClickableItems(dialogue=object_dialogue['lampB'],     hspot=(30,582,90,134)),
    "laptop":    ClickableItems(dialogue=object_dialogue['laptop'],     hspot=(1086,514,122,164)),
    "pencilCan":ClickableItems(dialogue=object_dialogue['pencilCan'], hspot=(599,226,33,68)),
    "pictureBdrm":ClickableItems(dialogue=object_dialogue['pictureBdrm'], hspot=(30,40,89,180)),
    "pillow":     ClickableItems(dialogue=object_dialogue['pillow'],         hspot=(76,450,130,114)),
    "phone":      ClickableItems(dialogue=object_dialogue['phone'],       hspot=(202,360,86,71)),
    "plant":      ClickableItems(dialogue=object_dialogue['wrongPlant'],       hspot=[(758,160,88,130),
                                                                                 (476,4,74,122)]),
    "poster":      ClickableItems(dialogue=object_dialogue['poster'],       hspot=(758,472,143,100)),
    "sofa":      ClickableItems(dialogue=object_dialogue['sofa'],       hspot=(359,262,156,189)),
}
define kitchen_items = {
    "greenApple": ClickableItems(dialogue=object_dialogue['greenApple'],  hspot=(786,235,35,43)),
    "bread":      ClickableItems(dialogue=object_dialogue['bread'],       hspot=(621,288,57,91)),
    "broom":      ClickableItems(dialogue=object_dialogue['broom'],       hspot=(1158,344,113,365)),
    "cans":       ClickableItems(dialogue=object_dialogue['cans'],        hspot=[(536,16,79,49),
                                                                                 (630,6,60,39),
                                                                                 (628,104,66,42),
                                                                                 (719,6,46,35),
                                                                                 (784,0,37,34),
                                                                                 (781,89,39,39)]),
    "faucet":     ClickableItems(dialogue=object_dialogue['faucet'],      hspot=(1052,214,17,56)),
    "mugs":       ClickableItems(dialogue=object_dialogue['mugs'],        hspot=[(562,404,144,105),
                                                                                  (524,120,95,64),
                                                                                  (899,251,29,34)]),
    "painting":   ClickableItems(dialogue=object_dialogue['painting'],    hspot=(855,441,200,117)),
    "plant":      ClickableItems(dialogue=object_dialogue['plant'],       hspot=(840,178,46,87)),
    "milk":       ClickableItems(dialogue=object_dialogue['milk'],        hspot=(719,79,45,80)),
    "saucepan":   ClickableItems(dialogue=object_dialogue['saucepan'],    hspot=(689,270,89,61)),
    "tissue":     ClickableItems(dialogue=object_dialogue['tissue'],      hspot=(1089,234,41,38)),
    "tray":       ClickableItems(dialogue=object_dialogue['tray'],        hspot=(856,606,272,115)),
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
    "bread":       (897, 291, 174, 67),
    "spray":       (241, 300, 62, 61),
    "oatmeal":     (225, 399, 147, 59),
}
