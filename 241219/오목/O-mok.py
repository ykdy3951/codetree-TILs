def read_input():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    board = [list(map(int, line.split())) for line in data]
    return board

def check_five_in_a_row(board, x, y, dx, dy):
    color = board[x][y]
    count = 0

    for i in range(5):
        nx, ny = x + i * dx, y + i * dy
        if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
            count += 1
        else:
            break

    if count == 5:
        before_x, before_y = x - dx, y - dy
        after_x, after_y = x + 5 * dx, y + 5 * dy

        if (0 <= before_x < 19 and 0 <= before_y < 19 and board[before_x][before_y] == color) or \
           (0 <= after_x < 19 and 0 <= after_y < 19 and board[after_x][after_y] == color):
            return False

        return True

    return False

def find_winner(board):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

    for x in range(19):
        for y in range(19):
            if board[x][y] != 0:
                for dx, dy in directions:
                    if check_five_in_a_row(board, x, y, dx, dy):
                        center_x = x + 2 * dx
                        center_y = y + 2 * dy
                        return board[x][y], center_x + 1, center_y + 1

    return 0, -1, -1


def main():
    board = read_input()
    winner, row, col = find_winner(board)

    if winner:
        print(winner)
        print(row, col)
    else:
        print(0)

if __name__ == "__main__":
    main()
