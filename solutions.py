
"""
Poniższe rozwiązania zostały napisane przez uczestników spotkania PyLadies w dniu 24 X 2016.
"""


# Adrian Wojtczak
def state(board):
    output = [] # Here we put characters which create a winning streak
    for i in range (0, len(board)): # loop checks our list of lists whether it's n x n dimension
        if len(board)!=len(board[i]):
            return False
            
    #Horizontal
    wasError = False #helps us determine if there was a mismatch in a streak we're looking for
    for i in range (0, len(board)):
        expected = board[i][0] # we declare what characters we wanna find -ex in line:'x.o', we look for 'x'es
        wasError = False
        for j in range (0,len(board)):
            if board[i][j]!=expected:# if there is a mismatch
                wasError=True       # we have an 'error'
        if wasError == False and expected != '.': # if there was no error -
            output.append(expected)         # -we put our expected char into the output
    #Vertical
    for i in range (0, len(board)):
        expected = board[0][i]
        wasError = False
        for j in range (0,len(board)):
            if board[j][i]!=expected:
                wasError = True
        if wasError == False and expected != '.':
            output.append(expected)
    #diagonal1
    expected = board[0][0] #expected char
    wasError = False
    for j in range (0,len(board)): #looking for a diagonal streak, we iterate both indexes with the same variable
        if board[j][j] != expected:
            wasError = True
    if wasError == False and expected != '.':
        output.append(expected)

    #diagonal2
    expected = board[len(board)-1][0]
    wasError = False
    for j in range (0,len(board)): #look for 2nd diag. streak - we look for indexes where one of them is decrementing
        if board[j][len(board)-1-j]!= expected:
            wasError = True
    if wasError == False and expected != '.':
        output.append(expected)
    #simple checking for what we've found
    if len(output) == 0:
        return '.'
    if len(output) == 1:
        if output[0] == 'X':
            return 'X'
        if output[0] == 'O':
            return 'O'
    else:
        if (output[0] =='X' and output[1] == 'O') or (output[1] == 'X' and output[0] == 'O'):
            return 'XO'
#
# END - good_bye
################################################



def state(board):

    size = len(board)
    for line in board:
        if len(line) != size:
            return False

    for player in ("X", "O"):
        # pionowo
        for i in range(size):
            if all([line[i] == player for line in board]):
                return player

        # poziomo
        for line in board:
                if line == player * size:
                    return player

        # ukośna gl-dp
        if all([board[i][i] == player for i in range(size)]):
            return player

        # ukośna gp-dl
        if all([board[i][size-1-i] == player for i in range(size)]):
                return player

    return '.'

################################################






def state(board):

    # Sprawdź czy tablica jest kwadratowa
    for row in board:
        if len(row) != len(board):
            return False

    # Utwórz nową listę, która będzie przechowywać wszystkie sekwencje i skopiuj sekwencje rzędów
    # z tablicy board
    sequences = board[:]

    # Dodaj sekwencje symboli odpowiadających kolumnom
    for index in range(0, len(board[0])):
        sequences.append('')
        for row in board:
            sequences[-1] += row[index]

    # Dodaj sekwencję symboli odpowiadającej przekątnej lewy górny róg -> prawy dolny róg
    sequences.append('')
    for index in range(len(board)):
        sequences[-1] += board[index][index]

    # Dodaj sekwencję symboli odpowiadającej przekątnej prawy górny róg -> lewy dolny róg
    sequences.append('')
    for index in range(len(board)):
        sequences[-1] += board[index][len(board) - 1 - index]

    # Utwórz zbiór, który będzie przechowywał symbole, które wygrały
    winners = set()

    # Sprawdź każdą sekwencję i jeśli składa się z takich samych symboli to dodaj ten symbol do listy winners
    for sequence in sequences:
        if len(set(sequence)) == 1:
            winners.add(sequence[0])

    # Jeżeli któraś z sekwencji zawiera same kropki i symbol kropki zostanie
    # dodany do zboru winners, usuń ją stamtąd
    winners.discard('.')

    # Sprawdź kto wygrał i zwróc odpowiedni symbol
    if len(winners) == 1:
        return winners.pop()
    elif len(winners) == 2:
        return 'XO'
    else:
        return '.'


