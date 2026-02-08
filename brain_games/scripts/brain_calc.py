import brain_games.scripts.brain_games as brain_games
import random
import prompt


def main():
    name = brain_games.main()
    wins = 0
    print('What is the result of the expression?')

    while wins < 3:
        opers = ['-', '+', '*']
        oper = random.randint(0,2)
        first = random.randint(0, 20)
        second = random.randint(0, 20)
        quest = f'{first} {opers[oper]} {second}'
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