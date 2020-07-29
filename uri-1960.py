def Roman_numerals(x):
    n = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    m = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = ""
    for i in range(13):
        count = x // n[i]
        result += m[i] * count
        x -= n[i] * count
    return result

pages = int(input())
print(Roman_numerals(pages))