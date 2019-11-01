#!/usr/bin/env python3

import math

def biseccion(f, a, b, ER, N):
    """
    Implementa el Algoritmo de Biseccion y retorna la aproximación de la raíz.

    Parámetros:
    f: función de variable real f(x).
    a: límite inferior del intervalo.
    b: límite superior del intervalo.
    ER: cota mínima del error relativo.
    N: número máximo de iteraciones.
    """
    if f(a)*f(b) > 0:
        raise Exception("No existe un cambio de signo de f(x) en [a, b].")
    err = 1
    i   = 0
    while i < N and err > ER:
        pm_actual = (a + b)/2
        if f(a)*f(pm_actual) < 0:
            b = pm_actual
        else:
            a = pm_actual
        if i:
            err = math.fabs((pm_actual - pm_anterior)/pm_actual)
        pm_anterior = pm_actual
        i += 1
        print("Iteración:", i, "Punto Medio:", pm_actual, "Error:", err)
    return pm_actual


if __name__ == '__main__':
    # Testing ...

    f = lambda x: math.exp(-x) - math.log(x)
    g = lambda x: x - math.cos(x)
    h = lambda x: x**2 - 5*x - math.exp(x)

    casos_prueba = ((f, 1, 2, 0.02, 1000),
                   (g, 0, 1, 0.02, 1000),
                   (h, -1, 1, 0.02, 1000))

    for caso in casos_prueba:
        print("Caso:", caso)
        raiz = biseccion(*caso)
        print("Raíz:", raiz)
        print("Comprobación: f({}) = {}\n".format(raiz, caso[0](raiz)))