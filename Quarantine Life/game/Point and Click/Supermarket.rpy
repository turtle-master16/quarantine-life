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
    'redcan': MartItem("redcan", shopItemMap['redcan'], 28, 0, alt_name="Red can"),
    'yellowcan': MartItem("yellowcan", shopItemMap['yellowcan'], 22, 0, alt_name="Yellow can"),
    'orangecan': MartItem("orangecan", shopItemMap['greencan'], 34, 0, alt_name="Orange can"),
    'greencan': MartItem("greencan", shopItemMap['browncan'], 23, 0, alt_name="Green can"),
    'browncan': MartItem("browncan", shopItemMap['toiletroll'], 27, 0, alt_name="Brown can"),
    'toiletroll': MartItem("toiletroll", shopItemMap['redcan'], 15, 0, alt_name="Toilet Roll"),
    'facemask': MartItem("facemask", shopItemMap['facemask'], 25, 0, alt_name="Facemask"),
    'hygiene': MartItem("hygiene", shopItemMap['hygiene'], 36, 0, alt_name="Hygiene Products"),
}

transform t_flapButton:
    yanchor 1.0
    on show:
        ypos 1.0
        yoffset 75
        linear 0.3 yoffset 0
    on hide:
        linear 0.3 yoffset 75

transform t_price_list:
    on show:
        yoffset 700
        linear 0.8 yoffset 0
    on hide:
        yoffset 0
        linear 0.8 yoffset 700

transform t_instructions:
    on show:
        yoffset 700
        linear 0.6 yoffset 0
    on hide:
        linear 0.6 yoffset 700

# Supermart ------------------
screen supermarket:
    layer "background"
    imagemap:
        ground "images/bg/bg supermarket.png"
        hotspot mart_items["redcan"] action Call("shopItemTake", "redcan")
        hotspot mart_items["redcan2"] action Call("shopItemTake", "redcan")
        hotspot mart_items["yellowcan"] action Call("shopItemTake", "yellowcan")
        hotspot mart_items["orangecan"] action Call("shopItemTake", "orangecan")
        hotspot mart_items["orangecan2"] action Call("shopItemTake", "orangecan")
        hotspot mart_items["orangecan3"] action Call("shopItemTake", "orangecan")
        hotspot mart_items["greencan"] action Call("shopItemTake", "greencan")
        hotspot mart_items["greencan2"] action Call("shopItemTake", "greencan")
        hotspot mart_items["browncan"] action Call("shopItemTake", "browncan")
        hotspot mart_items["toiletroll"] action Call("shopItemTake", "toiletroll")
        hotspot mart_items["toiletroll2"] action Call("shopItemTake", "toiletroll")
        hotspot mart_items["facemask"] action Call("shopItemTake", "facemask")
        hotspot mart_items["hygiene"] action Call("shopItemTake", "hygiene")
        hotspot mart_items["hygiene2"] action Call("shopItemTake", "hygiene")
    imagebutton:
        idle im.Flip("images/misc/arrow.png", horizontal=True)
        xalign 1.0
        yalign 0.5
        action Call("supermarket.shop_win_conditions")

screen price_list:
    modal True
    zorder 1
    frame:
        background Solid("#fff")
        at t_price_list
        xpos 0.5
        ypos 0.2
        xanchor 0.5
        vbox:
            hbox:
                vbox:
                    text "ITEMS":
                        color "#000"
                        xalign 0.5
                    null height 15
                    for item in shopItems:
                        text "{}".format(shopItems[item].alt_name):
                            color "#000"
                        null height 5
                null width 10
                vbox:
                    text "PRICE":
                        color "#000"
                        xalign 0.5
                    null height 15
                    for item in shopItems:
                        text "₱{}.0".format(shopItems[item].price):
                            color "#000"
                        null height 5
                null width 15
                vbox:
                    text "ON HAND":
                        color "#000"
                        xalign 0.5
                    null height 15
                    for item in shopItems:
                        text "x{}".format(shopItems[item].onhand):
                            color "#000"
                            xalign 0.5
                        null height 5
            null height 5
            hbox:
                textbutton "Close[[X]":
                    text_color "#000"
                    action [Hide("price_list"), Function(showFlapButtons)]
                text "Total cost: ₱{}.0".format(getCost()):
                    color "#000"
                    xpos 0.4

label shopItemTake(item):
    $ renpy.hide_screen("flapButton")
    show bg supermarket onlayer background
    if not(item == 'hygiene'):
        $ item_name = shopItems[item].alt_name
        pl "How many [item_name]s should I take?"
    else:
        pl "How many hygiene products should I take?"
    menu:
        "One":
            $ shopItems[item].takeItem(1)
        "Two":
            $ shopItems[item].takeItem(2)
        "Three":
            $ shopItems[item].takeItem(3)
        "Return One" if shopItems[item].onhand > 0:
            pl "I'll just put one back."
            $ shopItems[item].takeItem(-1)
        "Nevermind":
            pl "I don't need any more of these."
    return

init python:
    class MartItem():
        def __init__(self, name, img, price, onhand, alt_name=None):
            self.name = name
            self.img = img
            self.price = price
            self.onhand = onhand
            self.alt_name = alt_name

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
