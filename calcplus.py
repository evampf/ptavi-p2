#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcoohija


operaciones = open('numeros.csv', 'r')
lineas = operaciones.readlines()



if __name__ == "__main__":


    calculadora2 = calcoohija.CalculadoraHija()
    
    for linea in lineas:
        operacion = linea.split(',')[0]
        numeros = linea.split(',')[1:]
        resultado = int(numeros[0])

        if operacion == "suma":
            for num in numeros[1:]:
                resultado = calculadora2.suma(resultado, int(num))
        elif operacion == "resta":
            for num in numeros[1:]:
                resultado = calculadora2.resta(resultado, int(num))
        elif operacion == "multiplica":
            for num in numeros[1:]:
                resultado = calculadora2.multiplica(resultado, int(num))
        elif operacion == "divide":
            for num in numeros[1:]:
                resultado = calculadora2.divide(resultado, int(num))

        else:
            sys.exit('Operación sólo puede ser sumar, restar, multiplicar o dividir.')

        print(resultado)


	




