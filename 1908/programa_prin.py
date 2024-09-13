for y in range(int(input())):
    a=input()
    lis=list(a)
    su=""
    li=len(lis)
    li=li-1
    for i in range(len(lis)):
        
        if(i==0):
            x=lis[i].upper()
            su=su+x
        elif(lis[i]==" "):
            if(i==li):
                if(lis[i-1]==" "):
                    x=lis[i].upper()
                    su=su+x
                elif(i==0):
                    x=lis[i].upper()
                    su=su+x
            else:
                x=lis[i+1].upper()
                su=su+x
    print(su)