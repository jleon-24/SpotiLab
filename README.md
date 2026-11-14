# SPOTILAB 🎧
### Explorador y analizador de datos de Spotify

## 1. Descripción del proyecto

SPOTILAB es un programa desarrollado en Python que permite explorar, consultar y analizar información de canciones populares de Spotify durante 2023.

El programa funciona mediante un menú interactivo en consola y utiliza el dataset Spotify 2023, compuesto por 953 registros.

Su propósito es facilitar la consulta de información musical, realizar análisis estadísticos, filtrar canciones según diferentes criterios y conservar los resultados de las consultas para acceder a ellos posteriormente.

El proyecto aplica conceptos fundamentales de programación, estructuras de datos, modularización, procesamiento de archivos y persistencia de información.

## 2. Dataset utilizado

El proyecto utiliza el dataset **Spotify 2023**, almacenado en el archivo `spotify-2023.csv`.

La información se carga mediante el módulo `csv` de Python, sin utilizar bibliotecas externas como Pandas.

Cada registro se representa mediante un diccionario que relaciona los nombres de las columnas con sus respectivos valores. Los registros se almacenan en una lista para facilitar su procesamiento y consulta.

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

Calcula estadísticas descriptivas de las columnas numéricas, incluyendo valores mínimos, máximos, promedios y otras medidas estadísticas implementadas en el programa.

### 3.3. Buscar canciones por cantidad de streams

Permite filtrar canciones según su cantidad de reproducciones, utilizando un valor de streams como criterio de búsqueda.

### 3.4. Generar resumen general

Genera un resumen del dataset que contiene:

- Cantidad total de registros.
- Valores únicos de las columnas de texto.
- Valores mínimos y máximos de las columnas numéricas.

El resumen se genera automáticamente al iniciar el programa y también puede generarse desde el menú. La información se almac
