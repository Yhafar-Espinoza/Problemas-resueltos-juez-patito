n= int(input())
a=[]
if(n==0):
    print(0)
while n!= 0: 
    modulo = n % 2
    cociente = n // 2
    a.append(modulo)
    n = cociente
li=len(a)-1
for i in range(li,-1,-1):
    print(a[i],end="")
