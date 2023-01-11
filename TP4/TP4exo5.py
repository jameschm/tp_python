while True:
        
    date = str(input("Veuillez donner la date : "))
    c = []
    c = [int(i) for i in date]

    v = len(c) - 4

    jour = 10 * c[0] + c[1]
    mois = 10 * c[2] + c[3]
    print(jour)
    annee=0

    while v > 0 :

        annee += c[len(c) - v] * 10**(v-1)
        v-=1
    
    if jour >=1 and jour <=31:
        if mois >=1 and mois<=12:
            if(annee%4==0 and annee%100!=0 or annee%400==0):
                print("L'année est valide!!!")
            else:
                print("invalide")
                continue
        else:
            print("invalide")
            continue
    else:
        print("invalide")
        continue    








