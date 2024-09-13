def factores(numero):
    factor = 2
    while factor <= numero:
        if not (numero % factor != 0):
            a=factor
            numero /= factor
        else:
            factor += 1
    return (a)
while True:
    try:
        a=factores(int(input()))
        print(a)
    except EOFError:
        break
        