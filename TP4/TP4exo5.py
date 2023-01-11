def verificateur():
    
    date = str(input("Veuillez donner la date : "))
    c = [int(i) for i in date]

    v = len(c) - 4

    jour = 10 * c[0] + c[1]
    mois = 10 * c[2] + c[3]
    print(f"Jour = {jour}")
    print(f"\nMois = {mois}")
    
    annee=0

    while v > 0 :

        annee += c[len(c) - v] * 10**(v-1)
        v-=1
        
    print(f"\nAnnee = {annee}\n")
    
    nbre_jours(annee, mois, jour)
    
    
    
def nbre_jours (annee,mois, jour):
    if mois == 4 or mois == 6 or mois == 9 or mois == 11:
        if jour <= 30:
            return print("valide")
        else: 
            return print("invalide")
    elif mois == 1 or mois == 3 or mois == 5 or mois ==7 or mois == 8 or mois == 10 or mois == 12:
        if jour <= 31:
            return print("valide")
        else: 
            return print("invalide")
    elif (mois == 2):
        if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0) and jour <=29:
            return print("valide")
        elif not (annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0)) and jour <=28:
            return print("valide4")
        else:
            return print("invalide")           
        
verificateur()





