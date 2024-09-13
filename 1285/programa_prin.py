import sys
if __name__ == "__main__":
    for num in sys.stdin:
        i = 0            
        p = 0              
        sw = True           
        for dig in num:
            if dig == '\n': 
                continue
            if sw:
                i += int(dig)
                sw = False
            else:
                p += int(dig)
                sw = True
        if i == p:
            print("SI")
        else:
            print("NO")
