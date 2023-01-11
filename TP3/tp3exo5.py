



while True:
    print("\n\nDebut du programme!!!\n\n")
    
    x=0
    y=0
    
    while True:
        heure_debut = int(input("Donnez l’heure de début de la location (un entier) : "))
        
        heure_fin = int(input("\nDonnez l’heure de fin de la location (un entier) : "))
        
        if heure_debut>=0 and heure_debut<=24 and heure_fin>=0 and heure_fin<=24:
            
            if heure_debut == heure_fin:
                print("Attention ! l’heure de fin est identique à l’heure de début.\n")
                continue
            else:
                
                if heure_debut>heure_fin:
                    print("Attention ! le début de la location est après la fin ...\n")
                    continue
                else:
                    break
        else:
            print("Les heures doivent être comprises entre 0 et 24 !\n")
            continue
        
        
    
    
    
    for _ in range(heure_debut, heure_fin):
        if _>=0 and _<7 or _>=17 and x<=24:
            x += 1
        else:
            y+=1

    temps_1 = x
    temps_2 = y

    total = temps_1*1 + temps_2*2

    if temps_1>0:
        print(f"\n{temps_1} heure(s) au tarif horaire de 1.0 euro(s)")
    else:
        pass
    if temps_2>0:
        print(f"\n{temps_2} heure(s) au tarif horaire de 2.0 euro(s)")
    else:
        pass


    print(f"\nLe montant total à payer est de {total} euro (s).")
    print("\n\n\n")
    print("Voulez-vous refaire cette opération ?")
    
  
           
    re = int(input("1 - yes\n2- no\n>: "))  
        
    if re==1:
        continue
    elif re == 2:
        print("Fin du programme!!!")
        break
    else:
        print("Fin du programme!!!")
        break
    
     


