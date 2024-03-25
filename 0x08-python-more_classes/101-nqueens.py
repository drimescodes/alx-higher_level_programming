#!/usr/bin/python3
from sys import argv, stdout

"""
A program that solves the N queens problem.
"""


def err(message: str, code: int):
    """Prints an error message to stderr and exits the program with the
    given code.
    """
    print(message)
    exit(code)


def solve(n: int, rows, cols, d1, d2, k=0, poss=[]) -> None:
    """
    Solve the N-Queens problem recursively using backtracking.

    Args:
        n (int): The number of queens to place on the board.
        rows (list): List representing the rows on the board.
        cols (list): List representing the columns on the board.
        d1 (list): List representing the diagonal from top-left to bottom-right
            on the board.
        d2 (list): List representing the diagonal from top-right to bottom-left
            on the board.
        k (int): The starting index for the rows.
        poss (list): List to store the possible queen positions.

    Returns:
        None: The function does not return a value, but prints the possible
            solutions.
    """
    if n == 0:
        stdout.write(str(poss) + "\n")
        return
    for i in range(k, len(rows)):
        for j in range(len(rows)):
            if not (
                rows[i] or cols[j] or d1[i + j] or d2[len(rows) - j + i - 1]
            ):
                cols[j] = rows[i] = d1[i + j] = d2[
                    len(rows) - j + i - 1
                ] = True
                poss.append([i, j])
                solve(n - 1, rows, cols, d1, d2, i + 1, poss)
                poss.pop()
                cols[j] = rows[i] = d1[i + j] = d2[
                    len(rows) - j + i - 1
                ] = False


def main():
    """Main function for the program."""
    if len(argv) != 2:
        err("Usage: nqueens N", 1)
    n = 4
    try:
        n = int(argv[1])
    except ValueError:
        err("N must be a number", 1)
    if n < 4:
        err("N must be at least 4", 1)
    solve(
        n,
        [False] * n,
        [False] * n,
        [False] * (n * 2 - 1),
        [False] * (n * 2 - 1),
    )


if __name__ == "__main__":
    main()
