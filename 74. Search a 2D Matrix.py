class Solution:
    # flatten matrix
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols -1
        while (left <= right):
            mid = (left + right) // 2
            mid_val = matrix[mid // cols][mid % cols]
            if (mid_val == target):
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
            
# Time: O ( log ( m * n ))
# Space: O ( 1 )

'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        row = 0
        col = cols-1
        while (row >= 0 and row <= rows-1 and col >= 0 and col <= cols-1):
            if target == matrix[row][col]:
                return True
            elif (target > matrix[row][col]):
                row += 1
            else:
                col -= 1
        return False
            
# Time: O(m + n)
# Space: O(1)
'''