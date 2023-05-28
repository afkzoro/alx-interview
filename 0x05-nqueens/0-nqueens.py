import sys


def is_safe(board, row, col):
    # Check if a queen can be placed at board[row][col]

    # Check row on the left side
    for i in range(col):
        if board[i] == row or board[i] == row + col - i or board[i] == row - col + i:
            return False

    return True


def solve_nqueens(n):
    board = [-1] * n
    solutions = []
    solve_util(board, 0, n, solutions)
    return solutions


def solve_util(board, col, n, solutions):
    # Base case: all queens are placed
    if col == n:
        solutions.append(board[:])
        return

    for row in range(n):
        if is_safe(board, row, col):
            # Place the queen
            board[col] = row

            # Recur for the next column
            solve_util(board, col + 1, n, solutions)


def print_solutions(solutions):
    for solution in solutions:
        solution_list = [[row, solution[row]] for row in range(len(solution))]
        print(solution_list)


def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is within the valid range
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions)


if __name__ == '__main__':
    main()
