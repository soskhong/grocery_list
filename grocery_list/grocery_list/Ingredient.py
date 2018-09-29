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

        
    def createFromString(desc):
        d = desc.replace(" ","")
        l = d.split(",")
        name = l[0];
        pos = re.search(r"[A-Z,a-z]", l[1])
        idx = pos.regs[0][0]
        amount = int(l[1][0:idx])
        unit = l[1][idx:]
        return Ingredient(name, amount, unit)


        


if __name__ == "__main__":

    Ingredient.createFromString("pork, 1234kg")
    
