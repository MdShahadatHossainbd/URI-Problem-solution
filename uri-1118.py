N = 0
while N != 2:
    x, y = 0, 0
    while x < 2:
        nota = float(input())
        if nota < 0 or nota > 10:
            print("nota invalida")
        else:
            x += 1
            y += nota
    print("media = {}".format(format(y / 2, ".2f")))
    N = int(input("novo calculo (1-sim 2-nao)\n"))
    while N not in [1, 2]:
        N = int(input("novo calculo (1-sim 2-nao)\n"))