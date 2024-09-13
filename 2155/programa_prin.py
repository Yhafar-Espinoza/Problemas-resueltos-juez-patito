def prim(n):
    a=0
    for i in range(1,n+1):
        if(n%i==0):
            a=a+1
    if(a==2):
        return(True)
    else:
        return(False)
for y in range(int(input())):
    n=int(input())
    cop=n
    cip=n
    if(n%5==0):
        print(n,"es multiplo de 5")
    elif(prim(n)):
        print(n,"es primo")
    else:
        l=str(n)
        lis=list(l)
        li=len(lis)-1
        x=(int(lis[li]))
        z=(int(lis[li]))
        co=0
        ci=0
        if(x>=5):
            while(x>5):
                x=x-1
                co=co+1
            while(z<10):
                z=z+1
                ci=ci+1
            cip=cip-co
            cop=cop+ci
        else:
            while(x>0):
                x=x-1
                co=co+1
            while(z<5):
                z=z+1
                ci=ci+1
            cip=cip-co
            cop=cop+ci
        print(n ,"se encuentra entre", cip, "y" ,cop)
