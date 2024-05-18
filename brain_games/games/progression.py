import random


TASK = 'What number is missing in the progression?'
MIN_FIRST_NUMBER = 1
MAX_FIRST_NUMBER = 10
MIN_LENGTH = 10
MAX_LENGTH = 15
MIN_STEP = 2
MAX_STEP = 6


def generate_progression():
    first_number = random.randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
    next_number = first_number
    progression = [first_number]
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    step = random.randint(MIN_STEP, MAX_STEP)
    while len(progression) <= length:
        next_number += step
        progression.append(next_number)
    last_index = len(progression) - 1
    random_index = random.randint(1, last_index)
    correct_answer = str(progression[random_index])
    progression[random_index] = '..'
    return progression, correct_answer


def generate_question():
    hidden_progression = generate_progression()
    progression, correct_answer = hidden_progression
    question = ' '.join(str(item) for item in progression)
    return question, correct_answer
