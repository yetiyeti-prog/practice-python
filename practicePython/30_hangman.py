import random
import sys

MAX_GUESSES = 6


def display_word(copy_word_list, input_list, user_input):
    found = False
    for i in range(len(copy_word_list)):
        if user_input == copy_word_list[i]:
            input_list[i] = user_input
            found = True
    print("".join(input_list))
    return found


def validate_if_already_guessed(input_list):
    return True if "_" not in input_list else False


def guess_word(word):
    print("Lets Play a game of Hangman.!")
    print("Here you need to guess a randomly generated word. you have max {} incorrect guesses".format(MAX_GUESSES))
    print("You can exit by typing exit at any prompt")
    word_list = list(word)
    copy_word_list = word_list
    input_list = list("_" * len(word_list))
    guessed_list = []
    count_of_guesses = 0
    while True:
        if count_of_guesses >= MAX_GUESSES:
            print("You have reached the Max Guesses:{}. Word was {}".format(MAX_GUESSES, word))
            break
        if validate_if_already_guessed(input_list):
            print("You have Guessed the word: {}.!".format(word))
            break
        user_input = input("Enter the Letter: ").upper()
        if user_input == "EXIT":
            sys.exit("User Exited.!")
        if user_input in guessed_list:
            print("Oops.! Already Guessed it.!")
            continue
        found = display_word(copy_word_list, input_list, user_input)
        if not found:
            count_of_guesses += 1
        guessed_list.append(user_input)
        print("You have {} incorrect guesses left".format(MAX_GUESSES - count_of_guesses))


def hangman():
    with open("sowpad_dictionary.txt", 'r') as f:
        words = list(f)
    while True:
        word = random.choice(words).strip()
        print("A word is Randomly Picked")
        guess_word(word)
        continue_game = input("Do you want to continue: y/n ").lower()
        if continue_game != "y":
            sys.exit("Exiting..! User does not want to continue.! ")


if __name__ == '__main__':
    hangman()
