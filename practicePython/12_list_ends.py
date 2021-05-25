def list_end():
    input_list = [2, 4, 5, 1, 7, 99, 23, 63]
    list_ends = [input_list[0], input_list[len(input_list) - 1]]
    print("Input List : {} \nList Ends :{}".format(input_list, list_ends))


if __name__ == '__main__':
    list_end()
