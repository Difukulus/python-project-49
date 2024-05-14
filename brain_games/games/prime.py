import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_question():
    random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = random_number
    correct_answer = ''
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
    if random_number:
        correct_answer += 'yes'
    else:
        correct_answer += 'no'
    return question, correct_answer
