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




# Questions ------------------------
def get_objects_list():
    obj=second_theory()
    quantities=obj.number_of_types()
    listA=quantities["listA"]
    listB=quantities["listB"]
    listC=quantities["listC"]
    # generate my list of objects with 10000 elements
    objects_list=obj.random_list_objects(listA,listB,listC)
    
    return objects_list

# separate the objects into different lists
def lists(objects_list):
    listA=[] # int
    listB=[] # float
    listC=[] # string
     
    for element in objects_list:
        if type(element)==int:
            listA.append(element)
        elif type(element)==float:
            listB.append(element)
        elif type(element)==str:
            listC.append(element)

    return {'listA':listA,'listB':listB,'listC':listC}

def search_value(list_name, search):
    my_list=get_objects_list()
    my_objects=lists(my_list)
    listA=my_objects.get('listA')
    listB=my_objects.get('listB')
    listC=my_objects.get('listC')

    # List is empty ? 



# main program -------------------------------------------------------

input_option=input("¿Qué desea hacer?: \n 1)Buscar un valor \n 2)Ordenar una lista \n : ")
try:
    if input_option=="1":
        list_name=input("Escriba la inicial de la lista en la que desea buscar \n ejemplo: A, B, C \n : ")
        if list_name=="A" or list_name=="a":
            search=int(input("Valor que deseas buscar en la lista A: "))
            search_value(list_name, search)
        elif list_name=="B" or list_name=="b":
            search=float(input("Valor que deseas buscar en la lista B: "))
            search_value(list_name, search)
        elif list_name=="C" or list_name=="c":
            search=input("Valor que deseas buscar en la lista C: ")
            search_value(list_name, search)
        else:
            print("Opción errónea")
    
except:
    pass