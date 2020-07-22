data = list(map(int, input().split()))
a, N = data[0], 0
for i in data[1:]:
    if i > 0:
        for j in range(i):
            N += a + j
        print(N)