
#YHERCO YHAFAR ESPINOZA TICONA
#CI. 6854467

a, b, c = map(int, input().split())
ma = max(a, b, c)
mi = min(a, b, c)
med = (a + b + c)-(ma+ mi)
if((mi+med) == ma):
    print(ma)