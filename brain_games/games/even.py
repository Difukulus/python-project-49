import random


task = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    num = random.randint(1, 100)
    return num


def ask_question(num):
    print(f'Question: {num}')
    return num


def is_even(num):
    return num % 2 == 0


def result(num):
    if is_even(num):
        return 'yes'
    return 'no'
