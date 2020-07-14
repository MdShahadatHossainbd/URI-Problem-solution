x = int(input())
y = int(input())
n=0
for i in range ((y+1),x):
    if (i%2==1):
        n += i
print(n)