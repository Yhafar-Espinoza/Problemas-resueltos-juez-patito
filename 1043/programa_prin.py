for y in range(int(input())):
    a,b=map(int,input().split())
    co=0
    while(a>=3 and b>=2):
        a=a-3
        co=co+1
        b=b-2
    su=a+b
    print(co,su)
    