lis=list(map(str,input().split()))
co=1
for y in range(len(lis)):
    a=len(lis[y])
    z=list(lis[y])
    a=a-1
    suma=""
    for i in range(a,-1,-1):
        suma=suma+z[i]
    if(lis[y]==suma):
        co=co+1
print(co)