def triNnombre(liste):
    for i in range(len(liste)):
        r = i
        for j in range(i+1, len(liste)):
            if liste[j] < liste[r]:
                r = j
        liste[i], liste[r] = liste[r], liste[i]
        print(liste)
    return liste

liste = [5, 2, 4, 8, 1, 3]
print(liste)
triNnombre(liste)