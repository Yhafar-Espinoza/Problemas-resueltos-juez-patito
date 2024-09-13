def aqui(z):
    a=z.isdigit()
    return(a)

n=input()
lis=list(n)
x=len(lis)
x=x-1
z=lis[0]
a=aqui(z)
y=lis[x]
b=aqui(y)
if(a==True):
    if(b==True):
        print("SI")
    else:
        print("NO")
else:
    print("NO")