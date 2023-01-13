import random
import string

T = [random.choice(string.ascii_letters) for _ in range(random.randint(0, 100))]
r = 0
for x in T:
    r += 1
print(r)
voyels= {'a','e','y','u','i','o'}
n = len(T)
nv = 0
for i in range(0,n):
    if(T[i] in voyels):
        nv = nv + 1
print("Le pourcentage de voyelles de la chaine 't' est : ", nv/r * 100 ,"%")

t = input("entrez la chaine : ")
resultat = []
for _ in t:
    if _ in T:
        resultat.append(_)
resultat = ''.join(c for c in resultat)
print(f"Il y a donc {len(resultat)} occurence(s) et les lettres présentes sont {resultat} ")

