# put your python code here
import math


def fourth_root(num):
    # return math.log(num, 4)
    return math.sqrt(math.sqrt(num))


u_input = float(input())
print(fourth_root(u_input))
