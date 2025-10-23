
Análisis de Datos Públicos de Medellín

1. Descripción:
Este proyecto realiza un análisis exploratorio de datos (EDA) sobre bases de datos públicas de la ciudad de Medellín.
Su objetivo es limpiar, transformar y visualizar la información para descubrir patrones, tendencias y posibles insights relevantes.
El proyecto está preparado para evolucionar hacia la automatización de la carga y preparación de datos, y su conexión con Power BI para visualizaciones profesionales.

2. Estructura del proyecto

analisis-datos-medellin/
├─ data/
│   ├─ raw/           # Archivos CSV originales
│   └─ processed/     # Datos limpios y transformados
├─ notebooks/         # Jupyter notebooks exploratorios
├─ src/               # Scripts Python: carga, transformación y traducción
├─ sql/               # Scripts de creación de tablas y queries (pendiente)
├─ powerbi/           # Archivos PBIX para visualización final
├─ docs/              # Documentación y apuntes técnicos
├─ logs/              # Registros de ejecución y errores
├─ README.md          # Documentación del proyecto
├─ requirements.txt   # Librerías Python necesarias
└─ .gitignore         # Archivos/carpetas ignoradas por Git


3. Tecnologías utilizadas

Python – Limpieza, transformación y preparación de datos
Jupyter Notebook – Exploración inicial de datos
Pandas y NumPy – Manipulación y análisis de datos
MySQL – Almacenamiento y consulta de datos (futuro)
Power BI – Visualización de datos interactiva 
Git & GitHub – Control de versiones y portafolio

4. Cómo usar este proyecto

4.1. Clona el repositorio:
    git clone https://github.com/kdelosrios/analisis-medellin
    cd analisis-datos-medellin

4.2. Activa el entorno virtual e instala las dependencias:
    pip install -r requirements.txt

4.3. Abre el notebook exploratorio:
    jupyter notebook notebooks/analisis.ipynb
Los datos procesados pueden luego cargarse en Power BI para generar los dashboards finales.

5. Dataset

Datos públicos de  la ciudad Medellín en formato CSV, acompañados de diccionarios que permiten traducir los códigos a valores legibles.

5.1. Ubicación:

    data/raw/ → datos originales
    data/processed/ → datos limpios y transformados

6. Objetivos del análisis

Inspección inicial de los datasets
Limpieza y transformación de datos (valores nulos, duplicados, estandarización)
Traducción de códigos a etiquetas legibles usando diccionarios
Preparación de datos lista para visualización en Power BI
Generación de insights para la toma de decisiones

Autor

Viviana De Los Ríos – Especialización en desarrollo de software.