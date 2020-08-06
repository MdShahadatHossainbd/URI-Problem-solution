loops = int(input())
for i in range(loops):
    data = input().split()
    hour, minute, event = data
    if int(hour) < 10:
        hour = "0" + str(hour)
    if int(minute) < 10:
        minute = "0" + str(minute)
    if event == "1":
        print("{}:{} - A porta abriu!".format(hour, minute))
    else:
        print("{}:{} - A porta fechou!".format(hour, minute))