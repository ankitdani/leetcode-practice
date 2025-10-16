'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''

'''
search for the starting letter
once 1st letter found then use dfs
for each step, check all 4 directions
if letters match move to next step
else backtrack
to keep track of visited steps, use a boolean array

Time: O(m*n*4**len(word))
Space: O(m*n)

space can be optimized by marking the board itself and assign letter back to board
'''

class Solution:
    def helper (self, board, word, r, c, i, visited):
        if i == len(word):
            return True
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or i > len(word) or visited[r][c] or word[i] != board[r][c]:
            return False
        visited[r][c] = True
        flag = (self.helper (board, word, r+1, c, i+1, visited) or
        self.helper (board, word, r, c+1, i+1, visited) or
        self.helper (board, word, r-1, c, i+1, visited) or
        self.helper (board, word, r, c-1, i+1, visited))
        visited[r][c] = False
        return flag

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if (self.helper (board, word, i, j, 0, visited)):
                        return True
        return False