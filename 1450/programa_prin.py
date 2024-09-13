a,b=map(int,input().split())
ma=max(a,b)
mi=min(a,b)
lis=list(map(int,input().split()))
suma=0
for i in range(len(lis)):
    if(lis[i]>=mi and lis[i]<=ma):
        suma=suma+lis[i]
print(suma)