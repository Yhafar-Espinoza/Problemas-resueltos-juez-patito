a, b=map(int,input().split())
if(a<b):
    copia=a
    a=b
    b=copia  
for i in range(a,b-1,-1):
    print(i)