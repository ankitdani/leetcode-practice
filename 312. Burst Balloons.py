'''
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.
'''

'''
2,3
1,2,3,1

take coin 2 1st
1*2*3 + 1*3*1 = 9 => result

take coin 3 1st
2*3*1 + 1*2*1 = 8

to minimize operations, cache them

Time: O(n^3)
Space: O(n^2)
'''

class Solution:
    def helper (self, nums, l, r, memo):
        if r-l == 1:
            return 0
        if (l, r) in memo:
            return memo[(l, r)]
        max_coins = 0
        for i in range(l+1, r):
            coins = nums[l] * nums[i] * nums[r]
            total = self.helper(nums, l, i, memo) + coins + self.helper(nums, i, r, memo)
            max_coins = max(max_coins, total)
        memo[(l, r)] = max_coins
        return memo[(l, r)]

    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}
        return self.helper (nums, 0, len(nums)-1, memo)