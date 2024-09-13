A=[]
B=[]
for y in range(int(input())):
    A.append(input())
for i in range(len(A)):
    a=A[i]
    z=len(A[i])
    z=z-1
    suma=""
    for p in range(z,-1,-1):
        suma=suma+a[p]
    B.append(suma)
m1=len(B)
m1=m1-1
for t in range(m1,-1,-1):
    print(B[t])