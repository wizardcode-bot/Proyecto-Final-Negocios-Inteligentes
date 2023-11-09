import pandas as pd
import numpy as np
from statistics import mode
import math


# Ruta del archivo Excel
ruta = 'C:\\Users\\HOME\\Downloads\\finalPoyectNegocios\\archivos\\PromClima.xlsx'
df = pd.read_excel(ruta, sheet_name='Brillo Solar')

# Cargar el archivo Excel en un DataFrame
data = pd.read_excel(ruta)

# Ruta del archivo CSV de salida
csv_file = "PromClimat.csv"

# Guardar los datos en un archivo CSV
data.to_csv(csv_file, index=False)

resultado = data[(data['DEPARTAMENTO'] == 'Meta') & (data['MUNICIPIO'] == 'Villavicencio') & (data['NOMBRE'] == 'Unillanos')]
print("\n",resultado)

#convierte el resultado en una lista
resultado_lista = resultado.values.tolist()

ENE = resultado_lista[0][3]
FEB = resultado_lista[0][4]
MAR = resultado_lista[0][5]
ABR = resultado_lista[0][6]
MAY = resultado_lista[0][7]
JUN = resultado_lista[0][8]
JUL = resultado_lista[0][9]
AGO = resultado_lista[0][10]
SEP = resultado_lista[0][11]
OCT = resultado_lista[0][12]
NOV = resultado_lista[0][13]
DIC = resultado_lista[0][14]

Meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
BrilloSolar = [ENE, FEB, MAR, ABR, MAY, JUN, JUL, AGO, SEP, OCT, NOV, DIC]

#PREDICCION DE DATOS
#valor1 = float(input("\nIngresa el dato de el brillo solar: "))
#valor2 = float(input("\nIngresa la cantidad de meses: "))

# Calcular el resultado
k = math.log( DIC/ENE) / 11
print("\nK tiene un valor de: ", k)
valor3 = float(input("\nIngresa la cantidad de años que quieres estimar: "))
valor4 = valor3 * 12
Estimacion = ENE * math.exp(k * valor4)
print("\nSu prediccion es de:", round(Estimacion, 4))