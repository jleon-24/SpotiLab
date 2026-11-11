# SPOTILAB 🎧
## Entrega 2: Explorador y análisis de datos

## 1. Descripción del proyecto

SPOTILAB es un programa desarrollado en Python que permite explorar y analizar el dataset de canciones populares de Spotify de 2023. Funciona mediante un menú interactivo en consola y permite realizar búsquedas, consultar estadísticas, generar un resumen general y guardar los resultados de las consultas.

## 2. Dataset utilizado

El programa utiliza el dataset **Spotify 2023**, almacenado en el archivo `spotify-2023.csv`.

Python lee el archivo CSV y procesa sus registros. Los resultados de las consultas y el resumen se almacenan por separado en archivos JSON. El historial de consultas se registra en un archivo CSV independiente.

Algunas columnas del dataset son:

- `track_name`: nombre de la canción.
- `artist(s)_name`: nombre del artista o artistas.
- `released_year`: año de lanzamiento.
- `streams`: cantidad de reproducciones.
- `bpm`: pulsaciones por minuto.

## 3. Organización de los archivos

- **`principal.py`**: contiene el menú, solicita los datos al usuario, muestra los resultados y coordina las opciones del programa.
- **`analisis.py`**: contiene las funciones para cargar y analizar el dataset, generar el resumen, guardar y recuperar resultados JSON y administrar el historial.
- **`spotify-2023.csv`**: dataset original. No se modifica.
- **`resultados.json`**: se crea automáticamente para guardar los resultados de las consultas.
- **`resumen.json`**: se crea automáticamente para guardar el resumen general.
- **`historial.csv`**: se crea automáticamente para registrar las consultas realizadas.

Los archivos `resultados.json`, `resumen.json` y `historial.csv` se generan al utilizar las funcionalidades correspondientes. No es necesario crearlos manualmente.

## 4. Funcionalidades

### 4.1. Buscar canciones o artistas

Permite seleccionar una columna del dataset e ingresar un término de búsqueda. El programa muestra las coincidencias y guarda la consulta y sus resultados.

### 4.2. Consultar estadísticas

Permite seleccionar un campo y calcular su máximo, mínimo, promedio y cantidad de valores numéricos válidos.

### 4.3. Buscar canciones por cantidad de streams

Permite ingresar una cantidad de reproducciones y consultar las canciones que superan ese valor.

### 4.4. Generar resumen general

Calcula el total de registros, la cantidad de valores únicos de algunos campos de texto y los valores máximos y mínimos de campos numéricos. El resumen se guarda en `resumen.json`.

### 4.5. Consultar resultados guardados

Muestra las consultas almacenadas en `resultados.json` y permite seleccionar una para recuperar su información.

### 4.6. Consultar resumen guardado

Lee y muestra el resumen previamente almacenado en `resumen.json`.

### 4.7. Consultar historial

Muestra las consultas registradas en `historial.csv`, incluyendo el tipo de consulta, el término o criterio, la cantidad de resultados y la fecha y hora.

## 5. Persistencia de la información

El programa utiliza JSON para almacenar y recuperar resultados y el resumen general. Python realiza las operaciones de lectura y escritura mediante el módulo `json`.

El historial se guarda en formato CSV mediante el módulo `csv`.

El dataset original permanece en `spotify-2023.csv`. Los archivos JSON no reemplazan el dataset ni contienen la lógica de procesamiento.

## 6. Conceptos de programación aplicados

- **Funciones propias:** separan las tareas del programa.
- **Condicionales:** controlan las opciones del menú y validan entradas.
- **Bucles:** recorren los registros y mantienen activo el menú.
- **Listas y diccionarios:** organizan los datos y resultados.
- **Conjuntos:** permiten contar valores únicos.
- **Manejo de archivos:** permite leer el dataset y guardar información.
- **Manejo de excepciones:** permite controlar entradas no numéricas y valores inválidos.
- **Módulos:** permiten separar la interfaz del análisis de datos.
- **Persistencia:** permite conservar resultados entre ejecuciones.

## 7. Estructura del proyecto

```text
SpotiLab/
├── principal.py
├── analisis.py
├── spotify-2023.csv
├── resultados.json   (se genera al guardar consultas)
├── resumen.json      (se genera al guardar el resumen)
├── historial.csv     (se genera al registrar consultas)
└── README.md
```

## 8. Requisitos de ejecución

- Python 3 instalado.
- Los archivos `principal.py`, `analisis.py` y `spotify-2023.csv` ubicados en la misma carpeta.
- No se requieren instalaciones adicionales: se utilizan módulos de la biblioteca estándar de Python.

## 9. Instrucciones de ejecución

1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar el siguiente comando:

```powershell
py principal.py
```

3. Seleccionar una opción del menú e ingresar los datos solicitados.
