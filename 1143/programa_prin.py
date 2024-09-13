for y in range(int(input())):
    n=int(input())
    a=0
    b=1
    c=1
    suma=0
    if(n==1):
        print(a)
    elif(n==2):
        print(a+b)
    elif(n==3):
        print(a+b+c)
    else:
        suma=a+b+c
        for i in range(n-3):
            d=a+b+c             
            a=b
            b=c
            c=d
            suma=suma+d
        print(suma)