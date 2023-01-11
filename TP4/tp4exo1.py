x = float(input("Vous cherchez la table de multiplication de quel nombre ? "))
result = 0
table=[]

for _ in range(0, 10):
    result = _*x
    print(f"{x} * {_} = {round(result, 1)}")
    table.append(result)
    
    
while True:
    v  = int(input(f"Quelle multiplication de la table de {x} voulez vous afficher? entre 0 et 9? "))
    
    if v>=0 and v<=9:
        print(f"{x} * {v} = {round(table[v], 1)}")
        p = int(input("1 - continuer\n2 - stop\n>: "))
        
        if p == 1:
            continue
        else:
            print("\nFin du programme!!!")
            break
    else:
        print("Veuilliez reessayer!!!")
        continue