__author__ = 'yetiyeti-prog'


def odd_even():
    num = int(input("Enter a number to check: "))
    check = int(input("Enter a number to divide by: "))

    if num % check == 0:
        print("{} divides by {}".format(num, check))
    else:
        print("{} does not divide by {}".format(num, check))

    if num % 4 == 0:
        print("{} is divisible by 4 and an even Number30".format(num))
    elif num % 2 == 0:
        print("{} is an even Number".format(num))
    else:
        print("{} is an odd Number".format(num))


if __name__ == '__main__':
    odd_even()