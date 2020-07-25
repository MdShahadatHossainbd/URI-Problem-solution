n = int(input())
x = 0
a = {}
for i in range(n):
    data = input().split()
    if float(data[1]) >= 8:
        a[data[0]] = float(data[1])

if len(a) > 0:
    print(max(a, key=a.get))
else:
    print("Minimum note not reached")
