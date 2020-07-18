n1, n2, t = int(input()), int(input()), 0
x, y = max(n1, n2), min(n1, n2)
for i in range(y, x + 1):
    if i % 13:
        t += i
print(t)