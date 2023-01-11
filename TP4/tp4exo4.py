L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
def occu(L1):
    v=0
    y=0

    
    for i in L1:
        if L1.count(i) > v:
            v = L1.count(i)
            y = i
        else:
            continue
    print(f"Le nombre le plus frequent dans la liste est le : {y} ({v} x)")
    
#occu(L1)

def histogramme(liste):
    n = min(liste)
    j = 0
    r = 0
    while n <= max(liste)+1:
        v = 0
        for _ in range(len(liste)):
            if liste[_] == n:
                v += 1
            else:
                continue
        if v > j:
            j = v
            r = n             
            pass
        n += 1
    
    print(f"Le nombre le plus frequent dans la liste est le : {r} ({j} x)")

histogramme(L1)

      
        
              
        



""""
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
