n = int(input())
for i in range(n):
    data = input().split()
    x = data[0]
    if x == "Thor":
        print("Y")
    else:
        print("N")

"""
for i in range(int(input(""))):
    print("Y" if input("").split()[0].lower() == "thor" else "N")
"""
