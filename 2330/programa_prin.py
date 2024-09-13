a, b=map(int,input().split())
A=[]
li=b-1
a1=1
b1=1
a2=0
b2=1
for l in range(a):
    A.append([0]*b)
for f in range(a):
    if(f%2!=0):
        for c in range(b):
            A[f][c]=a1
            c1=a1+b1
            a1=c1
            b1=a1
    else:
        for c in range(b):
            if(f==0 and c==0):
                A[f][c]=0
            else:
                A[f][c]=a2
                c2=a2+b2
                b2=a2
                a2=c2
for f3 in range(a):
    for c3 in range(b):
        if(li==c3):
            print(A[f3][c3],end="")
        else:
            print(A[f3][c3],end=" ")  
    print("")             
                
