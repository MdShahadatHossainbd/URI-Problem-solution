N = int(input())
for j in range(N):
    text = input()
    code = int(input())
    r = ""

    if code == 0:
        r += text
    else:
        for i in text:
            de = ord(i) - code
            if de < ord("A"):
                de += 26
            r += chr(de)
    print(r)