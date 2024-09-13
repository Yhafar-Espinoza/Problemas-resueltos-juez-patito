while True:
    try:
        n=int(input())
        a=0
        b=0
        for i in range(1,n+1):
            if(i%2==0):
                b=b+i
                print(b,end=" ")
            else:
                a=a+i
                print(a,end=" ")       
        print("")
    except EOFError:
        break
