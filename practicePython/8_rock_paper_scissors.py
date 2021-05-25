import sys

ROCK = "r"
PAPER = "p"
SCISSORS = "s"


def compare(user_1_choice, user_2_choice, user_1, user_2):
    if user_1_choice == user_2_choice:
        print("Its a Tie")
    elif user_1_choice == "r":
        if user_2_choice == "p":
            print("{} Wins : Paper Wins".format(user_2))
        else:
            print("{} Wins : Rock Wins".format(user_1))
    elif user_1_choice == "p":
        if user_2_choice == "s":
            print("{} Wins : Scissors Wins".format(user_2))
        else:
            print("{} Wins : Papers Wins".format(user_1))
    elif user_1_choice == "s":
        if user_2_choice == "r":
            print("{} Wins : Rock Wins".format(user_2))
        else:
            print("{} Wins : Scissors Wins".format(user_1))


def validate_continue(retry):
    return retry == "y"


def rock_paper_scissors():
    retry = "y"
    user_1 = input("Enter your name Player1: ")
    user_2 = input("Enter your name Player2: ")
    while retry == "y":
        print("Welcome to Game of Rock Papers Scissors")
        user_1_choice = input("Enter your choice - Player 1 - Rock/Paper/Scissor: ")
        user_1_choice = validate_users_choice(user_1_choice)
        user_2_choice = input("Enter your choice - Player 2 - Rock/Paper/Scissor: ")
        user_2_choice = validate_users_choice(user_2_choice)
        compare(user_1_choice, user_2_choice, user_1, user_2)
        retry = input("Do you want to Continue: y/n: ")
        retry = retry if validate_continue(retry) else sys.exit()


def validate_users_choice(user_choice):
    while 1:
        if user_choice in [ROCK, PAPER, SCISSORS]:
            break
        else:
            user_choice = input("Enter Again (r / p / s): ")
    return user_choice


if __name__ == '__main__':
    rock_paper_scissors()
