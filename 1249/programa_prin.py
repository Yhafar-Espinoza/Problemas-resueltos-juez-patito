while True:
    try:
        a, b=input().split()
        lis=list(a)
        copia=list(a)
        ma=max(lis)
        z=len(lis)
        z=z-1
        if(ma==b):
            for p in range(len(copia)):
                if(copia[p]==ma):
                    aqui=ma
                    copia[p]="1"
            ma=max(copia)
        for i in range(len(lis)):
            if(lis[i]==b):
                lis[i]=ma
        for y in range(len(lis)):
            print(lis[y],end="")
        print("")
    except EOFError:
        break
