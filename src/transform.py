import pandas as pd


def rellenar_valores(df, columna, metodo="ffill"):
    df[columna]=df[columna].replace(r'^\s*$', pd.NA, regex=True)
    df[columna] = df[columna].replace('nan', pd.NA)

    df[columna]= df[columna].fillna(method=metodo)
    return df

def estandarizar_diccionario(dic2):
    dic2 = dic2.rename(columns={"Unnamed: 2": "Codigo"})
    return  dic2

