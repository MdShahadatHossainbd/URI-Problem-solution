N, a, b = int(input()), 0, 0
while N > 0:
    a += N
    b += 1
    N = float(input())
print(format(a / b, ".2f"))