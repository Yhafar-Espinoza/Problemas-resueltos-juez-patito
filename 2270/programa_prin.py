n=int(input())
copia=n
kilo=0
me=0
cm=0
while(n>=100000):
    n=n-100000
    kilo=kilo+1
while(n>=100):
    n=n-100
    me=me+1
while(n>=1):
    n=n-1
    cm=cm+1
print(copia,"centímetros son",kilo,"km",me,"m",cm,"cm")