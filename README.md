# SPOTILAB 🎧

## Entrega 2: Explorador y analizador de datos de Spotify

## 1. Descripción del proyecto

SPOTILAB es un programa desarrollado en Python que permite explorar, consultar y analizar datos de canciones populares de Spotify durante 2023.

Funciona mediante un menú interactivo en consola y utiliza el dataset completo de Spotify 2023, compuesto por 953 registros.

El proyecto aplica conceptos de programación como funciones, estructuras de datos, manejo de archivos CSV y JSON, búsqueda, procesamiento de información y persistencia de datos entre sesiones.

## 2. Dataset utilizado

El programa utiliza el dataset **Spotify 2023**, almacenado en el archivo `spotify-2023.csv`.

Los datos se cargan utilizando el módulo `csv` de Python, sin recurrir a bibliotecas externas como Pandas.

Cada registro se almacena mediante un diccionario que relaciona los nombres de las columnas con sus respectivos valores.

Algunas de las columnas utilizadas son:

- `track_name`: nombre de la canción.
- `artist(s)_name`: nombre del artista o artistas.
- `released_year`: año de lanzamiento.
- `streams`: cantidad de reproducciones.
- `bpm`: pulsaciones por minuto.
- `danceability_%`: porcentaje de bailabilidad.
- `energy_%`: porcentaje de energía.

## 3. Funcionalidades

### 3.1. Buscar canciones o artistas

Permite buscar información dentro del dataset mediante un término ingresado por el usuario. Se pueden consultar coincidencias en los registros y visualizar los resultados encontrados.

### 3.2. Consultar estadísticas

Calcula estadísticas descriptivas de las columnas numéricas, como mínimo, máximo, promedio y otras medidas de resumen.

### 3.3. Buscar canciones por cantidad de streams

Permite filtrar canciones según su cantidad de reproducciones, utilizando un valor de streams como criterio de búsqueda.

### 3.4. Generar resumen general

Genera un resumen del dataset que incluye:

- Cantidad total de registros.
- Valores únicos de las columnas de texto.
- Valores mínimos y máximos de las columnas numéricas.

El resumen se genera automáticamente al iniciar el programa y también puede generarse desde el menú.

### 3.5. Consultar resultados guardados

Permite recuperar resultados de consultas realizadas anteriormente, almacenados en un archivo JSON para conservar la información entre ejecuciones.

### 3.6. Consultar resumen guardado

Permite acceder al resumen general generado y almacenado en formato JSON.

### 3.7. Consultar historial

Registra automáticamente las consultas realizadas por el usuario en un archivo CSV. Desde el menú se puede consultar el historial de operaciones anteriores.

## 4. Preguntas que busca responder el proyecto

- ¿Qué canciones o artistas aparecen en el dataset?
- ¿Cuántas canciones coinciden con un término de búsqueda?
- ¿Cuáles son las estadísticas principales de las variables numéricas?
- ¿Qué canciones superan o cumplen un determinado número de reproducciones?
- ¿Cuáles son los valores únicos de las columnas de texto?
- ¿Cuáles son los valores mínimos y máximos de las variables numéricas?
- ¿Qué consultas se han realizado anteriormente?

## 5. Conceptos de programación aplicados

- **Funciones propias:** organizan el código en tareas específicas, facilitando su reutilización y mantenimiento.
- **Condicionales y bucles:** permiten controlar el menú y procesar los registros del dataset.
- **Strings:** permiten manipular y comparar los valores de texto durante las búsquedas.
- **Listas:** almacenan los registros y los resultados de las consultas.
- **Diccionarios:** representan cada registro mediante pares de columnas y valores.
- **Conjuntos (sets):** permiten identificar valores únicos dentro del dataset.
- **Manejo de archivos CSV:** permite cargar los datos originales y registrar el historial de consultas.
- **Manejo de archivos JSON:** permite almacenar y recuperar resultados y resúmenes.
- **Modularización:** divide el programa en diferentes archivos Python para organizar las responsabilidades del código.

## 6. Estructura del proyecto

```text
SpotiLab/
├── principal.py
├── analisis.py
├── spotify-2023.csv
├── resultados.json
├── resumen.json
├── historial.csv
└── README.md
```

**Descripción de los archivos:**

- `principal.py`: contiene el menú interactivo y coordina la ejecución del programa.
- `analisis.py`: contiene las funciones encargadas de cargar, buscar, filtrar, analizar y guardar información.
- `spotify-2023.csv`: dataset original utilizado para el análisis.
- `resultados.json`: almacena los resultados de las consultas realizadas.
- `resumen.json`: almacena el resumen general del dataset.
- `historial.csv`: registra las consultas realizadas durante el uso del programa.
- `README.md`: contiene la documentación del proyecto.

Los archivos JSON y el historial CSV se generan durante la ejecución del programa, por lo que no necesariamente estarán presentes antes de utilizarlo.

## 7. Requisitos de ejecución

- Python 3 instalado.
- Los archivos `principal.py`, `analisis.py` y `spotify-2023.csv` ubicados en la misma carpeta.
- No se requieren bibliotecas externas. Se utilizan módulos de la biblioteca estándar de Python: `csv`, `json`, `os` y `datetime`.

## 8. Instrucciones de ejecución

1. Descargar o clonar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar el siguiente comando:

```bash
py principal.py
```

4. Seleccionar una opción del menú e ingresar los datos solicitados.
5. Para finalizar la ejecución, seleccionar la opción `0`.

