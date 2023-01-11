from recurr import recur

n = int(input("Détermine la factorielle d’un entier n = "))



while True:
    metho = int(input("\n1 - for \n2 - while\n3 - recursif\n>: "))
    
    if metho == 1:
        v=1
        for x in range(1, n+1):
            v*=x 
        print(v) 
        break   

    elif metho == 2:
        
        f=1
        v=1
        while v<=n:
            f *=v
            v +=1
        print(f)
        break
    elif metho==3:
        print(recur(n))
        break
    else:
        print("\nVeilliez choisir la bonne methode!!!\n")
        


