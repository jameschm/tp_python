import gc


def gcd(a, b):
  
    if (a == 0):
        return b
    if (b == 0):
        return a
  
    if (a == b):
        return a
  
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)

print(gcd(a =int(input('choisir un nombre  ')),b =int(input('choisir un nombre  ')) ))