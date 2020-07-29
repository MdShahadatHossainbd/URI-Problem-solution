n, x = map(int, input().split())
if x in range(0, 3):
    print("nova")
elif x in range(3, 97):
    if n > x:
        print("minguante")
    else:
        print("crescente")
else:
    print("cheia")