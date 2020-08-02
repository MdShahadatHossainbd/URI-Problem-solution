while True:
    try:
        value = float(input())
        radius = float(input()) / 2
    except EOFError:
        break
    area_base = 3.14 * radius * radius
    print("ALTURA = {}".format(format(value / area_base, ".2f")))
    print("AREA = {}".format(format(area_base, ".2f")))