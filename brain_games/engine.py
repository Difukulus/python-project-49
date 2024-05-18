import prompt


ROUNDS_COUNT = 3


def welcome_user():
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def start(game):
    name = welcome_user()
    print(game.TASK)
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.generate_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if not user_answer == correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
