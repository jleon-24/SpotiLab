import csv

with open("spotify-2023.csv", encoding="utf-8-sig", newline="") as archivo:
    lector = csv.reader(archivo)
    spotify = list(lector)

print(spotify[0][0])

