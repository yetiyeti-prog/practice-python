import random
import string
import sys

MAGIC_NUMBER_LENGTH = 4


def cows_and_bulls():
    playing = True
    guesses = 0
    magic_number = random.choices(string.digits, k=MAGIC_NUMBER_LENGTH)
    print("Let's play a game of Cowbull!")  # explanation
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")
    while playing:
        user_number = input("Guess the Magic Number: ")
        if user_number == "exit":
            sys.exit()
        cows = 0
        bulls = 0
        for i in range(MAGIC_NUMBER_LENGTH):
            if user_number[i] == magic_number[i]:
                cows += 1
            else:
                bulls += 1
        guesses += 1
        print("Cows:{} Bulls:{}".format(cows, bulls))
        if cows == MAGIC_NUMBER_LENGTH:
            print("You win the game.!")
            sys.exit()
        elif bulls == MAGIC_NUMBER_LENGTH:
            print("You lose the game! Magic Number was {}".format(''.join(magic_number)))
            sys.exit()
        else:
            print("Not a quiet good guess - try again.")


if __name__ == '__main__':
    cows_and_bulls()
