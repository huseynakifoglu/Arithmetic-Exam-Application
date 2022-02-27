import math

a = int(input())
area = round((2 * math.sqrt(3) * a * a), 2)
vol = round(((1 / 3) * math.sqrt(2) * math.pow(a, 3)), 2)
print(f'{area} {vol}')
