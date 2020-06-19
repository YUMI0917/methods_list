#!/usr/bin/python3

# Author: Elkin
# Program: second_theory.py
# Version: Python 3.8.2


import random 
import string

class second_theory:
    def random_alphaNumeric_string(self,lettersCount, digitsCount):
        sampleStr = ''.join((random.choice(string.ascii_letters) for i in range(lettersCount)))
        sampleStr += ''.join((random.choice(string.digits) for i in range(digitsCount)))
    
        # Convert string to list and shuffle it to mix letters and digits
        sampleList = list(sampleStr)
        random.shuffle(sampleList)
        finalString = ''.join(sampleList)

        return finalString

    # Returns the number of elements of each type to generate
    def number_of_types(self): # 10000 elements



obj=second_theory()
print("First Random alphaNumeric String is ", obj.random_alphaNumeric_string(5, 3))
#print("Second Random alphaNumeric String is ", random_alphaNumeric_string(6, 2))
#print(round(random.random(), 4) )

