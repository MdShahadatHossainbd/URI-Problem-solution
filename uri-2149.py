def fib(n):
    list_phil = [0, 1]
    a, b = 0, 1
    for i in range(n - 1):
        if i % 2 == 0:
            a, b = b, a + b
        else:
            a, b = b, a * b
        list_phil.append(a)
    return list_phil[-1]

while True:
    try:
        n = int(input())
    except EOFError:
        break

    if n == 1:
        print(0)
    else:
        print(fib(n))