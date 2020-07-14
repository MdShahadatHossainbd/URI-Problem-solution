value = int(input())

count = 0

while True:
    if(value%2 != 0):
        count += 1
        print(value)
    value += 1
    if(count == 6):
        break