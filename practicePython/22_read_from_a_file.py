def read_from_a_file():
    counter = {}
    with open("temp_file.txt", 'r') as f:
        line_number = 0
        for lines in f.readlines():
            print("Line{}:{}".format(line_number, lines))
            line = lines.strip()
            if line in counter:
                counter[line] += 1
            else:
                counter[line] = 1
            line_number += 1
    print("LineNumbers:{} NameCounter:{}".format(line_number, counter))


if __name__ == '__main__':
    read_from_a_file()
