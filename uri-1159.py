while True:
    n = int(input())
    if n == 0:
        break
    if n % 2:
        print((n + 1) * 5 + 20)
    else:
        print(n * 5 + 20)