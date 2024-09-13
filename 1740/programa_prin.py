n=int(input())
a=n
b=1
for i in range(1,n+1):
    su=""
    o=""
    l=str(i)
    for i1 in range(1,a+1):
        su=su+"-"
    a=a-1
    for i3 in range(1,b+1):
        o=o+l
    b=b+2
    fin=su+o+su
    print(fin)

