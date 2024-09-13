while(True):
    try:
        z = 1
        x = 0
        n = int(input())
        a = 4
        b = 2
        co = 3
        su = 0
        for i in range(1,n+1):
            re = a / b
            su = su + re
            a = a + co
            co = co + z
            p = z+x
            x = z
            z = p
            b = b + 2
        print("%.4f" % su)
    except:
        EOFError