for i in range(int(input())):
    t = 0
    a1, a2, b1, b2 = map(float, input().split())
    while a2 >= a1:
        if t > 99:
            print("Mais de 1 seculo.")
            break
        a1 += int(a1 * b1 / 100)
        a2 += int(a2 * b2 / 100)
        t += 1
    else:
        print(t, "anos.")