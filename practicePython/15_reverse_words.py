def reverse_words():
    input_string = input("Enter a sentence: ")
    word_list = input_string.split()
    reversed_list = list(reversed(word_list))
    print("Input String :{} Reversed String:{} ".format(input_string, " ".join(reversed_list)))


if __name__ == '__main__':
    reverse_words()