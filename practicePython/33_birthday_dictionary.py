import sys
import json


def birthday_dictionary():
    input_dictionary = get_birthday_input()
    birthday_game(input_dictionary)


def get_birthday_input():
    # input_dictionary = {
    #     "Albert": "02-05-1992",
    #     "Jon": "01-06-1990",
    #     "Martin": "03-04-1880"
    # }
    with open("birthday.json", 'r') as f:
        input_dictionary = json.load(f)
    return input_dictionary


def update_data_and_json_file(input_dictionary):
    name = input("Enter a Name: ")
    birthday = input("Enter the birthday for {}: ".format(name))
    input_dictionary[name] = birthday
    with open("birthday.json", "w") as f:
        json.dump(input_dictionary, f)


def birthday_game(input_dictionary):
    while True:
        print("Welcome to the birthday dictionary.! We know the birthdays of ")
        print("\n".join(input_dictionary.keys()))
        print("Select from the following")
        print("1. Seek the birthday info.")
        print("2. Add/Update the birthday info.")
        print("exit. to exit")
        option = input()
        if option == "exit":
            sys.exit("Exiting.!")
        elif int(option) == 1:
            user_input = input("Who's birthday do you want to look up? ")
            if user_input not in input_dictionary.keys():
                sys.exit("Name Not Found.!")
            birthday = input_dictionary.get(user_input)
            print("{}'s birthday is on {}".format(user_input, birthday))
        elif int(option) == 2:
            update_data_and_json_file(input_dictionary)
        else:
            sys.exit("Exiting due to Wrong Option")


if __name__ == '__main__':
    birthday_dictionary()
