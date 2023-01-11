nombre =  int(input("Veuilliez saisir le nombre de minutes : "))

jour = nombre // (60*24)
nombre -= jour * 60 * 24
heure = nombre // 60
nombre -= heure * 60
minutes = nombre

print(f"{jour}:{heure}:{minutes}")