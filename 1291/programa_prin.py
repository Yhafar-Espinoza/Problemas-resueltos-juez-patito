while True:
     try:
        lista=list(map(int,input().split()))
        print(sum(lista))
     except EOFError:
          break
