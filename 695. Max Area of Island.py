'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
'''

'''
1 0 1
0 1 1
result => 3

dfs on every 1 that we encounter and calculate area 
tp avoid visiting already visited node, track using visited array

Time: O(m*n)
Space: O(m*n)
'''

class Solution:
    def dfs (self, grid, r, c, visited):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or visited[r][c] or grid[r][c] == 0:
            return 0
        visited[r][c] = True
        area = 1
        area += self.dfs(grid, r+1, c, visited)
        area += self.dfs(grid, r-1, c, visited)
        area += self.dfs(grid, r, c+1, visited)
        area += self.dfs(grid, r, c-1, visited)
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(grid, i, j, visited   ))
        return max_area