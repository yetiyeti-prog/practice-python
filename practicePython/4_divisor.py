__author__ = 'yetiyeti-prog'


def divisor():
    divisor_list = []
    number = int(input("Enter the number: "))
    for i in range(1, number):
        if number % i == 0:
            divisor_list.append(i)

    print("Divisors for number {} are : {}".format(number, divisor_list))


if __name__ == '__main__':
    divisor()
