'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
'''

'''
start with the end and work towards the start.
use recursion
if start is reached, return 1
if we are out of bounds, return 0
cache the results

Time: O()
Space: O()
'''

class Solution:
    def helper (self, m, n, memo):
        # terminating condition
        if (m == 0 and n == 0):
            return 1
        if (m < 0 or n < 0):
            return 0
        if memo[m][n] != -1:
            return memo[m][n]
        moves = self.helper (m-1, n, memo) + self.helper (m, n-1, memo)
        memo[m][n] = moves
        return memo[m][n]
        
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]
        return self.helper (m-1, n-1, memo)