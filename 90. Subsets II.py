'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

'''
1,2,2
result => null,(1),(2),(1,2),(2,2),(1,2,2)

1,1
result => null,(1),(1,1)

backtracking
at every step, there is a choice to pick current element or none

Time: O(nlogn)
Space: O(nlogn)
'''

class Solution:
    def helper (self, nums, index, lst, result):
        # terminating condition
        if index >= len(nums):
            result.append(lst.copy())
            return 
        # pick
        lst.append(nums[index])
        self.helper (nums, index+1, lst, result)
        # do not pick
        lst.pop()
        # check for duplicates
        while index+1 < len(nums) and nums[index] == nums[index+1]:
            index += 1
        self.helper (nums, index+1, lst, result)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        lst, result = [], []
        nums.sort()
        self.helper (nums, 0, lst, result)
        return result