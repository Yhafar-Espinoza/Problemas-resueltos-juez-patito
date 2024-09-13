a=int(input())
ul=a
ul=ul-1
A=[]
uno=1
z=1
p=2
h=0
for i in range(a):
        A.append([0]*a)
if(a%2==0):
    for f in range(a):
        for c in range(a):
            if(f==0):
                if(z%2==0):
                    A[f][c]=uno
                    z=1
                else:
                    z=2
            else:
                if(A[f-1][ul]!=uno):
                    if(z%2==0):
                        A[f][c]=uno
                        z=1
                    else:
                        z=2
                    h=h+1
                else:
                    if(p%2==0):
                        A[f][c]=uno
                        p=1
                    else:
                        p=2

    for f1 in range(a):
        for c1 in range(a):
            print(A[f1][c1],end=" ")
        print("")


else:
    for f in range(a):
        for c in range(a):
            if(z%2==0):
                A[f][c]=uno
                z=1
            else:
                z=2
    for f1 in range(a):
        for c1 in range(a):
            print(A[f1][c1],end=" ")
        print("")


