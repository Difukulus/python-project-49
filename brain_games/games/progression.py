import random


TASK = 'What number is missing in the progression?'


def generate_progression(progression):
    last_index = len(progression) - 1
    random_index = random.randint(1, last_index)
    correct_answer = str(progression[random_index])
    progression[random_index] = '..'
    return progression, correct_answer


def generate_question():
    first_number = random.randint(1, 10)
    length = random.randint(10, 15)
    step = random.randint(2, 6)
    next_number = first_number
    progression = [first_number]
    while len(progression) <= length:
        next_number += step
        progression.append(next_number)
    hiden_progression = generate_progression(progression)
    progression, correct_answer = hiden_progression
    question = ' '.join(str(item) for item in progression)
    return question, correct_answer
