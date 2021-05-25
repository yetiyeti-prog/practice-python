import random
import string


# List - 2 4 5 6 8 9 11 12 33
# element - 11
# mid_element - 8 < 11 --> check in upper half

def search_element(element, sorted_list):
    start = 0
    end = len(sorted_list) - 1
    while True:
        mid = (start + end) // 2
        print("Start:{} Mid:{} End:{}".format(start, mid, end))
        if start > end or mid > end:
            print("Element:{} is not present in the list".format(element))
            break
        if sorted_list[mid] > element:
            print("{} > {}: element is in lower half".format(sorted_list[mid], element))
            end = mid - 1
        elif sorted_list[mid] < element:
            print("{} > {}: element is in Upper half".format(sorted_list[mid], element))
            start = mid + 1
        else:
            print("Element:{} is Present at {}".format(element, mid))
            break


def element_search():
    length_of_list = int(input("Enter the length of list: "))
    element = input("Enter an element to search in list: ")
    input_list = random.choices(string.digits, k=length_of_list)
    input_list.sort()
    print("Inputlist:{} Type:{}".format(input_list, type(input_list)))
    search_element(element, input_list)


if __name__ == '__main__':
    element_search()
    print("-------------------Alternate Way-----------------------")
    search_element(4343, [2, 4, 6, 7, 11, 44, 55, 77, 88, 99, 112, 4343, 5555])
