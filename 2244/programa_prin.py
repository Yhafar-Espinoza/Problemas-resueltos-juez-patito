def primos(UVW):
    Z=[]
    for i in range(len(UVW)):
        contador=0
        x=UVW[i]
        for l in range(1,x+1):
            if(x%l==0):
                contador=contador+1
        if(contador==2):
            Z.append(x)
    return(Z)
m=int(input())
U=list(map(int,input().split()))
n=int(input())
V=list(map(int,input().split()))
o=int(input())
W=list(map(int,input().split()))
Z=[]
res=primos(U)
for i in range(len(res)):
    Z.append(res[i])
res=primos(V)
for i in range(len(res)):
    Z.append(res[i])
res=primos(W)
for i in range(len(res)):
    Z.append(res[i])
ma=max(Z)
mi=min(Z)
vAux=[]
for y in range(ma,mi-1,-1):
    for i1 in range(len(Z)):
        if(y==Z[i1]):
            vAux.append(Z[i1])
s=len(vAux)
copia=s
s=s-1
print(copia)
for fin in range(len(vAux)):
    if(fin==s):
        print(vAux[fin],end="")
    else:
        print(vAux[fin],end=" ")