def read_file_and_return_list(filename):
    temp_list = []
    with open(filename, 'r') as f:
        for lines in f.readlines():
            line = lines.strip()
            temp_list.append(line)
    return temp_list


def file_overlap():
    happy_list = read_file_and_return_list("happy.txt")
    prime_list = read_file_and_return_list("prime.txt")
    overlap_list = [i for i in happy_list if i in prime_list]
    print("Overlapping List :{}".format(overlap_list))


if __name__ == '__main__':
    file_overlap()
