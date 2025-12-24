'''
Docstring for 36. Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''

'''
use 3 sets: col_set, row_set, 3*3 squares set
if number is repeated in each set then return false

Time: O(3 * n) = O(n)
Space: O(3 * n) = O(n)
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            row_set = set()
            for c in range(cols):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row_set and board[r][c] != '.':
                    return False
                row_set.add(board[r][c])
        for c in range(cols):
            col_set = set()
            for r in range(rows):
                if board[r][c] == '.':
                    continue
                if board[r][c] in col_set and board[r][c] != '.':
                    return False
                col_set.add(board[r][c])
        for r in range(0, rows, 3):
            for c in range(0, cols, 3):
                square_set = set()
                for i in range(r, r+3):
                    for j in range(c, c+3):
                        if board[i][j] == '.':
                            continue
                        if board[i][j] in square_set and board[i][j] != '.':
                            return False
                        square_set.add(board[i][j])
        return True