co=0
for i in range(int(input())):
    a=0
    n=int(input())
    for s in range(1,n+1):
        if(n%s==0):
            a=a+1
    if(a==2):
        co=co+1
print(co)
