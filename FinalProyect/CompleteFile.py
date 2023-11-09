import pandas as pd
import numpy as np
from statistics import mode
import math


# Ruta del archivo Excel
ruta = 'C:\\Users\\HOME\\Downloads\\finalPoyectNegocios\\archivos\\DatosCompletos.xlsx'

# Cargar el archivo Excel en un DataFrame
data = pd.read_excel(ruta, sheet_name='Brillo Solar')

# Ruta del archivo CSV de salida
csv_file = "PromClimat.csv"

# Guardar los datos en un archivo CSV
data.to_csv(csv_file, index=False)


#print(data.head(5))
#print(data.tail(5))

resultado = data.loc[data['DEPARTAMENTO'] == 'Meta']
print(resultado)

'''
resultado = data[(data['DEPARTAMENTO'] == 'Meta') & (data['MUNICIPIO'] == 'Villavicencio')]
print(resultado)'''

'''
resultado = data[(data['DEPARTAMENTO'] == 'Meta') & (data['MUNICIPIO'] == 'Villavicencio') & (data['NOMBRE'] == 'Unillanos')]
print("\n",resultado)'''

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

#Ordena el arreglo de menor a mayor
arreglo_ordenado = sorted(BrilloSolar)
print("")
#Imprime el arreglo ordenado
for elemento in arreglo_ordenado:
    print(elemento)

#Muestra el primer y último dato del arreglo ordenado
print("")
print(round(arreglo_ordenado[11], 4))
print(round(arreglo_ordenado[0], 4))

print("")
Another = resultado_lista[1][3]
print(round(Another, 4))

for indice, elemento in enumerate(resultado_lista):
    print(f"Elemento en el índice {indice}: {elemento}")


# Usamos zip(*matriz) para transponer la matriz (convertir filas en columnas)
columnas = [list(columna) for columna in zip(*resultado_lista)]

# Ordenamos cada columna
columnas_ordenadas = [sorted(columna) for columna in columnas]

# Finalmente, transponemos de nuevo las columnas ordenadas para obtener las columnas de la matriz ordenadas
matriz_ordenada = [list(columna) for columna in zip(*columnas_ordenadas)]

# Matriz ordenada
for fila in matriz_ordenada:
    print("")
    print(fila)




#print(data["MUNICIPIO"]) #IMPRIME COLUMNAS

#print(data.loc[0]) #IMPRIME FILAS

#imprimir todos los datos
'''
for index, row in data.iterrows():
    uno = row[0]
    dos = row[1]
    print(uno, dos)'''


