import os
import re

class IngredientBase(object):

    INVALID_UNIT = "INVALID"

    AVAILABLE_UNITS = [
        INVALID_UNIT,
        "g",
        "kg",
        "ea",
        "cloves",
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

    def __str__(self):
        ret = self.__class__.__name__
        ret = ret + ": " + self.getName()
        ret = ret + " " + str(self.getAmount()) + self.getUnit()
        return ret

    def getFileName(self):
        ret = self.__class__.__name__
        ret = ret + "_" + self.getName()

        ret = "__" + ret
        return ret
