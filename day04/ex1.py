list_input = open('input.txt', 'r').read().split('\n')

list_board = []
list_drawn = [int(i) for i in list_input[0].split(",")]

current = []
for element in list_input[2:]:
    if len(element) > 0:
        current.append([int(i) for i in element.split(" ") if len(i) > 0 ])
    else:
        list_board.append(current)
        current = []
list_board.append(current)

nb_board = len(list_board)
line = len(list_board[0])
column = len(list_board[0][0])
list_check_board = [[[0] * column for j in range(line)] for i in range(nb_board)]

def check_winning(board):
    for line in board:
        if (all(map(bool, line))):
            return True
    for col in range(column):
        found = False
        for line in board:
            if line[col]:
                found = True
            else:
                found = False
                break
        if found:
            return True
    return False

nb_pos = 0
won = False
while not won and nb_pos < len(list_drawn):
    for pos, board in enumerate(list_board):
        for row in range(line):
            for col in range(column):
                if board[row][col] == list_drawn[nb_pos]:
                    list_check_board[pos][row][col] = 1
                if check_winning(list_check_board[pos]):
                    winner = pos
                    won = True
                    nb_won = list_drawn[nb_pos]
                    break
    nb_pos += 1

def calculate_score(check_board, board, nb_won):
    unmarked = 0
    for row in range(line):
        for col in range(column):
            if check_board[row][col] == 0:
                unmarked += board[row][col]

    return nb_won * unmarked

print(calculate_score(list_check_board[winner], list_board[winner], nb_won))