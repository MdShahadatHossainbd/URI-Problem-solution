bills = [200, 150, 120, 110, 105, 102, 100, 70, 60, 55, 52, 40, 30, 25, 22, 20, 15, 12, 10, 7,  4]
while True:
    n = input().split()
    if int(n[0]) + int(n[1]) == 0:
        break
    if int(n[1]) - int(n[0]) in bills:
        print("possible")
    else:
        print("impossible")