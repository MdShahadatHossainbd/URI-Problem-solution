l = []
for i in range(20):
    N = int(input())
    l.append(N)
positive = 0
for j in l[::-1]:
    print("N[%d] = %d" %(positive,j))
    positive += 1