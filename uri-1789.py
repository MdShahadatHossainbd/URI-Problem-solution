while True:
    try:
        l = int(input())
        data = input().split()
    except EOFError:
        break
    x = max(map(int, data))
    if x < 10:
        print(1)
    elif x in range(10, 20):
        print(2)
    else:
        print(3)