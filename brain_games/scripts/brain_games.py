import brain_games.scripts.cli as cli


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    return name


if __name__ == '__main__':
    main()
