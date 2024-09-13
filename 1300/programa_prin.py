while True:
    try:
        n=int(input())
        lis=list(map(int,input().split()[:n]))
        n=n-1
        a=lis[n]
        co=0
        for i in range(len(lis)):
            if(a==lis[i]):
                co=co+1
        print(co)
    except EOFError:
        break