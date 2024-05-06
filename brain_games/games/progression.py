import random


task = 'What number is missing in the progression?'


def generate_progression(progression):
    random_index = random.randint(1, len(progression) - 1)
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    return correct_answer, progression


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
    return hiden_progression


def ask_question(hiden_progression):
    correct_answer, progression = hiden_progression
    progression = ' '.join(str(item) for item in progression)
    print(f'Question: {progression}')


def result(hiden_progression):
    correct_answer, progression = hiden_progression
    return str(correct_answer)
