# Example 12: Queen's Attack Range
# Read the input data
position = input("Enter the position of the queen (e.g., e2): ")

# Initialize the chessboard
board = [['.'] * 8 for _ in range(8)]

# Convert position to board indices
col = ord(position[0]) - ord('a')
row = 8 - int(position[1])

# Mark the queen's position
board[row][col] = 'Q'

# Mark the rows and columns
for i in range(8):
    if i != row:
        board[i][col] = '*'
    if i != col:
        board[row][i] = '*'

# Mark the diagonals
for i in range(1, 8):
    if row + i < 8 and col + i < 8:
        board[row + i][col + i] = '*'
    if row - i >= 0 and col - i >= 0:
        board[row - i][col - i] = '*'
    if row + i < 8 and col - i >= 0:
        board[row + i][col - i] = '*'
    if row - i >= 0 and col + i < 8:
        board[row - i][col + i] = '*'

# Print the chessboard
for row in board:
    print(" ".join(row))
