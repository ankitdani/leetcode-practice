'''
Docstring for 54. Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.
'''

'''
1 2 3
4 5 6
7 8 9

left = 0, right = cols, top = 0, down = rows

while left < right: print
top++
while top <= down: print
right--
while right >= left: print
down--
while down > top: print
left++

Time: O(n*m)
Space: O(n*m)
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        left, right = 0, cols-1
        up, down = 0, rows-1
        res = []
        while (left <= right and up <= down):
            for i in range(left, right+1):
                res.append(matrix[up][i])
            up += 1
            if left <= right:
                for i in range(up, down+1):
                    res.append(matrix[i][right])
                right -= 1
            if up <= down:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1
            if left <= right:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res