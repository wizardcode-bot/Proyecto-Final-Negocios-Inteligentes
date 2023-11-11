import pandas as pd
import numpy as np
from statistics import mode
import math
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Ruta del archivo Excel
ruta = 'C:\\Users\\HOME\\Downloads\\finalPoyectNegocios\\archivos\\DatosCompletos.xlsx'

# Cargar el archivo Excel en un DataFrame
data = pd.read_excel(ruta, sheet_name='Brillo Solar')

# Ruta del archivo CSV de salida
csv_file = "PromClimat.csv"

# Guardar los datos en un archivo CSV
data.to_csv(csv_file, index=False)

#Imprimir los 5 primeros o los 5 últimos datos del archivo
#print(data.head(5))
#print(data.tail(5))

# Muestra los departamentos sin repetirlos en la columna "DEPARTAMENTO"
departamentos_unicos = data['DEPARTAMENTO'].unique()
print("\nDepartamentos en la columna 'DEPARTAMENTO':")
for departamento in departamentos_unicos:
    print(departamento)

# Solicita al usuario que ingrese el nombre del departamento a filtrar
departamento_seleccionado = input("\nIngresa el nombre del Departamento que deseas filtrar: ")

#Busca en las columnas el departamento seleccionado
resultadoDepartamento = data.loc[data['DEPARTAMENTO'] == departamento_seleccionado]
#print(resultadoDepartamento)

#FILTRAR MUNICIPIO
municipio_unico = resultadoDepartamento['MUNICIPIO'].unique()
print("")
print(f"Municipios del Departamento '{departamento_seleccionado}'")
print("")
for municipio in municipio_unico:
    print(municipio)

# Solicita al usuario que ingrese el nombre del municipio a filtrar
municipio_seleccionado = input("\nIngresa el nombre del Municipio que deseas filtrar: ")

#Busca en las columnas el municipio seleccionado
resultadoMunicipio = data.loc[data['MUNICIPIO'] == municipio_seleccionado]
print(resultadoMunicipio)

#FILTRAR NOMBRE
nombre_unico = resultadoMunicipio['NOMBRE'].unique()
print("")
print(f"Lugares del Municipio '{municipio_seleccionado}'")
print("")
for nombre in nombre_unico:
    print(nombre)

# Solicita al usuario que ingrese el nombre del nombre a filtrar
nombre_seleccionado = input("\nIngresa el nombre del lugar que deseas filtrar: ")

resultadoNombre = data.loc[data['NOMBRE'] == nombre_seleccionado]
print(resultadoNombre)


#convierte el resultado en una lista
resultado_lista = resultadoNombre.values.tolist()

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

# Define las columnas de meses
#columnas_meses = ['ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN', 'JUL', 'AGO', 'SEP', 'OCT', 'NOV', 'DIC']
columnas_meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#Meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
BrilloSolar = [ENE, FEB, MAR, ABR, MAY, JUN, JUL, AGO, SEP, OCT, NOV, DIC]

# Organizar los datos de menor a mayor
datos_ordenados = sorted(zip(columnas_meses, BrilloSolar), key=lambda x: x[1])

# Imprimir los datos ordenados
print("")
for mes, valor in datos_ordenados:
    print(f"{mes}: {valor}")

#Ordena el arreglo de menor a mayor
arreglo_ordenado = sorted(BrilloSolar)
print("")

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


# Calcular el resultado
k = math.log( arreglo_ordenado[11]/arreglo_ordenado[0]) / 11
print("\nK tiene un valor de: ", k)
numero3 = float(input("\nIngresa la cantidad de años que quieres estimar: ")) #Entre 2000 y 2020
if (numero3 > 2026):
    print("Número erróneo")
#numero4= numero3 - 2000
Estimacion = arreglo_ordenado[0] * math.exp(k * numero3)
print("\nSu prediccion es de:", round(Estimacion, 4))

#modelo de regresion
modeloregre = np.polyfit(columnas_meses, arreglo_ordenado, 5)
predecir = np.poly1d(modeloregre)
print(modeloregre)
print(predecir)

cantpredicion = int(input("A que mes quiere predecir: "))
cantregresion = predecir(cantpredicion)
# formato de presentación 2f quiere decir 2 decimales despues
print(f"La cantidad de precipitación(mm) para el mes {cantpredicion} sera de: {cantregresion:.2f}")
# Modelo Prediccion
cantpredicion = range(12,  cantpredicion + 1)
precipitapredi = predecir(cantpredicion)

buffer = BytesIO()#Almacena temporalmente las imagenes
plt.figure(figsize=(10, 5))  # dimensiones
# modelo de predicción datos anteriores
plt.plot(arreglo_ordenado, columnas_meses , 'o-', color='red')
plt.xlabel('Meses')
plt.ylabel('Precipitacion')
plt.title('Regresion y Prediccion')
plt.grid(True)
plt.plot(columnas_meses, predecir(columnas_meses), '--',color='green')  # modelo de regresión
plt.plot(cantpredicion, precipitapredi, '--',color='blue')  # datos predichos
plt.legend(['Datos', 'Regresión', 'Predicción'])
plt.show()

'''
#Grafica de datos
fig, ax = plt.subplots(figsize=(30, 10))#dimensiones
ax.plot(arreglo_ordenado, columnas_meses, marker='o', linestyle='-', color='blue') #eje x, eje y
ax.grid(True)
ax.set_title(f"Distribución Brillo solar y Meses para '{municipio_seleccionado}'")
ax.set_xlabel('Brillo Solar')
ax.set_ylabel('Meses')
plt.show()'''



