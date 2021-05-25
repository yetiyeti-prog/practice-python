import string
import random
from random import randint

SPECIAL_CHARACTERS = ["%", "@", "!", "^", "&", "*"]

def create_password(number_of_letters):
    password_list = []
    digits = randint(0, 9)
    password_list.extend(random.choices(SPECIAL_CHARACTERS, k=1))
    random_strings = random.choices(string.ascii_uppercase +
                                    string.digits, k=number_of_letters-2)
    password_list.extend(random_strings)
    password_list.append(str(digits))
    print("Password List:{}".format(password_list))
    return password_list


def password_generator():
    print("Welcome to Password Generator")
    print("Password will have at-least 1 digit and 1 special character")
    retry = True
    while retry:
        number_of_letters = int(input("Enter number of letter of password: "))
        password_list = create_password(number_of_letters)
        print("Password:{}".format("".join(password_list)))
        value = input("Do you want to Continue ? y/n : ")
        retry = value == "y"


if __name__ == '__main__':
    password_generator()
