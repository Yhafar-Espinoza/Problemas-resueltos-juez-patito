#2426
n=int(input())
if(n > 0):
    if(n > 9 and n < 100):
        mo= n % 10
        di = n // 10
        print(mo, end="")
        print(di)
    else:
        print(n)