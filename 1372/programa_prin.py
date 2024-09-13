a = int(input())
divi= a//100
di=a%4
modu=a%100
if(modu==0):
    modu2= divi % 4
    if(modu2 == 0):
        print("si")
    else:
        print("no")
else:
    if(di==0):
        print("si")
    else:
        print("no") 