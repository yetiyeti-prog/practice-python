def write_to_a_file():
    some_stupid_string = "Sameer\nRamesh\nSameer\nRamesh\nSameer\nRamesh\nGoku\nPoku\nVegeta"
    with open("temp_file.txt", 'w') as file:
        file.write(some_stupid_string)


if __name__ == '__main__':
    write_to_a_file()