A = input().split()
B = float(A[0])
final = float(A[1])
percentage = ((final * 100) / B) - 100
print(format(percentage, ".2f") + "%")