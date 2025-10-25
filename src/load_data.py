import pandas as pd

def load_excel(ruta, sheetname=0,skiprows=None,usecols=None):
    df= pd.read_excel(ruta,sheet_name=sheetname,dtype=str, skiprows=skiprows, usecols=usecols )
    df= df.astype(str).apply(lambda col: col.str.strip())
    return df

def load_excel_sheets(ruta, sheet_names= None,sheet_params=None):

    if sheet_names is None:
        xls =pd.ExcelFile(ruta)
        sheet_names= xls.sheet_names
    
    dfs={}
    for sheet in sheet_names:
        params= sheet_params.get(sheet, {}) if sheet_params else {}
        df=pd.read_excel(ruta,sheet_name=sheet,dtype=str, **params)
        df= df.astype(str).apply(lambda col: col.str.strip())
        dfs[sheet] = df
    
    return dfs

