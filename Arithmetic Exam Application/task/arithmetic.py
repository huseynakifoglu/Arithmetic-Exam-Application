# write your code here
import random


def easy_task():
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


def difficult_task():
    number = random.randint(11, 29)
    answer = number * number
    return [number, answer]


counter, r = 0, 0
response = ''
result = 0

difficulty = input("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
""")
# print(f'Difficulty is: {difficulty}')
wrong_format_messages = ['Incorrect format.', 'Wrong format! Try again.']


def ask_difficulty():
    if difficulty == '1':
        chosen_difficulty = 'easy'
    elif difficulty == '2':
        chosen_difficulty = 'difficult'
    else:
        chosen_difficulty = 'Incorrect format.'
    return chosen_difficulty


def save_file(content, filename):
    with open(filename, 'a') as file:
        file.write(content)
        return f'The results are saved in "{filename}".'


while counter < 5:

    if response not in wrong_format_messages and ask_difficulty() == 'easy':
        task = easy_task()
        print(task[0])
        result = task[1]
    elif response not in wrong_format_messages and ask_difficulty() == 'difficult':
        task = difficult_task()
        print(task[0])
        result = task[1]
    elif response in wrong_format_messages[0]:
        print(response)
    elif response in wrong_format_messages[1]:
        print(response)
        print(task[0])

    u_answer = input()
    if not u_answer.lstrip('-').isnumeric() and ask_difficulty() == 'difficult':
        response = 'Wrong format! Try again.'
        continue
    elif not u_answer.lstrip('-').isnumeric() and ask_difficulty() == 'easy':
        response = 'Incorrect format.'
        continue
    elif int(u_answer) == result:
        r += 1
        counter += 1
        response = 'Right!'
    elif int(u_answer) != result:
        counter += 1
        response = 'Wrong!'
    print(response)
save_result = input(f'Your mark is {r}/5 Would you like to save the result? Enter yes or no.\n')
positive_answers = ['YES', 'yes', 'Yes', 'y']
diff_level = ''
if save_result in positive_answers:
    if ask_difficulty() == 'easy':
        diff_level = '1 (simple operations with numbers 2-9)'
    elif ask_difficulty() == 'difficult':
        diff_level = '2 (integral squares of 11-29)'
    name = input("What is your name?\n")
    content = f'{name}: {r}/5 in level {diff_level}.\n'
    print(save_file(content, 'results.txt'))
elif save_result == 'no':
    exit()
# print(f'Your mark is {r}/{5} Would you like to save the result? Enter yes or no.')
