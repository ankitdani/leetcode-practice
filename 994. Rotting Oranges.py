'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''

'''
0 0 2
0 1 2
result => 1

bfs because spreading needs to start at every rotten orange at the same time
search and append all rotten apple positions to the queue at the same time
for each position in queue, check all 4 directions
only after checking all 4 positions, increment time.
track fresh orange since if it not possible to reach all fresh orange return -1

Time: O(m*n)
Space: O(m*n)
'''
from collections import deque

class Solution:
    def is_valid (self, grid, r, c):
        return (r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]))
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        time = 0
        que = deque()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    que.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        while que and fresh > 0:
            time += 1
            for _ in range(len(que)):
                curr = que.popleft()
                for i in range(4):
                    new_r = curr[0] + dx[i]
                    new_c = curr[1] + dy[i]
                    if self.is_valid(grid, new_r, new_c) and grid[new_r][new_c] == 1:
                        que.append((new_r, new_c))
                        grid[new_r][new_c] = 2
                        fresh -= 1
        return time if fresh == 0 else -1