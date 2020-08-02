value = {"ataque": 3, "pedra": 2, "papel": 1 }
for i in range(int(input())):
    jog1 = value[input()]
    jog2 = value[input()]
    if jog1 == jog2:
        if jog1 == 1:
            print("Ambos venceram")
        elif jog1 == 2:
            print("Sem ganhador")
        else:
            print("Aniquilacao mutua")
    elif jog1 > jog2:
        print("Jogador 1 venceu")
    else:
        print("Jogador 2 venceu")