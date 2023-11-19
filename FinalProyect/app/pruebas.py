from flask import Flask, render_template
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
columnas_meses = ['ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN', 'JUL', 'AGO', 'SEP', 'OCT', 'NOV', 'DIC']
columnas_meses_numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

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
# Ajusta manualmente el valor de k
k_factor = 1  
k = k_factor * (math.log(arreglo_ordenado[-1] / arreglo_ordenado[0]) / len(arreglo_ordenado))

print("\nK tiene un valor de: ", k)
numero3 = float(input("\nIngresa la cantidad de años que quieres estimar: "))  # Años adicionales a predecir
if numero3 < 0:
    print("Ingrese un número positivo para los años")
else:
    estimacion = arreglo_ordenado[-1] * np.exp(k * numero3)
    print("\nLa estimación para el año será:", round(estimacion, 4))

    # Gráfica de datos existentes y predicción
    plt.figure(figsize=(8, 6))
    plt.scatter(columnas_meses_numero, arreglo_ordenado, label='Datos existentes', color='blue')
    
    # Se generan los valores para la predicción
    rango_prediccion = np.linspace(1, 12 + numero3, 100)
    prediccion = arreglo_ordenado[-1] * np.exp(k * (rango_prediccion - 12))

    plt.plot(rango_prediccion, prediccion, label='Predicción', color='red')
    plt.xlabel('Meses')
    plt.ylabel('Brillo Solar')
    plt.title('Predicción con Modelo Exponencial')
    plt.legend()
    plt.grid(True)
    plt.show()