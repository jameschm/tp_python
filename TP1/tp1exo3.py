jour = int(input("Veuilliez entrer le jour : "))
heure = int(input("Veuillez entrer l'heure : "))
minute = int(input("Veuillez entrer les minutes : "))

temps = (jour * 60 * 24) + (heure * 60) + minute

print(temps)
