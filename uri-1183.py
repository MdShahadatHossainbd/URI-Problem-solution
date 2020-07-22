# No submit
soma_ou_media = input()
matriz = []

for i in range(12):
    for j in range(12):
        valor = float(input())
        if i < j:
            matriz.append(valor)

if soma_ou_media == "S":
    print(("%.1f")%(sum(matriz)))
else:
    print(("%.1f")%(sum(matriz)/len(matriz)))

"""
soma_ou_media = input()
matriz = []
pos = 0

for i in range(12):
    linha = []
    for j in range(12):
        if i < j:
            valor = "XXXX"
        else:
            valor = float(input())
        linha.append(valor)
    matriz.append(linha)
    pos += 1
'''
if soma_ou_media == "S":
    print(("%.1f")%(sum(matriz)))
else:
    print(("%.1f")%(sum(matriz)/len(matriz)))

print(matriz)
'''
for linhas in range(12):
    for colunas in range(12):
        print("%6s"% (matriz[linhas][colunas]), end=" ")
    print("\n")
"""