from random import randint
import sys

MIN_RANGE = 0
MAX_RANGE = 10


def get_users_input():
    users_inpput = int(input("Enter number between " + str(MIN_RANGE) + "-" + str(MAX_RANGE) + ": "))
    return validate_users_input(users_inpput)


def validate_users_input(users_input):
    while 1:
        if MAX_RANGE > users_input > MIN_RANGE:
            break
        else:
            users_input = int(input("Enter the number again: "))
    return users_input


def guess_number(users_input, magic_number):
    if magic_number > users_input:
        print("Magic Number is a bit higher.!")
    elif magic_number < users_input:
        print("Magic Number is a bit Lower.!")
    else:
        print("Bulls Eye..! You guessed it right.!")
        return False
    return True


def guessing_game():
    print("Welcome to Guessing Game")
    print("You need to guess numbers between 0 - 10")
    retry = "y"
    while retry == "y":
        magic_number = randint(0, 9)
        users_input = get_users_input()
        while guess_number(users_input, magic_number):
            users_input = get_users_input()
        retry = input("Do you want to Continue: y/n: ")
        retry = retry if retry == "y" else sys.exit()


if __name__ == '__main__':
    guessing_game()