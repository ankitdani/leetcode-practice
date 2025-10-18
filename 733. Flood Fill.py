'''
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.
'''

'''
1 1
1 0
sr = 0, sc = 0, color = 2

result =>
2 2
2 0

check adjacent directions. 
if neighbor's color is same as starting position then change colour.
repeat until their neighbors have same color and change colour till neighbors dont have original color

can be done in both: dfs or bfs

Time: O(m*n)
Space: O(m*n)
'''

class Solution:
    def dfs (self, image, r, c, color, visited, original_color):
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or visited[r][c] or image[r][c] != original_color:
            return
        image[r][c] = color
        visited[r][c] = True
        self.dfs (image, r+1, c, color, visited, original_color)
        self.dfs (image, r-1, c, color, visited, original_color)
        self.dfs (image, r, c+1, color, visited, original_color)
        self.dfs (image, r, c-1, color, visited, original_color)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        visited = [[False] * cols for _ in range(rows)]
        original_color = image[sr][sc]
        self.dfs (image, sr, sc, color, visited, original_color)
        return image