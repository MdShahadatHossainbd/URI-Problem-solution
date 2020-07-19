Dic = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6, 0: 6}
N = int(input())
for i in range(N):
    sum = 0
    value = list(input())
    for v in value:
        for d in Dic:
            if int(v) == d:
                sum += Dic[d]
    print(sum, "leds")