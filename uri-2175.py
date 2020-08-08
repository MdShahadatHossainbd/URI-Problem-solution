data = input().split()
O = float(data[0])
B = float(data[1])
I = float(data[2])

if O < min(I, B):
    print("Otavio")
elif B < min(I, O):
    print("Bruno")
elif I < min(O, B):
    print("Ian")
else:
    print("Empate")