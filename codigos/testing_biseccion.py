#!/usr/bin/env python3
import math
import biseccion

f = lambda x: math.exp(-x) - math.log(x)
g = lambda x: x - math.cos(x)
h = lambda x: x**2 - 5*x - math.exp(x)

casos_prueba = ((f, 1, 2, 0.02, 1000),
               (g, 0, 1, 0.02, 1000),
               (h, -1, 1, 0.02, 1000))

def testing(participantes):
    """
    Retorna un diccionario con la notas de los participantes del Proyecto de
    Bisección.

    Parámetros:
    participantes: es una lista de los módulos de los participantes del
    proyecto.
    """
    notas = dict()
    for participante in participantes:
        print(participante.__name__)
        errores = list()
        for caso in casos_prueba:
            print("    Caso:", caso)
            raizhat = participante.biseccion(*caso)
            raiz    = biseccion.biseccion(*caso)
            error   = math.fabs(raiz - raizhat)
            errores.append(error)
            print("    Error:", error)

        notas[participante.__name__] = sum(errores)/len(errores)

    nota_minima = 0
    nota_maxima = 10
    min_error   = min(notas.values())
    max_error   = max(notas.values())
    for participante in participantes:
        participantes[participante] = nota_minima \
    + ((participantes[participante] - min_error)*(nota_maxima - nota_minima))\
    / (max_error - min_error)

    return participantes