""""
N = int(input("Saisir le nombre N : "))



somm = 0
    
for x in range(1, N+1,1):
    somm += x

print(somm)
"""
"""
while True:
    x = int(input("entrez un nombre : "))
    
    if x == 100:
        print("C'est bon")
        break
    else:
        continue
"""
""""
x=0
y=0
z=0
c=0
v=0
while v<10:

    x = int(input("entrez un valeur entre 0 et 20 : "))
    
    if x >= 0 and x <= 20:
        
        if x < 10:
            y += 1
        elif x >= 10 and x < 15:
            z+= 1
        else:
            c+= 1
        
        v += 1
    else:
        continue
            

    
print(f"Le nombre de valeurs inférieur strictement à 10 = {y}")
print(f"Le nombre de valeurs inférieur strictement à 10 = {z}")
print(f"Le nombre de valeurs supérieur ou égale à 15 = {c}")
 """           
 
vuser = int(input("donner une valeur : "))
s = 0
n=0

while s < vuser:
    
    n += 1
    s = n*(n+1)/2
    
print(f"Donc la somme de {n} entier conséutifs donne {s} qui est bien superieur a {vuser}")

    
    
        
       

    