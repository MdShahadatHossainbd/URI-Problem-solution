p = input().split()
n = input().split()
next = int(p[0])
for i in n:
    if abs(int(i) - next) > int(p[0]):
        print("GAME OVER")
        break
    next = int(i)
else:
    print("YOU WIN")