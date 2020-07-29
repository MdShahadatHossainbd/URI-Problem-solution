loops = int(input())
for i in range(loops):
    data = input().split()
    n = input().split()
    if (int(n[0]) + int(n[1])) % 2 == 0:
        if data[1] == "PAR":
            print(data[0])
        else:
            print(data[2])
    else:
        if data[1] == "IMPAR":
            print(data[0])
        else:
            print(data[2])