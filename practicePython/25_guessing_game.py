import random
import sys


def guessing_game():
    print("Consider a number in your mind. Code will try to guess it")
    print("After displaying the game you can choose if the number was too high or too low or its correct")
    random_number = random.randint(0, 100)
    start = 0
    end = 100
    count = 0
    while True:
        print("Guessed Number is :{}".format(random_number))
        print("Enter the option from the following")
        print("1. Too High")
        print("2. Too Low")
        print("3. Correct.!")
        count += 1
        user_input = int(input())
        if user_input == 1:
            end = random_number
        elif user_input == 2:
            start = random_number
        else:
            print("Number Found is {}. It took only {} tries".format(random_number, count))
            sys.exit()
        random_number = (start + end) // 2


if __name__ == '__main__':
    guessing_game()
