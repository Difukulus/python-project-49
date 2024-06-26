import random
from operator import add, sub, mul


TASK = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 10
OPERATORS = ('+', add), ('-', sub), ('*', mul)


def generate_question():
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    symbol, operator = random.choice(OPERATORS)
    question = f'{number1} {symbol} {number2}'
    correct_answer = str(operator(number1, number2))
    return question, correct_answer
