# Supermart ------------------
screen supermarket():
    layer "background"
    $ mart_items = {
        "redcan":(0, 343, 195, 25),
        "redcan2": (241, 361, 654, 21),
        "yellowcan":(240, 285, 655, 28),
        "orangecan":(462, 486, 217, 26),
        "greencan": (1, 414, 198, 60),
        "greencan2": (234, 421, 455, 28),
        "browncan":(1, 218, 199, 70),
        "toiletroll":(824, 180, 137, 36),
        "toiletroll2":(990, 280, 216, 73),
        "facemask":(709, 404, 502, 314),
        "hygiene":(212, 495, 231, 221),
        "hygiene2":(88, 522, 97, 196),
        "hygiene3":(10, 579, 67, 139),
    }
    imagemap:
        ground "images/bg/bg supermarket.png"
        hotspot mart_items["redcan"] action Call("shopItemTake", "redcan")
        hotspot mart_items["redcan2"] action Call("shopItemTake", "redcan")
        hotspot mart_items["yellowcan"] action Call("shopItemTake", "yellowcan")
        hotspot mart_items["orangecan"] action Call("shopItemTake", "orangecan")
        hotspot mart_items["greencan"] action Call("shopItemTake", "greencan")
        hotspot mart_items["greencan2"] action Call("shopItemTake", "greencan")
        hotspot mart_items["browncan"] action Call("shopItemTake", "browncan")
        hotspot mart_items["toiletroll"] action Call("shopItemTake", "toiletroll")
        hotspot mart_items["toiletroll2"] action Call("shopItemTake", "toiletroll")
        hotspot mart_items["facemask"] action Call("shopItemTake", "facemask")
        hotspot mart_items["hygiene"] action Call("shopItemTake", "hygiene")
        hotspot mart_items["hygiene2"] action Call("shopItemTake", "hygiene")
        hotspot mart_items["hygiene3"] action Call("shopItemTake", "hygiene")
    imagebutton:
        idle im.Flip("images/misc/arrow.png", horizontal=True)
        xalign 1.0
        yalign 0.5
        action Call("supermarket.shop_win_conditions")

init python:
    class MartItem():
        def __init__(self, name, img, price, onhand):
            self.name = name
            self.img = img
            self.price = price
            self.onhand = onhand
        def totalAmount(self):
            return self.onhand * self.price
        def showItem(self):
            renpy.show(self.img[0], at_list=[self.img[1]], layer='background')
        def takeItem(self, qnty):
            self.onhand += qnty
            self.updateOverallCost()
        def updateOverallCost(self):
            cost = 0
            for item in shopItems:
                cost += shopItems[item].totalAmount()
            globals()['currentItemCost'] = cost
    def getCost():
        return currentItemCost
    def hasAcquiredNeedItems():
        enufHygiene = shopItems['hygiene'].onhand >= 2
        enufToiletPaper = shopItems['toiletroll'].onhand >= 3
        enufGreencan = shopItems['greencan'].onhand >= 1
        return enufHygiene and enufToiletPaper and enufGreencan
default currentItemCost = 0
default shopItemMap = {
    'redcan': ["bedkey", Transform(xalign=0.5, yalign=0.5)],
    'yellowcan': ["bedkey", Transform(xalign=0.5, yalign=0.5)],
    'orangecan': ["bedkey", Transform(xalign=0.5, yalign=0.5)],
    'greencan': ["bedkey", Transform(xalign=0.5, yalign=0.5)],
    'browncan': ["bedkey", Transform(xalign=0.5, yalign=0.5)],
    'toiletroll': ["bedkey", Transform(xalign=0.5, yalign=0.5)],
    'facemask': ["bedkey", Transform(xalign=0.5, yalign=0.5)],
    'hygiene': ["bedkey", Transform(xalign=0.5, yalign=0.5)],
}
default shopItems = {
    'redcan':MartItem("redcan", shopItemMap['redcan'], 28, 0),
    'yellowcan':MartItem("yellowcan", shopItemMap['yellowcan'], 22, 0),
    'orangecan':MartItem("orangecan", shopItemMap['greencan'], 34, 0),
    'greencan':MartItem("greencan", shopItemMap['browncan'], 23, 0),
    'browncan':MartItem("browncan", shopItemMap['toiletroll'], 27, 0),
    'toiletroll':MartItem("toiletroll", shopItemMap['redcan'], 15, 0),
    'facemask':MartItem("facemask", shopItemMap['facemask'], 25, 0),
    'hygiene':MartItem("hygiene", shopItemMap['hygiene'], 36, 0),
}
label shopItemTake(item):
    if not(item=='hygiene'):
        pl "How many [item]s should I take?"
    else:
        pl "How many hygiene products should I take?"
    menu:
        "One":
            $ shopItems[item].takeItem(1)
        "Two":
            $ shopItems[item].takeItem(2)
        "Three":
            $ shopItems[item].takeItem(3)
        "Nevermind":
            pl "I don't need any more of these."
    return
