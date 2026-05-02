import pandas as pd
import numpy as np

edades = pd.Series([25, 30, 35, 40], name='Edad')
nombres = pd.Series(["Fulanito", "Juanito", "Ajalas", "Mike"], name='Nombre')

tabla = pd.concat([nombres, edades], axis=1)

data = {
        'Motor': ['AC_Standar', 'Servo', 'Stepper', 'DC_Brushless'],
        'Voltaje': [220, 24, 12, 5],
        'Corriente': [5.5, 2.1, 1.8, 0.8],
        'Eficiente': [True, True, False, True]
        }

df = pd.DataFrame(data)

""" Manejo de Archivos """
df = pd.read_csv('automobile_parts.csv')
