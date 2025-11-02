'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.
'''

'''
2,-4,13
result=2(2,13)

brute force:
start from each element and check if next elements are increasing
if increasing then track count

optimize:
iterate from end and store longest till current element 
as we go towards the start, we have to calculate till only next element and get the stored value

num=13
dp[2]=1

num=-4
dp[1]=1+dp[2]=2

num=2 and -4
num=2 and 13
dp[0]=1+dp[2]=2

Time: O(n^2)
Space: O(n)
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n-2,-1,-1):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)