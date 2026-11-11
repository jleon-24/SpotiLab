# Funciones para cargar y analizar el dataset de Spotify.

import csv


def cargar_datos(ruta):
    """
    Lee el dataset completo usando csv.reader.
    Devuelve una lista de diccionarios: cada diccionario representa una canción.
    """
    datos = []

    with open(ruta, mode="r", encoding="latin-1", newline="") as archivo:
        lector = csv.reader(archivo)
        encabezados = next(lector)

        for fila in lector:
            if len(fila) == len(encabezados):
                cancion = {}

                for i in range(len(encabezados)):
                    cancion[encabezados[i]] = fila[i]

                datos.append(cancion)

    return encabezados, datos


def buscar_registros(datos, campo, termino):
    """Busca un término dentro de los valores de un campo."""
    coincidencias = []
    termino = termino.lower().replace(" ", "")

    for cancion in datos:
        valor = cancion[campo].lower().replace(" ", "")

        if termino in valor:
            coincidencias.append(cancion)

    return coincidencias


def calcular_estadisticas(datos, campo):
    """Calcula máximo, mínimo y promedio de un campo numérico."""
    valores = []

    for cancion in datos:
        try:
            numero = float(cancion[campo].replace(",", "").strip())
            valores.append(numero)
        except (ValueError, AttributeError):
            continue

    if len(valores) == 0:
        return None

    maximo = max(valores)
    minimo = min(valores)
    promedio = sum(valores) / len(valores)

    return {
        "maximo": maximo,
        "minimo": minimo,
        "promedio": promedio,
        "cantidad": len(valores)
    }


def canciones_por_streams(datos, valor):
    """Devuelve las canciones que superan el número de streams indicado."""
    resultados = []

    for cancion in datos:
        try:
            streams = int(cancion["streams"].replace(",", "").strip())

            if streams > valor:
                resultados.append(cancion)
        except (ValueError, AttributeError, KeyError):
            continue

    return resultados


def generar_resumen(encabezados, datos):
    """
    Calcula estadísticas generales del dataset.
    Usa conjuntos para contar valores únicos sin repetirlos.
    """
    resumen = {
        "total_registros": len(datos),
        "valores_unicos": {},
        "maximos_minimos": {}
    }

    # Campos de texto de interés: contamos valores distintos con conjuntos.
    campos_texto = ["track_name", "artist(s)_name", "key", "mode"]

    for campo in campos_texto:
        if campo in encabezados:
            valores = set()

            for cancion in datos:
                valor = cancion[campo].strip()

                if valor != "":
                    valores.add(valor)

            resumen["valores_unicos"][campo] = len(valores)

    # Campos numéricos: guardamos máximo y mínimo cuando hay datos válidos.
    campos_numericos = ["streams", "bpm", "released_year"]

    for campo in campos_numericos:
        if campo in encabezados:
            estadisticas = calcular_estadisticas(datos, campo)

            if estadisticas is not None:
                resumen["maximos_minimos"][campo] = {
                    "maximo": estadisticas["maximo"],
                    "minimo": estadisticas["minimo"]
                }

    return resumen
