a, b=map(int, input().split())
if(a >= 6):
    if(a > b):
        if(a == 7 and b > 5):
            print("Gano A")
        else:
            re=a-b
            if(re==2):
                print("Gano A")
            else:
                if(re > 2):
                    print("Invalido")
                else:
                    print("Aun no termina")
    else:
        if(b == 7 and a > 5):
            print("Gano B")
        else:
            print("Aun no termina")
        
else:
    if(b >= 6):
        if(b > a):
            if(b == 7 and a > 5):
                print("Gano B")
            else:    
                re=b-a
                if(re==2):
                    print("Gano B")
                else:
                    if(re > 2):
                        print("Invalido")
                    else:
                        print("Aun no termina")
        else:
            print("Aun no termina")
    else:
            print("Aun no termina")