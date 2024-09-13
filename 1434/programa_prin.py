# Se dice que un número es capicúa cuando puede ser leído de la misma forma de izquierda a derecha, que de derecha a izquierda por ejemplo 1001 es un número capicúa, ya que 1001 al revés es también 1001 y 123 no es porque 123 al revés es 321. Se pide realizar un programa para ver si un número es capicúa o no.

# Salida
# Imprimir la letra 'S' (sin las comillas) si el número es capicúa y 'N' en caso de que no lo sea.

# Ejemplo Entrada
# 1001
# Ejemplo Salida
# S

# Ejemplo 2:
# Entrada:
# 123
# Salida:
# N

n = input()
suma = ""
for i in range (len(n)-1, -1, -1):
    suma = suma + n[i]
if(n == suma):
    print("S")
else:
    print ("N")

