import random


task = 'Find the greatest common divisor of given numbers.'


def generate_question():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    num_lst = [num1, num2]
    return num_lst


def ask_question(num_lst):
    print(f'Question: {num_lst[0]}, {num_lst[1]}')
    return num_lst


def result(num_lst):
    num1 = num_lst[0]
    num2 = num_lst[1]
    if num1 < num2:
        num1, num2 = num2, num1
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return str(num1)
