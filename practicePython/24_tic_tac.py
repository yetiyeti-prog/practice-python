def print_horizontal_border(board_length):
    print(" --- " * board_length)


def print_vertical_border(board_length):
    print("|    " * (board_length + 1))


def tic_tac_print_board():
    board_length = int(input("Enter the board length for TicTac: "))
    for i in range(board_length):
        print_horizontal_border(board_length)
        print_vertical_border(board_length)
    print_horizontal_border(board_length)


if __name__ == '__main__':
    tic_tac_print_board()
