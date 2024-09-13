for i in range(int(input())):
    lis=list(map(int,input().split()))
    co=0
    for i in range(len(lis)-1):
        if(lis[i]<lis[i+1]):
            co=co+1
    print(co)
