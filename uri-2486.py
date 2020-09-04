vitamin_C = {"suco": 120, "morango": 85, "mamao": 85, "goiaba": 70, "manga": 56, "laranja": 50, "brocolis": 34}
while True:
    loops = int(input())
    if loops == 0:
        break
    total = 0
    for i in range(loops):
        data = input().split()
        total += vitamin_C[data[1]] * int(data[0])
    if total in range(110, 131):
        print(total, "mg")
    elif total in range(0, 110):
        print("Mais", 110 - total, "mg")
    else:
        print("Menos", total - 130, "mg")