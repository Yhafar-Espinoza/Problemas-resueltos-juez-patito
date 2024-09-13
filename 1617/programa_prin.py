from collections import OrderedDict
while True:
    try:
        a, b=input().split()
        coa=0
        cob=0
        a1=list(a.upper())
        b1=list(b.upper())
        finala= list(OrderedDict.fromkeys(a1))
        finalb= list(OrderedDict.fromkeys(b1))
        for i in range(len(finala)):
            xa=finala[i].upper()
            if(xa=="A"or xa=="E"or xa=="I"or xa=="O"or xa=="U"):
                coa=coa+1
        for y in range(len(finalb)):
            xb=finalb[y].upper()
            if(xb=="A"or xb=="E"or xb=="I"or xb=="O"or xb=="U"):
                cob=cob+1
        if(coa==cob):
            print("AMOR VERDADERO")
        else:
            print("MEJOR PRUEBA OTRO NOMBRE")
    except EOFError:
        break
