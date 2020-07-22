for i in range(int(input())):
    a, b = map(int, input().split())
    sum = 0
    for x in range(a, a + (b * 2)):
        if x % 2:
            sum += x
    print(sum)