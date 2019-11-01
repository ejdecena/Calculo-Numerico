#!/usr/bin/env python3
"""Este script genera un archivo para el proyecto de prueba de PR."""

import os
import csv
import random
import shutil

DATA = "../evaluaciones/participantes.csv"
PATH = "proyecto_pull_request{}".format(os.sep)

try:
    shutil.rmtree(PATH)
except FileNotFoundError:
    pass
finally:
    os.mkdir(PATH)

PREGUNTAS = [
"Recibe como parámetro una lista y retorna el promedio de la lista.",
"Recibe como parámetro una lista y retorna la lista invertida.",
"Recibe como parámetro un diccionario y retorna una lista con las claves del diccionario.",
"Recibe como parámetro un diccionario y retorna una lista con los valores del diccionario.",
"Recibe como parámetro los valores a, b, c y retorna el mínimo.",
"Recibe como parámetro una lista y retorna el mínimo valor de la lista.",
"Recibe como parámetro una lista y retorna el máximo valor de la lista.",
"Recibe como parámetro un diccionario y retorna el máximo valor del diccionario.",
"Recibe como parámetro un diccionario y retorna el mínimo valor del diccionario.",
"Recibe como parámetro a, b, c y retorma el máximo.",
"Recibe como parámetro una cadena y retorna una lista con las vocales de la cadena.",
"Recibe como parámetro una cadena y retorma una lista con las consonantes de la cadena.",
"Recibe como paŕametro una cadena y retorna el número de caracteres de la cadena.",
"Recibe como parámetro una cadena y retorna la cadena invertida.",
"Recibe como parámetro una tupla y retorna el primer elemento de la tupla.",
"Recibe como parámetro una tupla y retorna el último elemento de la tupla.",
"Recibe como parámetro un conjunto y retorna el mayor elemento del conjunto.",
"Recibe como parámetro un conjunto y retorna el menor elemento del conjunto."
]

proyecto  = '''#!/usr/bin/env python3
"""
Proyecto sobre Python y el workflow Pull-Request en GitHub.

Cada participante debe completar su función y luego solicitar el Pull-Request.
"""\n'''


with open(DATA) as fdata:
    data = csv.reader(fdata)
    random.shuffle(PREGUNTAS)
    for i, par in enumerate(data):
        if not i:
            continue
        proyecto += "\n\ndef {}".format(par[0].split()[0] + "_" + par[1]+"():")
        proyecto += '\n    """'
        proyecto += '\n    {}'.format(PREGUNTAS[i - 1])
        proyecto += '\n    """'
        proyecto += '\n    pass\n'

    print(proyecto, file = open(PATH + "funciones_python.py", "w"))
    print("__pycache__\n", file = open(PATH + ".gitignore", "w"))
    shutil.copy("README_PR.md", PATH + "README.md")