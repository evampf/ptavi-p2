#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class calculadora():

	def suma(num1,num2):
		"""Funcion que suma números"""
		return num1 + num2

	def resta(num1,num2):
		"""Función que resta números"""
		return num1 - num2

if __name__ == "__main__":
    try:
        numero1 = float(sys.argv[1])
        numero2 = float(sys.argv[3])
    except ValueError:
        sys.exit("Error: Parámetros incorrectos")

    if sys.argv[2] == "suma":
        result = calculadora.suma(numero1, numero2)
    elif sys.argv[2] == "resta":
        result = calculadora.resta(numero1, numero2)

    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)

