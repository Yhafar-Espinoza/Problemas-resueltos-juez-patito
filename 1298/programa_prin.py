import sys
for linea in sys.stdin:
 if linea == "\n":
    break
 lista =list(map(int,linea.split()[1:]))
 x=[]
 if(lista==x):
    print("")
 else:
    s=len(lista)
    s=s-1
    for q in range(s,-1,-1):
        if(q==0):
            print(lista[q],end="")
        else:
            print(lista[q],end=" ")
    print("")
    
