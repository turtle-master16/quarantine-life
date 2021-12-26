init python:
    class InstructionElement:
        def __init__(self, img, desc, xalign, yalign, zoom=1.0, isMenu=False, xzoom=1.0):
            self.img = img
            self.desc = desc
            self.xalign = xalign
            self.yalign = yalign
            self.zoom = zoom
            self.isMenu = isMenu
            self.xzoom = xzoom

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
            "Tap an item in the room to interact with it.",
        ],
        "findActivity":[
            "Tap on an item in the room to try an activity.",
            "The basket button opens the basket menu.",
        ],
        "workprep":[
            "Tap an item in the room to interact with it.",
            "Tap on an arrow to switch to a different room.",
            "The checklist button shows the items you need to find and the items you already found.",
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
        "instructions":InstructionElement("gui/quick/instructions_icon.png",           btn_desc_set["general"][1],     0.9,    0.023),
        "skip":        InstructionElement("gui/quick/skipGame_btn.png",                btn_desc_set["general"][2],     0.81,   0.023),
    }

    btn_sets = {
#       Key                     Image of the button                          Description                     xalign  yalign  zoom*  isMenu  xzoom
        "broomfind":[
            btn_desc_set["broomfind"][0],
            general_btns["spark_toggle"],
            general_btns["instructions"],
            general_btns["skip"],
        ],
        "findActivity":[
            btn_desc_set["findActivity"][0],
            InstructionElement("images/misc/arrow.png",                      btn_desc_set["workprep"][1],    0.0,    0.5,    1.0),
            general_btns["spark_toggle"],
            general_btns["instructions"],
            general_btns["skip"],
        ],
        "workprep":[
            btn_desc_set["workprep"][0],
            InstructionElement("images/misc/arrow.png",                      btn_desc_set["workprep"][1],    0.0,    0.75,    1.0),
            InstructionElement("images/misc/arrow.png",                      btn_desc_set["workprep"][1],    1.0,    0.75,    1.0,  False,  -1.0),
            InstructionElement("images/misc/flapcheck.png",                  btn_desc_set["workprep"][2],    0.8,    1.0,     0.3),
            general_btns["spark_toggle"],
            general_btns["instructions"],
            general_btns["skip"],
        ],
        "supermarket":[
            btn_desc_set["supermarket"][0],
            InstructionElement("images/instructions/i_itemtake.png",         btn_desc_set["supermarket"][1], 0.5,    0.5,     1.0,  True),
            InstructionElement("images/instructions/i_itemtake.png",         btn_desc_set["supermarket"][2], 0.5,    0.5,     1.0,  True),
            InstructionElement("images/supermarket/groceryList_icon.png",    btn_desc_set["supermarket"][3], 0.83,   0.95),
            InstructionElement("images/supermarket/basket_btn.png", btn_desc_set["supermarket"][4], 0.98,   0.95),
            InstructionElement("images/Instructions/i_basketMenu.png",       btn_desc_set["supermarket"][5], 0.5,    0.5,     1.0,  True),
            general_btns["spark_toggle"],
            general_btns["instructions"],
            general_btns["skip"],
        ],
    }

    instruct_data = {
        "broomfind":    InstructionSet("bg/bg living room animated/6.png",
                                       btn_sets["broomfind"],
                                       "Find the broom."),
        "findActivity": InstructionSet("bg/bg living room animated/6.png",
                                       btn_sets["findActivity"],
                                       "Find something to do."),
        "workprep":     InstructionSet("images/clickables/livingroom_workprep.png",
                                       btn_sets["workprep"],
                                       "Find all the items on the list."),
        "supermarket":  InstructionSet("images/bg/bg supermarket.png",
                                       btn_sets["supermarket"],
                                       "Purchase exactly 200.0 worth of items along with the items in the list."),
    }
