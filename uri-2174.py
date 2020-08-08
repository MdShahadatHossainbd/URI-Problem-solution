loops = int(input())
list1 = []
for i in range(loops):
    pomekon = input()
    list1.append(pomekon)
area = len(set(list1))
print("Falta(m)", 151 - area, "pomekon(s).")