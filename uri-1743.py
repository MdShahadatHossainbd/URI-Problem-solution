p1 = input().split()
p2 = input().split()
count = 0
for i in range(5):
    if p1[i] != p2[i]:
        count += 1
if count == 5:
    print("Y")
else:
    print("N")