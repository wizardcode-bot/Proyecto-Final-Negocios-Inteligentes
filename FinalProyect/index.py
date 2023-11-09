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

# Muestra los departamentos únicos en la columna "DEPARTAMENTO"
departamentos_unicos = data['DEPARTAMENTO'].unique()
print("\nDepartamentos únicos en la columna 'DEPARTAMENTO':")
for departamento in departamentos_unicos:
    print(departamento)

# Solicita al usuario que ingrese el nombre del departamento a filtrar
departamento_seleccionado = input("Ingresa el nombre del Departamento que deseas filtrar: ")


resultadoDepartamento = data.loc[data['DEPARTAMENTO'] == departamento_seleccionado]
#print(resultadoDepartamento)

#FILTRAR MUNICIPIO
municipio_uni = resultadoDepartamento['MUNICIPIO'].unique()
print(f"Municipio del  '{departamento_seleccionado}'")
for municipio in municipio_uni:
    print(municipio)

# Solicita al usuario que ingrese el nombre del municipio a filtrar
municipio_seleccionado = input("Ingresa el nombre del Municipio que deseas filtrar: ")

resultadoMunicipio = data.loc[data['MUNICIPIO'] == municipio_seleccionado]
print(resultadoMunicipio)

#FILTRAR NOMBRE
nombre_uni = resultadoMunicipio['NOMBRE'].unique()
print(f"Nombre del  '{municipio_seleccionado}'")
for nombre in nombre_uni:
    print(nombre)

nombre_seleccionado = input("Ingresa el nombre del lugar que deseas filtrar: ")

resultadoNombre = data.loc[data['NOMBRE'] == nombre_seleccionado]
print(resultadoNombre)


'''
resultado = data[(data['DEPARTAMENTO'] == 'Meta') & (data['MUNICIPIO'] == 'Villavicencio') & (data['NOMBRE'] == 'Unillanos')]
print("\n",resultado)'''

#convierte el resultado en una lista
resultado_lista = resultadoMunicipio.values.tolist()

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


#ESTADÍSTICA
print("\n MEDIDAS DE TENDENCIA CENTRAL Y MEDIDAS DE DISPERSIÓN")
moda = mode(BrilloSolar)
media = np.mean(BrilloSolar)
mediana = np.median(BrilloSolar)
desvEst = np.std(BrilloSolar)
#Se guardan los valores en variables para poder reducirlos a 4 decimales después de la coma
print("La moda de el Brillo Solar es:", round(moda, 4))
print("La media de el Brillo Solar es:", round(media, 4))
print("La mediana de el Brillo Solar es:", round(mediana, 4))
print("La desviacion estandar de el Brillo Solar es:", round(desvEst, 4))


#PREDICCION DE DATOS
#valor1 = float(input("\nIngresa el dato de el brillo solar: "))
#valor2 = float(input("\nIngresa la cantidad de meses: "))

# Calcular el resultado
k = math.log( arreglo_ordenado[11]/arreglo_ordenado[0]) / 11
print("\nK tiene un valor de: ", k)
numero3 = float(input("\nIngresa la cantidad de años que quieres estimar: ")) #Entre 2000 y 2026
if (numero3 > 2026):
    print("Número erróneo")
numero4= numero3 - 2000
numero5 = numero4 * 12
Estimacion = arreglo_ordenado[0] * math.exp(k * numero5)
print("\nSu prediccion es de:", round(Estimacion, 4))




#print(data["MUNICIPIO"]) #IMPRIME COLUMNAS

#print(data.loc[0]) #IMPRIME FILAS

#imprimir todos los datos
'''
for index, row in data.iterrows():
    uno = row[0]
    dos = row[1]
    print(uno, dos)'''


