n, a = list(map(int, input().split()))
for i in range(a):
    data = input()
    if data == "fechou":
        n += 1
    else:
        n -= 1
print(n)