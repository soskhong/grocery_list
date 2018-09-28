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

from FoodIngredientList import *
from viewTerminal import *
import os

def clear_screen():
    os.system('cls')

if __name__ == "__main__":

    done = False

    shop_list = FoodIngredientList("Shopping List")

    food_list = []

    jimdak = FoodIngredientList("Braised chicken")

    jimdak.createAndAddIng("whole chicken", 1, "kg")
    jimdak.createAndAddIng("potato", 2, "ea")
    jimdak.createAndAddIng("carrot", 1, "ea")
    jimdak.createAndAddIng("noodle (dangmyun)", 1, "ea")
    jimdak.createAndAddIng("spring onion", 2, "ea")
    jimdak.createAndAddIng("garlic", 4, "cloves")
    jimdak.createAndAddIng("onion", 1, "ea")

    food_list.append(jimdak)

    sooyook = FoodIngredientList("Boiled Port")
    sooyook.createAndAddIng("pork belly", 600, "g")
    sooyook.createAndAddIng("apple", 1, "ea")
    sooyook.createAndAddIng("spring onion", 3, "ea")
    sooyook.createAndAddIng("onion", 2, "ea")

    food_list.append(sooyook)

    for food in food_list:
        for ing in food.getIngList():
            shop_list.addIng(ing)

    #print(shop_list.toString())

    v = terminalIngredientView()
    v.setFoodList(food_list)

    while(1):
        v.update()

# user scenario

###

###

