n=int(input())
for i in range(0,n):
    x=2**i
    z=(2**x)+1
    if(i==(n-1)):
        print(z,end="")
    else:
        print(z,end=" ")