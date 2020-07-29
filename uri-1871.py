while True:
    data = input().split()
    m = int(data[0])
    n = int(data[1])
    if m + n == 0:
        break
    total = str(m + n).replace("0", "")
    print(total)