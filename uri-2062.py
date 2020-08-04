loops = int(input())
data = input().split()
final = ""
for j in data:
    if j[:2] in ["OB", "UR"] and len(j) == 3:
        final += j[:2] + "I" + " "
    else:
        final += j + " "
print(final[:-1])
