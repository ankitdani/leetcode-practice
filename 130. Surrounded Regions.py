'''
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.
'''

'''
X O X
X O X
X O X

replace all Os on border to 1s(temp symbol)
change all Os surrounded to Xs
change the border 1s back to Os

X O X
X O X
X O X

X 1 X
X 1 X
X 1 X

X O X
X O X
X O X

Time: O(m*n)
Space: O(1)
'''

class Solution:
    def dfs (self, board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == '1' or board[i][j] == 'X':
            return
        board[i][j] = '1'
        self.dfs (board, i+1, j)
        self.dfs (board, i-1, j)
        self.dfs (board, i, j+1)
        self.dfs (board, i, j-1)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            if board[i][0] == 'O':
                self.dfs (board, i, 0)
            if board[i][cols-1] == 'O':
                self.dfs (board, i, cols-1)
        for j in range(cols):
            if board[0][j] == 'O':
                self.dfs (board, 0, j)
            if board[rows-1][j] == 'O':
                self.dfs (board, rows-1, j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '1':
                    board[i][j] = 'O'