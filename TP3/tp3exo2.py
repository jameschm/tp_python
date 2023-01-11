from time import sleep


while True:
    n = int(input("Entrez un nombre entier positif : "))
    if n < 0:
        continue
    else:
        break

""""
y = 0
for x in range(0, n+1):
    y = n - x
    sleep(0.2)
    print(y)
"""


x = 0
while x != n+1:
    y = n - x
    x+=1
    sleep(0.2)
    print(y)



