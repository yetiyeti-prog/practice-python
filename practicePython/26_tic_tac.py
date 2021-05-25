MATRIX_DIMENTION = 3


def is_winner(input_list):
    for i in range(0, MATRIX_DIMENTION):
        row = {input_list[i][0], input_list[i][1], input_list[i][2]}
        if len(row) == 1 and input_list[i][0] != 0:
            return input_list[i][0]
        column = {input_list[0][i], input_list[1][i], input_list[2][i]}
        if len(column) == 1 and input_list[0][i] != 0:
            return input_list[0][i]
    if input_list[1][1] == input_list[2][2] == input_list[0][0]:
        return input_list[1][1]
    if input_list[0][2] == input_list[1][1] == input_list[2][0]:
        return input_list[1][1]
    return 0


def fill_completed(input_list):
    for i in range(0, MATRIX_DIMENTION):
        for j in range(0, MATRIX_DIMENTION):
            if input_list[i][j] == 0:
                return False
    return True


def print_horizontal_border(board_length):
    print(" --- " * board_length)


def plot_current_position(input_list):
    for i in range(0, MATRIX_DIMENTION):
        print_horizontal_border(board_length=MATRIX_DIMENTION)
        print("| {} | {} | {} |".format(input_list[i][0], input_list[i][1], input_list[i][2]))
    print_horizontal_border(board_length=MATRIX_DIMENTION)


def generate_from_user_inputs():
    print("Lets Play a game of Tic-Tac-Toe !")
    input_list = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
    i = 1
    while True:
        print("------- Current Position -------")
        plot_current_position(input_list)
        winner = is_winner(input_list)
        if fill_completed(input_list) or winner != 0:
            return winner
        row = int(input("Enter the Row for placing your Xs or Ox like 1,2: "))
        column = int(input("Enter the Column for placing your Xs or Ox like 1,2: "))
        if i % 2 == 0:
            input_list[row][column] = 2 if input_list[row][column] == 0 else input_list[row][column]
        else:
            input_list[row][column] = 1 if input_list[row][column] == 0 else input_list[row][column]
        i += 1


def tic_tac_game():
    winner = generate_from_user_inputs()
    get_and_display_winner(winner)


def get_and_display_winner(winner):
    if winner == 1:
        print("Winner is Player {}".format(winner))
    elif winner == 2:
        print("Winner is Player {}".format(winner))
    else:
        print("This is Draw")


if __name__ == '__main__':
    tic_tac_game()
