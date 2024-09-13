while True:
    try:
        a,b=map(int,input().split())
        cociente=a//b
        resto=a%b
        if(resto==0):
            print("La división es exacta. Cociente:",cociente)
        else:
           print("La división no es exacta. Cociente:", cociente, "Resto:",resto) 

    except EOFError:
        break
