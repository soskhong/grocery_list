from IngredientBase import *
from math import ceil

class ShopItem(IngredientBase, object):
    def __init__(self, name):
        super(ShopItem, self).__init__()
        self.setName(name)

    def __init__(self, name, amount, unit):
        super(ShopItem, self).__init__()
        self.setName(name)
        self.setAmount(amount)
        self.setUnit(unit)
    
    def setIngredientMapping(self, ing):
        self.mapped_ingredient = ing
    def getIngredientMapping(self):
        return self.mapped_ingredient

    def howMantItemForIng(buy_item, ing):
        assert buy_item.getUnit() == ing.getUnit()
        assert but_item.getName() == ing.getName()

        total_amount = ing.getAmount()
        unit_amount = buy_item.getAmount()

        return ceil(float(total_amount) / unit_amount)

