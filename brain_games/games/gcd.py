import random


TASK = 'Find the greatest common divisor of given numbers.'


def generate_question():
    rand_number1 = random.randint(1, 50)
    rand_number2 = random.randint(1, 50)
    numbers_lst = [rand_number1, rand_number2]
    return numbers_lst


def ask_question(numbers_lst):
    print(f'Question: {numbers_lst[0]}, {numbers_lst[1]}')
    return numbers_lst


def result(numbers_lst):
    number1 = numbers_lst[0]
    number2 = numbers_lst[1]
    if number1 < number2:
        number1, number2 = number2, number1
    while number2 != 0:
        number1, number2 = number2, number1 % number2
    return str(number1)
