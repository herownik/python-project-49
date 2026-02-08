import math
import random
import sys

import prompt

sys.path.append("/home/nikon/test/edu/projects/python-project-49/brain_games/scripts/")
import brain_games.cli as cli


def main():
    name = cli.welcome_user()
    wins = 0
    print('Find the greatest common divisor of given numbers.')

    while wins < 3:
        first = random.randint(0, 100)
        second = random.randint(0, 100)
        print(f'Question: {first} {second}')
        ans = prompt.string('Your answer: ')
        result = math.gcd(first, second)

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