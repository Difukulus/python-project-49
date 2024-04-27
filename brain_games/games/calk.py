import random


task = 'What is the result of the expression?'


def generate_question():
    num = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    equation = f'{num} {operator} {num2}'
    return equation


def ask_question(equation):
    print(f'Question: {equation}')
    return equation


def result(equation):
    return str(eval(equation))
