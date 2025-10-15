'''
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
'''

'''
1,1,2,3
k=2,target=3
result=>(1,2)

Time: O(nlogn)
Space: O(n)
'''

class Solution:
    def helper (self, k, n, i, sum, lst, result):
        if sum == n and len(lst) == k:
            result.append(lst.copy())
            return
        if i > 9 or sum > n or (sum == n and len(lst) > k):
            return
        lst.append(i)
        self.helper (k, n, i+1, sum+i, lst, result)
        lst.pop()
        self.helper (k, n, i+1, sum, lst, result)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        lst, result = [], []
        self.helper(k, n, 1, 0, lst, result)
        return result