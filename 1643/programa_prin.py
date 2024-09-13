a,b,c=map(int,input().split())
if a >b:
    if(a>c):
        print("Escala la primera")
    else:
        print("Escala la tercera")
else:
    if(b>c):
        print("Escala la segunda")
    else:
        print("Escala la tercera")