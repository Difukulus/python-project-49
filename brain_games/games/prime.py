import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question():
    random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = random_number
    correct_answer = 'yes' if is_prime(random_number) else 'no'
    return question, correct_answer
