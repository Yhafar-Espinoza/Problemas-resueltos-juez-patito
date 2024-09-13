for y in range(int(input())):
    n=int(input())
    a=0
    b=0
    for i in range(1,n+1):
        if(b<=2):
            print(a,end=" ")
            b=b+1
            if(b==2):
                a=a+1
                b=0
    print("")
    
        