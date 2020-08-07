import math
data = int(input())
count = (math.pow(1.618033988749895, data) - math.pow(-0.6180339887498949, data)) / math.sqrt(5)
print(format(count, ".1f"))