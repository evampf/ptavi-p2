#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcoohija

if __name__ == "__main__":

    datos = sys.argv[1]
    with open(datos) as operaciones:

        datos = csv.reader(operaciones)
        calculadora2 = calcoohija.CalculadoraHija()
        for linea in datos:
            operacion = linea[0]
            numeros = linea[1:]
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
                sys.exit('Operación inválida.')

            print(resultado)
