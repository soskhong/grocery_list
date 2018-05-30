from IngredientBase import *

class Ingredient(IngredientBase, object):
    def __init__(self, name):
        super(Ingredient, self).__init__()
        self.setName(name)

    def __init__(self, name, amount, unit):
        super(Ingredient, self).__init__()
        self.setName(name)
        self.setAmount(amount)
        self.setUnit(unit)

