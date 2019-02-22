import os
from abc import *
from FoodIngredientList import *

class ingredientViewBase(object):

    __metaclass__ = ABCMeta

    USER_SIGNALS = {
        "main page":1,
        "add food":2,
        "del food":3,
        "modify food":4,
        "food info":5,
        "sum up":6,
        
        }

    def __init__(self):
        self.signal = ingredientViewBase.USER_SIGNALS["main page"];
        self.next_signal = ingredientViewBase.USER_SIGNALS["main page"];
        self.fl = []
        self.addedFoodName = ""

    def addUserDefinedSignal(self,str):
        self.USER_SIGNALS[str] = max(self.USER_SIGNALS.values()) + 1

    @abstractmethod
    def showMain(self):
        pass

    @abstractmethod
    def showAddFood(self):
        pass

    @abstractmethod
    def showDelFood(self):
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
        elif self.getSignal() is self.USER_SIGNALS["food info"]:
            return self.showFoodInfo()
        elif self.getSignal()  is self.USER_SIGNALS["sum up"]:
            return self.showSumUp()
        elif self.getSignal() is self.USER_SIGNALS["del food"]:
            return self.showDelFood()

    def isValidSig(self, sig):
        return sig in self.USER_SIGNALS.values()

    def isExitSignal(self):
        return False

    def getRemovedFoodName(self):
        return self.removed_food_name

    def getModifiedFoodName(self):
        return self.modified_food_name

    def getAddedFoodIngs(self):
        return self.added_food_ing

    def getRemovedFoodIngs(self):
        return self.removed_food_ing

    def setNoFoodRegisteredWarning(self):
        self.addWarning("No food has been added")
        self.setSignal(self.USER_SIGNALS["main page"])
        self.setNextSignal(self.USER_SIGNALS["main page"])

class webIngredientView(ingredientViewBase):

    def __init__(self):
        super(webIngredientView, self).__init__()
        self.pw = []
        self.removed_food_name = ""
        self.modified_food_name = ""

    def showMain(self):
        pass

    def showAddFood(self):
        pass

    def showDelFood(self):
        pass

    def showModifyFood(self):
        pass

    def showSumUp(self):
        pass

    def showFoodInfo(self, food):
        pass





class terminalIngredientView(ingredientViewBase):

    def __init__(self):
        super(terminalIngredientView, self).__init__()
        self.addUserDefinedSignal("exit");
        self.pw = []
        self.removed_food_name = ""
        self.modified_food_name = ""

    def isExitSignal(self, sig):
        if sig is self.USER_SIGNALS["exit"]:
            return True
        return False

    def clearScreen(self):
        os.system('cls||clear')
        for w in self.pw:
            print ("WARNING: " + w)
        del self.pw[:]       

    def addWarning(self, msg):
        self.pw.append(msg)

    def getUserSignalString(self):
        ret = ""

        for sig_name in sorted(self.USER_SIGNALS, key=self.USER_SIGNALS.get):
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

    def setRemovedFoodName(self, name):
        self.removed_food_name = name
    
    def showDelFood(self):
        self.clearScreen()
        if len(self.fl) < 1:
            self.addWarning("no food has been added")
            return

        self.showFoodList()
        food_num = self.getFoodNumber()

        if food_num >= len(self.fl):
            self.addWarning("wrong food number input")
            return

        self.setRemovedFoodName(self.fl[food_num].name)

    def setModifiedFoodName(self, name):
        self.modified_food_name = name

    def getModifiedFoodName(self):
        return self.modified_food_name

    def setAddedFoodIngs(self, ings):
        self.added_food_ing = ings

    def setRemovedFoodIngs(self, ings):
        self.removed_food_ing = ings


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

            if food_num >= len(self.fl):
                self.addWarning("wrong food number input")
                return

            self.clearScreen()
            selected_food = self.fl[food_num]

            print(selected_food.toString())

            next = int(input("want to see another = 1, goto main = 2 :"))
            if next == 2:
                self.setNextSignal(self.USER_SIGNALS["main page"])
            else:
                self.setNextSignal(self.USER_SIGNALS["food info"])

        else:
            self.setNoFoodRegisteredWarning()        

    def showModifyFood(self):
        self.clearScreen()

        food_num = 0
        add_inputed = []
        del_inputed = []

        if len(self.fl) > 0:
            self.showFoodList()
            food_num = self.getFoodNumber()
            if food_num >= len(self.fl):
                self.addWarning("wrong food number input")
                return

            self.clearScreen()
            print("current ingredients=\n")
            print(self.fl[food_num].toString())
            print("\n")

            while True:
                ing = input("{add/del}, name, amount = ")

                ing = ing.replace(" ","")
                if len(ing) is 0:
                   break
                
                ing = ing.split(",",1)

                if ing[0] != "add" and ing[0] != "del":
                    break

                if ing[0] == "add":
                    add_inputed.append(ing[1])
                if ing[0] == "del":
                    del_inputed.append(ing[1])
                    
                self.clearScreen()

                print("current ingredients=\n")
                print(self.fl[food_num].toString())
                print("\n")

                for i in add_inputed:
                    print("ADD: " + i)
                for i in del_inputed:
                    print("DEL: " + i)

            self.setModifiedFoodName(self.fl[food_num].name)
            self.setAddedFoodIngs(add_inputed)
            self.setRemovedFoodIngs(del_inputed)

        else:
            self.setNoFoodRegisteredWarning()
        
        return

    def showSumUp(self):
        self.clearScreen()

        summed_up_list = FoodIngredientList("Shopping List")

        for food in self.fl:
            for ing in food.getIngList():
                summed_up_list.addIng(ing)

        while(1):

            self.clearScreen()

            i = 0

            if len(summed_up_list.getIngList()) == 0:
                print ("Done! bye!")
                input()
                exit()

            for ing in summed_up_list.getIngList():
                print (str(i) + ": " + str(ing))
                i = i+1

            print ("type shopped,n -> n th item is deleted)")
            print ("type exit -> exit the program")
             
            i = input()

            i = i.replace(" ","")
            
            if i == "exit":
                exit()
            
            i = i.split(",")

            num = int(i[1])

            if i[0] != "shopped" or num >= len(summed_up_list.getIngList()):
                self.addWarning("wrong input")
            else:
                summed_up_list.subIng(summed_up_list.getIngList()[num-1])

if __name__ == "__main__":

    v = terminalIngredientView()

    while(1):
        v.update()

