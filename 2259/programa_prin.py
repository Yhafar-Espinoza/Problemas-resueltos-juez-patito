n=int(input())
A=[]
while(n>0):
    if(n==1):
        A.append(1)
    else:
        mo=n%3
        A.append(mo)
    n=n//3
z=len(A)
z=z-1
for i in range(z,-1,-1):
    print(A[i],end="")