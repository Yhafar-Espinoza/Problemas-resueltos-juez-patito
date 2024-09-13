while True:
    try:
        n=int(input())
        a=5
        b=-4
        c=-6
        d=3
        t=8
        for i in range(n-1):
            print(t,end=" ")
            t= t + a
            aux=a
            a=b
            b=c
            c=d
            d=aux
        print(t)

    except EOFError:
        break