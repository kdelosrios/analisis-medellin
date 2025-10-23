from src.load_data import cargar_csv
from src.transform import estandarizar_diccionario
from src.translate_codes import traducir_columnas

#Cargar datos
df_datos= cargar_csv("data/crudos/ECV_2024.csv",sep=";")
df_diccionario1= cargar_csv("data/crudos/informacion _variable.csv", sep=";",header=2)
df_diccionario2= cargar_csv("data/crudos/valores_variables.csv",  sep=";", header=2)

# Procesar y traducir los datos
df_diccionario2= estandarizar_diccionario(df_diccionario2)
df_datos = traducir_columnas(df_datos, df_diccionario2)


