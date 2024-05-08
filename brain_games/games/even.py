import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    random_number = random.randint(1, 100)
    return random_number


def ask_question(random_number):
    print(f'Question: {random_number}')
    return random_number


def is_even(random_number):
    return random_number % 2 == 0


def result(random_number):
    if is_even(random_number):
        return 'yes'
    return 'no'
