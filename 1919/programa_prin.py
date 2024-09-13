for i in range(int(input())):
    n=int(input())
    for y in range(1,n+1):
        if(n%y==0):
            if(y==n):
                print(y,end="")
            else:
                print(y,end=" ")
    print("")
