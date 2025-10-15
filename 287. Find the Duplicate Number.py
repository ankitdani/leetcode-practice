'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        1,2,1

        nums[abs(1)] => nums[1] = -2
        nums[abs(-2)] => nums[2] = -1
        nums[abs(-1)] => nums[1] == -1 already -ve then return 1
        '''

        '''
        index = curr value
        take the value of index and mark as -ve
        if we encounter a -ve value then return the index as duplicate
        '''

        '''
        Time: O(n)
        Space: O(1)
        '''

        for num in nums:
            index = abs(num)
            if nums[index] < 0:
                return index
            nums[index] = -nums[index]
        
        return -1

