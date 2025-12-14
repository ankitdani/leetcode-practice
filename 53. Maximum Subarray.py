'''
Docstring for 53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.
'''

'''
intuition is :
either extend the array sum or
start sum from curr position

nums=[-1,-2,-3]

init
curr_sum = -1
max_sum = -1

num = -2
curr_sum = max(curr_sum, num) = -3
max_sum = max(max_sum, curr_sum) = -1

num = -2
curr_sum = max(curr_sum, num) = -6
max_sum = max(max_sum, curr_sum) = -1

result = -1

Time: O(n)
Space: O(1)
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]
        for num in nums[1:]:
            curr_sum = max(curr_sum + num, num)
            max_sum = max(max_sum, curr_sum, num)
        return max_sum