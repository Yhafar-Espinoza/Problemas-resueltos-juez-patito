from cmath import pi
import sys
i=int(input())
p=0
for linea in sys.stdin:
    A=[]
    lista = list(map(str,linea.split()))
    p=p+1
    if(lista[0]=="rectangle"):
        m=float(lista[1])
        n=float(lista[2])
        re=m*n
        print("{:.2f}".format(re))
    elif(lista[0]=="circle"):
        k=pi
        l=float(lista[1])
        res=k*(l**2)
        print("{:.2f}".format(res))
    if(p==i):
        break

