from collections import OrderedDict
while True:
    try:
        avecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        abe=len(avecedario)
        n=input()
        a=input()
        res=n+a
        A=[]
        for i in range(len(avecedario)):
            for y in range(len(res)):
                if(avecedario[i]==res[y]):
                    A.append(res[y])
        final= list(OrderedDict.fromkeys(A))
        if(avecedario==final):
            print("Correcto")
        else:
            print("Incorrecto")
    except EOFError:
        break
