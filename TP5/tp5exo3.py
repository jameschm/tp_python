chaine = str(input("Entrez un mot ou une phrase : "))
chaine = ''.join(c for c in chaine if c.isalpha())
m = len(chaine)/2
m = int(m)
chaine = list(chaine)
print(chaine)
c1 = []
for _ in range(0, m):
    print(chaine[_])
    c1.append(chaine[_])
    del chaine[_]

print(chaine, c1)