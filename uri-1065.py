list = []
count = 0

for i in range(0,5):
    n = int(input())
    list.append(n)

for i in range(0,5):
    if(list[i]%2==0):
        count = count+1

print(count,"valores pares")