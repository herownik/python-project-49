import brain_games.scripts.brain_games as brain_games
import random
import prompt
import math


def main():
    name = brain_games.main()
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