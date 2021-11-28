# Supermart ------------------
init python:
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
    'redcan':     MartItem("redcan",    28,   0,    alt_name="Red can"),
    'yellowcan':  MartItem("yellowcan", 22,   0,    alt_name="Yellow can"),
    'orangecan':  MartItem("orangecan", 34,   0,    alt_name="Orange can"),
    'greencan':   MartItem("greencan",  23,   0,    alt_name="Green can"),
    'browncan':   MartItem("browncan",  27,   0,    alt_name="Brown can"),
    'toiletroll': MartItem("toiletroll",15,   0,    alt_name="Toilet roll"),
    'facemask':   MartItem("facemask",  25,   0,    alt_name="Face mask"),
    'hygiene':    MartItem("hygiene",   36,   0,    alt_name="Hygiene product"),
    'bread':      MartItem("bread",     40,   0,    alt_name="Bread"),
    'spray':      MartItem("spray",     45,   0,    alt_name="Bug spray can"),
    'oatmeal':    MartItem("oatmeal",   32,   0,    alt_name="Oatmeal Pack"),
}

screen supermarket():
    layer "background"
    imagemap:
        ground "images/bg/bg supermarket.png"
        for item in mart_items:
            $ item_dialogue = truncateNumber(item)
            hotspot mart_items[item] action Show("shopItemTakeMenu", shopItem=item_dialogue)

    use supermarket_ui

    imagebutton:
        idle "spark_toggle"
        at transform:
            xalign 0.9
            yalign 0.03
            zoom 0.5

        action ToggleScreen("spk")

default itemIncrementer = 1

screen shopItemTakeMenu(shopItem="redcan"):
    zorder 2
    modal True

    add "images/supermarket/price_overlay.png":
        xalign 0.5
        yalign 0.5
    text "{}s in the basket:{}".format(shopItems[shopItem].alt_name ,shopItems[shopItem].onhand):
        xalign 0.6
        yalign 0.35
    hbox:
        xalign 0.7
        yalign 0.48
        imagebutton:
            idle "images/supermarket/sub_item_btn.png"
            sensitive If(itemIncrementer > 1)
            action [SensitiveIf(itemIncrementer > 0) ,SetVariable("itemIncrementer", itemIncrementer-1)]

        null width 35

        fixed:
            xmaximum 132
            ymaximum 56
            add "images/supermarket/item_counter-textbox.png"
            text "{}".format(itemIncrementer):
                xalign 0.5
                yalign 0.5

        null width 35

        imagebutton:
            idle "images/supermarket/add_item_btn.png"
            action [SensitiveIf(itemIncrementer < 10) ,SetVariable("itemIncrementer", itemIncrementer+1)]

    add "images/supermarket/{}_price.png".format(shopItem):
        xalign 0.22
        yalign 0.53

    imagebutton:
        idle "images/supermarket/addToBasket_btn.png"
        xalign 0.7
        yalign 0.63
        action [SetVariable("itemIncrementer", 1),
                Function(shopItems[shopItem].takeItem, itemIncrementer),
                Hide("shopItemTakeMenu")]

    imagebutton:
        idle "images/supermarket/cancel_btn.png"
        xalign 0.85
        yalign 0.18
        action Hide("shopItemTakeMenu")

screen basketMenu:
    zorder 2
    modal True
    add "images/supermarket/price_overlay.png":
        xalign 0.5 yalign 0.5
    add "images/supermarket/basket_overlay.png":
        xalign 0.5 yalign 0.5
    add "images/supermarket/vertical_line.png":
        xalign 0.65 yalign 0.61
    text "Total:":
        xalign 0.73 yalign 0.35
        size 40 color "#000"
    text "{}.0".format(getCost()):
        xalign 0.78 yalign 0.45
        size 50 color "#000"

    imagebutton:
        idle "images/supermarket/checkout_btn.png"
        xalign 0.83 yalign 0.73
        action Call("supermarket.shop_win_conditions")
    imagebutton:
        idle "images/supermarket/cancel_btn.png"
        xalign 0.85 yalign 0.18
        action [Hide("basketMenu"), showFlapButtons()]
    viewport:
        xalign 0.3
        yalign 0.58
        draggable True
        xmaximum 612
        ymaximum 392
        hbox:
            vbox: # Img
                xsize 60
                for item in shopItems:
                    if shopItems[item].onhand > 0:
                        fixed:
                            ysize 60
                            add "images/supermarket/{}.png".format(item)
            vbox: # Name
                xsize 310
                for item in shopItems:
                    if shopItems[item].onhand > 0:
                        fixed:
                            ysize 60
                            text "{}".format(shopItems[item].alt_name) size 40 color "#000"
            vbox: # Onhand
                xsize 70
                for item in shopItems:
                    if shopItems[item].onhand > 0:
                        fixed:
                            ysize 60
                            text "x{}".format(shopItems[item].onhand) size 40 color "#000"
            vbox: # Cost
                xsize 120
                for item in shopItems:
                    if shopItems[item].onhand > 0:
                        fixed:
                            ysize 60
                            text "{}.0".format(shopItems[item].totalAmount()) size 40 color "#000"
            vbox: # Remove button
                for item in shopItems:
                    if shopItems[item].onhand > 0:
                        fixed:
                            ysize 60
                            imagebutton:
                                idle "images/supermarket/removeItem_btn.png"
                                action Function(shopItems[item].takeItem, -1)

screen fly_in_image(img):
    zorder 2
    modal True
    imagebutton:
        idle img
        at t_flyingimage
        action Hide("fly_in_image")

screen supermarket_ui:
    $ renpy.hide_screen("flapButton")
    $ renpy.hide_screen("instructions")
    imagebutton:
        idle "images/supermarket/basket_btn.png"
        xalign 0.98
        yalign 0.95
        action Show("basketMenu")
    imagebutton:
        idle "images/supermarket/groceryList_icon.png"
        xalign 0.83
        yalign 0.95
        action Show("fly_in_image", img="images/supermarket/grocery_list.png")
