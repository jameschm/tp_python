
#avant 
x = input("Entrez x: ")
b = input("Entrez y: ")
#après

print("Avant permutation:")
print(f"{x} : x")
print(f"{b} : y")
temp = x
x = b
b = temp

print("Apres permutation:")
print(f"{x} : x")
print(f"{b} : y")