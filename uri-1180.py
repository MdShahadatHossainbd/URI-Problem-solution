n = int(input())
x = input().split()
y = min(map(int, x))
print("Menor valor:", y)
print("Posicao:", x.index(str(y)))