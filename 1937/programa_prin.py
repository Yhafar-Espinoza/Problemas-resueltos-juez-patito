n=int(input())
lis=list(map(int,input().split()))
cero=0
for i in range(len(lis)):
    if(lis[i]<0):
        lis[i]=cero
li=len(lis)
li=li-1
for i1 in range(len(lis)):
    if(i1==li):
        print(lis[i1],end="")
    else:
        print(lis[i1],end=" ")
