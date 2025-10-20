'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
'''

'''
dfs 
if neighboring cell's height less than current height then add current to result
keep track of visited to pacific and atlantic using 2 arrays

Time: O(m*n)
Space: O(m*n)
'''

class Solution:
    def is_valid (self, heights, r, c):
        return (r >= 0 and r < len(heights) and c >= 0 and c < len(heights[0]))

    def dfs (self, heights, r, c, visited):
        visited[r][c] = True
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        for i in range(4):
            new_r = dx[i] + r
            new_c = dy[i] + c
            if self.is_valid(heights, new_r, new_c) and not visited[new_r][new_c] and heights[new_r][new_c] >= heights[r][c]:
                self.dfs (heights, new_r, new_c, visited)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]
        for i in range(rows):
            self.dfs (heights, i, 0, pacific)
            self.dfs (heights, i, cols-1, atlantic)
        for i in range(cols):
            self.dfs (heights, 0, i, pacific)
            self.dfs (heights, rows-1, i, atlantic)
        result = []
        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] and atlantic[i][j]:
                    result.append((i, j))
        return result