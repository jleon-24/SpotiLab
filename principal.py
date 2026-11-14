
# ==================== IMPORTACIONES ====================

import analisis
from pprint import pprint


# ==================== PRESENTACIÓN DE RESULTADOS ====================

def mostrar_canciones(resultados):
    if len(resultados) == 0:
        print("No se encontraron canciones.")

    for cancion in resultados:
        nombre = cancion.get("track_name", "Sin nombre")
        artista = cancion.get("artist(s)_name", "Sin artista")

        print("Canción:", nombre, "| Artista:", artista)


def mostrar_menu():
    print("\n=== SPOTILAB: EXPLORADOR DE SPOTIFY ===")
    print("1. Buscar canciones o artistas")
    print("2. Consultar estadísticas")
    print("3. Buscar canciones por cantidad de streams")
    print("4. Generar resumen general")
    print("5. Consultar resultados guardados")
    print("6. Consultar resumen guardado")
    print("7. Consultar historial")
    print("0. Salir")

    return input("Elige una opción: ")


# ==================== PROGRAMA PRINCIPAL ====================

def main():

    # ---------- CARGA DEL DATASET ----------

    encabezados, datos = analisis.cargar_datos("spotify-2023.csv")

    print("Se cargaron", len(datos), "registros correctamente.")

    # ---------- GENERACIÓN AUTOMÁTICA DEL RESUMEN ----------

    resumen = analisis.generar_resumen(encabezados, datos)

    analisis.guardar_resumen(resumen)

    print("Resumen general generado y guardado correctamente.")

    # ---------- MENÚ PRINCIPAL ----------

    while True:
        opcion = mostrar_menu()

        # ---------- OPCIÓN 1: BÚSQUEDA ----------

        if opcion == "1":
            print("\nCampos disponibles:")
            print(encabezados)

            campo = input("¿En qué campo quieres buscar?: ")

            if campo not in encabezados:
                print("Ese campo no existe.")
                continue

            termino = input("Escribe el término que quieres buscar: ")

            resultados = analisis.buscar_registros(
                datos, campo, termino
            )

            mostrar_canciones(resultados)

            print("Se encontraron", len(resultados), "registros.")

            analisis.guardar_resultado(
                "Búsqueda",
                campo + ": " + termino,
                resultados
            )

            analisis.registrar_consulta(
                "Búsqueda",
                campo + ": " + termino,
                len(resultados)
            )

        # ---------- OPCIÓN 2: ESTADÍSTICAS ----------

        elif opcion == "2":
            print("\nCampos disponibles:")
            print(encabezados)

            campo = input("¿De qué campo quieres las estadísticas?: ")

            if campo not in encabezados:
                print("Ese campo no existe.")
                continue

            resultado = analisis.calcular_estadisticas(datos, campo)

            if resultado is None:
                print("No se encontraron valores numéricos válidos.")
                cantidad = 0
            else:
                print("\n--- ESTADÍSTICAS ---")
                print("Máximo:", resultado["maximo"])
                print("Mínimo:", resultado["minimo"])
                print("Promedio:", round(resultado["promedio"], 2))
                print("Cantidad de valores:", resultado["cantidad"])

                cantidad = resultado["cantidad"]

            analisis.guardar_resultado(
                "Estadísticas",
                campo,
                resultado
            )

            analisis.registrar_consulta(
                "Estadísticas",
                campo,
                cantidad
            )

        # ---------- OPCIÓN 3: BÚSQUEDA POR STREAMS ----------

        elif opcion == "3":
            try:
                valor = int(input("¿Más de cuántos streams?: "))
            except ValueError:
                print("Debes escribir un número entero.")
                continue

            resultados = analisis.canciones_por_streams(datos, valor)

            mostrar_canciones(resultados)

            print("Se encontraron", len(resultados), "canciones.")

            analisis.guardar_resultado(
                "Búsqueda por streams",
                "Más de " + str(valor),
                resultados
            )

            analisis.registrar_consulta(
                "Búsqueda por streams",
                "Más de " + str(valor),
                len(resultados)
            )

        # ---------- OPCIÓN 4: RESUMEN GENERAL ----------

        elif opcion == "4":
            resumen = analisis.generar_resumen(encabezados, datos)

            print("\n--- RESUMEN GENERAL ---")
            pprint(resumen)

            analisis.guardar_resumen(resumen)

            analisis.guardar_resultado(
                "Resumen general",
                "Dataset completo",
                resumen
            )

            analisis.registrar_consulta(
                "Resumen general",
                "Dataset completo",
                resumen["total_registros"]
            )

            print("Resumen guardado correctamente.")

        # ---------- OPCIÓN 5: RECUPERAR RESULTADOS ----------

        elif opcion == "5":
            resultados = analisis.cargar_resultados()

            if len(resultados) == 0:
                print("Todavía no hay resultados guardados.")
                continue

            print("\n--- RESULTADOS GUARDADOS ---")

            for i, resultado in enumerate(resultados):
                print(
                    i + 1,
                    "-",
                    resultado["tipo"],
                    "|",
                    resultado["consulta"],
                    "|",
                    resultado["fecha"]
                )

            try:
                seleccion = int(
                    input("¿Qué resultado quieres consultar?: ")
                )

                if seleccion < 1 or seleccion > len(resultados):
                    print("Número fuera del rango.")
                    continue

                print("\n--- RESULTADO RECUPERADO ---")
                pprint(resultados[seleccion - 1])

            except ValueError:
                print("Debes escribir un número.")

        # ---------- OPCIÓN 6: RECUPERAR RESUMEN ----------

        elif opcion == "6":
            resumen = analisis.cargar_resumen()

            if resumen is None:
                print("Todavía no existe un resumen guardado.")
            else:
                print("\n--- RESUMEN RECUPERADO ---")
                pprint(resumen)

        # ---------- OPCIÓN 7: HISTORIAL ----------

        elif opcion == "7":
            historial = analisis.cargar_historial()

            if len(historial) == 0:
                print("Todavía no hay consultas registradas.")
            else:
                print("\n--- HISTORIAL DE CONSULTAS ---")

                for consulta in historial:
                    print(
                        "Tipo:", consulta["tipo"],
                        "| Consulta:", consulta["consulta"],
                        "| Resultados:", consulta["cantidad_resultados"],
                        "| Fecha:", consulta["fecha_hora"]
                    )

        # ---------- SALIR ----------

        elif opcion == "0":
            print("Gracias por utilizar SpotiLab.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


# ==================== EJECUCIÓN ====================

main()
