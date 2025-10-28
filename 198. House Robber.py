'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''

'''
1,2,3,4

take i or take i+1

1+2->not possible
1+3->4
1+4->5
2+3->not possible
2+4->6

Time: O(n)
Space: O(n)
'''

class Solution:
    def helper (self, nums, i, memo):
        if i >= len(nums):
            return 0
        if memo[i] != -1:
            return memo[i]
        take = nums[i] + self.helper(nums, i+2, memo)
        skip = self.helper(nums, i+1, memo)
        memo[i] = max(take, skip)
        return memo[i]

    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        return self.helper(nums, 0, memo)