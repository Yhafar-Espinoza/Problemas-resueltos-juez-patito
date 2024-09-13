a, b=input().split()
for x in range(len(a)):
    m=x
for y in range(len(b)):
    mi=y
if(m>mi):
    print(a,">",b)
elif(m<mi):
    print(a,"<",b)
else:
    print(a,"=",b)