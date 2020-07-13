list1 = []
N = 6
count = 0
for i in range (0,N):
    list = input()
    list1.append(float(list))
for i in range(0,N):
    if list1[i] >=0:
        count =count+1
print(count,"valores positivos")