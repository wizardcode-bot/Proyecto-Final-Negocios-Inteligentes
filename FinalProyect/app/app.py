from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np
from statistics import mode
import math
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/prediccion', methods=['GET', 'POST'])
def prediccion():

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

    return render_template('prediccion.html', departamentos=departamentos_unicos)

@app.route('/municipios', methods=['GET', 'POST'])
#Se crea una vista  que se expresa en forma de una función
def municipios():
    if request.method == 'POST':
     # Obtener datos del formulario
     departamento_seleccionado = request.form.get("departamento")
    else:
        # Valores predeterminados o manejar el caso en que no se haya enviado el formulario aún
        departamento_seleccionado = ""

    # Ruta del archivo Excel
    ruta = 'C:\\Users\\HOME\\Downloads\\finalPoyectNegocios\\archivos\\DatosCompletos.xlsx'

    # Cargar el archivo Excel en un DataFrame
    data = pd.read_excel(ruta, sheet_name='Brillo Solar')

    # Ruta del archivo CSV de salida
    csv_file = "PromClimat.csv"

    # Guardar los datos en un archivo CSV
    data.to_csv(csv_file, index=False)

    #Busca en las columnas el departamento seleccionado
    resultadoDepartamento = data.loc[data['DEPARTAMENTO'] == departamento_seleccionado]

    #FILTRAR MUNICIPIO
    municipio_unico = resultadoDepartamento['MUNICIPIO'].unique()

    return render_template('municipios.html', municipios=municipio_unico)

@app.route('/formulario', methods=['GET', 'POST'])
#Se crea una vista  que se expresa en forma de una función
def formulario():
    if request.method == 'POST':
     # Obtener datos del formulario
     municipio_seleccionado = request.form.get("municipio")
    else:
        # Valores predeterminados o manejar el caso en que no se haya enviado el formulario aún
        municipio_seleccionado = ""

       # Ruta del archivo Excel
    ruta = 'C:\\Users\\HOME\\Downloads\\finalPoyectNegocios\\archivos\\DatosCompletos.xlsx'

    # Cargar el archivo Excel en un DataFrame
    data = pd.read_excel(ruta, sheet_name='Brillo Solar')

    # Ruta del archivo CSV de salida
    csv_file = "PromClimat.csv"

    # Guardar los datos en un archivo CSV
    data.to_csv(csv_file, index=False)

    resultadoMunicipio = data.loc[data['MUNICIPIO'] == municipio_seleccionado]

    resultado_municipio_lista = resultadoMunicipio.to_dict(orient='records')

    return render_template('formulario.html', resultado_municipio=resultado_municipio_lista)


@app.route('/medicion')
def medicion():
    # Puedes realizar lógica específica para esta página si es necesario
    return render_template('medicion.html')

@app.route('/formula')
def formula():
    # Puedes realizar lógica específica para esta página si es necesario
    return render_template('formula.html')

@app.route('/brillo_solar')
def brillo_solar():
    # Puedes realizar lógica específica para esta página si es necesario
    return render_template('brillo_solar.html')

@app.route('/analisis')
def analisis():
    # Puedes realizar lógica específica para esta página si es necesario
    return render_template('analisis.html')

@app.route('/soluciones_g', methods=['GET', 'POST'])
def soluciones_g():

    if request.method == 'POST':
     # Obtener datos del formulario
     departamento_seleccionado = request.form.get("departamento")
     municipio_seleccionado = request.form.get("municipio")
     nombre_seleccionado = request.form.get("nombre")
     rangoPrediccion = int(request.form.get("rangoPrediccion"))
     rango_k = int(request.form.get("rango_k"))
    else:
        # Valores predeterminados o manejar el caso en que no se haya enviado el formulario aún
        departamento_seleccionado = ""
        municipio_seleccionado = ""
        nombre_seleccionado = ""
        rangoPrediccion = ""

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
    # departamento_seleccionado = input("\nIngresa el nombre del Departamento que deseas filtrar: ")

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
    # municipio_seleccionado = input("\nIngresa el nombre del Municipio que deseas filtrar: ")

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
    # nombre_seleccionado = input("\nIngresa el nombre del lugar que deseas filtrar: ")

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
    #(Se ajustan las variables a un polinomio de grado n)
    coeficientes = np.polyfit(columnas_meses_numero, arreglo_ordenado, 3)
    #Se crea una función polinómica a partir de los coeficientes
    funcPolinomial = np.poly1d(coeficientes)

    # Calcula los valores de la función polinómica en el rango dado
    prediccion = funcPolinomial(rangoPrediccion)

    # Prediccion
    rangoPrediccion = range(12,  rangoPrediccion + 1)
    prediccionGrafica = funcPolinomial(rangoPrediccion)

    buffer = BytesIO()#Almacena temporalmente las imagenes
    plt.figure(figsize=(10, 5))  # dimensiones
    # modelo de predicción datos anteriores
    plt.plot(columnas_meses_numero, arreglo_ordenado , 'o-', color='red')
    plt.xlabel('Tiempo')
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
    plt.xlabel('Tiempo')
    plt.ylabel('Brillo Solar')
    plt.title('Datos de Brillo Solar registrados')
    plt.grid(True)
    img2 = BytesIO()
    plt.savefig(img2, format='png')
    img2.seek(0)
    imagen_datos = base64.b64encode(img2.read()).decode() 

    # MODELO EXPONENCIAL
    k_factor = 1  
    k = k_factor * (math.log(arreglo_ordenado[-1] / arreglo_ordenado[0]) / len(arreglo_ordenado))

    estimacion = arreglo_ordenado[0] * np.exp(k * rango_k)

    # Gráfica de datos existentes y predicción
    plt.figure(figsize=(8, 6))
    plt.scatter(columnas_meses_numero, arreglo_ordenado, label='Datos existentes', color='blue')

    # Se generan los valores para la predicción
    rango_prediccion = np.linspace(1, rango_k, 100)
    prediccion_con_k = arreglo_ordenado[0] * np.exp(k * rango_prediccion)

    plt.plot(rango_prediccion, prediccion_con_k, label='Predicción', color='red')
    plt.xlabel('Tiempo')
    plt.ylabel('Brillo Solar')
    plt.title('Predicción con Modelo Exponencial')
    plt.legend()
    plt.grid(True)
    img3 = BytesIO()
    plt.savefig(img3, format='png')
    img3.seek(0)
    imagen_prediccion_k = base64.b64encode(img3.read()).decode() 

    
    return render_template('soluciones_g.html', data=resultadoNombre, datos=datos_ordenados, mes=mes, valor=valor, img1=imagen_prediccion, img2= imagen_datos, prediccion=prediccion, resultado_nombre=resultado_nombre_lista, departamento=departamento_seleccionado, municipio=municipio_seleccionado, nombre=nombre_seleccionado, moda=moda, media=media, mediana=mediana, desvEst=desvEst, estimacion_con_k=estimacion, img3=imagen_prediccion_k)

#Si está en la página principal, llama a la función
if __name__=='__main__':
    app.run(debug=True, port=5000)