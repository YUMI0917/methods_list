#!/usr/bin/python3

# Author: Elkin
# Program: second_theory.py
# Version: Python 3.8.2


from random import * 
import string
import random

class second_theory:
    def random_list_objects(self,lettersCount, digitsCount, floats):
        elements=[] 
        # add those of type string
        for index in range(lettersCount):
            elements.append(random.choice(string.ascii_letters)) 
        # add those of type int
        for index in range(digitsCount):
            elements.append(int(random.choice(string.digits)))
        # add those of type float
        for index in range(floats):
            elements.append(round(random.random(),2)) # two decimals
    
        return elements

    # Returns the number of elements of each type to generate
    def number_of_types(self): # 10000 elements
        qty_int=0 # list A
        qty_float=0 # list B
        qty_string=0 # list C and D (char type not supported on python)
        total=0
        while(total!=100):
            qty_int=randint(1,100)
            qty_float=randint(1,100)
            qty_string=randint(1,100)
            total=qty_int+qty_float+qty_string
            
        return {'listA':qty_int,'listB':qty_float,'listC':qty_string}


# main program ------------------------
def execute_program():
    obj=second_theory()
    quantities=obj.number_of_types()
    listA=quantities["listA"]
    listB=quantities["listB"]
    listC=quantities["listC"]
    
    # generate my list of objects with 10000 elements
    objects_list=obj.random_list_objects(listA,listB,listC)
    print(obj.random_list_objects(listA,listB,listC))

execute_program()
#print("Second Random alphaNumeric String is ", random_alphaNumeric_string(6, 2))
#print(round(random.random(), 4) )

