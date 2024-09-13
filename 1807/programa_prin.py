while True:
    try:
        n=int(input())
        s=n%10
        if(n%4==0) or (s==4):
            print("YES")
        elif(n%7==0) or (s==7):
            print("YES")
        else:
            print("NO")
    except EOFError:
        break