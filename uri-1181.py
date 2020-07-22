
n = int(input())
s = input()
sum = 0
for h in range(12):
    for v in range(12):
        value = float(input())
        if h == n:
            sum += value
if s == 'S':
    print(format(sum, ".1f"))
else:
    print(format(sum / 12.0, ".1f"))