'''
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
'''

'''
nums=[1,2,1]
result=[2,-1,2]

i = 0
stk = empty 
stk = [0]
result = [-1,-1,-1]

i = 1
stk = 0
nums[stk[-1]] < nums[i] => 1 < 2
result = [-]


Time: O(2 * n)
Space: O(2 * n)
'''

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stk = []
        for i in range(2 * n):
            while stk and nums[i] > nums[stk[-1]]:
                j = stk.pop()
                result[j] = nums[i]
            if i < n:
                stk.append(i)
        return result