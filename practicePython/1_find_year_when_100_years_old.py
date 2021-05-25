__author__ = 'yetiyeti-prog'
from datetime import datetime


def find_year():
    name = input("Enter your Name: ")
    age = input("Enter your age: ")
    year = 100 - int(age) + datetime.today().year
    print("{} will be 100 years old in the year {}".format(name, year))


if __name__ == '__main__':
    find_year()