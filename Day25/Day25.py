
def dump_board(board):
    for line in board:
        print("".join(line))


def run_step(board):
    new_board = [['.' for x in range(len(board[0]))] for y in range(len(board))]

    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == '>':
                if x + 1 == len(board[0]):
                    if board[y][0] == '.':
                        new_board[y][0] = '>'
                        new_board[y][x] = '.'
                    else:
                        new_board[y][x] = '>'
                else:
                    if board[y][x+1] == '.':
                        new_board[y][x+1] = '>'
                        new_board[y][x] = '.'
                    else:
                        new_board[y][x] = '>'
            elif board[y][x] == 'v':
                new_board[y][x] = 'v'

    # print("Half step")
    # dump_board(new_board)

    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 'v':
                if y + 1 == len(board):
                    if new_board[0][x] == '.' and board[0][x] != 'v':
                        new_board[0][x] = 'v'
                        new_board[y][x] = '.'
                    else:
                        new_board[y][x] = 'v'
                else:
                    if new_board[y + 1][x] == '.' and board[y+1][x] != 'v':
                        new_board[y+1][x] = 'v'
                        new_board[y][x] = '.'
                    else:
                        new_board[y][x] = 'v'

    return new_board


def main():
    with open('input.txt') as my_file:
        input_lines = my_file.readlines()
    input_lines = [s.strip() for s in input_lines]
    line_count = len(input_lines)
    print(f"{line_count} lines read")

    board = []
    for line in input_lines:
        board.append([ch for ch in line])

    print(board)
    dump_board(board)

    columns = len(input_lines[0])
    rows = len(input_lines)

    print(f"{rows} rows, {columns} columns")

    board = input_lines

    step = 0
    while step < 100000:
        new_board = run_step(board)

        step += 1
        if board == new_board:
            print(f"\nafter {step} steps")
            dump_board(new_board)
            break
        board = new_board




if __name__ == '__main__':
    main()

