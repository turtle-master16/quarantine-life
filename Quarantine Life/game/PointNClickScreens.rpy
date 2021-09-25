# Event Flags
define itemselected = ""
define itemchoices = {"Reset":0, "A": 1, "B": 2, "C":3, "D":4, "E":5, "F":6}
define correctans = 0 # Quiz game

screen broomfind():
    $ broom = (1206, 432, 65, 278)
    imagemap:
        ground "images/bg/bg livingroom back.png"
        hotspot broom action Return()

# Activity Pick ------------------
screen livingroomact():
    $ ret = 2
    $ lvroom_items = {
        "tv":(986, 296, 118, 234),
        "mat":(412, 608, 441, 83),
        "mugs":(448, 461, 102, 45),
        "couch":(94, 500, 302, 185),
        "mirror":(127, 198, 42, 158),
        "window": (296, 181, 655, 208)
    }
    imagemap:
        ground "images/bg/bg livingroom back.png"
        hotspot lvroom_items["tv"] action [SetVariable("itemselected", itemchoices["A"]), Jump("livingroomact")]
        hotspot lvroom_items["mat"] action Call("livingroomact.misc_item_dialog", 1)
        hotspot lvroom_items["mugs"] action Call("livingroomact.misc_item_dialog", 2)
        hotspot lvroom_items["couch"] action Call("livingroomact.misc_item_dialog", 3)
        hotspot lvroom_items["mirror"] action Call("livingroomact.misc_item_dialog", 4)
        hotspot lvroom_items["window"] action Call("livingroomact.misc_item_dialog", 5)

    imagebutton:
        idle "images/misc/arrow.png"
        yalign 0.5
        action [SetVariable("itemselected", 2), Jump("livingroomact")]

screen bedroomact():
    $ ret = 4
    $ bdroom_items = {
        "bed":(91, 434, 624, 182),
        "phone":(206, 358, 63, 28),
        "exercise":(903, 365, 178, 133),
        "books": (209, 48, 145, 105),
        "mirror": (60, 60, 64, 115),
        "drawer": (556, 284, 253, 131),
        }
    imagemap:
        ground "images/bg/bg bedroom back.png"
        hotspot bdroom_items["bed"] action [SetVariable("itemselected", itemchoices["A"]), Jump("bedroomact")]
        hotspot bdroom_items["phone"] action [SetVariable("itemselected", itemchoices["B"]), Jump("bedroomact")]
        hotspot bdroom_items["exercise"] action [SetVariable("itemselected", itemchoices["C"]), Jump("bedroomact")]
        hotspot bdroom_items["books"] action Call("bedroomact.misc_item_dialog", 1)
        hotspot bdroom_items["mirror"] action Call("bedroomact.misc_item_dialog", 2)
        hotspot bdroom_items["drawer"] action Call("bedroomact.misc_item_dialog", 3)
    imagebutton:
        idle im.Flip("images/misc/arrow.png", horizontal=True)
        xalign 1.0
        yalign 0.5
        action [SetVariable("itemselected", 4), Jump("bedroomact")]

# Supermart ------------------
define mart_item_count = {
    "facemask":0,
    "toiletpaper":0,
    "redcan": 0,
    "greencan": 0,
    "orangecan": 0,
    "browncan": 0,
    "yellowcan": 0,
    "hygiene": 0,
}
screen supermarket:
    layer "background"
    $ mart_items = {
        "facemask":(709, 404, 502, 314),
        "toiletpaper":(824, 180, 137, 36),
        "toiletpaper2":(990, 280, 216, 73),
        "redcan":(0, 343, 195, 25),
        "redcan2": (241, 361, 654, 21),
        "greencan": (1, 414, 198, 60),
        "greencan2": (234, 421, 455, 28),
        "orangecan":(462, 486, 217, 26),
        "browncan":(1, 218, 199, 70),
        "yellowcan":(240, 285, 655, 28),
        "hygiene":(212, 495, 231, 221),
        "hygiene2":(88, 522, 97, 196),
        "hygiene3":(10, 579, 67, 139),
    }
    imagemap:
        ground "images/bg/bg supermarket.png"
        hotspot mart_items["facemask"] action Call("supermarket.item_take", 1)
        hotspot mart_items["toiletpaper"] action Call("supermarket.item_take", 2)
        hotspot mart_items["toiletpaper2"] action Call("supermarket.item_take", 2)
        hotspot mart_items["redcan"] action Call("supermarket.item_take", 3)
        hotspot mart_items["redcan2"] action Call("supermarket.item_take", 3)
        hotspot mart_items["greencan"] action Call("supermarket.item_take", 4)
        hotspot mart_items["greencan2"] action Call("supermarket.item_take", 4)
        hotspot mart_items["orangecan"] action Call("supermarket.item_take", 5)
        hotspot mart_items["browncan"] action Call("supermarket.item_take", 6)
        hotspot mart_items["yellowcan"] action Call("supermarket.item_take", 7)
        hotspot mart_items["hygiene"] action Call("supermarket.item_take", 8)
        hotspot mart_items["hygiene2"] action Call("supermarket.item_take", 8)
        hotspot mart_items["hygiene3"] action Call("supermarket.item_take", 8)

    imagebutton:
        idle im.Flip("images/misc/arrow.png", horizontal=True)
        xalign 1.0
        yalign 0.5
        action Call("supermarket.maingame", True)

# Work preparation ---------------
define hasBedkey = False
define hasFaceshield = False
screen workprep(location="livingroom"):
    $ ret = 2
    $ lvroom_items = {
        "faceshield": (1006, 526, 68, 46),
        "drawer": (35, 573, 199, 141),
        "correctPlant":(854, 419, 54, 84),
        "picture":(127, 198, 42, 158),
        "wrongPlantA":(288, 416, 57, 72),
        "wrongPlantB":(518, 324, 50, 67),
        "wrongPlantC":(733, 318, 50, 73),
        "tv":(1014, 283, 132, 218),
        "mugs":(448, 461, 102, 45),
        "sofaPartA":(252, 503, 138, 173),
        "sofaPartB":(98, 443, 159, 114),
        "window": (293, 178, 660, 123),
    }
    if location == "livingroom":
        imagemap:
            ground "images/bg/bg livingroom back.png"
            hotspot lvroom_items["faceshield"] action [SetVariable("itemselected", itemchoices["A"]), Jump("workprep")]
            hotspot lvroom_items["tv"] action Call("workprep.misc_item_dialog", 1)
            hotspot lvroom_items["picture"] action Call("workprep.misc_item_dialog", 2)
            hotspot lvroom_items["correctPlant"] action Call("workprep.misc_item_dialog", 3)
            hotspot lvroom_items["wrongPlantA"] action Call("workprep.misc_item_dialog", 4)
            hotspot lvroom_items["wrongPlantB"] action Call("workprep.misc_item_dialog", 4)
            hotspot lvroom_items["wrongPlantC"] action Call("workprep.misc_item_dialog", 4)
            hotspot lvroom_items["mugs"] action Call("workprep.misc_item_dialog", 5)
            hotspot lvroom_items["sofaPartA"] action Call("workprep.misc_item_dialog", 6)
            hotspot lvroom_items["sofaPartB"] action Call("workprep.misc_item_dialog", 6)
            hotspot lvroom_items["window"] action Call("workprep.misc_item_dialog", 7)
            hotspot lvroom_items["drawer"] action Call("workprep.misc_item_dialog", 8)

        imagebutton:
            idle "images/misc/arrow.png"
            yalign 0.5
            action [SetVariable("itemselected", 2), Jump("livingroomact")]

# Escape Room ------------------------
define haskey = False
define screenon = False
screen escaperoom():
    layer "background"
    $ items = {
    "books":(11, 79, 160, 167),
    "door":(1021, 3, 74, 494),
    "window":(358, 1, 205, 299),
    "pot": (309, 187, 50, 105),
    "dumbell":(419, 340, 92, 92),
    "phone":(369, 497, 113, 26),
    "drawer":(239, 299, 171, 166),
    "sidetable":(1049, 522, 228, 194),
    "bed":(572, 404, 425, 312),
    }
    imagemap:
        ground "images/bg/bg bedroom left evening.png"
        hotspot items["books"] action [SetVariable("itemselected", itemchoices["A"]), Jump("escaperoom")]
        hotspot items["door"] action [SetVariable("itemselected", itemchoices["B"]), Jump("escaperoom")]
        hotspot items["pot"] action Call("escaperoom.misc_item_dialog", 1)
        hotspot items["dumbell"] action Call("escaperoom.misc_item_dialog", 2)
        hotspot items["phone"] action Call("escaperoom.misc_item_dialog", 3)
        hotspot items["drawer"] action Call("escaperoom.misc_item_dialog", 4)
        hotspot items["window"] action Call("escaperoom.misc_item_dialog", 5)
        hotspot items["sidetable"] action Call("escaperoom.misc_item_dialog", 6)
        hotspot items["bed"] action Call("escaperoom.misc_item_dialog", 7)
