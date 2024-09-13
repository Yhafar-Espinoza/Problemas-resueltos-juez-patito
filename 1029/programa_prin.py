while True:
     try:
        a=0
        sp=0
        sc=0
        n=list(map(int,input().split()))
        for i in range(len(n)):
            if(a==0):
                ma=max(n)
                sp=sp+ma
                n.remove(ma)
                a=1
            else:
                mas=max(n)
                sc=sc+mas
                n.remove(mas)
                a=0
        re=sp-sc
        print(re)
     except EOFError:
          break