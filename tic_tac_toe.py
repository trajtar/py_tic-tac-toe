# """Funkcja sprawdzająca stan gry w 'kółko i krzyżyk'.
#
# Wejście:
#   board
#     Lista ciągów znaków reprezentujących planszę.
#     Dozwolone znaki:
#       '.' - niezajęte pole
#       'X' - pole zajęte przez gracza X
#       'O' - pole zajęte przez gracza O
#     Przykład:
#       board = [
#           'XO.",
#           '.0X',
#           '.X.',
#       ]
#
# Wyjście:
#   '.' jeśli nikt nie wygrywa
#   'X' jeśli X wygrywa
#   'Y' jeśli Y wygrywa
#   'XY' jeśli jest remis
#
# Zadania dodatkowe:
#   Zwróć False jeśli plansza jest niepoprawna (nie jest kwadratowa).
#   Napisz funkcję tak by działała niezależnie od rozmiaru planszy.
# """


# solution by: Tomek Rajtar
def state(board):
    result = ''
    board_size = len(board[0])
    rboard = []

    # check dimmensions first & create reversed board
    for line in board:
        rboard.append('')
        if len(line) != board_size:
            return False

    # fill reversed board
    for line in board:
        for i in range(0, board_size):
            rboard[i] += line[i]

    # print("Board: ", board)
    # print("RBoard: ", rboard)

    # create diagonals
    first_diagonal = ''
    second_diagonal = ''

    for i in range(0, board_size):
        first_diagonal += board[i][i]
        second_diagonal += board[i][board_size - 1 - i]

    # main loop
    for player in ('X', 'O'):

        # check rows
        for line in board:
            if line == player * board_size:
                if result.find(player) == -1:
                    result += player

        # check columns
        for line in rboard:
            if line == player * board_size:
                if result.find(player) == -1:
                    result += player

        # check diagonals
        if first_diagonal == player * board_size:
            if result.find(player) == -1:
                result += player

        if second_diagonal == player * board_size:
            if result.find(player) == -1:
                result += player

                # print(first_diagonal)
                # print(second_diagonal)

    if result == '':
        result = '.'

    return result
