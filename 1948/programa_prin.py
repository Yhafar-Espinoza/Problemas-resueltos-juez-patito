a,b=map(int,input().split())
A=[]
cero=0
for i in range(a):
    A.append([1]*b)
for c in range(b):
    for f in range(a):
        if(c%2==0):
            A[f][c]=cero
for f1 in range(a):
    for c1 in range(b):
        print(A[f1][c1],end=" ")
    print("")
