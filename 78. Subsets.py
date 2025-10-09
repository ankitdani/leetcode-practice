'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

'''
1,2,3
result => null,1,2,3,(1,2),(1,3),(2,3)

for each element, we have 2 choices - pick and not pick 
terminating condition = index out of bounds then return nothing

Time: O(n * 2**n)
Space: O(n * 2**n)
'''

class Solution:
    def dfs (self, i, nums, subset, result):
        if i >= len(nums):
            result.append(subset.copy())
            return 
        subset.append(nums[i])
        self.dfs(i+1, nums, subset, result)
        subset.pop()
        self.dfs(i+1, nums, subset, result)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset, result = [], []
        self.dfs (0, nums, subset, result)
        return result