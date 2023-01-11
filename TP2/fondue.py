BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400

nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))

noufromage = fromage * nbConvives / BASE
noueau = eau * nbConvives / BASE
nouail = ail * nbConvives / BASE
noupain = pain * nbConvives / BASE

print(f" - {noufromage} gr de fromage")
print(f" - {noueau} dl d'eau")
print(f" - {nouail} gousse(s) d'ail")
print(f" - {noupain} gr de pain")
