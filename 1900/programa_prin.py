for y in range(int(input())):
    n=int(input())
    a=0
    b=1
    a1=0
    b1=1
    for i in range(1,n+1):
        if(i%2==0):
            print(a, end=" ")
            c=a+b
            b=a
            a=c
        else:
            print(a, end=" ")
            c1=a1+b1
            b1=a1
            a1=c1
    print("")