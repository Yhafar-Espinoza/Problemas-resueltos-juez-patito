n=int(input())
A=[]
for l in range(n):
    A.append([0]*n)
a=n-1
uno=1
for f in range(n):
    for c in range(n):
        if(f==0 or f==a):
            A[f][c]=uno
for c1 in range(n):
    for f1 in range(n):
        if(c1==0 or c1==a):
            A[f1][c1]=uno
for f2 in range(n):
    for c2 in range(n):
        print(A[f2][c2],end=" ")
    print("")
