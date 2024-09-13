a,b,c = map(float, input().split())
if (a==b and a==c and c==b):
    print("El triangulo es equilatero")
else:
    if(a==b or a==c or b==c):
        print("El triangulo es isoseles")
    else:
        maximo=max(a, b, c)
        cu1=maximo**2
        minimo=min(a, b, c)
        cu2=minimo**2
        medio=(a+b+c)-(maximo+minimo)
        cu3=medio**2
        igual=cu2+cu3
        if(igual==cu1):
            print("El triangulo es rectangulo")
        else:
            suma1=a + b
            suma2=a + c
            suma3=b + c
            if(suma1 >= c):
                if(suma2 >= b):
                    if(suma3 >= a):
                        print("El triangulo es escaleno")
                    else:
                        print("El triangulo es invalido")
                else:
                    print("El triangulo es invalido")
            else:
                 print("El triangulo es invalido")   
