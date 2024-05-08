import random


TASK = 'What is the result of the expression?'


def generate_question():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    equation = f'{number1} {operator} {number2}'
    return equation


def ask_question(equation):
    print(f'Question: {equation}')


def result(equation):
    return str(eval(equation))
