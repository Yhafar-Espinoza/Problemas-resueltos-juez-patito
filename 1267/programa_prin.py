while True:
    n = int(input())
    if n == -1:
        break
    elif(n == 0):
        print ("1")
    else:
        suma = 1
        for i in range(1,n+1):
            suma = suma + 2
        print (suma)