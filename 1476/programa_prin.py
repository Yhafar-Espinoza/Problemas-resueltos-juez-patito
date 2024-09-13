N,M=map(int,input().split())
lisa=list(map(int,input().split()[:N]))
lisb=list(map(int,input().split()[:M]))
C=lisa
for i in range(len(lisb)):
    C.append(lisb[i])
ma=max(C)
mi=min(C)
vAux=[]
for y in range(mi,ma+1,1):
    for i1 in range(len(C)):
        if(y==C[i1]):
            vAux.append(C[i1])
for y1 in range(len(vAux)):
    print(vAux[y1])

    
