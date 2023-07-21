import sys

def is_safe(board, row, col):
    # Check if there is a queen in the same column on any row above
    for i in range(row):
        if board[i][col]:
            return False
    
    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    
    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j]:
            return False
    
    return True

def nqueens(board, row, N, solutions):
    if row == N:
        solution = [[i, j] for i in range(N) for j in range(N) if board[i][j]]
        solutions.append(solution)
        return
    
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            nqueens(board, row + 1, N, solutions)
            board[row][col] = 0

def print_solutions(solutions):
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    nqueens(board, 0, N, solutions)
    print_solutions(solutions)

