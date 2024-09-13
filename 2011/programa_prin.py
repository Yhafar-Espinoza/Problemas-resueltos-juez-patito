from collections import OrderedDict
lis=list(map(str,input().split()))
for l in range(len(lis)):
    x=lis[l]
    xl=list(x)
    co=[]
    for i in range(len(xl)):
        if(xl[i]=="a" or xl[i]=="e" or xl[i]=="i" or xl[i]=="o" or xl[i]=="u"):
            co.append(xl[i])
    final=list(OrderedDict.fromkeys(co))
    fi=len(final)
    if(fi==5):
        print(lis[l])
