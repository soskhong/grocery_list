
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

if __name__ == "__main__":

    ing1 = Ingredient("onion", 1, "ea")
    ing2 = Ingredient("apple", 2, "ea")
    #print(str(ing1))
    food = FoodIngredientList()
    food.addIng(ing1)
    food.addIng(ing2)

    print(food.toString())


