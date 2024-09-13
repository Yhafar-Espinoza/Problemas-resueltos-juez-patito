import math
for i in range(int(input())):
    co=0
    a,b=map(int,input().split())
    for l in range(a,b+1):
        a=math.sqrt(l)
        z=a%1
        if(z==0):
            co=co+1
    print(co)