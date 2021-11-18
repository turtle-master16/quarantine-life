# Supermart ------------------
init python:
    def getCost():
        return currentItemCost
    def hasAcquiredNeedItems():
        enufHygiene =     shopItems['hygiene'].onhand >= 2
        enufToiletPaper = shopItems['toiletroll'].onhand >= 3
        enufGreencan =    shopItems['greencan'].onhand >= 1
        return enufHygiene and enufToiletPaper and enufGreencan

default currentItemCost = 0

default shopItems = {
#   KEY                    NAME         PRC   ONHD  IN-GAME-NAME
    'redcan':     MartItem("redcan",    28,   0,    alt_name="Red can"),
    'yellowcan':  MartItem("yellowcan", 22,   0,    alt_name="Yellow can"),
    'orangecan':  MartItem("orangecan", 34,   0,    alt_name="Orange can"),
    'greencan':   MartItem("greencan",  23,   0,    alt_name="Green can"),
    'browncan':   MartItem("browncan",  27,   0,    alt_name="Brown can"),
    'toiletroll': MartItem("toiletroll",15,   0,    alt_name="Toilet Roll"),
    'facemask':   MartItem("facemask",  25,   0,    alt_name="Face mask"),
    'hygiene':    MartItem("hygiene",   36,   0,    alt_name="Hygiene Product"),
}

screen supermarket():
    layer "background"
    imagemap:
        ground "images/bg/bg supermarket.png"
        for item in mart_items:
            $ item_dialogue = item
            if item[-1] == "2":
                $ item_dialogue = item_dialogue.replace("2", "")
            hotspot mart_items[item] action Call("shopItemTake", item_dialogue)
    imagebutton:
        idle "images/misc/cashreg.png"
        at transform:
            xanchor 1.0
            xpos 1.02
            yalign 1.0
            xoffset -90
            yoffset -70
            zoom 0.4
            on show:
                xoffset 125
                linear 0.4 xoffset -70
            on hide:
                xoffset -70
                linear 0.4 xoffset 125
        action Call("supermarket.shop_win_conditions")
    for item in mart_items:
        add "spark":
            pos getRectCenter(mart_items[item])

screen price_list():
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
    $ item_name = shopItems[item].alt_name
    pl "How many [item_name]s should I take?"
    menu:
        "One":
            $ shopItems[item].takeItem(1)
        "Two":
            $ shopItems[item].takeItem(2)
        "Three":
            $ shopItems[item].takeItem(3)
        "Return one" if shopItems[item].onhand > 0:
            $ shopItems[item].takeItem(-1)
        "Nevermind":
            pl "I don't need any more of these."
    return
