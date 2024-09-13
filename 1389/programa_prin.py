while True:
     try:
        n=input()
        suma=0
        vo=int(n)
        for i in range(len(n)):
            b=int(n[i])
            suma=suma+b
        print("La suma de los digitos de", vo, "es", suma)
     except EOFError:
          break