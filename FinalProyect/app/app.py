from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np
from statistics import mode
import math
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

#Se indica que es la ruta raíz
@app.route('/', methods=['GET', 'POST'])
#Se crea una vista llamada index que se expresa en forma de una función
def index():

    if request.method == 'POST':
     # Obtener datos del formulario
     departamento_seleccionado = request.form['departamento']
     municipio_seleccionado = request.form['municipio']
     nombre_seleccionado = request.form['nombre']
    else:
        # Valores predeterminados o manejar el caso en que no se haya enviado el formulario aún
        departamento_seleccionado = ""
        municipio_seleccionado = ""
        nombre_seleccionado = ""

    # Ruta del archivo Excel
    ruta = 'C:\\Users\\HOME\\Downloads\\finalPoyectNegocios\\archivos\\DatosCompletos.xlsx'

    # Cargar el archivo Excel en un DataFrame
    data = pd.read_excel(ruta, sheet_name='Brillo Solar')

    # Ruta del archivo CSV de salida
    csv_file = "PromClimat.csv"

    # Guardar los datos en un archivo CSV
    data.to_csv(csv_file, index=False)

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

    # Convertir resultadoMunicipio a una lista de diccionarios para pasar a la plantilla
    resultado_nombre_lista = resultadoNombre.to_dict(orient='records')

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
    
    #MODELO DE REGRESION POLINOMICA 
    #(Se ajustan las variables a un polinomio de grado 5)
    coeficientes = np.polyfit(columnas_meses_numero, arreglo_ordenado, 3)
    #Se crea una función polinómica a partir de los coeficientes
    funcPolinomial = np.poly1d(coeficientes)
    #print(coeficientes)
    print(funcPolinomial)

    rangoPrediccion = int(input("A que mes quiere predecir: "))

    # Calcula los valores de la función polinómica en el rango dado
    prediccion = funcPolinomial(rangoPrediccion)


    # formato de presentación 2f, 2 decimales despues del punto
    print(f"La cantidad de Brillo Solar para el mes {rangoPrediccion} sera de: {prediccion:.2f}")
    # Modelo Prediccion
    rangoPrediccion = range(12,  rangoPrediccion + 1)
    prediccionGrafica = funcPolinomial(rangoPrediccion)

    buffer = BytesIO()#Almacena temporalmente las imagenes
    plt.figure(figsize=(10, 5))  # dimensiones
    # modelo de predicción datos anteriores
    plt.plot(columnas_meses_numero, arreglo_ordenado , 'o-', color='red')
    plt.xlabel('Meses')
    plt.ylabel('Brillo Solar')
    plt.title('Modelo de Regresión Polinómica y Predicción')
    plt.grid(True)
    plt.plot(columnas_meses_numero, funcPolinomial(columnas_meses_numero), '--',color='green')  # Grafica modelo de regresión
    plt.plot(rangoPrediccion, prediccionGrafica, '--',color='blue')  # Grafica datos predecidos
    plt.legend(['Datos', 'Regresión', 'Predicción'])
    img1 = BytesIO()
    plt.savefig(img1, format='png')
    img1.seek(0)
    imagen_prediccion = base64.b64encode(img1.read()).decode() 

    plt.figure(figsize=(10, 5))  # dimensiones
    # modelo de predicción datos anteriores
    plt.plot(columnas_meses_numero, arreglo_ordenado , 'o-', color='red')
    plt.xlabel('Meses')
    plt.ylabel('Brillo Solar')
    plt.title('Datos de Brillo Solar registrados')
    plt.grid(True)
    img2 = BytesIO()
    plt.savefig(img2, format='png')
    img2.seek(0)
    imagen_datos = base64.b64encode(img2.read()).decode() 

    
    return render_template('index.html', data=resultadoNombre, datos=datos_ordenados, mes=mes, valor=valor, img1=imagen_prediccion, img2= imagen_datos, prediccion=prediccion, resultado_nombre=resultado_nombre_lista, departamento=departamento_seleccionado, municipio=municipio_seleccionado, nombre=nombre_seleccionado, moda=moda, media=media, mediana=mediana, desvEst=desvEst)

#Si está en la página principal, llama a la función
if __name__=='__main__':
    app.run(debug=True, port=5000)