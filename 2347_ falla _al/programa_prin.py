for l in range(int(input())):
    n=int(input())
    lis=list(map(int,input().split()[:n]))
    for i in range(len(lis)-1):
        if(lis[0]==25):
            if(lis[i+1]==25 or lis[i+1]==50):
                co=1
            else:
                co=0
        else:
            co=0
    if(co==0):
        print("NO")
    else:
        print("SI")