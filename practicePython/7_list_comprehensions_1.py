def list_comprehensions_1():
    input_list = [1, 4, 4, 12, 43, 51, 33, 66]
    new_list = [x for x in input_list if x % 2 == 0]
    print("InputList:{}:NewList where element is even:{}".format(input_list, new_list))


if __name__ == '__main__':
    list_comprehensions_1()