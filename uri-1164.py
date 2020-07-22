for i in range(int(input())):
    n, t = int(input()), 0
    for x in range(1, n):
        if n % x == 0:
            t += x
    if t == n:
        print(n, "eh perfeito")
    else:
        print(n, "nao eh perfeito")