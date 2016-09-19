#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def plus(op1, op2):
    """ Function to sum the operands """
    return op1 + op2


def minus(op1, op2):
    """ Function to substract the operands """
    return op1 - op2

def mult(op1,op2):
	""" Function to mult the operands """
	return op1 * op2

def div(op1,op2):
    """Function to divide the operands """
    try:
        return op1/op2
    except:     
        sys.exit("Error: Divide 0")

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = minus(operando1, operando2)
    elif sys.argv[2] == "multiplica":
        result = mult(operando1,operando2)
    elif sys.argv[2] == "divide":
        result = div(operando1,operando2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
