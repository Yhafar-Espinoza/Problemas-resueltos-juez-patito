def lle(A,n):
    a=1
    cl=n
    cll=n-1
    me=n-1
    medio=(n-1)//2
    f1=0
    c1=n
    fc=0
    for i in range(n):
        A.append([0]*n)
    for c in range(n):
        if(c==0 or c==cl):
            cop=cl
            for f in range(n):
                A[f][c]=a
        elif(c==me):
            if(c==me):
                for cf in range(cll,medio-1,-1):
                    for f in range(fc,c1):
                        A[f][cf]=a
                    c1=c1-1
                    fc=fc+1
        else:
            for f2 in range(f1,cop):
                A[f2][c]=a
        f1=f1+1
        cop=cop-1
    return(A)
A=[]
n=int(input())
A=lle(A,n)
for f in range(n):
    for c in range(n):
        print(A[f][c],end="")
    print("")

