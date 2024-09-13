for y in range(int(input())):
    a=input()
    cop=int(a)
    z=list(a)
    lis=[]
    suma=0
    for p in range(len(z)):
        if(z[p]!=" "):
            lis.append(z[p])
    for i in range(len(lis)):
        x=int(lis[i])
        fa=1
        for i1 in range(1,x+1):
            fa=fa*i1
        suma=suma+fa
    if(suma==cop):
        print("Y")
    else:
        print("N")