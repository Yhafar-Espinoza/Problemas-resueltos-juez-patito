n=int(input())
a=n
b=n
h=n
ce=0
for i in range(1,n+1):
    sua=""
    for l in range(1,a+1):
        x=str(l)
        sua=sua+x
    sub=""
    for l1 in range(h,0,-1):
        if(l1!=n):
            x1=str(l1)
            sub=sub+x1
    esp=""
    for l3 in range(1,ce+1):
        x3=str(l3)
        esp=esp+" "
    if(ce==0):
        ce=1
    else:
        ce=ce+2
    final=sua+esp+sub
    a=a-1
    b=b-1
    h=h-1
    print(final)
