import csv

with open("spotify-2023.csv", encoding="latin-1", newline="") as archivo:
    lector = csv.reader(archivo)
    spotify = list(lector)

print(spotify[0][0])
print(spotify[1][0])