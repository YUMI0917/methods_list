#!/usr/bin/python3

# Author: Elkin
# Program: bubble.py
# Version: Python 3.8.2

from quicksort import ordination
from time import time

class bubble_method:
    def order_values(self, numbers): # numbers = list
        for number in range(0,len(numbers)-1):
            # goes through all the elements from the last to the first
            for index in range(len(numbers)-1,number,-1):
                # if the value is smaller than the previous one, exchange it
                if numbers[index]<numbers[index-1]:
                    numbers[index-1],numbers[index]=numbers[index],numbers[index-1]

        return numbers

    
# main program ------------------------------
def execute_bubble():
    start_time = time()
    user=int(input("Enter the number of items for bubble method: "))    
    obj=ordination(user)
    my_list=obj.generate_boxes(user) # elements of list

    myclass=bubble_method()
    ordered_list=myclass.order_values(my_list)

    print("BUBBLE METHOD: ", ordered_list)

    elapsed_time = time() - start_time
    print("Elapsed time: ",round(float(elapsed_time*1000), 2), " milliseconds" ) # two decimals
    print("Elapsed time: %.10f seconds." % elapsed_time)
    

execute_bubble()