# SPOTILAB 🎧
## Entrega 1: Explorador de datos

**Integrantes del grupo:**
-
-
-
-

## 1. Descripción del proyecto

SPOTILAB es un programa desarrollado en Python que permite explorar y analizar datos de canciones populares de Spotify durante 2023. Funciona mediante un menú interactivo en consola y utiliza un subconjunto de 50 registros del dataset.

El proyecto aplica conceptos de programación como condicionales, bucles, strings y funciones para responder preguntas básicas sobre las canciones y sus artistas.

## 2. Dataset utilizado

El programa utiliza el dataset **Spotify 2023**, almacenado en el archivo `spotify-2023.csv`.

Se trabaja con los primeros 50 registros del archivo, además de los encabezados. Los datos se cargan utilizando `open()` y se procesan línea por línea, sin utilizar bibliotecas externas.

Algunas de las columnas utilizadas son:

- `track_name`: nombre de la canción.
- `artist(s)_name`: nombre del artista o artistas.
- `released_year`: año de lanzamiento.
- `streams`: cantidad de reproducciones.

## 3. Funcionalidades

### 3.1. Buscar registros

El usuario ingresa un término y selecciona la columna en la que desea buscar. El programa muestra los registros que contienen el término y la cantidad de coincidencias encontradas.

### 3.2. Estadísticas básicas

El programa calcula el máximo, el mínimo y el promedio de la columna numérica `streams`, utilizando bucles y variables acumuladoras.

### 3.3. Agrupar por categoría

El programa cuenta cuántos registros corresponden a cada valor de la columna `artist(s)_name` y muestra los resultados ordenados de mayor a menor frecuencia.

## 4. Preguntas que busca responder el proyecto

- ¿Qué canciones o artistas aparecen en los registros del dataset?
- ¿Cuántos registros contienen un término específico?
- ¿Cuál es el máximo, el mínimo y el promedio de reproducciones de las canciones analizadas?
- ¿Qué artistas aparecen con mayor frecuencia en el subconjunto de datos?

## 5. Conceptos de programación aplicados

- **Condicionales:** permiten ejecutar acciones según la opción seleccionada en el menú.
- **Bucles:** permiten recorrer las filas del archivo y mantener activo el menú interactivo.
- **Strings:** permiten procesar las líneas del archivo y buscar términos en los datos.
- **Funciones propias:** organizan el programa en tareas específicas con parámetros y valores de retorno.
- **Listas y diccionarios:** permiten almacenar registros y contar frecuencias por categoría.
- **Variables acumuladoras:** se utilizan para calcular estadísticas numéricas.

## 6. Estructura del proyecto

```text
proyecto programacion/
├── principal.py
├── spotify-2023.csv
└── README.md
```

## 7. Requisitos de ejecución

- Python 3 instalado.
- Los archivos `principal.py` y `spotify-2023.csv` ubicados en la misma carpeta.
- No se requieren bibliotecas externas.

## 8. Instrucciones de ejecución

1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar el siguiente comando:

```powershell
py principal.py
```

3. Seleccionar una opción del menú e ingresar los datos solicitados.

## 9. Producto creativo

Como parte de la presentación en video, el grupo mostrará un póster digital con el nombre SPOTILAB, el dataset utilizado y las preguntas que busca responder el proyecto.