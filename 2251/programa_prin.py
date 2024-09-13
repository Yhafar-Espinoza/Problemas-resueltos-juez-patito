while True:
    try:
        x,t,z1=map(int,input().split())
        if(x%2==0):
            a=str(x)
            x1=list(a)
            z=len(x1)
            z=z-1
            t=z-t
            su=""
            si=""
            for i1 in range(0,t+1):
                si=si+x1[i1]
            for i in range(t+1,z+1,+1):
                su=su+x1[i]
            su=list(su)
            mi=len(su)
            mi=mi-1
            for i3 in range(1,z1+1):
                aux=su[mi]
                for p in range(mi,-1,-1):
                    if(p==0):
                        su[p]=aux
                    else:
                        su[p]=su[p-1]
            fin=""
            for f in range(len(su)):
                fin=fin+su[f]
            resultado=si+fin
            print(resultado)
        else:
            a=str(x)
            x1=list(a)
            z=len(x1)
            z=z-1
            t=z-t
            su=""
            si=""
            for i1 in range(0,t+1):
                si=si+x1[i1]
            for i in range(t+1,z+1,+1):
                su=su+x1[i]
            su=list(su)
            mi=len(su)
            mi=mi-1
            for i3 in range(1,z1+1):
                aux=su[0]
                for p in range(len(su)):
                    if(p==mi):
                        su[p]=aux
                    else:
                        su[p]=su[p+1]
            fin=""
            for f in range(len(su)):
                fin=fin+su[f]
            resultado=si+fin
            print(resultado)
    except EOFError:
        break

