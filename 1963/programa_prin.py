n=int(input())
lis=list(map(int,input().split()[:n]))
ma=max(lis)
copia=[]
for i in range(len(lis)):
    if(lis[i]!=ma):
        copia.append(lis[i])
mas=max(copia)
print(mas)