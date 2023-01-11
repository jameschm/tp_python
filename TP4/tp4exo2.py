nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
print("\n")

notes = []

for _ in range (0, nombreEtudiants):
    v = float(input(f"Note etudiant {_} : "))
    while True:
        if 0<=v<=20 :
            break
        else:
            v = float(input(f"Note etudiant {_} : "))    
    notes.append(v)

moyenne = sum(notes)/nombreEtudiants
print(f"\nMoyenne de classe : {moyenne}")

print("\nNuméro de l’Etudiant | note | ecart a la moyenne\n")

for i in range(0, nombreEtudiants):
    print(f"{i} | {notes[i]} | {notes[i] - moyenne}")