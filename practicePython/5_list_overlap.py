__author__ = 'yetiyeti-prog'


def list_overlap():
    list_1 = [2, 4, 6, 1, 7, 8, 3, 31, 62, 7, 0, 1]
    list_2 = [4, 5, 7, 1, 7, 3, 0]
    overlapping_list = list({x for x in list_1 if x in list_2})
    print("Type :{} Overlapping List:{}".format(type(overlapping_list), overlapping_list))


if __name__ == '__main__':
    list_overlap()