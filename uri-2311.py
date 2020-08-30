loops = int(input())
for i in range(loops):
    name = input()
    difficulty = float(input())
    data = input().split()
    data_order = sorted(map(float, data))
    print(name, format(sum(data_order[1:-1]) * difficulty, ".2f"))