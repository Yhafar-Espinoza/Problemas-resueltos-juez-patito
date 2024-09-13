nu = int(input())
for p in range(1, nu+1):
    valor = int(input())
    x = 1
    y = 1
    for i in range(1, valor+1):
      if (i == valor):
        y = x * i
        print(y, end="")
        
      else:
        y = x * i
        print(y, end=" ")
        x = x + 2
    print("")
      

    
  


