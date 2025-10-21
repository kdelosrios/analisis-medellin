
def rellenar_valores(df, columna, metodo="ffill"):
    df[columna]=df[columna].fillna(method=metodo)
    return df

def estandarizar_diccionario(dic2):
    # Estandarizar nombres de las columnas para traducir valores
    dic2 = dic2.rename(columns={"Unnamed: 2": "Codigo"})
    return  dic2

