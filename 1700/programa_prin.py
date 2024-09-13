from collections import OrderedDict
while True:
    try:
        A=[]
        n=int(input())
        for i in range(1,n):
            a=(i*i)%n
            A.append(a)
        final = list(OrderedDict.fromkeys(A))
        vAux=[]
        ma=max(final)
        mi=min(final)
        for y in range(mi,ma+1):
            for y1 in range(len(final)):
                if(y==final[y1]):
                    vAux.append(final[y1])
        f=len(vAux)
        f=f-1
        for p in range(len(vAux)):
            if(p==f):
                print(vAux[p],end="")
            else:
                print(vAux[p],end=" ")
        print("")
    except EOFError:
        break