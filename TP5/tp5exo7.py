import os

fichier1 = os.path.isfile(r'TP5\f1.txt')
fichier2 = os.path.isfile(r'TP5\f2.txt')


if fichier1:
    o = os.path.getsize(r'TP5\f1.txt')
    print(f'fichier1 = {o}')
else:
    pass

if fichier2:
    p =  os.path.getsize(r'TP5\f2.txt')
    print(f'fichier2 = {p}')
else:
    pass

