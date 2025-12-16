'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
'''

'''
at each step, check if we reached the last step
track maximum step that can be reached at each iteration

nums=[2,1,3]
curr_num = 2
max_step = max(max_step, nums[i]+i) = nums[i] + i = 2 + 0 = 2
reached the last step ? -> no
move to next element

curr_num = 1
max_step = max(max_step, nums[i]+i) = max(2, 1 + 1) = 2
reached last step ? -> no -> return false

curr_num = 3
max_step = max(max_step, nums[i]+i) = max(2, 3+2) = 5
reached last step ? -> yes -> return true

if index reaches ahead of max_step then early return 

Time: O(n)
Space: O(1)
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_step = 0
        n = len(nums)-1
        for i, jump in enumerate(nums):
            if i > max_step:
                return False
            max_step = max(max_step, jump + i)
            if (max_step >= n):
                return True
        return False