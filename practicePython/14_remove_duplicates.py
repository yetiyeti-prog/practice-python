def remove_duplicates(input_list):
    print("input List:{}".format(input_list))
    input_set = set(input_list)
    removed_duplicate_list = list(input_set)
    print("Duplicates Removed List:{}".format(removed_duplicate_list))


def remove_duplicates_other_way(input_list):
    removed_duplicate_list = []
    for i in input_list:
        if i not in removed_duplicate_list:
            removed_duplicate_list.append(i)
    print("Duplicates Removed list:{}".format(removed_duplicate_list))
    removed_duplicate_list.sort()
    print("Sorted List:{}".format(removed_duplicate_list))


if __name__ == '__main__':
    input_list = [2, 5, 7, 12, 15, 32, 424, 23, 32, 7, 1, 5]
    remove_duplicates(input_list)
    remove_duplicates_other_way(input_list)
