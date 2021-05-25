def find_max(one, two, three):
    if one > two and one > three:
        return one
    elif two > one and two > three:
        return two
    else:
        return three


def get_max():
    one = 11111
    two = 11111
    three = 43211
    max_number = find_max(one, two, three)
    print("Max Number is :{}".format(max_number))


if __name__ == '__main__':
    get_max()
