x = int(input())
z = 0
while True:
    z = int(input())
    if(z > x):
        break
sum = x
result = 1
while(sum < z):
    sum += x + result
    result += 1

print(result)