X, Y = int(input()), int(input())
for i in range(min(X, Y) + 1, max(X, Y)):
    if i % 5 in [2, 3]:
        print(i)