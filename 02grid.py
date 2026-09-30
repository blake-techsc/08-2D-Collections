import random

rows = 5
columns = 6
board = []

treasure_row = random.randint(0, rows)
treasure_col = random.randint(0, columns)
print(treasure_row, treasure_col)

for row in range(rows):
    board.append([])
    for col in range(columns):
        board[-1].append("X")

print(board)

for i in board:
    print(i)

# print the board so it looks like:
# x x x x x x
# x x x x x x
# x x x x x x
# x x x x x x
# x x x x x x

# print("")
# for row in board:
#     for cell in row:
#         print(cell, end=" ")
#     print()
# print("")


# print the board so it looks like:
#   0 1 2 3 4 5
# 0 x x x x x x
# 1 x x x x x x
# 2 x x x x x x
# 3 x x x x x x
# 4 x x x x x x


print("")
def printBoard():
    print("  ", end = "")
    for i in range(len(board[0])):
        print(i, end = " ")
    print()
    for i in range(len(board)):
        print(i, end = " ")
        for r in board[i]:
            print(r, end = " ")
        print()
print("")

printBoard()
found = False
while not found:
    userrow = int(input("Enter the row you wish to check: "))
    usercol = int(input("Enter the column you wish to check: "))
    # we will assume we get ints and in range
    if userrow == treasure_row and usercol == treasure_col:
        print("Yay! You found it!")
        board[userrow][usercol] = "🐋"
        found = True
    else:
        # if we guess wrong - provide number saying how far away we are
        row_distance = abs(userrow - treasure_row)
        col_distance = abs(usercol - treasure_col)
        total_distance = row_distance + col_distance
        board[userrow][usercol] = total_distance

    printBoard()