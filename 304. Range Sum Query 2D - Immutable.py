'''
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.
'''

'''
brute force: calculate sum everytime O(m*n)
contradicts sumRegion in O(1) time

optimization = 
calculate prefix sum and store in matrix while initializing
each cell will include sum of that rectangle
prefix of left + prefix of above - prefix from diagonal for initiation

Time: O(1)
Space: O(m*n)
'''

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix = [[0] * (cols+1) for _ in range(rows+1)]
        for r in range(1, rows+1):
            for c in range(1, cols+1):
                self.prefix[r][c] = self.prefix[r-1][c] + self.prefix[r][c-1] - self.prefix[r-1][c-1] + matrix[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)