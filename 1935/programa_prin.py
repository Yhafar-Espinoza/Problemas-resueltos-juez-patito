def mini(mi,lis):
    for i in range(len(lis)):
        if(mi==lis[i]):
            a=i
            return(a)
n=int(input())
lis=list(map(int,input().split()))
mi=min(lis)
minimo=mini(mi,lis)
print(minimo)       
