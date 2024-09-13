def aqui(a,co):
    if "SI" in a:
        co=co+1
    return(co)
co=0
a=input()
b=input()
c=input()
d=input()
co=aqui(a,co)
co=aqui(b,co)
co=aqui(c,co)
co=aqui(d,co)
if(co==4):
    print("SI")
else:
    print("NO")