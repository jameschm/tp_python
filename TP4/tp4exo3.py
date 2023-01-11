nMax = 10

v1 = []
v2 = []

while True:
    
    produit_scalaire = 0.0
    n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ? "))
    m = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ? "))

    if n >=1 and n<=nMax and m >=1 and m<=nMax :
        print("\nSaisie du premier vecteur : ")
        
        for _ in range(0, n):
            v = float(input(f"v1[{_}] = "))
            v1.append(v)
        
        print("\nSaisie du second vecteur : ")
        
        for i in range(0, m):
            x = float(input(f"v2[{i}] = "))
            v2.append(x)
            
        if n == m :
            for r in range(0, n):
                produit_scalaire += v1[r] * v2[r] 
                r+=1 
        else:
            v = n- m
            if v < 0:
                for r in range(0, n):
                    produit_scalaire += v1[r] * v2[r] 
                    r+=1 
            else:
                for r in range(0, n):
                    produit_scalaire += v1[r] * v2[r] 
                    r+=1 
                
                
            
        
            
        print(f"\nLe produit scalaire de v1 par v2 vaut {produit_scalaire}")
        break
       
    else:
        continue
        
        
