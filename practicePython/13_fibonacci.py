def fibo():
    range_of_numbers = int(input("Enter the total numbers for Fibonacci series: "))
    fibo_list = [0, 1]
    i = 1
    while len(fibo_list) < range_of_numbers:
        fibo_list.append(fibo_list[i] + fibo_list[i - 1])
        i += 1

    print("Fibonacci List:{}".format(fibo_list))


if __name__ == '__main__':
    fibo()
