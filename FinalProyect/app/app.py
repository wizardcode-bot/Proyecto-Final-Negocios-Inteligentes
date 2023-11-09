import pandas as pd

# Especifica la ruta del archivo Excel
ruta = 'C:\\Users\\HOME\\Downloads\\finalPoyectNegocios\\archivos\\DatosCompletos.xlsx'
df = pd.read_excel(ruta, sheet_name='Brillo Solar')

# Ruta del archivo CSV de salida
csv_file = "PromClimat.csv"

# Guardar los datos en un archivo CSV
df.to_csv(csv_file, index=False)

# Muestra los nombres de las columnas en el DataFrame
print("Nombres de las columnas en el DataFrame:")
print(df.columns)

# Muestra los departamentos únicos en la columna "DEPARTAMENTO"
departamentos_unicos = df['DEPARTAMENTO'].unique()
print("\nDepartamentos únicos en la columna 'DEPARTAMENTO':")
for departamento in departamentos_unicos:
    print(departamento)

# Solicita al usuario que ingrese el nombre del departamento a filtrar
departamento_seleccionado = input("Ingresa el nombre del departamento que deseas filtrar: ")

# Filtra los datos por el departamento seleccionado
departamento_df = df[df['DEPARTAMENTO'] == departamento_seleccionado]

# Define las columnas de meses
columnas_meses = ['ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN', 'JUL', 'AGO', 'SEP', 'OCT', 'NOV', 'DIC']

# Initialize an empty DataFrame to store the sorted data
sorted_department_df = pd.DataFrame()

# Sort each month's column individually
for column in departamento_df:
    sorted_column = departamento_df.sort_values(by=column)
    sorted_department_df[column] = sorted_column[column]


# Print the sorted data for all months
print(f"Datos ordenados en orden ascendente para todos los meses en {departamento_seleccionado}:")
print(sorted_department_df)
