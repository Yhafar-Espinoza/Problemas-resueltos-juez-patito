while True:
    try:
        n=input()
        s=list(n)
        li=len(s)
        li=li-1
        su=""
        si=""
        A=[]
        for i in range(li,-1,-1):
            if(s[i]!=" "):
                su=su+s[i]
        for i1 in range(len(s)):
            if(s[i1]!=" "):
                si=si+s[i1]
        if(si==su):
            print("palindrome")
        else:
            print("no palindrome")
    except EOFError:
        break