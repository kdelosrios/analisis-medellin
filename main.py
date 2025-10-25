import pandas as pd
from scripts import download_data
download_data.main()


from src.load_data import load_excel, load_excel_sheets
from src.transform import estandarizar_diccionario, rellenar_valores
from src.translate_codes import traducir_columnas, traducir_encabezados

#Cargar datos
df_datos= load_excel("data/raw/ECV_2024.xlsx", sheetname=0)
diccionario = load_excel_sheets(
    "data/raw/diccionario.xlsx",
    sheet_names=["Etiquetas Vbles", "Valores Vbles"],
    sheet_params={
        "Etiquetas Vbles": {"skiprows": 2}, 
        "Valores Vbles": {"skiprows": 2}  
    }
)

df_diccionario1 = diccionario["Etiquetas Vbles"]
df_diccionario2 = diccionario["Valores Vbles"]

# Procesar y traducir los datos

# Rellenar valores faltantes en columna "Valor"
df_diccionario2= estandarizar_diccionario(df_diccionario2)
df_diccionario2 = rellenar_valores(df_diccionario2, "Valor")
assert df_diccionario2['Valor'].isna().sum() == 0, "Quedan valores vacíos en 'Valor'"

# Traducir filas 
df_datos = traducir_columnas(df_datos, df_diccionario2)
df_datos= traducir_encabezados(df_datos, df_diccionario1)


