a, b, c=map(int,input().split())
suma=0
for i in range(1,a+1):
    print(i)
    z=b*i
    suma=suma+z
re=suma%c
    
print(re)