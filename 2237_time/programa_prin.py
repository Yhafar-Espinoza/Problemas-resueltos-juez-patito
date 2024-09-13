import math

while True:
    try:
        n, k = map(int, input().split())
        y = sum(math.ceil((i + k) / (2 + i + k)) for i in range(n-2))
        print(y)
  
    except EOFError:
        break
67