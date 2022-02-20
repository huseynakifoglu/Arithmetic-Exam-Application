# write your code here
import random


def find_sum(a, b):
    return a + b


def find_diff(a, b):
    return a - b


def multiply(a, b):
    return a * b


def math_task():
    operations = ['+', '-', '*']
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    operation = random.choice(operations)
    if operation == '+':
        task = f'{a} {operation} {b}'
        result = a + b
    elif operation == '-':
        task = f'{a} {operation} {b}'
        result = a - b
    elif operation == '*':
        task = f'{a} {operation} {b}'
        result = a * b
    return [task, result]


counter, r, w = 0, 0, 0
response = ''
while counter < 5:
    if response != 'Incorrect format.':
        task = math_task()
        print(task[0])
        result = task[1]
    elif response == 'Incorrect format.':
        print(response)

    u_answer = input()
    if not u_answer.lstrip('-+').isnumeric():
        response = 'Incorrect format.'
        continue
    elif int(u_answer) == result:
        r += 1
        counter += 1
        response = 'Right!'
    elif int(u_answer) != result:
        w += 1
        counter += 1
        response = 'Wrong!'
    print(response)
print(f'Your mark is {r}/{5}')
