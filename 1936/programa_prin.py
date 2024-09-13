n=int(input())
lis=list(map(int,input().split()))
vAux=[]
ma=max(lis)
mi=min(lis)
for i in range(mi,ma+1):
    for f in range(len(lis)):
        if(lis[f]==i):
            vAux.append(lis[f])
li=len(vAux)
li=li-1
for i1 in range(len(vAux)):
    if(i1==li):
        print(vAux[i1],end="")
    else:
        print(vAux[i1],end=" ")