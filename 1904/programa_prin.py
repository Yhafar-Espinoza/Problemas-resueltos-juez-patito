for y in range(int(input())):
    n=input()
    h=len(n)
    h=h-1
    s=list(n)
    su=s[0]+s[1]+s[2]
    suu=s[h-2]+s[h-1]+s[h]
    print(su,suu)
