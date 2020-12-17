while True:
    try:
        loops = input().split()
    except EOFError:
        break
    n = []
    for i in range(int(loops[0])):
        data = int(input())
        n.append(data)
    for j in range(int(loops[1])):
        position = int(input())
        print(sorted(n, reverse=True)[position - 1])