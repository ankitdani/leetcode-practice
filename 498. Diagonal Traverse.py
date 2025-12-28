'''
Docstring for 498. Diagonal Traverse
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
'''

'''
1 2 3
4 5 6
7 8 9

00 -> 01 -> 10 -> 20 -> 11 -> 02 -> 12 -> 21 -> 22

up_to_down = true
row--
col++

up_to_down = false
row++
col--

Time: O(n*m)
Space: O(n*m)
'''

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        up_to_down = False
        result = []
        r, c = 0, 0
        for _ in range(rows * cols):
            result.append(mat[r][c])                    
            if up_to_down:
                if r == rows-1:
                    up_to_down = False
                    c += 1
                elif c == 0:
                    up_to_down = False
                    r += 1
                else:
                    r += 1
                    c -= 1
            else:
                if c == cols-1:
                    up_to_down = True
                    r += 1
                elif r == 0:
                    up_to_down = True
                    c += 1
                else:
                    r -= 1
                    c += 1
        return result