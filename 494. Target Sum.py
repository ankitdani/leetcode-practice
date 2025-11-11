'''
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.
'''

'''
nums=2,1
target=3
result=1

all combinations=
[+2+1],[+2-1],[-2,+1],[-2,-1]
but only 1 has sum == target
[+2+1]

Time: O(n * total_sum)
Space: O(n * total_sum)
'''

class Solution:
    def helper (self, nums, target, i, curr_sum, memo):
        if i == len(nums):
            return 1 if target == curr_sum else 0 
        if i > len(nums):
            return 0
        if (i, curr_sum) in memo:
            return memo[(i, curr_sum)]
        add = self.helper(nums, target, i+1, curr_sum+nums[i], memo)
        subtract = self.helper(nums, target, i+1, curr_sum-nums[i], memo)
        memo[(i, curr_sum)] = add + subtract
        return memo[(i, curr_sum)]
        
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        return self.helper(nums, target, 0, 0, memo)