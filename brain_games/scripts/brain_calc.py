import random

import prompt

import sys

sys.path.append("/home/nikon/test/edu/projects/python-project-49/brain_games/scripts/")
import brain_games.cli as cli


def main():
    name = cli.welcome_user()
    wins = 0
    print('What is the result of the expression?')

    while wins < 3:
        oper = random.choice(['-', '+', '*'])
        first = random.randint(0, 20)
        second = random.randint(0, 20)
        quest = f'{first} {oper} {second}'
        print(f'Question: {quest}')
        ans = prompt.string('Your answer: ')
        result = eval(quest)

        if str(result) == str(ans):
            print('Correct!')
            wins += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{result}.'")
            print(f"Let's try again, {name}!")
            break
    
    if wins == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()