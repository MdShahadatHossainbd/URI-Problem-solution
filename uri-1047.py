hi, mi, hf, mf = map(int, input().split())
if hf == hi == mi == mf:
    hour, minute = 24, 0
else:
    if mf >= mi:
        minute = mf - mi
    else:
        minute = 60 - abs(mf - mi)
        hf -= 1
    if hf >= hi:
        hour = hf - hi
    else:
        hour = 24 - abs(hf - hi)
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hour, minute))