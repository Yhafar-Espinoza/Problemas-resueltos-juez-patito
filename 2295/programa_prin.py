for i in range(int(input())):   
    n=input()
    ñ=len(n)
    a=list(n)
    Z=[]
    limite=3
    co=1
    if(ñ!=2):
        while(co<=limite):
            z=max(a)
            Z.append(z)
            a.remove(z)
            co=co+1
        ma=int(max(Z))
        mi=int(min(Z))
        vAux=[]
        for y in range(mi,ma+1):
            x=str(y)
            for y1 in range(len(Z)):
                if(x==Z[y1]):
                    vAux.append(Z[y1])
        limite=len(vAux)
        limite=limite-1
        for fin in range(len(vAux)):
            if(limite==fin):
                print(vAux[fin],end="")
            else:
                print(vAux[fin],end=" ")
        print("")
        

