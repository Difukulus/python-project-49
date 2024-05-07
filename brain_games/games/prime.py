import random


task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question():
    num = random.randint(1, 100)
    return num


def ask_question(num):
    print(f'Question: {num}')


def is_prime(num):
    if num == 1:
        num = False
        return num
    i = 2
    while i <= num // 2:
        if num % i == 0:
            num = False
            break
        i += 1
    else:
        num = True
    return num


def result(num):
    if is_prime(num):
        return 'yes'
    return 'no'
