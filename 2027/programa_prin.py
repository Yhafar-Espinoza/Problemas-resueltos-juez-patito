n=int(input())
suma=0
for i in range(1,n):
    if(n%i==0):
        suma=suma+i
if(suma==n):
    print("SI")
else:
    print("NO")