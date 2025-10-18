'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

'''
1 0
0 1
islands = 2

dfs -> if neighbors == island(1) then check their neighbors

Time: O(m*n)
Space: O(m*n)

Optimization can be done for memory = instead of using visited array, input grid can be changed to 0 
'''

class Solution:
    def dfs (self, grid, r, c, visited):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != '1' or visited[r][c]:
            return
        visited[r][c] = True
        self.dfs(grid, r+1, c, visited)
        self.dfs(grid, r-1, c, visited)
        self.dfs(grid, r, c+1, visited)
        self.dfs(grid, r, c-1, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = [[False] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.dfs(grid, i, j, visited)
                    islands += 1
        return islands