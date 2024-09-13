def buscar(lista,bu):
    a=0
    for i in range(len(lista)):
        if(lista[i]==bu):
            a=1
            return(a)
    return(a)
n=int(input())
lista=list(map(int,input().split()[:n]))
bu=int(input())
bu=buscar(lista,bu)
if(bu==1):
    print("SI")
else:
    print("NO")
