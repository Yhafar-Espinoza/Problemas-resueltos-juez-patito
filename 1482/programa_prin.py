a=-1
b=2
c=1
n=int(input())
for i in range(1,n+1):
    if(i%2!=0):
        c=c*a
        print(c)
        a=a-2
        
    else:
       c=(-c)*b
       print(c)
       b=b+2
