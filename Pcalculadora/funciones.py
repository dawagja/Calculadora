# -*- coding: UTF-8 -*-

'''
@author: Jose Antonio Aguilar Granados
'''

        
def sumar(a, b):
    """Función que resta las variables a y b"""
    return a+b 
    
    
def restar(a, b):
    """Función que resta las variables a y b"""
    return a-b
    
    
def multiplicar(a, b):
    """Función que multiplica las variables a y b"""
    return a*b
        
        
def dividir(a, b):
    """Función que dividir las variables a y b"""
    try:
        a/b
    except ZeroDivisionError:
            print("Error, el segundo argumento no puede ser 0")
    return a/b