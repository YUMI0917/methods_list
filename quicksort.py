#!/usr/bin/python3

# Author: Elkin
# Program: quicksort.py
# Version: Python 3.8.2

from random import *
from time import time


class ordination:

    # constructor -------------
    def __init__(self, size):
        self.elements = size # number of items for the list

    def order_list(self):
        """Sort the list by using quicksort."""
        numbers=self.generate_boxes(self.elements)
        less = []
        equal = []
        greater = []

        if len(numbers) > 1:
            position=0
            stored=numbers[position]
            for number in numbers:
                position+=1
                if number < stored:
                    less.append(number)
                elif number == stored: 
                    equal.append(number)
                elif number > stored:
                    greater.append(number)

            # returns the numbers from least to greatest
            return sorted(less+equal+greater)

        else: 
            return numbers
    
    # generates a list of n elements
    def generate_boxes(self,size):
        numbers=[]
        # add the elements to the list  
        for number in range(0,size):
            n_random=randint(1,1000) # generate numbers list
            numbers.append( n_random ) 
            
        return numbers


# main program ------------------------------
start_time = time()

user=int(input("Enter the number of items: "))
obj=ordination(user)
print(obj.order_list())

elapsed_time = time() - start_time
print("Elapsed time: ",round(float(elapsed_time*1000), 2), " milliseconds" ) # two decimals
print("Elapsed time: %.10f seconds." % elapsed_time)
