import pandas as pd

def cargar_csv(ruta, sep=";",header=0):
    df= pd.read_csv(ruta,sep=sep, header=header)
    df= df.astype(str).applymap(lambda x: x.strip())
    return df




