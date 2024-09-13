while True:
    try:
        n=input()
        lis=list(n)
        suma=0
        for i in range(len(lis)):
            x=int(lis[i])
            if(x%2==0):
                suma=suma+x
        print(suma)
    except EOFError:
        break