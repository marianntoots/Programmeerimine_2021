
def get_col_items(board, col):
    items = []
    for row in board:
        items.append(row[col])
    return items


def get_box_items(board, row, col):
    boxI = row // 3
    boxJ = col // 3
    items = []
    for i in range(boxI*3, (boxI+1)*3):
        items.extend(board[i][boxJ*3:(boxJ+1)*3])
    return items


filename = input("Sisesta kontrollitava lahenduse failinimi: ")
sudoku_board = []
with open(filename) as f:
    for line in f:
        sudoku_board.append(line.split())

correct = True
for row in range(9):
    for col in range(9):
        item = sudoku_board[row][col]
        if int(item) not in range(1, 10):
            print("Sisestatud sudoku lahendus ei ole õige", item)
            correct = False
        if (sudoku_board[row].count(item) > 1 or
                get_col_items(sudoku_board, col).count(item) > 1 or
                get_box_items(sudoku_board, row, col).count(item) > 1):
            print("Sama number ", row+1, ", veerus", col+1,
                  ", kastis", row//3+1, "/", col//3+1,
                  ", element:", item)
            correct = False

if correct:
    print("Sisestatud faili lahendus on korrektne")
else:
    print("Sisestatud lahendus ei ole korrektne")
