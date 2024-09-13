while True:
    try:
        v=[]
        n=input()
        s=list(n)
        ma=int(max(s))
        mi=int(min(s))
        for i in range(mi,ma+1):
            i=str(i)
            for o in range(len(s)):
                if(i==s[o]):
                    v.append(i)
        for l in range(len(v)):
            print(v[l],end="")
        print("")
    except EOFError:
        break