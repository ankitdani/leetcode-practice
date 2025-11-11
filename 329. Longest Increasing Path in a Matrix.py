'''
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
'''

'''
1 2 3
4 5 6
7 8 9

longest increasing path
result=5(either 1->4->7->8->9 or 1->2->3->6->9)

Time: O(4^m*n)
Space: O(4^m*n)
'''

class Solution:
    def helper (self, matrix, r, c, prev, memo):
        if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
            return 0
        if matrix[r][c] <= prev:
            return 0
        if (r, c) in memo:
            return memo[(r, c)]
        prev = matrix[r][c]
        down = 1 + self.helper (matrix, r+1, c, prev, memo)
        up = 1 + self.helper (matrix, r-1, c, prev, memo)
        right = 1 + self.helper (matrix, r, c+1, prev, memo)
        left = 1 + self.helper (matrix, r, c-1, prev, memo)
        memo[(r, c)] = max(down, up, right, left)
        return memo[(r, c)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 0
        memo = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, self.helper (matrix, i, j, -1, memo))
        return res