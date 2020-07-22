list = [0, 1, 1]

r = "0,1,1"
a = 1
b = 1
N = int(input())

for i in range(N - 3):
    t = b
    b += a
    a = t
    list.append(b)

print(str(list[0:N]).replace(",", "").replace("[", "").replace("]", ""))