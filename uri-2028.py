case = 0
while True:
    try:
        data = int(input())
    except EOFError:
        break
    case += 1
    list_number = ["0"]
    if data == 0:
        print("Case {}: 1 number\n0".format(case))
    else:
        for i in range(data + 1):
            for j in range(i):
                list_number.append(str(i))

        print("Case {}: {} number\n{}".format(case, len(list_number), " ".join(list_number)))
    print()