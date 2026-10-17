
# PROYECTO SPOTIFY 2023
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
    """Busca un término en una columna y devuelve coincidencias."""
    coincidencias = []
    indice = encabezados.index(campo)

    print("Término recibido:", repr(termino))
    print("Campo elegido:", repr(campo))
    print("Primera fila de esa columna:", repr(datos[0][indice]))

    for fila in datos:
        if termino.lower() in fila[indice].lower():
            coincidencias.append(fila)

    return coincidencias


def calcular_estadisticas(encabezados, datos, campo):
    """Calcula máximo, mínimo y promedio de una columna numérica."""
    indice = encabezados.index(campo)
    valores = []

    for fila in datos:
        try:
            numero = int(fila[indice])
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


def mostrar_menu():
    print("\n=== EXPLORADOR DE SPOTIFY ===")
    print("1. Buscar canciones o artistas")
    print("2. Estadísticas de reproducciones")
    print("0. Salir")

    return input("Elige una opción: ")


def main():
    encabezados, datos = cargar_datos("spotify-2023.csv", 50)

    print("Se cargaron", len(datos), "registros.")

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            termino = input("Escribe el término que quieres buscar: ")

            print("Campos disponibles:", encabezados)
            campo = input("¿En qué campo quieres buscar? ")

            if campo not in encabezados:
                print("Ese campo no existe.")
                continue

            resultados = buscar_registros(
                encabezados, datos, campo, termino
            )

            for fila in resultados:
                print(" | ".join(fila))

            print("Se encontraron", len(resultados), "registros.")

        elif opcion == "2":
            campo = "streams"

            resultado = calcular_estadisticas(
                encabezados, datos, campo
            )

            if resultado is None:
                print("No se encontraron valores numéricos.")
            else:
                maximo, minimo, promedio = resultado
                print("Campo: streams")
                print("Máximo:", maximo)
                print("Mínimo:", minimo)
                print("Promedio:", round(promedio, 2))

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

main() 