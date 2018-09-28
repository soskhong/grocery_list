import os
from abc import *

class ingredientViewBase(metaclass=ABCMeta):

    USER_SIGNALS = {
        "main page":1,
        "add food":2,
        "modify food":3,
        "food info":4,
        "sum up":5,
        }

    def __init__(self):
        self.signal = ingredientViewBase.USER_SIGNALS["main page"];
        self.next_signal = ingredientViewBase.USER_SIGNALS["main page"];
        self.fl = []
        self.addedFoodName = ""

    @abstractmethod
    def showMain(self):
        pass

    @abstractmethod
    def showAddFood(self):
        pass

    def getAddedFoodName(self):
        return self.addedFoodName

    @abstractmethod
    def showModifyFood(self):
        pass

    @abstractmethod
    def showSumUp(self):
        pass

    @abstractmethod
    def showFoodInfo(self, food):
        pass

    def isInvalidSignal(self, sig):
        return sig not in self.USER_SIGNALS.values()

    def getSignal(self):
        return self.signal

    def setSignal(self, sig):
        self.signal = sig

    def setNextSignal(self, sig):
        self.next_signal = sig

    def getNextSignal(self):
        return self.next_signal

    def updateSignal(self):
        self.signal = self.next_signal

    def setFoodList(self, fl_):
        self.fl = fl_

    def update(self):
        if self.getSignal() is self.USER_SIGNALS["main page"]:
            return self.showMain()
        elif self.getSignal()  is self.USER_SIGNALS["add food"]:
            return self.showAddFood()
        elif self.getSignal()  is self.USER_SIGNALS["modify food"]:
            return self.showModifyFood()
        elif self.getSignal()  is self.USER_SIGNALS["sum up"]:
            return self.showSumUp()

    def isValidSig(self, sig):
        return sig in self.USER_SIGNALS.values()

    def isExitSignal(self):
        return False

    def getModifiedFoodName(self):
        return self.modified_food_name

    def getModifiedFoodIngs(self):
        return self.modified_food_ing

    def setNoFoodRegisteredWarning(self):
        self.addWarning("No food has been added")
        self.setSignal(self.USER_SIGNALS["main page"])
        self.setNextSignal(self.USER_SIGNALS["main page"])

class terminalIngredientView(ingredientViewBase):

    def __init__(self):
        super(terminalIngredientView, self).__init__()
        self.USER_SIGNALS["exit"] = 6
        self.pw = []

    def isExitSignal(self, sig):
        if sig is self.USER_SIGNALS["exit"]:
            return True
        return False

    def clearScreen(self):
        os.system('cls');
        for w in self.pw:
            print ("WARNING: " + w)
        del self.pw[:]       

    def addWarning(self, msg):
        self.pw.append(msg)

    def getUserSignalString(self):
        ret = ""
        for sig_name in self.USER_SIGNALS.keys():
            ret = ret + str(self.USER_SIGNALS[sig_name]) + ": " + sig_name + " "
        return ret

    def getNextInput(self):
        input_msg = self.getUserSignalString() + " > "
        new_sig = int(input(input_msg))        
        self.setNextSignal(new_sig)

    def showMain(self):
        self.clearScreen()
        print ("##################################")
        print ("Welcome to Ingredient List")
        print ("##################################")
        print ("Current Food List:\n")
        for food in self.fl:
            print("\t * " + food.name)
        print ("====================")
        self.getNextInput()

    def showAddFood(self):
        self.clearScreen()
        name = input ("Name of food: ")
        self.addedFoodName = name

    def setModifiedFoodName(self, name):
        self.modified_food_name = name

    def getModifiedFoodName(self):
        return self.modified_food_name

    def setModifiedFoodIngs(self, ings):
        self.modified_food_ing = ings

    def getModifiedFoodIngs(self):
        return self.modified_food_ing

    def showFoodList(self):
        if len(self.fl) > 0:
            for i in range(0, len(self.fl)):
                print (str(i+1) + " : " + self.fl[i].name)

    def getFoodNumber(self):
        food_num = int(input("which food number = "))
        food_num = food_num-1
        return food_num


    def showFoodInfo(self):
        self.clearScreen()
        if len(self.fl) > 0:
            self.showFoodList()
            food_num = self.getFoodNumber()

        else:
            self.setNoFoodRegisteredWarning()        

    def showModifyFood(self):
        self.clearScreen()

        food_num = 0
        inputed = []

        if len(self.fl) > 0:
            self.showFoodList()
            food_num = self.getFoodNumber()
            if food_num >= len(self.fl):
                self.addWarning("wrong food number input")
                return

            self.clearScreen()

            while True:
                ing = input("name, amount = ")
                ing = ing.replace(" ","")
            
                if len(ing) is 0:
                   break

                inputed.append(ing)

                self.clearScreen()

                for i in inputed:
                    print(i)

            self.setModifiedFoodName(self.fl[food_num].name)
            self.setModifiedFoodIngs(inputed)
        else:
            self.setNoFoodRegisteredWarning()
        
        return

    def showSumUp(self):
        self.clearScreen()
        print ("showSumUp")
        self.getNextInput()

if __name__ == "__main__":

    v = terminalIngredientView()

    while(1):
        v.update()

