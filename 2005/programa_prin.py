n=int(input())
a=2
b=4
for i in range(1,n+1):
    if(i%2==0):
        print(a,end=" ")
        a=a+3
    else:
        print(b,end=" ")
        b=b+3