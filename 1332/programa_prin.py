
caracteres = input()
suma = ""
for i in range(0, len(caracteres)):
    ca = caracteres[i].lower()
    if(ca != "a" and ca != "e" and ca != "i" and ca != "o" and ca != "u" and ca != "y"):
        suma = suma + "."
        suma = suma + ca
print(suma)