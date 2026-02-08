import random

import prompt

import brain_games.scripts.brain_games as brain_games


def main():
    name = brain_games.main()
    wins = 0
    print('What number is missing in the progression?')

    while wins < 3:
        opers = ['-', '+', '*']
        elem = random.randint(0, 9)
        start = random.randint(0, 20)
        step = random.randint(0, 20)
        length = 10
        arr = [start + step * i for i in range(length)]
        result = arr[elem]
        arr[elem] = '..'
        print(f'Question: {arr}')
        ans = prompt.string('Your answer: ')

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