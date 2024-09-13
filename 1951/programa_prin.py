a,b=map(int,input().split())
A=[]
for y in range(a):
    A.append([0]*b)
for f in range(a):
    A[f]=list(map(int,input().split()[:b]))
z=int(input())
suma=0
for f1 in range(a):
    if(f1==z):
        for c in range (b):
            suma=suma+A[f1][c]
print(suma)
