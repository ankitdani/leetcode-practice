'''
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.
'''

'''
2,4
result=>8

-2,4
product = 1
num=-2
product=-2
if product < 0 or == 0 then reset product
product=1
product=4
result=>4

-2,-4
product=1
num=-2
product=-2
min_product=-2
max_product=-2
num=-4
min_product=-2*-4=8
max_product=-2*-4=8

Time: O(n)
Space: O(1)
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = 1
        min_product = 1
        result = 1
        for num in nums:
            if num == 0:
                max_product = 1
                min_product = 1
                result = max(result, 0)
            else:
                prev_min = min_product
                prev_max = max_product
                min_product = min(num, prev_min * num, prev_max * num)
                max_product = max(num, prev_min * num, prev_max * num)
                result = max(result, max_product)
        return result