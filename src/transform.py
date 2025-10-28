import pandas as pd


def rellenar_valores(df, columna, metodo="ffill"):
    df[columna]=df[columna].replace(r'^\s*$', pd.NA, regex=True)
    df[columna] = df[columna].replace('nan', pd.NA)

    df[columna]= df[columna].fillna(method=metodo)
    return df

def estandarizar_diccionario(dic2):
    dic2 = dic2.rename(columns={"Unnamed: 2": "Codigo"})
    return  dic2

def convertir_numeros(valor):
   
    if isinstance(valor, str):
        valor = valor.strip()          
        valor = valor.replace(',', '.') 
    try:
        return float(valor)
    except:
        return valor


def crear_tabla_ingresos(df, inicio, fin):
   '''
    Parámetros:
    - df: DataFrame original.
    - inicio: índice de la primera columna a seleccionar (0-based).
    - fin: índice de la última columna a seleccionar (exclusivo).
    '''
   tabla_filtrada = df.iloc[:, [3] + list(range(inicio, fin))]

   return tabla_filtrada


