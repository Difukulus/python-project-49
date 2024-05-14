import random


TASK = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 10


def generate_question():
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(['+', '-', '*'])
    question = f'{number1} {operator} {number2}'
    correct_answer = str(eval(question))
    return question, correct_answer
