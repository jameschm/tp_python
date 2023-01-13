moyenne = 0
cc = 0
vn = []
for x in range(5):
    v = input("Veuillez entrer la note du module 1 et le coefficient correspondant : ")
    l = v.split(" ")
    note = int(l[0])
    coef = int(l[1])
    moyenne += note*coef
    vn.append(note)
    cc += coef
moyenne /= cc

if moyenne > 10:
    for i in vn:
        if i > 8:
            r = True
        else:
            r = False
else:
    r = False

if r:
    print(f"{moyenne} admis")
else:
    print(f"{moyenne} refuse")