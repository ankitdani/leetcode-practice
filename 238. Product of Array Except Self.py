'''
Docstring for 238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''

'''
nums=[1,2,3,4]

calculate products to the left of the current element.
calculate products to the right of the current element.
multiple left and right products.

calculate left product
curr_element = curr = 1
left_prod = [1,1,1,1]

curr_element = curr = 2
left_prod = [1,1,1,1]

curr_element = curr = 3
left_prod = [1,1,2,1]

curr_element = curr = 4
left_prod = [1,1,2,6]

calculate right product 
curr_element = 4
right_prod = [1,1,1,1]

curr_element = 3
right_prod = [1,1,4,1]

curr_element = 2
right_prod = [1,12,4,1]

curr_element = 1
right_prod = [24,12,4,1]

left_prod = [1,1,2,6]
right_prod = [24,12,4,1]
result = [24,12,8,6]

curr_left_prod = prev_left_prod * prev_element
curr_right_prod = prev_right_prod * prev_element (iterate from last)

Time: O(n)
Space: O(n)
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [-1] * n
        right_prod = [-1] * n
        result = [1] * n
        for i in range(1, n):
            left_prod[i] = left_prod[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            right_prod[i] = right_prod[i+1] * nums[i+1]
        for i in range(n):
            result[i] = left_prod[i] * right_prod[i]
        return result