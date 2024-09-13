from tokenize import Double
from collections import OrderedDict



while True:
    try:
        a=input()
        b=input()
        suma=[]
        for i in range(len(a)):
            for y in range(len(b)):
               if (b[y]==a[i]):
                suma.append(b[y])
        final = list(OrderedDict.fromkeys(suma))
        mini=len(min(a, b))
        letra=len(final)
        re=(letra/mini)*100
        print(float(re))

    except:
        EOFError
