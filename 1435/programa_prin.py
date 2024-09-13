# Dado un número entero N averiguar la cantidad de dígitos que tiene esté número, y además determinar cual es su k-esimo dígito.

# Por ejemplo para N=18421
#  y k=3
# ,  el número tiene 5
#  dígitos y el tercer dígito es 4. 


import math
a, b=map(int,input().split())
dig=int(math.log10(a))+1
pot=10**(dig - b)
a=a//pot
digi = a%10
print(dig, digi)