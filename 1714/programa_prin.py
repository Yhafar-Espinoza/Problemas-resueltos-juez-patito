import sys

if __name__ == "__main__":
    for line in sys.stdin:
        lista = input()                 
        lista = lista.split()           
        lista2 = []
        for i in lista:
            lista2.append(int(i))      
        turno = 0
        lista2.sort()                   
        for i in range(0, len(lista2)):
            elemento = lista2[i]
            if elemento == 0:           
                continue
            else:                         
                x = lista2.index(elemento)
                if x+1 < len(lista2):
                    if elemento+1 == lista2[x+1]:
                        lista2[x+1] = 0
                if elemento-1 == lista2[x-1]:
                    lista2[x+1] = 0
                lista2[x] = 0
                turno += 1
        print(turno)
