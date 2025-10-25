import requests
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_RAW_DIR= os.path.join(BASE_DIR, "data", "raw")

datasets = [
    {
        "url": "https://www.medellin.gov.co/es/wp-content/uploads/2025/04/ECV_2024.xlsx",
        "filename":"ECV_2024.xlsx"
    },
    {
        "url": "https://www.medellin.gov.co/es/wp-content/uploads/2025/04/Diccionario-de-datos-ECV-2024.xlsx",
        "filename":"diccionario.xlsx"
    },
]

def descargar_archivo(url,ruta_destino):

    try:
        response= requests.get(url)
        response.raise_for_status()
        with open(ruta_destino, "wb") as f:
            f.write(response.content)
        print(f"Archivo descargado correctamente:{ruta_destino}")
        return True
    except Exception as e:
        print(f"Error al descargar{ruta_destino}: {e}")
        return False
    
def main ():
    os.makedirs(DATA_RAW_DIR, exist_ok=True)

    resultados={}

    for i in datasets:
        ruta_destino= os.path.join(DATA_RAW_DIR, i["filename"])
        exito = descargar_archivo(i["url"], ruta_destino)
        resultados[i["filename"]]=exito

    print(f"\n Resumen de descarga:")
    for i, exito in resultados.items():
        estado = "OK" if exito else "FALLIDO"
        print(f"{i}:{estado}")
if __name__=="__main__":
    main()

