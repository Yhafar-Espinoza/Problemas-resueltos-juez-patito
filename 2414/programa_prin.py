for y in range(int(input())):
    co = 0
    con = 0
    n = int(input())
    for p in range(1,n+1):
        co = co + p
        if(n > co or n == co):
            con = con +1
            if(n == co):
                print("Llegas al cuadrado",con)
                break
        else:
            print("No llegas")
            break

