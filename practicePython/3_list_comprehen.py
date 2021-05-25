__author__ = 'yetiyeti-prog'
LESS_THAN_VALUE = 5


def list_comprehension():
    input_data = int(input("Enter the number of elements in list: "))
    list_input = []
    for i in range(input_data):
        list_input.append(int(input()))
    print("Input List:{}".format(list_input))
    print("Data < {} in Input List:{}".format(LESS_THAN_VALUE, [i for i in list_input if i < LESS_THAN_VALUE]))


if __name__ == '__main__':
    list_comprehension()
