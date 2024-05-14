import prompt


GAME_ROUNDS = 3


def welcome_user():
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def start(game):
    name = welcome_user()
    print(game.TASK)
    cnt = 0
    while cnt < GAME_ROUNDS:
        question, correct_answer = game.generate_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            cnt += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer \
was '{correct_answer}'.\nLet\'s try again, {name}!")
            break
        if cnt == 3:
            print(f'Congratulations, {name}!')
