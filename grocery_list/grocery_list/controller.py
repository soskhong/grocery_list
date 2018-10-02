from FoodIngredientList import *
from viewTerminal import *

import os
from abc import *

class controllerBase(metaclass=ABCMeta):
    def __init__(self, model, view: ingredientViewBase):
        self.v = view
        self.m = model

    def isFoodAlreadyExist(self, added):
        for food in self.m:
            if food.name == added:
                return True
        return False
    
    def getExistingFood(self, name):
        for food in self.m:
            if food.name == name:
                return food


    @abstractmethod
    def start(self):
        pass

    def doAddFood(self):
        added = self.v.getAddedFoodName()
            
        if self.isFoodAlreadyExist(added):
            self.v.addWarning("The food " + added + " already exists")
        else:
            self.m.append(FoodIngredientList(self.v.getAddedFoodName()))
            self.v.setFoodList(self.m)
            
        self.v.setNextSignal(self.v.USER_SIGNALS["main page"]) 


    def doModifyFood(self):
        modified = self.v.getModifiedFoodName()
        add_ings = self.v.getAddedFoodIngs()
        del_ings = self.v.getRemovedFoodIngs()
            
        if self.isFoodAlreadyExist(modified):
            f = self.getExistingFood(modified)
            
            for i in add_ings:
                f.addIng(Ingredient.createFromString(i))
            for i in del_ings:
                f.subIng(Ingredient.createFromString(i))
        else:
            self.v.addWarning("the food has not been added")
            
        self.v.setNextSignal(self.v.USER_SIGNALS["main page"])
    
    def doRemoveFood(self):
        removed = self.v.getRemovedFoodName()

        if self.isFoodAlreadyExist(removed):
            self.m.remove(self.getExistingFood(removed))
            self.v.setFoodList(self.m)

        self.v.setNextSignal(self.v.USER_SIGNALS["main page"])


    def do(self):
        next_sig = self.v.getNextSignal()

        if self.v.isInvalidSignal(next_sig):
                self.v.addWarning("Your input " + str(next_sig) + " is invalid")
                self.v.setNextSignal(self.v.getSignal())
        else:
            if self.v.getSignal() is self.v.USER_SIGNALS["add food"]:
                self.doAddFood();
            
            elif self.v.getSignal() is self.v.USER_SIGNALS["modify food"]:
                self.doModifyFood();

            elif self.v.getSignal() is self.v.USER_SIGNALS["del food"]:
                self.doRemoveFood()
                

class terminalController(controllerBase):

    def __init__(self, model, view: ingredientViewBase):
        super(terminalController, self).__init__(model, view)

    def start(self):
        while(1):
            self.v.update()
            next_sig = self.v.getNextSignal()
            
            if self.v.isExitSignal(next_sig):
                exit()
            
            self.do()
            self.v.updateSignal()

class webController(controllerBase):
    def __init__(self, model, view: webIngredientView):
        super(webController, self).__init__(model, view)

    def start(self):
        pass

if __name__ == "__main__":

    v = terminalIngredientView()
    c = terminalController([], v)

    c.start()

