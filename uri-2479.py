list_names = []
well_behaved = 0
misbehaved = 0
for i in range(int(input())):
    behaved, names = input().split()
    list_names.append(names)
    if behaved == "+":
        well_behaved += 1
    else:
        misbehaved += 1
print("\n".join(sorted(list_names)))
print("Se comportaram: {} | Nao se comportaram: {}".format(well_behaved, misbehaved))