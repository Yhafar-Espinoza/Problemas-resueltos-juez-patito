while True:
    try:
        n=input()
        lis=list(n)
        li=len(lis)
        li=li-1
        su=""
        for i in range(li,-1,-1):
            su=su+lis[i]
        if(n==su):
            print("SI")
        else:
            print("NO")
    except EOFError:
        break