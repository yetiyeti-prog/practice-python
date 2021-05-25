import sys


def validate_input(users_input):
    if users_input in [0, 1]:
        print("Number : {} is Not a Prime".format(users_input))
        sys.exit()


def prime():
    users_input = int(input("Enter a number: "))
    validate_input(users_input)
    is_prime = True
    for i in range(2, users_input):
        if users_input % i == 0:
            is_prime = False
    print("Number : {} Prime : {}".format(users_input, is_prime))


if __name__ == '__main__':
    prime()
