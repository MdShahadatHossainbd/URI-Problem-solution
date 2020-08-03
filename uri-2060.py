loops = int(input())
data = input().split()
second = 0
third = 0
fourth = 0
fifth = 0
for j in map(int, data):

    if j % 2 == 0:
        second += 1
    if j % 4 == 0:
        fourth += 1
    if j % 3 == 0:
        third += 1
    if j % 5 == 0:
        fifth += 1
print(second, "Multiplo(s) de 2")
print(third, "Multiplo(s) de 3")
print(fourth, "Multiplo(s) de 4")
print(fifth, "Multiplo(s) de 5")