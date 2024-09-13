n=input()
lis=list(n)
b="c"
co=0
for i in range(len(lis)):
    if(b==lis[i]):
        co=co+1
print(co)