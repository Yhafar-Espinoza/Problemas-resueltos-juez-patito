for y in range(int(input())):
    a, b ,c=map(int,input().split())
    if(b>=1 and b<=12):
        if(b==2):
            if(a==29):
                divi= c//100
                di=c%4
                modu=c%100
                if(modu==0):
                    modu2= divi % 4
                    if(modu2 == 0):
                        print("Fecha correcta")
                    else:
                        print("Fecha incorrecta")
                else:
                    if(di==0):
                        print("Fecha correcta")
                    else:
                        print("Fecha incorrecta") 
            elif(a>=1 and a<=28):
                print("Fecha correcta")
            else:
                print("Fecha incorrecta")
        elif(b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12):
            if(a>=1 and a<=31):
                print("Fecha correcta")
            else:
                print("Fecha incorrecta")
        elif(b==4 or b==6 or b==9 or b==11 ):
            if(a>=1 and a<=30):
                print("Fecha correcta")
            else:
                print("Fecha incorrecta")
        else:
            print("Fecha incorrecta")
    else:
        print("Fecha incorrecta")
