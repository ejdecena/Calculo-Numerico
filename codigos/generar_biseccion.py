#!/usr/bin/env python3
"""Este script genera los archivos para el Proyecto de Biseccion."""

import csv
import os
import shutil

DATA = "../evaluaciones/participantes.csv"
PATH = "proyecto_biseccion{}".format(os.sep)

try:
    shutil.rmtree(PATH)
except FileNotFoundError:
    pass
finally:
    os.mkdir(PATH)

cabecera  = '''#!/usr/bin/env python3
"""
Proyecto en Python sobre el Algoritmo de Bisección.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""\n'''

testing = ""
modulos = ""


with open(DATA) as fdata:
    data = csv.reader(fdata)
    for i, par in enumerate(data):
        if not i:
            continue
        modulo = "{}".format(par[0].split()[0] + "_" + par[1])
        testing +=  "import " + modulo + "\n"
        modulos += modulo + ",\n"
        proyecto  = cabecera
        proyecto += "\nimport math"
        proyecto += "\n\n\ndef biseccion(f, a, b, ER, N):"
        proyecto += '\n    """'
        proyecto += '\n    Implementa el Algoritmo de Biseccion y retorna la aproximación de la raiz.'
        proyecto += '\n'
        proyecto += '\n    Parámetros:'
        proyecto += '\n    f: función de variable real f(x).'
        proyecto += '\n    a: límite inferior del intervalo.'
        proyecto += '\n    b: límite superior del intervalo.'
        proyecto += '\n    ER: cota mínima del error relativo.'
        proyecto += '\n    N: número máximo de iteraciones.'
        proyecto += '\n    """'
        proyecto += '\n\n    print("Iteración:", i, "Punto Medio:", pm_actual, "Error:", err)\n\n    return pm_actual'
        proyecto += '\n\n\nif __name__ == "__main__":'
        proyecto += '\n    # Pruebe aquí su función.'
        proyecto += '\n    pass'
        # print(proyecto, file = open(PATH + modulo + ".py", "w"))

    # Generando el archivo de testing ...
    testing = '''#!/usr/bin/env python3\n"""\nTests de los Algoritmos de Bisección.\n"""\n\n''' + testing + "import testing_biseccion\n\n"
    testing += "participantes = [" + modulos + "]\n\n"
    testing += "notas = testing_biseccion.testing(participantes)\n"
    testing += "print(notas)"

    print(testing, file = open(PATH + "testing.py", "w"))
    print("__pycache__\nbiseccion.py\ntesting.py\ntesting_biseccion.py",
        file = open(PATH + ".gitignore", "w"))
    shutil.copy("README_BI.md", PATH + "README.md")
    shutil.copy("biseccion.py", PATH + "biseccion.py")
    shutil.copy("testing_biseccion.py", PATH + "testing_biseccion.py")