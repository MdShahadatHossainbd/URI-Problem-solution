s = 0
div = 1
for i in range(1, 40, 2):
    s += i / div
    div *= 2
print(format(s, ".2f"))