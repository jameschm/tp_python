nombre = int(input("Entrez un nombre entier: "))

if nombre > 0:
    if nombre % 2 == 0:
        print("Le nombre est positif et paire")
    else:
        print("Le nombre est positif et impaire")
elif nombre < 0:
    if nombre % 2 == 0:
        print("Le nombre est negatif et paire")
    else:
        print("Le nombre est negatif et impaire")
else:
    print("Le nombre est zéro (et il est pair)")