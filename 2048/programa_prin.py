from collections import deque
a, b = map(int, input().split())
lis = deque(map(int, input().split()[:a]))
lis.rotate(b) #operacion ya importada
 # rota la lista b veces a la derecha si b es positivo, o a la izquierda si b es negativo

print(*lis, end='') # imprime la lista separada por espacios y end quita el final del espacio
