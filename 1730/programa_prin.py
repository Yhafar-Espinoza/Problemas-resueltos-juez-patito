n=int(input())
while(n>9):
    x=str(n)
    lis=list(x)
    su=0
    for i in range(len(lis)):
        a=int(lis[i])
        su=su+(a**2)
    n=su
print(n)