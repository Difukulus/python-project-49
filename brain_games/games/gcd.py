import random
import math


TASK = 'Find the greatest common divisor of given numbers.'
START = 1
STOP = 50


def generate_question():
    number1 = random.randint(START, STOP)
    number2 = random.randint(START, STOP)
    question = f'{number1} {number2}'
    correct_answer = str(math.gcd(number1, number2))
    return question, correct_answer
