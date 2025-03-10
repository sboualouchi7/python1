nombre = int(input("Entrez un nombre :) "))
longueur = int(input("Entrez la longueur de la liste :) "))

m = []

for i in range(1, longueur + 1):
    m.append(nombre * i)

print(m)