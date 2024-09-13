n=int(input())
for j in range(0, n):
    m = input()
    v = m.split()
    c = []
    for i in v:
        c.append(int(i))
    c.sort()
    print('Case {0}: {1}'.format(j+1,c[1])) 
