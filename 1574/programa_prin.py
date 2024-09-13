import sys
gen = []
for i in range(0, 100000):
    gen.append(0)
def sdigitos(n):         
    if n == 0:
        return 0
    else:
        return n % 10 + sdigitos(n // 10)
def generador(n):                   
    c = n + sdigitos(n)
    if c <= 10000:
        if gen[c] != 1:
            gen[c] = 1
            generador(c)
for i in range(1, 9999):            
    generador(i)
if __name__ == "__main__":
    for line in sys.stdin:
        line = line.split()         
        s = 0
        for i in range(int(line[0]), int(line[1])+1):
            if gen[i] == 0:         
                s += 1
        print(s)