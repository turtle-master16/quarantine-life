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
            self.updateOverallCost()
        def updateOverallCost(self):
            cost = 0
            for item in shopItems:
                cost += shopItems[item].totalAmount()
            globals()['currentItemCost'] = cost

    def createDelay(start, stp):
        return renpy.random.randint(start, stp)
