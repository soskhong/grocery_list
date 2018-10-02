from IngredientBase import *
from ShopItem import *
from Ingredient import *

class FoodIngredientList(object):

    def __init__(self, name):
        self.ing_list = []
        self.name = name


    def isIngExist(self, ing):
        for item in self.ing_list:
            if item.isSameIng(ing):
                return True
        return False

    def findIng(self, ing):
        assert self.isIngExist(ing)

        for item in self.ing_list:
            if item.isSameIng(ing):
                return item
    
    def subIng(self, ing):
        if self.isIngExist(ing):
            curr = self.findIng(ing)
            curr.sub(ing)
            if curr.getAmount() == 0:
                self.ing_list.remove(curr)

    def addIng(self, ing):
        if self.isIngExist(ing):
            curr = self.findIng(ing)
            curr.add(ing)
        else:
            self.ing_list.append(ing)

    def createAndAddIng(self, name, amount, unit):
        ing = Ingredient(name, amount, unit)
        self.addIng(ing)

    def getIngList(self):
        return self.ing_list
    
    def toString(self):
        ret = "Food: " + self.name + "\n"
        for item in self.ing_list:
            ret += str(item)
            ret += "\n"
        return ret


