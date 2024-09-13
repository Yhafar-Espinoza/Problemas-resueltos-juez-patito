par=0
impa=0
for i in range(int(input())):
    n=int(input())
    if(n%2==0):
        par=par+1
    else:
        impa=impa+1
print("Pares:",par)
print("Impares:",impa)

