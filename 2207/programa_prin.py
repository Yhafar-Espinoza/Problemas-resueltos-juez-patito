hora_actual, cantidad_de_horas=map (int, input().split())
suma=hora_actual+cantidad_de_horas
if(suma>12):
    dias=suma//12
    horas=dias*12
    total=suma-horas
    print("Hora actual:",hora_actual)
    print("Cantidad de horas:",cantidad_de_horas)
    print("En",cantidad_de_horas,"horas, el reloj marcara las",total)
else:
    if(suma==12):
        print("Hora actual:",hora_actual)
        print("Cantidad de horas:",cantidad_de_horas)
        print("En",cantidad_de_horas,"horas, el reloj marcara las 0")
    else:
            print("Hora actual:",hora_actual)
            print("Cantidad de horas:",cantidad_de_horas)
            print("En",cantidad_de_horas,"horas, el reloj marcara las",suma)
