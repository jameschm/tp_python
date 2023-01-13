heure = int(input("Entrez le nombres d'heures : "))
sHoraire = int(input("Entrez le salaire horaire : "))

if heure<=160:
    print(f'salaire = {heure*sHoraire}')
elif heure>160 and heure<=200:
    heurev = heure - 160
    print(f"salaire = {heure*sHoraire + heurev*(sHoraire*1.25)} ")
else:
    heurev = heure - 200
    print(f"salaire = {160*sHoraire + 40*(sHoraire*1.25) + heurev*(sHoraire*1.50)}")