while True:
    try:
        n = int(input())
    except EOFError:
        break
    print(n - 1)