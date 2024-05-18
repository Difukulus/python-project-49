import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even(number):
    return number % 2 == 0


def generate_question():
    random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = random_number
    correct_answer = 'yes' if is_even(random_number) else 'no'
    return question, correct_answer
