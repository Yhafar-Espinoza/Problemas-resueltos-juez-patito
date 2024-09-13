while True:
    try:
        n=input()
        s=n.upper()
        print(s)
    except EOFError:
        break