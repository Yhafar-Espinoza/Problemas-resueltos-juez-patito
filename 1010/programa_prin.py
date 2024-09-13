def es_posible_formar_palabra(cadena, palabra):
    conteo_cadena = {}
    conteo_palabra = {}
    for letra in cadena:
        conteo_cadena[letra] = conteo_cadena.get(letra, 0) + 1
    for letra in palabra:
        conteo_palabra[letra] = conteo_palabra.get(letra, 0) + 1
    for letra, cantidad in conteo_palabra.items():
        if letra not in conteo_cadena or conteo_cadena[letra] < cantidad:
            return False

    return True

for i in range(int(input())):
    S = input()
    if es_posible_formar_palabra(S.upper(), "UMSA"):
        if es_posible_formar_palabra(S.upper(), "ICPC"):
            print("ES POSIBLE")
        else:
            print("NO ES POSIBLE")
    else:
        print("NO ES POSIBLE")
    
