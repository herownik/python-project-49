import sys

sys.path.append("/home/nikon/test/edu/projects/python-project-49/brain_games/scripts/")

import brain_games.cli as cli


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    return name


if __name__ == '__main__':
    main()
