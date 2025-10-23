def traducir_columnas (df_datos, df_diccionario2):
    df_diccionario2["Codigo"] = df_diccionario2["Codigo"].astype(str).str.strip()
    df_diccionario2["Etiqueta"] = df_diccionario2["Etiqueta"].astype(str).str.strip()
    df_diccionario2["Valor"] = df_diccionario2["Valor"].astype(str).str.strip()


    df_datos= df_datos.astype(str).applymap(lambda x: x.strip())
   
    for i in df_datos.columns:     
        if i in df_diccionario2["Valor"].values:
            filtro=df_diccionario2[df_diccionario2["Valor"]==i]
            dict_trad = filtro.set_index("Codigo")["Etiqueta"].to_dict()
            df_datos[i] = df_datos[i].map(dict_trad).fillna(df_datos[i])

    return df_datos

