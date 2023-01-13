somme = int(input("Entrez la somme : "))
rr = somme
cent  = somme//100
somme -= 100 * cent
cinquante  = somme//50
somme -= 50 * cinquante
dix  = somme//10
somme -= 10 * dix
deux  = somme//2
somme -= 2 * deux
un  = somme//1
somme -= 1 * un

print(f"{rr} euros, c’est donc {cent} billets de 100, {cinquante} de 50, {dix} de 10, {deux} pièces de 2 et {un} pièce 1. ")

