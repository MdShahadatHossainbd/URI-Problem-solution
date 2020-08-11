data = input()
vowels = []
for char in data:
    if char in ["a", "e", "i", "o", "u"]:
        vowels.append(char)
if vowels == vowels[::-1]:
    print("S")
else:
    print("N")