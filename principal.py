# PROYECTO SPOTIFY 2023 - SPOTILAB
# Entrega 1: Explorador de datos

def separar_linea(linea):
    campos = []
    campo = ""
    dentro_comillas = False

    for caracter in linea:
        if caracter == '"':
            dentro_comillas = not dentro_comillas

        elif caracter == "," and dentro_comillas == False:
            campos.append(campo)
            campo = ""

        elif caracter != "\n" and caracter != "\r":
            campo = campo + caracter

    campos.append(campo)
    return campos


def cargar_datos(ruta, limite):
    datos = []

    with open(ruta, encoding="latin-1") as archivo:
        primera_linea = archivo.readline()
        encabezados = separar_linea(primera_linea)

        contador = 0

        for linea in archivo:
            if contador < limite:
                fila = separar_linea(linea)
                datos.append(fila)
                contador = contador + 1
            else:
                break

    return encabezados, datos


def buscar_registros(encabezados, datos, campo, termino):
    """Busca un término en una columna y devuelve las coincidencias."""
    coincidencias = []
    indice = encabezados.index(campo)

    for fila in datos:
        if termino.lower().replace(" ", "") in fila[indice].lower().replace(" ", ""):
            coincidencias.append(fila)

    return coincidencias


def calcular_estadisticas(encabezados, datos, campo):
    """Calcula máximo, mínimo y promedio de una columna numérica usando bucles y acumuladores."""
    indice = encabezados.index(campo)
    valores = []

    for fila in datos:
        try:
            # Limpiamos comas o espacios por si acaso en los números grandes
            valor_limpio = fila[indice].replace(",", "").strip()
            numero = float(valor_limpio)
            valores.append(numero)
        except ValueError:
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

    return maximo, minimo, promedio


def agrupar_por_categoria(encabezados, datos, campo):
    """Cuenta cuántas veces aparece cada valor de una columna."""
    indice = encabezados.index(campo)
    conteo = {}

    for fila in datos:
        valor = fila[indice].strip()

        if valor in conteo:
            conteo[valor] += 1
        else:
            conteo[valor] = 1

    conteo_ordenado = sorted(conteo.items(),key=lambda x: x[1],reverse=True)

    return conteo_ordenado


def mostrar_menu():
    print("\n=== EXPLORADOR DE SPOTIFY (SPOTILAB) ===")
    print("1. Buscar canciones o artistas")
    print("2. Estadísticas básicas (Streams)")
    print("3. Artistas más frecuentes (Agrupar por categoría)")
    print("0. Salir")

    return input("Elige una opción: ")


def main():
    # Carga el subconjunto de 50 filas requerido para la Entrega 1
    encabezados, datos = cargar_datos("spotify-2023.csv", 50)

    print("Se cargaron", len(datos), "registros correctamente.")

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            termino = input("Escribe el término que quieres buscar: ")
            print("Campos disponibles:", encabezados)
            campo = input("¿En qué campo quieres buscar? (ej. track_name, artist(s)_name): ")

            if campo not in encabezados:
                print("Ese campo no existe en los encabezados.")
                continue

            resultados = buscar_registros(encabezados, datos, campo, termino)

            for fila in resultados:
                print(" | ".join(fila))

            print("Se encontraron", len(resultados), "registros.")

        elif opcion == "2":
            campo = "streams"
            if campo not in encabezados:
                print(f"El campo '{campo}' no se encuentra en los encabezados.")
                continue

            resultado = calcular_estadisticas(encabezados, datos, campo)

            if resultado is None:
                print("No se encontraron valores numéricos válidos.")
            else:
                maximo, minimo, promedio = resultado
                print(f"\n--- Estadísticas para el campo: {campo} ---")
                print("Máximo:", maximo)
                print("Mínimo:", minimo)
                print("Promedio:", round(promedio, 2))

        elif opcion == "3":
            campo = "artist(s)_name"

            if campo not in encabezados:
                print("No se encontró la columna de artistas.")
                continue
            
            print("\n--- Artistas más frecuentes ---")
            
            conteo = agrupar_por_categoria(encabezados, datos, campo)
            
            for valor, frecuencia in conteo:
                print(f"{valor}: {frecuencia} registro(s)")

        elif opcion == "0":
            print("¡Hasta luego! Éxito con el video.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")
main()