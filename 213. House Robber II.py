'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''

'''
1,2,3,4
->1+2=X
->1+3=4
->1+4=X
->2+3=X
->2+4=6

if the robber robs 1st house then he cant rob last house
so robbing can start either from house 0 or house 1

Time: O(n)
Space: O(n)
'''

class Solution:
    def helper (self, nums, s, e, memo):
        if s > e:
            return 0
        if memo[s] != -1:
            return memo[s]
        take = nums[s] + self.helper (nums, s+2, e, memo)
        skip = self.helper (nums, s+1, e, memo)
        memo[s] = max(take, skip)
        return memo[s]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        memo1 = [-1] * (n)
        memo2 = [-1] * (n)
        result1 = self.helper (nums, 0, n-2, memo1)
        result2 = self.helper (nums, 1, n-1, memo2)
        return max(result1, result2)