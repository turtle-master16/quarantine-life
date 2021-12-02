# Supermart ------------------
init python:
    class MartItem():
        def __init__(self, name, price, onhand, alt_name):
            self.name = name
            self.price = price
            self.onhand = onhand
            self.alt_name = alt_name
        def totalAmount(self):
            return self.onhand * self.price
        def takeItem(self, qnty):
            self.onhand += qnty
            updateOverallCost()

    def updateOverallCost():
        cost = 0
        for item in shopItems:
            cost += shopItems[item].totalAmount()
            globals()['currentItemCost'] = cost

    def getCost():
        return currentItemCost

    def hasAcquiredNeedItems():
        enufHygiene =     shopItems['hygiene'].onhand >= 2
        enufToiletPaper = shopItems['toiletroll'].onhand >= 3
        enufGreencan =    shopItems['greencan'].onhand >= 1
        return enufHygiene and enufToiletPaper and enufGreencan

    # Removes the number at the end of the string if it has one
    def truncateNumber(str):
        trtd_str = str
        if str[-1].isnumeric():
            trtd_str = str.replace("{}".format(str[-1]), "")
            return trtd_str
        return str



default currentItemCost = 0

default shopItems = {
#   KEY                    NAME         PRC   ONHD  IN-GAME-NAME
    'redcan':     MartItem("redcan",    28,   0,    alt_name="Red Can"),
    'yellowcan':  MartItem("yellowcan", 22,   0,    alt_name="Yellow Can"),
    'orangecan':  MartItem("orangecan", 34,   0,    alt_name="Orange Can"),
    'greencan':   MartItem("greencan",  23,   0,    alt_name="Green Can"),
    'browncan':   MartItem("browncan",  27,   0,    alt_name="Brown Can"),
    'toiletroll': MartItem("toiletroll",15,   0,    alt_name="Toilet Roll"),
    'facemask':   MartItem("facemask",  25,   0,    alt_name="Box of Face Masks"),
    'hygiene':    MartItem("hygiene",   36,   0,    alt_name="Hygiene Products"),
    'bread':      MartItem("bread",     40,   0,    alt_name="Sliced Bread"),
    'spray':      MartItem("spray",     45,   0,    alt_name="Bug Spray Can"),
    'oatmeal':    MartItem("oatmeal",   32,   0,    alt_name="Oatmeal Pack"),
}

screen supermarket():
    layer "background"
    imagemap:
        ground "images/bg/bg supermarket.png"
        for item in mart_items:
            $ item_dialogue = truncateNumber(item)
            hotspot mart_items[item] action ShowTransient("shopItemTakeMenu", shopItem=item_dialogue)

    use supermarket_ui

default itemIncrementer = 1

screen shopItemTakeMenu(shopItem="redcan"):
    zorder 2
    modal True
    add Solid("#ffffff88")

    imagemap:
        ground "images/supermarket/price_left_overlay.png"
        xalign 0.2
        yalign 0.5
        add "images/supermarket/items/{}.png".format(shopItem):
            xalign 0.45
            yalign 0.5
            if shopItem == "spray":
                zoom 1.005
            elif shopItem != "bread":
                zoom 0.75

        add "images/supermarket/pricetag.png":
            xalign 0
            yalign 0.98

        text "{}".format(shopItems[shopItem].price):
            xalign 0.33
            yalign 0.94
            size 43 color "#333"

    imagemap:
        ground "images/supermarket/price_right_overlay.png"
        xalign 0.79
        yalign 0.5

        text "{{color=#333}}{{size=+2}}{}{{/size}}{{/color}} in Basket: {{color=#333}}{{b}}{{size=+20}}{}{{/size}}{{/b}}{{/color}}".format(
            shopItems[shopItem].alt_name ,shopItems[shopItem].onhand
        ):
            xalign 0.5
            yalign 0.30
            color "#888"
            size 30

        hbox:
            xalign 0.5
            yalign 0.48
            if itemIncrementer > 1:
                imagebutton:
                    idle "images/supermarket/sub_item_btn.png"
                    action [SetVariable("itemIncrementer", itemIncrementer-1)]
            else:
                imagebutton:
                    idle "images/supermarket/inactive_sub_item_btn.png"
                    action 0

            null width 35

            fixed:
                xmaximum 132
                ymaximum 56
                add "images/supermarket/item_counter-textbox.png"
                text "{}".format(itemIncrementer):
                    xalign 0.5
                    yalign 0.5
                    color "#000"
                    size 40
            null width 35

            if itemIncrementer < 10:
                imagebutton:
                    idle "images/supermarket/add_item_btn.png"
                    action [SetVariable("itemIncrementer", itemIncrementer+1)]
            else:
                imagebutton:
                    idle "images/supermarket/inactive_add_item_btn.png"
                    action 0

        imagebutton:
            idle "images/supermarket/addToBasket_btn.png"
            xalign 0.5
            yalign 0.7
            action [SetVariable("itemIncrementer", 1),
                    Function(shopItems[shopItem].takeItem, itemIncrementer),
                    Hide("shopItemTakeMenu")]

    imagebutton:
        idle "images/misc/black close.png"
        xalign 0.845
        yalign 0.18
        action [Hide("shopItemTakeMenu"), SetVariable("itemIncrementer", 1)]

screen basketMenu:
    zorder 2
    modal True
    add Solid("#ffffff88")

    add "images/supermarket/basket_overlay.png":
        xalign 0.5 yalign 0.5

    imagemap:
        ground "images/supermarket/basket_right_overlay.png"
        xalign 0.84 yalign 0.5
        text "Total:":
            xalign 0.5 yalign 0.30
            size 30 color "#fff"
        text "{}.0".format(getCost()):
            xalign 0.5 yalign 0.40
            size 70 color "#fff"
        imagebutton:
            idle "images/supermarket/checkout_btn.png"
            xalign 0.5 yalign 1.0
            at double
            action Call("supermarket.shop_win_conditions")

    imagebutton:
        idle "images/misc/white close.png"
        xalign 0.85 yalign 0.18
        action Hide("basketMenu")

    viewport:
        xalign 0.3
        yalign 0.58
        draggable True
        xmaximum 612
        ymaximum 392
        hbox:
            vbox: # Img
                xsize 60
                for item in sorted(shopItems):
                    if shopItems[item].onhand > 0:
                        fixed:
                            ysize 80
                            add "images/supermarket/mini items/{}.png".format(item)
            vbox: # Name
                xsize 310
                for item in sorted(shopItems):
                    if shopItems[item].onhand > 0:
                        fixed:
                            ysize 80
                            text "{}".format(shopItems[item].alt_name) size 35 color "#111"
            vbox: # Onhand
                xsize 70
                for item in sorted(shopItems):
                    if shopItems[item].onhand > 0:
                        fixed:
                            ysize 80
                            text "x{}".format(shopItems[item].onhand) size 35 color "#7C7258"
            vbox: # Cost
                xsize 120
                for item in sorted(shopItems):
                    if shopItems[item].onhand > 0:
                        fixed:
                            ysize 80
                            text "{}.0".format(shopItems[item].totalAmount()) size 35 color "#5B533C"
            vbox: # Remove button
                for item in sorted(shopItems):
                    if shopItems[item].onhand > 0:
                        fixed:
                            ysize 80
                            imagebutton:
                                idle "images/supermarket/removeItem_btn.png"
                                action Function(shopItems[item].takeItem, -1)
