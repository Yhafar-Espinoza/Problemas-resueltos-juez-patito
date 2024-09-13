for y in range(int(input())):
    n=int(input())
    su=0
    for i in range(1,n+1):
        su=su+i
        if(i%2!=0):
            a=1
        else:
            if(su%2==0):
                a=2
            else:
                a=3
    if(a==1):
        print("Cualquiera")
    elif(a==2):
        print("Par")
    elif(a==3):
        print("Impar")
