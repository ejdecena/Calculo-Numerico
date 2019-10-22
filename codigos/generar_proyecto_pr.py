#!/usr/bin/env python3
"""Este script genera un archivo para el proyecto de prueba de PR."""

import csv
import random

DATA      = "../evaluaciones/participantes.csv"
PREGUNTAS = [
"Recibe como parámetro una lista y retorna el promedio de la lista.",
"Recibe como parámetro una lista y retorna la lista invertida.",
"Recibe como parámetro un diccionario y retorna las claves del diccionario.",
"Recibe como parámetro un diccionario y retorna los valores del diccionario.",
"Recibe como parámetro los valores a, b, c y retorna el mínimo.",
"Recibe como parámetro una lista y retorna el mínimo valor de la lista.",
"Recibe como parámetro una lista y retorna el máximo valor de la lista.",
"Recibe como parámetro un diccionario y retorna el máximo valor del diccionario.",
"Recibe como parámetro un diccionario y retorna el mínimo valor del diccionario.",
"Recibe como parámetro a, b, c y retorma el máximo.",
"Recibe como parámetro una cadena y retorna las vocales de la cadena.",
"Recibe como parámetro una cadena y retorma las consonantes de la cadena.",
"Recibe como paŕametro una cadena y retorna el número de caracteres de la cadena.",
"Recibe como parámetro una cadena y retorna la cadena invertida.",
]

proyecto  = '''#!/usr/bin/env python3
"""Proyecto sobre Python y el workflow Pull-Request en GitHub.

Cada participante debe completar su función y luego solicitar el Pull-Request.

Este código fue generado por:
https://github.com/ejdecena/calculo_numerico/codigos/generar_proyecto_pr.py
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

    print(proyecto, file = open("proyecto_calculo.py", "w"))