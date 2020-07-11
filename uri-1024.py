loops = int(input())
for l in range(loops):
    value = input()
    value1 = ""
    for letter in value:
        if letter.isalpha():
            value1 += chr(ord(letter) + 3)
        else:
            value1 += letter
    final_value = value1[::-1]
    number_value= len(value1) // 2
    value_final = final_value[:number_value]
    for letter in final_value[number_value:]:
        value_final += chr(ord(letter) - 1)

    print(value_final)