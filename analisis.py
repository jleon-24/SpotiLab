# ==================== IMPORTACIONES ====================

import csv
import json
import os
from datetime import datetime


# ==================== CARGA DEL DATASET ====================

def cargar_datos(ruta):
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


# ==================== BÚSQUEDA ====================

def buscar_registros(datos, campo, termino):
    coincidencias = []
    termino = termino.lower().replace(" ", "")

    for cancion in datos:
        valor = cancion[campo].lower().replace(" ", "")

        if termino in valor:
            coincidencias.append(cancion)

    return coincidencias


# ==================== ESTADÍSTICAS ====================

def calcular_estadisticas(datos, campo):
    valores = []

    for cancion in datos:
        try:
            numero = float(cancion[campo].replace(",", "").strip())
            valores.append(numero)
        except (ValueError, AttributeError, KeyError):
            continue

    if len(valores) == 0:
        return None

    maximo = valores[0]
    minimo = valores[0]
    suma = 0

    for numero in valores:
        if numero > maximo:
            maximo = numero

        if numero < minimo:
            minimo = numero

        suma += numero

    promedio = suma / len(valores)

    return {
        "maximo": maximo,
        "minimo": minimo,
        "promedio": promedio,
        "cantidad": len(valores)
    }


# ==================== CANCIONES POR STREAMS ====================

def canciones_por_streams(datos, valor):
    resultados = []

    for cancion in datos:
        try:
            streams = int(cancion["streams"].replace(",", "").strip())

            if streams > valor:
                resultados.append(cancion)

        except (ValueError, AttributeError, KeyError):
            continue

    return resultados


# ==================== RESUMEN GENERAL ====================

def generar_resumen(encabezados, datos):
    resumen = {
        "total_registros": len(datos),
        "valores_unicos": {},
        "maximos_minimos": {}
    }

    campos_texto = ["track_name", "artist(s)_name", "key", "mode"]

    for campo in campos_texto:
        if campo in encabezados:
            valores = set()

            for cancion in datos:
                valor = cancion[campo].strip()

                if valor != "":
                    valores.add(valor)

            resumen["valores_unicos"][campo] = len(valores)

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


# ==================== GUARDAR Y RECUPERAR RESULTADOS JSON ====================

def cargar_resultados(ruta="resultados.json"):
    if not os.path.exists(ruta):
        return []

    with open(ruta, mode="r", encoding="utf-8") as archivo:
        resultados = json.load(archivo)

    return resultados


def guardar_resultado(tipo, consulta, resultado, ruta="resultados.json"):
    resultados = cargar_resultados(ruta)

    nuevo_resultado = {
        "tipo": tipo,
        "consulta": consulta,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "resultado": resultado
    }

    resultados.append(nuevo_resultado)

    with open(ruta, mode="w", encoding="utf-8") as archivo:
        json.dump(resultados, archivo, indent=4, ensure_ascii=False)


# ==================== GUARDAR Y RECUPERAR RESUMEN JSON ====================

def guardar_resumen(resumen, ruta="resumen.json"):
    with open(ruta, mode="w", encoding="utf-8") as archivo:
        json.dump(resumen, archivo, indent=4, ensure_ascii=False)


def cargar_resumen(ruta="resumen.json"):
    if not os.path.exists(ruta):
        return None

    with open(ruta, mode="r", encoding="utf-8") as archivo:
        resumen = json.load(archivo)

    return resumen


# ==================== HISTORIAL DE CONSULTAS CSV ====================

def registrar_consulta(tipo, consulta, cantidad, ruta="historial.csv"):
    archivo_nuevo = not os.path.exists(ruta) or os.path.getsize(ruta) == 0

    with open(ruta, mode="a", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)

        if archivo_nuevo:
            escritor.writerow([
                "tipo",
                "consulta",
                "cantidad_resultados",
                "fecha_hora"
            ])

        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        escritor.writerow([
            tipo,
            consulta,
            cantidad,
            fecha_hora
        ])


def cargar_historial(ruta="historial.csv"):
    if not os.path.exists(ruta):
        return []

    with open(ruta, mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        historial = []

        for fila in lector:
            historial.append(fila)

    return historial
