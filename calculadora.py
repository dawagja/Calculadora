# -*- coding: UTF-8 -*-

'''
@author: Jose Antonio Aguilar Granados
'''
import os

from Pcalculadora.funciones import *

def menu():
    """Función que limpia la pantalla y muestra nuevamente el menu"""
    os.system('cls') # NOTA para windows tienes que cambiar clear por cls
    print ("Selecciona una opción")
    print ("\t1 - Sumar")
    print ("\t2 - Restar")
    print ("\t3 - Multiplicar")
    print ("\t5 - Dividir")
    print ("\t0 - Salir")
 
while True:
    # Mostramos el menu
    menu()
 
    # solicituamos una opción al usuario
    opcionMenu = input("inserta un numero valor >> ")
     
    if opcionMenu== 1:
        print sumar(int(input("inserta primer numero")), int (input("inserta segundo numero")))
    elif opcionMenu== 2:
        print restar(int(input("inserta primer numero")), int (input("inserta segundo numero")))
    elif opcionMenu== 3:
        print multiplicar(int(input("inserta primer numero")), int (input("inserta segundo numero")))
    elif opcionMenu== 4:
        print dividir(int(input("inserta primer numero")), int (input("inserta segundo numero")))    
    elif opcionMenu== 0:
        break
    else:
        print ("")
        input("No has pulsado ninguna opción correcta")