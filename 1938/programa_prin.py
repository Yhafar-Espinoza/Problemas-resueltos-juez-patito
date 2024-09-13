def amor(lis,z):
    a=0
    for i in range(len(lis)):
        su=lis[i]+z
        if(su>=100):
            a=1
            return(a)
    return(a)

n=int(input())
lis=list(map(int,input().split()[:n]))
z=int(input())
a=amor(lis,z)
if(a==1):
    print("SI")
else:
    print("NO")
