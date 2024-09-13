while True:
    try:
        n=input()
        li=list(n)
        lis=[]
        for i in range(len(li)):
            x=int(li[i])
            if(x!=0):
                lis.append(x)
                a=0
                while(x<10):
                    x=x+1
                    a=a+1
                lis.append(a)
        for y in range(len(lis)):
            print(lis[y],end="")
        print("")
    except:
        EOFError