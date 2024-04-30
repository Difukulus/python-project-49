import prompt


def welcome_user():
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def start(game):
    name = welcome_user()
    print(game.task)
    cnt = 0
    while cnt < 3:
        question = game.generate_question()
        game.ask_question(question)
        user_answer = prompt.string('Your answer: ')
        true_answer = game.result(question)
        if user_answer == true_answer:
            print('Correct!')
            cnt += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer \
was '{true_answer}'.\nLet\'s try again, {name}!")
            break
        if cnt == 3:
            print(f'Congratulations, {name}!')
