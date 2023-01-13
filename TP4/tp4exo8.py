dico = {}
dico['firstname'], dico['name'], dico['promo'], dico['group'] = 'James', 'Schmitt', '2025', 'RT12'

print(dico)

print(f"votre nom est {dico['name']}, prénom est {dico['firstname']}, vous faites partie de la promo {dico['promo']} et votre groupe est {dico['group']}")

print(f"Les clés du dictionnaire sont :\n-{list(dico.keys())[0]}, \n-{list(dico.keys())[1]}, \n-{list(dico.keys())[2]}, \n-{list(dico.keys())[3z]}")