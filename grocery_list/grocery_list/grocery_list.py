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
from controller import *
import os

if __name__ == "__main__":

    v = webIngredientView()
    c = webController([], v)

    c.start()


