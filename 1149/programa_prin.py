for i in range(int(input())):
    n=int(input())
    n=n-1
    n=n%60
    a=-1
    b=1
    for y in range(n+1):
        c=(a%10+b%10)%10;
        a=b
        b=c
    if(c%2==0):
        print(c,"par")
    else:
        print(c,"impar")