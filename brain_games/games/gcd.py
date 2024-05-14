import random


TASK = 'Find the greatest common divisor of given numbers.'
START = 1
STOP = 50


def generate_question():
    number1 = random.randint(START, STOP)
    number2 = random.randint(START, STOP)
    question = f'{number1} {number2}'
    if number1 < number2:
        number1, number2 = number2, number1
    while number2 != 0:
        number1, number2 = number2, number1 % number2
    correct_answer = str(number1)
    return question, correct_answer
