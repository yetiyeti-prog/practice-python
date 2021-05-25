def palindrome(input_string):
    length_of_string = len(input_string)
    end_pointer = length_of_string - 1
    for i in range(length_of_string):
        if input_string[i] == input_string[end_pointer]:
            end_pointer -= end_pointer
            if i == end_pointer:
                print("Input String: {} is a Palindrome String.".format(input_string))
            continue
        else:
            break


def palindrome_improved(input_string):
    reversed_string = input_string[::-1]
    print("-------------------------------------Alternate Solution----------------------------------------------")
    print("InputString:{} ReversedString:{}".format(input_string, reversed_string))
    if input_string == reversed_string:
        print("{} is a Palindrome".format(input_string))
    else:
        print("{} is not a Palindrome.".format(input_string))



if __name__ == '__main__':
    input_string = input("Enter a String to check for Palindrome: ")
    palindrome(input_string)
    palindrome_improved(input_string)
