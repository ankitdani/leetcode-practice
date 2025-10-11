'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''

'''
1,2,3
result = (1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)

Can the elements be duplicates?

backtracking
terminating condition = when len(list) == len(input) then append to result

Time: O(n!)
Space: O(n!)
'''

class Solution:
    def helper (self, nums, index, used, lst, result):
        if len(lst) == len(nums):
            result.append(lst.copy())
            return 
        if index > len(nums):
            return
        for i in range(len(nums)):
            if used[i]: 
                continue
            used[i] = True
            lst.append(nums[i])
            self.helper (nums, i+1, used, lst, result)
            lst.pop()
            used[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        lst, result = [], []
        used = [False] * len(nums)
        self.helper (nums, 0, used, lst, result)
        return result