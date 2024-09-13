n=int(input())
x = 0
M = []
for i in range(n):
   M.append([0]*3)
for y in range(n):
   M[y]= list(input()[:3])
for p in range(n):
   for l in range(3):
        if(M[p][l] == "+" ):
            x = x + 1
            break
        elif(M[p][l] == "-"):
            x = x - 1
            break
print(x)