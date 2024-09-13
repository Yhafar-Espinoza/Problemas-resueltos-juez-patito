a, b=map(int,input().split())
if(a>b):
    aux=b
    b=a
    a=aux
su=0
for i in range(a,b+1):
    z=0
    for y in range(1,i+1):
        if(i%y==0):
            z=z+1
    if(z==2):
        su=su+1
print(su)

