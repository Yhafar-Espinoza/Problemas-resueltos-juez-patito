n=int(input())
a=-1
b=1
for i in range(1,n+1):
    if(i%2!=0):
        aqui=a
        a=a*2
        b=b*2
    else:
        aqui=b
        b=b*2
        a=a*2
print(aqui)
