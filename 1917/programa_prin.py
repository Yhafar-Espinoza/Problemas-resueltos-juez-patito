suma=0
l=3
for i in range(1,int(input())+1):
    n=int(input())
    if(i<=l):
        suma=suma+n
        if(i==l):
            print(suma)
    else:
        suma=n
        l=l+3

