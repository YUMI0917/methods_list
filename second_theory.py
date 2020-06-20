#!/usr/bin/python3

# Author: Elkin
# Program: second_theory.py
# Version: Python 3.8.2

from time import time
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
        while(total!=10000):
            qty_int=randint(1,10000)
            qty_float=randint(1,10000)
            qty_string=randint(1,10000)
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
    if list_name=="A" or list_name=="a":
        start_time = time()
        print("lista A :", listA, "\n ----------------------------------------- \n")
        position=listA.index(search)
        print("LISTA A => Elemento : ", search ," está en el index : ", position, " de la lista")
        elapsed_time = time() - start_time
        print("LISTA A time: ",round(float(elapsed_time*1000), 2), " milliseconds" ) # two decimals
    elif list_name=="B" or list_name=="b":
        start_time = time()
        print("lista B :", listB)
        position=listB.index(search)
        print("LISTA B => Elemento : ", search ," está en el index : ", position, " de la lista")
        elapsed_time = time() - start_time
        print("LISTA B time: ",round(float(elapsed_time*1000), 2), " milliseconds" ) # two decimals
    elif list_name=="C" or list_name=="c":
        start_time = time()
        print("lista C :", listC)
        position=listC.index(search)
        print("LISTA C => Elemento : ", search ," está en el index : ", position, " de la lista")
        elapsed_time = time() - start_time
        print("LISTA C time: ",round(float(elapsed_time*1000), 2), " milliseconds" ) # two decimals
    else:
        print("El elemento buscado no se encuentra en la lista.")

    print("\n ----------------------------------------- \n")
    start_time = time()
    for key, value in my_objects.items():
        for element in value:
            if element==search: # if the search is effective
                my_search=value.index(element)

    print("LISTA DE OBJETOS => Elemento : ", search ," está en el index : ", my_search , " de la lista")
    elapsed_time = time() - start_time
    print("LISTA DE OBJETOS time: ",round(float(elapsed_time*1000), 2), " milliseconds" ) # two decimals

def order_values(option):

    my_list=get_objects_list()
    my_objects=lists(my_list)
    listA=my_objects.get('listA') # option 1
    listB=my_objects.get('listB') # option 2
    listC=my_objects.get('listC') # option 3
    # order
    if option=="1":
        start_time = time()
        listA.sort()
        print("Lista A ordenada: ",listA)
        elapsed_time = time() - start_time
        print("Lista A time: ",round(float(elapsed_time*1000), 2), " milliseconds" ) # two decimals
    elif option=="2":
        start_time = time()
        listB.sort()
        print("Lista B ordenada: ", listB)
        elapsed_time = time() - start_time
        print("Lista B time: ",round(float(elapsed_time*1000), 2), " milliseconds" ) # two decimals
    elif option=="3":
        start_time = time()
        listC.sort()
        print(listC)
        elapsed_time = time() - start_time
        print("Lista C time: ",round(float(elapsed_time*1000), 2), " milliseconds" ) # two decimals
    else:
        print("¡No existe la opción que haz escrito!")

    print("\n ----------------------------------------- \n")
    for key, value in my_objects.items():
        if key=="listA" and option=="1":
            start_time = time()
            print("Lista de Objetos: ",sorted(value))
            elapsed_time = time() - start_time
            print("Lista de Objetos time: ",round(float(elapsed_time*1000), 2), " milliseconds" ) # two decimals
        elif key=="listB" and option=="2":
            start_time = time()
            print("Lista de Objetos: ",sorted(value))
            elapsed_time = time() - start_time
            print("Lista de Objetos time: ",round(float(elapsed_time*1000), 2), " milliseconds" ) # two decimals
        elif key=="listC" and option=="3":
            start_time = time()
            print("Lista de Objetos: ",sorted(value))
            elapsed_time = time() - start_time
            print("Lista de Objetos time: ",round(float(elapsed_time*1000), 2), " milliseconds" ) # two decimals

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
    elif input_option=="2":
        type_order=input("Indique que tipo de lista desea ordenar \n ejemplo: 1)INT, 2)FLOAT, 3)STRING \n : ")
        order_values(type_order) # int, float or string
    else:
        print("Ha elegido una opción que no existe")
    
except ValueError:
    print("!El elemento buscado no se encuentra en la lista!")