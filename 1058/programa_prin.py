for i in range(int(input())):
    vAux=[]
    n=int(input())
    lista=list(map(int,input().split()[:n]))
    ma=max(lista)
    mi=min(lista)
    for r in range(mi,ma+1,+1):
        for o in range(len(lista)):
            if(r == lista[o]):
                vAux.append(r)
    m=len(vAux)
    for p in range(len(vAux)):
        if(p==(m-1)):
            print(vAux[p],end="")
        else:
            print(vAux[p],end=" ")
    print("")