for y in range(int(input())):
    a, b=map(int,input().split())
    s=1
    p=0
    for z in range(1,a+1):
        if(b>=p):
            p=p+1
            print(s,end=" ")
            if(p==b):
                z=z-1
                s=s+2
                p=0
    print("")