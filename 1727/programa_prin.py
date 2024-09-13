a,b,c=map(int,input().split())
co=0
for i in range(a,b+1):
    if(i%c==0):
        co=co+1
print(co)