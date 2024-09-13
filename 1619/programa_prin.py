while True:
    try:    
        a,b=map(int,input().split())
        suma=a+b
        resta=a-b
        multi=a*b
        maxi=max(suma,resta,multi)
        print(maxi)
    except EOFError:
        break