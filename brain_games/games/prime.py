import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question():
    random_number = random.randint(1, 100)
    return random_number


def ask_question(random_number):
    print(f'Question: {random_number}')


def is_prime(random_number):
    if random_number == 1:
        random_number = False
        return random_number
    i = 2
    while i <= random_number // 2:
        if random_number % i == 0:
            random_number = False
            break
        i += 1
    else:
        random_number = True
    return random_number


def result(random_number):
    if is_prime(random_number):
        return 'yes'
    return 'no'
