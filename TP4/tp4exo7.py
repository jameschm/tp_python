
#1

binome = ('james', 'thibaud')

print(f"L'etudiant {binome[0]} est en binome avec l'etudiant {binome[1]}")

#2

binome2 = list(binome)

binome2[1] = str(input("entrez nouveau binome : "))

binome = tuple(binome2)

print(f"L'etudiant {binome[0]} est en binome avec l'etudiant {binome[1]}")

#3
#impossible

#4

trinome = binome + ('lilian', )

print(f"L'etudiant {trinome[0]} est en trinome avec l'etudiant {trinome[1]} et avec l'etudiant {trinome[2]} ")
