while True:
 try:
    n=int(input())
    a=1
    for i in range(1,n+1):
        su=""
        for y in range(1,a+1):
            su=su+"1"
        a=a+1
        if(i==n):
            print(su,end="")
        else:
            print(su,end=" ")
    if(n==0):
        print("error")
    else:
        print("")
 except EOFError:
    break