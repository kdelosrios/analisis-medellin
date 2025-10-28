import re

def traducir_columnas (df_datos, df_diccionario2):
  
    # limpiar diccionario
    df_diccionario2["Codigo"] = df_diccionario2["Codigo"].astype(str).str.strip()
    df_diccionario2["Etiqueta"] = df_diccionario2["Etiqueta"].astype(str).str.strip()
    df_diccionario2["Valor"] = df_diccionario2["Valor"].astype(str).str.strip()

    # Solo aplicar strip a string en df_datos, mantener NaN
    df_datos= df_datos.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    columnas_traducidas=[]
   
    for i in df_datos.columns:     
        if i in df_diccionario2["Valor"].values:
            #Crear diccionario Código -> Etiqueta para esta columna
            filtro=df_diccionario2[df_diccionario2["Valor"]== i]
            
            if not filtro.empty:
                dict_trad = filtro.set_index("Codigo")["Etiqueta"].to_dict()

            #Mapear los códigos a etiquetas, mantener valores no encontrados
            df_datos[i] = df_datos[i].astype(str).map(dict_trad).fillna(df_datos[i])

    # Advertencia si hay columnas que no se pudieron traducir

    no_traducidas = set(df_datos.columns)- set(columnas_traducidas)
    if no_traducidas:
        print(f"Las siguientes columnas no tienen traducción: {no_traducidas}")
    
    return df_datos

def traducir_encabezados(df_datos, df_diccionario1):
    # Limpiar espacios
    df_diccionario1["Variable"] = df_diccionario1["Variable"].astype(str).str.strip()
    df_diccionario1["Etiqueta"] = df_diccionario1["Etiqueta"].astype(str).str.strip()

    # Crear diccionario Variable -> Etiqueta
    dicc_encabezados = dict(zip(df_diccionario1["Variable"], df_diccionario1["Etiqueta"]))

    # Traducir encabezados (renombrar columnas)
    df_datos = df_datos.rename(columns=dicc_encabezados)

    # Detectar columnas no traducidas
    columnas_originales = set(dicc_encabezados.keys())
    columnas_no_traducidas = [
        i for i in df_datos.columns
        if i not in dicc_encabezados.values() and i in columnas_originales
    ]

    if columnas_no_traducidas:
        print(f"Las siguientes columnas no tienen traducción: {columnas_no_traducidas}")
    else:
        print("Todas las columnas fueron traducidas correctamente")

    return df_datos


def limpiar_encabezados(df):
    def limpiar(nombre):
        nombre = str(nombre).strip()
        # Reemplazar múltiples espacios o tabulaciones
        nombre = re.sub(r'\s+', ' ', nombre)
        # Eliminar códigos tipo A.3, H.2A, etc.
        nombre = re.sub(r'^[A-Z]{1,2}\.\d+[A-Z]?\s*:\s*', '', nombre, flags=re.IGNORECASE)
        return nombre.strip()
    
    df.columns = [limpiar(col) for col in df.columns]
    return df

