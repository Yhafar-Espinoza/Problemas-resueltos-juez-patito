while True:
    try:
        a, b=map(int,input().split())
        if(b>a):
            if(b%a==0):
                print(b,"es divisible por",a)
            else:
                print(("-1"))
        else:
            if(a%b==0):
                print(a,"es divisible por",b)
            else:
                print(("-1"))

    except EOFError:
          break
