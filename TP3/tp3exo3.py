from random import randint

x = randint(0, 100)
y = -1
count = 0
while y != x:
    y = int(input("Devines le nombre : "))
    count+=1
    if y < x :
        print("plus grand")
    elif y > x:
        print("plus petit")
    else:
        print("bravo!")
        print(f"Il t'a fallu {count} essai(s)")