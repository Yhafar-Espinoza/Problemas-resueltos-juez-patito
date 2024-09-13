suma=0
a=0
for y in range(int(input())):
    n=int(input())
    if(n%7==0):
        suma=suma+n
        a=a+1
    if(a==2):
        print(suma)
        a=1
        suma=n
