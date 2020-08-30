N = int(input())
totals = 0
totalb = 0
totala = 0
totalsa = 0
totalba = 0
totalaa = 0
for i in range(N):
    name = input()
    data = input().split()
    service, block, attack = int(data[0]), int(data[1]), int(data[2])
    data2 = input().split()
    servicea, blocka, attacka = int(data2[0]), int(data2[1]), int(data2[2])
    totals += service
    totalb += block
    totala += attack
    totalsa += servicea
    totalba += blocka
    totalaa += attacka
print("Pontos de Saque:", format(totalsa / totals * 100, ".2f"), "%.")
print("Pontos de Bloqueio:", format(totalba / totalb * 100, ".2f"), "%.")
print("Pontos de Ataque:", format(totalaa / totala * 100, ".2f"), "%.")