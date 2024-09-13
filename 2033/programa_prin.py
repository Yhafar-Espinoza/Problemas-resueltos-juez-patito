for y in range(int(input())):
    n=input()
    lis=list(n)
    rojo=0
    amarillo=0
    verde=0
    for i in range(len(lis)):
        if(lis[i]=="r"):
            rojo=rojo+1
        elif(lis[i]=="a"):
            amarillo=amarillo+1
        elif(lis[i]=="v"):
            verde=verde+1
    mi=min(rojo,amarillo,verde)
    print(mi)
