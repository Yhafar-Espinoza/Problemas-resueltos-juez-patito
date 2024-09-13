for i in range(int(input())):
    x = input()
    nu = len(x)
    xx = list(x)
    if(nu > 10):
        print(xx[0],end="") 
        print(nu-2,end="")
        print(xx[nu-1],end="")
    else:
        print(x,end="")
    print()