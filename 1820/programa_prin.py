a,b,c=map(int,input().split())
aqui=input()
ma=max(a,b,c)
mi=min(a,b,c)
me=(a+b+c)-(ma+mi)
for i in range(len(aqui)):
    if(aqui[i]=="A"):
        print(mi,end=" ")
    elif(aqui[i]=="B"):
        print(me,end=" ")
    elif(aqui[i]=="C"):
        print(ma,end=" ")
