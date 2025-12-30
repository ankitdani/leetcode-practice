'''
Docstring for 48. Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''

'''
1 2
3 4

result =
3 1
4 2

transpose + reverse 

transpose =
1 3
2 4

reverse on transpose =
3 1
4 2

Time: O(n*m)
Space: O(n*m)
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose 
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(rows):
            for j in range(cols//2):
                matrix[i][j], matrix[i][cols-j-1] = matrix[i][cols-j-1], matrix[i][j]
        return matrix