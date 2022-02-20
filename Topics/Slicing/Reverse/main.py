# the following line reads the list from the input; do not modify it, please
numbers = [int(num) for num in input().split()]
# print(numbers)
start_index = 16
stop_index = 3
steps = -1
print(numbers[start_index:stop_index:steps])  # the line with an error