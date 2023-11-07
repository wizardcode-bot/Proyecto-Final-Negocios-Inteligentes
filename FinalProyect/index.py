import pandas as pd
import numpy as np
from statistics import mode

# Ruta del archivo Excel
ruta = r"C:\Users\HOME\Downloads\finalPoyectNegocios\PromClima.xlsx"

# Cargar el archivo Excel en un DataFrame
data = pd.read_excel(ruta)

# Ruta del archivo CSV de salida
csv_file = "PromClimat.csv"

# Guardar los datos en un archivo CSV
data.to_csv(csv_file, index=False)


#print(data.head(5))
#print(data.tail(5))
'''
resultado = data.loc[data['DEPARTAMENTO'] == 'Meta']
print(resultado)'''

'''
resultado = data[(data['DEPARTAMENTO'] == 'Meta') & (data['MUNICIPIO'] == 'Villavicencio')]
print(resultado)'''


resultado = data[(data['DEPARTAMENTO'] == 'Meta') & (data['MUNICIPIO'] == 'Villavicencio') & (data['NOMBRE'] == 'Unillanos')]
print(resultado)

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

#ESTADÍSTICA
print("MEDIDAS DE TENDENCIA CENTRAL Y MEDIDAS DE DISPERSIÓN")
moda = mode(BrilloSolar)
media = np.mean(BrilloSolar)
mediana = np.median(BrilloSolar)
desvEst = np.std(BrilloSolar)
#Se guardan los valores en variables para poder reducirlos a 4 decimales después de la coma
print("La moda de el Brillo Solar es:", round(moda, 4))
print("La media de el Brillo Solar es:", round(media, 4))
print("La mediana de el Brillo Solar es:", round(mediana, 4))
print("La desviacion estandar de el Brillo Solar es:", round(desvEst, 4))

'''
#PREDICCION DE DATOS
numero1 = float(input("Ingresa el dato de la tempreratura: "))
numero2 = float(input("Ingresa la cantidad de años: "))

# Calcular el resultado
k = math.log( numero1/24.2) / numero2
print("K tiene un valor de: ", k)
numero3 = float(input("Ingresa la cantidad de años que quieres estimar: "))
Estimacion = 24.2 * math.exp(k * numero3)
print("Su prediccion es de:", Estimacion)
'''



#print(data["MUNICIPIO"]) #IMPRIME COLUMNAS

#print(data.loc[0]) #IMPRIME FILAS

#imprimir todos los datos
'''
for index, row in data.iterrows():
    uno = row[0]
    dos = row[1]
    print(uno, dos)'''


