import random
import sys

import prompt

sys.path.append("/home/nikon/test/edu/projects/python-project-49/brain_games/scripts/")
import brain_games.cli as cli


def main():
    name = cli.welcome_user()
    wins = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    while wins < 3:
        rand = random.randint(0, 99)
        print(f'Question: {rand}')
        ans = prompt.string('Your answer: ')
        result = is_prime(rand) and 'yes' or 'no'

        if result == ans:
            print('Correct!')
            wins += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{result}.'")
            print(f"Let's try again, {name}!")
            break
    
    if wins == 3:
        print(f'Congratulations, {name}!')


def is_prime(count):
    prime = [2, 3, 5, 7]
    for i in prime:
        if count % i == 0 and count != i:
            return False
    return True


if __name__ == '__main__':
    main()