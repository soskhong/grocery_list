
# 
### ingredients
# Name
# basic unit
# amount
#
### food -> has list of ingredients
# for how many numbers of people
#
### shopping item -> mapping to ingredients
# list of shopping item is output of this. 

from math import ceil

class IngredientBase():

    INVALID_UNIT = "INVALID"

    AVAILABLE_UNITS = [
        INVALID_UNIT,
        "g",
        "kg",
        "ea",
        ]

    def __init__(self):
        self.name = ""
        self.amount = 0.0
        self.unit = ""
    
    def getAvailableUnit(self):
        return self.AVAILABLE_UNITS;
    
    def setName(self, name_):
        self.name = name_
    def getName(self):
        return self.name
    def setAmount(self, amount_):
        self.amount = amount_
    def getAmount(self):
        return self.amount;
    def setUnit(self, unit_):
        if unit_ in self.AVAILABLE_UNITS:
            self.unit = unit_
            return True
        else:
            self.unit = INVALID_UNIT
            return False
    def getUnit(self):
        return self.unit

    def isSameIng(self, other):
        return self.getName() == other.getName()

    def isSameUnit(self, other):
        return self.getUnit() == other.getUnit()
        
    def __cmp__(self, other):
        #return 1 if self  > other
        assert self.isSameIng(other)
        
        if not self.isSameUnit(other):
            return 0

        if self.getAmount() == other.getAmount():
            return 0

        if self.getAmount() > other.getAmount():
            return 1

        return -1

    def add(self, other):
        assert self.isSameIng(other)
        assert self.isSameUnit(other)

        self.setAmount(self.getAmount() + other.getAmount())

    def str_info(self):
        ret_str = self.getName() + ", "
        ret_str = ret_str + str(self.getAmount()) + self.getUnit()
        return ret_str

    def str_internal(self):
         raise NotImplementedError()


    def __str__(self):
        return self.str_internal()

class Ingredient(IngredientBase):
    def __init__(self, name):
        super().__init__()
        self.setName(name)

    def str_internal(self):
        ret_str = "ING: "
        ret_str = ret_str + self.str_info()
        return ret_str


class ShopItem(IngredientBase):
    def __init__(self, name):
        super().__init__()
        self.setName(name)
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
    def str_internal(self):
        ret_str = "ITEM: "
        ret_str = ret_str + self.str_info()
        return ret_str

    
class FoodIngredientList():

    def __init__(self):
        self.ing_list = []

    def isIngExist(self, ing):
        for item in self.ing_list:
            if item.isSameIng(ing):
                return True
        return False

    def findIng(self, ing):
        assert self.isIngExist()

        for item in self.ing_list:
            if item.isSameIng(ing):
                return item
    
    def addIng(self, ing):
        if self.isIngExist(ing):
            curr = findIng(ing)
            curr.add(ing)
        else:
            self.ing_list.append(ing)

    def getIngList(self):
        return self.ing_list

if __name__ == "__main__":
    ing = Ingredient("onion")
    print(str(ing))