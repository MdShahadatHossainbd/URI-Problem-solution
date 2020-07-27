A, B = list(map(int, input().split()))
result = (A + B) * (B - A + 1) / 2
print(int(result))