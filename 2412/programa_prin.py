import re

def encontrar_numeros_enteros(cadena, numero):
    if numero == 0:
        cadena_al_reves = cadena[::-1]
        patron_numeros = re.findall(r'-?\d+', cadena_al_reves)
        numeros_enteros = [str(num[::-1]) for num in patron_numeros]
    else:
        patron_numeros = re.compile(r'-?\d+')
        numeros_enteros = patron_numeros.sub(' ', cadena)

    return numeros_enteros

S = input()

z = encontrar_numeros_enteros(S, 0)
z1 = encontrar_numeros_enteros(S, 2)
co = 0
z1_lista = list(z1)

for i in range(len(z1_lista)):
    if z1_lista[i] == ' ':
        z1_lista[i] = z[co]
        co += 1

print(''.join(z1_lista))
