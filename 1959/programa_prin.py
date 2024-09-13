while True:
    try:
        n=input()
        co=0
        lis=list(n)
        for i in range(len(lis)):
            if(lis[i]=="a" or lis[i]=="e" or lis[i]=="i" or lis[i]=="o" or lis[i]=="u"):
                co=co+1
        li=len(lis)
        resultado=li-co
        print(resultado)
    except EOFError:
        break
