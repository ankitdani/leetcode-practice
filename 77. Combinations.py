'''
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
'''

'''
n = 3, k = 2
result =>  (1,2),(2,3),(1,3)

backtracking
terminating condition = when k == 2

Time: O(nlogk)
Space: O(nlognk)
'''

class Solution:
    def helper (self, i, n, k, lst, result):
        if len(lst) == k:
            result.append(lst.copy())
            return
        if i > n:
            return 
        lst.append(i)
        self.helper (i+1, n, k, lst, result)
        lst.pop()
        self.helper (i+1, n, k, lst, result)
        
    def combine(self, n: int, k: int) -> List[List[int]]:
        lst, result = [], []
        self.helper (1, n, k, lst, result)
        return result