while True:
    try:
        def aqui(ab):
            ñ=len(ab)
            lis=list(ab)
            AB=[]
            if(ñ==1):
                AB.append(ab)
            else:
                for i in range(len(lis)):
                    AB.append(lis[i])
            return(AB)
        a,b=input().split()
        A=[]
        B=[]
        A=aqui(a)
        B=aqui(b)
        za=len(A)
        zb=len(B)
        if(za==zb):
            su=""
            for i in range(len(A)):
                ma=max(A[i],B[i])
                su=su+ma
            print(su)
        elif(za>zb):
            eli=za-zb
            ceros=""
            for y1 in range(1,eli+1):
                ceros=ceros+"0"
            fin=""
            for i1 in range(len(B)):
                fin=fin+B[i1]
            concateno=ceros+fin
            B=list(concateno)
            su=""
            for i in range(len(A)):
                ma=max(A[i],B[i])
                su=su+ma
            print(su)
        elif(zb>za):
            eli=zb-za
            ceros=""
            for y1 in range(1,eli+1):
                ceros=ceros+"0"
            fin=""
            for i1 in range(len(A)):
                fin=fin+A[i1]
            concateno=ceros+fin
            A=list(concateno)
            su=""
            for i in range(len(B)):
                ma=max(A[i],B[i])
                su=su+ma
            print(su)
    except EOFError:
        break
