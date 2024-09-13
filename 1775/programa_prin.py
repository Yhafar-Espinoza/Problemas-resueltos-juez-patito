n=int(input())
co=0
lis=list(map(int,input().split()[:n]))
for i in range(len(lis)):
    if(lis[i]<0):
        co=co+1
print(co)