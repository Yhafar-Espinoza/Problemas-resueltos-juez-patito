import sys
if __name__ == "__main__":
    for line in sys.stdin:      
        mayor = 0
        l = input()
        l = l.split()
        for i in l:
            a = l.count(i)      
            if(a>mayor):        
                mayor = a
        if(mayor > 0):
            print(mayor)
