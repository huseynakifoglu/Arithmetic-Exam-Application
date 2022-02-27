import math

u_input = int(input())


def formula(x):
    result = round((1 / (1 + math.exp(-x))), 2)
    return result


print(formula(u_input))
