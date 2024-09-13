def es_primo(A,B):
    c=0
    for i in range(1,A+1):
        if(A%i==0):
            c=c+1
    if(c==2):
        B.append(A)
        return(B)
def primoooo(suma,contador):
    c=0
    for i in range(1,suma+1):
        if(suma%i==0):
            c=c+1
    if(c==2):
        contador=contador+1
        return(contador)
def esp(a):
    c=0
    for i in range(1,a+1):
        if(a%i==0):
            c=c+1
    if(c==2):
        return(True)
    else:
        return(False)
A=[]
B=[]
contador=0
a, b=map(int,input().split())
re=esp(a)
ri=esp(b)
if(re==True):
    contador=contador+1
    if(ri==True):
        contador=contador+1
        si=a*b
        for u in range(a):
            A.append([0]*b)
        for f1 in range(a):
            A[f1]=list(map(int,input().split()[:b]))
        for f in range(a):
            for c in range(b):
                primo=es_primo(A[f][c],B)
        k=len(B)
        if(si==k):
            suma=0
            for g in range(len(B)):
                suma=suma+B[g]
            contador=primoooo(suma,contador)
            if(contador==3):
                print("SI")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")