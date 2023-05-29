#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    # Check if a queen can be placed at board[row][col]

    for i in range(col):
        if (board[i] == row or board[i] == row + col - i or
                board[i] == row - col + i):
            return False

    return True


def solve_nqueens(N):
    board = [-1] * N
    solutions = []
    solve_util(board, 0, N, solutions)
    return solutions


def solve_util(board, col, N, solutions):
    # Base case: all queens are placed
    if col == N:
        solutions.append(board[:])
        return

    for row in range(N):
        if is_safe(board, row, col):
            # Place the queen
            board[col] = row

            # Recur for the next column
            solve_util(board, col + 1, N, solutions)


def print_solutions(solutions):
    for solution in solutions:
        solution_list = [[row, solution[row]] for row in range(len(solution))]
        print(solution_list)
    # print()


def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is within the valid range
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)


if __name__ == '__main__':
    main()
