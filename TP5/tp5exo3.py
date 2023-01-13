chaine = str(input("Entrez un mot ou une phrase : "))
chaine = ''.join(c for c in chaine if c.isalpha())
m = len(chaine)/2
m = int(m)
chaine = chaine
c1 = []

for _ in range(0, m):
    c1.append(chaine[_])
    del chaine[_]

chaine.reverse()

if chaine == c1:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome !")
