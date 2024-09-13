for i in range(int(input())):
    n=input()
    p=0
    n=list(n)
    for o in range(len(n)):
        if(n[o]!=" "):
            if (p == 0):
                a=n[o].isupper()
                if(a==False):
                    c=n[o].upper()
                    n[o]=c
                    p=1
                else:
                    p=1
            elif (p == 1):
                a=n[o].islower()
                if(a==False):
                    c=n[o].lower()
                    n[o]=c
                    p=0
                else:
                    p=0
    for m in range(len(n)):
        print(n[m],end="")
    print("")
