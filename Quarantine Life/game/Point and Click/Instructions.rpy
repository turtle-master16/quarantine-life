init python:
    class InstructionElement:
        def __init__(self, img, desc, xalign, yalign, zoom=1.0):
            self.img = img
            self.desc = desc
            self.xalign = xalign
            self.yalign = yalign
            self.zoom = zoom
            self.alpha = 0.7

    class InstructionSet:
        def __init__(self, bg, btn_set):
            self.bg = bg
            self.btn_set = btn_set
            self.pages = len(btn_set) - 1

    btn_sets = {
#                              Image of the button                           Description...
        "supermarket":[
            InstructionElement("images/supermarket/groceryList_icon.png",    "descA", 0.83, 0.95),
            InstructionElement("images/supermarket/inactive_basket_btn.png", "descB", 0.98, 0.95),
            InstructionElement("spark_toggle", "descC", 0.5, 0.97, 0.6),
        ]
    }

    instruct_data = {
        "supermarket": InstructionSet("images/bg/bg supermarket.png", btn_sets["supermarket"]),
    }
