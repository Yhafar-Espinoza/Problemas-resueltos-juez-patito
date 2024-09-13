while True:
    try:
        a=1
        b=1
        n=int(input())
        if(n==0):
            print(0)
        else:
            for i in range(1,n-1):
                c=a+b
                b=a
                a=c
            print(a)

    except EOFError:
        break