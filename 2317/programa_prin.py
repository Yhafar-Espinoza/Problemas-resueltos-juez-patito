M=[]
n=int(input())
p=2
im=1
for i in range(n):
    M.append([0]*n)
for f in range(n):
    if(f%2!=0):
        for c in range(n):
            M[f][c]=p
            p=p+2
    else:
        for s in range(n):
            M[f][s]=im
            im=im+2
for f1 in range(n):
    for c1 in range(n):
        if(c1==(n-1)):
            print(M[f1][c1],end="")
        else:
            print(M[f1][c1],end=" ")
    print("")