import brain_games
import random
import prompt
import cli


def game():
    name = brain_games.main()
    wins = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while wins < 3:
        rand = random.randint(0, 99)
        print(f'Question: {rand}')
        ans = prompt.string('Your answer: ')
        result = rand % 2 == 0 and 'yes' or 'no'

        if result == ans:
            print('Correct!')
            wins += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{result}.'")
            print(f"Let's try again, {name}!")
            break
    
    if wins == 3:
        print(f'Congratulations, {name}!')

if __name__ == '__main__':
    game()