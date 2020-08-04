m = 0
word = ""
while True:
    data = input().split()
    volume = []
    if data[0] == "0":
        break
    for i in data:
        volume.append(len(i))
        if len(i) >= m:
            m = len(i)
            word = i
    print("-".join(map(str, volume)))
print()
print("The biggest word:", word)