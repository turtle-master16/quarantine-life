init python:
    class InstructionElement:
        def __init__(self, img, desc, xalign, yalign, zoom=1.0, isMenu=False):
            self.img = img
            self.desc = desc
            self.xalign = xalign
            self.yalign = yalign
            self.zoom = zoom
            self.isMenu = isMenu

    class InstructionSet:
        def __init__(self, bg, btn_set, objective):
            self.bg = bg
            self.btn_set = btn_set
            self.objective = objective
            self.pages = len(btn_set) - 1

    btn_desc_set = {
        "general":[
            "This slider will toggle the item guide option, which adds an sparkle for every clickable item on the minigame when turned on",
            "The question mark button will display this guide again.",
            "The skip button allows you to instantly complete the minigame (Only available if the minigame is completed at least once).",
        ],
        "broomfind":[
            "The list button will display the list of needed items.",
            "The basket button opens the basket menu.",
        ],
        "findActivity":[
            "The list button will display the list of needed items.",
            "The basket button opens the basket menu.",
        ],
        "workprep":[
            "The list button will display the list of needed items.",
            "The basket button opens the basket menu.",
        ],
        "supermarket":[
            "Tap any of the items you see on the background to open the Item Take Menu.",
            "In the Item Take Menu, You can see how many of the item you tapped you currently have in the basket.",
            "You have the option to take as many of that item by adjusting the number in the middle using the + and - buttons and tapping the Add to basket button.",
            "The list button will display the list of needed items.",
            "The basket button opens the basket menu.",
            "The basket menu allows you to view details of your items on hand and their total amount. Tap the X button beside an item to return one of that item. Tap check out to see if you are ready to leave.",
        ],
    }

    general_btns = {
#                                          Image of the button                         Description                     xalign  yalign  zoom*
        "spark_toggle":InstructionElement("spark_toggle",                              btn_desc_set["general"][0],     0.5,    0.97,   0.6),
        "instructions":InstructionElement("gui/quick/instructions_icon.png",           btn_desc_set["general"][1],     0.9,    0.03),
        "skip":        InstructionElement("gui/quick/skipGame_btn.png",                btn_desc_set["general"][2],     0.84,   0.0),
    }

    btn_sets = {
#                                          Image of the button                         Description                     xalign  yalign  zoom*  isMenu
        "broomfind":[
                      general_btns["spark_toggle"],
                      general_btns["instructions"],
                      general_btns["skip"],
        ],
        "findActivity":[
                      general_btns["spark_toggle"],
                      general_btns["instructions"],
                      general_btns["skip"],
        ],
        "workprep":[
                      general_btns["spark_toggle"],
                      general_btns["instructions"],
                      general_btns["skip"],
        ],
        "supermarket":[
                      btn_desc_set["supermarket"][0],
                      InstructionElement("images/instructions/i_itemtake.png",         btn_desc_set["supermarket"][1], 0.5,    0.5,     1.0,  True),
                      InstructionElement("images/instructions/i_itemtake.png",         btn_desc_set["supermarket"][2], 0.5,    0.5,     1.0,  True),
                      InstructionElement("images/supermarket/groceryList_icon.png",    btn_desc_set["supermarket"][3], 0.83,   0.95),
                      InstructionElement("images/supermarket/inactive_basket_btn.png", btn_desc_set["supermarket"][4], 0.98,   0.95),
                      InstructionElement("images/Instructions/i_basketMenu.png",       btn_desc_set["supermarket"][5], 0.5,    0.5,     1.0,  True),
                      general_btns["spark_toggle"],
                      general_btns["instructions"],
                      general_btns["skip"],
        ],
    }

    instruct_data = {
        "broomfind":    InstructionSet("bg/bg living room animated/6.png",
                                       btn_sets["broomfind"],
                                       "Complete blablabla"),
        "findActivity": InstructionSet("bg/bg living room animated/6.png",
                                       btn_sets["findActivity"],
                                       "Complete blablabla"),
        "workprep":     InstructionSet("images/clickables/livingroom_workprep.png",
                                       btn_sets["workprep"],
                                       "Complete blablabla"),
        "supermarket":  InstructionSet("images/bg/bg supermarket.png",
                                       btn_sets["supermarket"],
                                       "Purchase exactly 200.0 worth of items along with the items in the list."),
    }
