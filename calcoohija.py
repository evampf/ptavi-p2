#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class calculadora():

    def suma(self,num1,num2):
        """Funcion que suma dos números"""
        return num1 + num2

    def resta(self,num1,num2):
        """Funcion que resta dos números"""
        return num1 - num2

    def multiplica(self,num1,num2):
        """Funcion que multiplica dos números"""
        return num1 * num2

    def divide(self,num1,num2):
        """Funcion que divide dos números"""
        try:
            return num1 / num2
        except:
            sys.exit("Error: Division by zero is not allowed")



if __name__ == "__main__":
    try:
        numero1 = float(sys.argv[1])
        numero2 = float(sys.argv[3])
    except ValueError:
        sys.exit("Error: Parámetros incorrectos")

    if sys.argv[2] == "suma":
        result = calculadora().suma(numero1, numero2)
    elif sys.argv[2] == "resta":
        result = calculadora().resta(numero1, numero2)
    elif sys.argv[2] == "multiplica":
        result = calculadora().multiplica(numero1,numero2)
    elif sys.argv[2] == "divide":
        result = calculadora().divide(numero1,numero2)

    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)

