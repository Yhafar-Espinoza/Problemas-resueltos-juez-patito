from collections import OrderedDict
while True:
    try:
        co=0
        n=input()
        lis=list(n)
        vAux=[]
        vo=["a","e","i","o","u"]
        for i in range(len(lis)):
            x=lis[i]
            for l in range(len(vo)):
                if(x==vo[l]):
                    vAux.append(x)
        final_list = list(OrderedDict.fromkeys(vAux))

        for i1 in range(len(final_list)):
            k=final_list[i1]
            for i3 in range((len(vo))):
                if(k==vo[i3]):
                    co=co+1
        if(co==5):
            print("SI")
        else:
            print("NO")
    except EOFError:
        break
        
