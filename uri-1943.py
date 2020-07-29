k = int(input())
if k == 1:
    print("Top 1")
elif k in range(2, 4):
    print("Top 3")
elif k in range(4, 6):
    print("Top 5")
elif k in range(6, 11):
    print("Top 10")
elif k in range(11, 26):
    print("Top 25")
elif k in range(26, 51):
    print("Top 50")
elif k in range(51, 101):
    print("Top 100")