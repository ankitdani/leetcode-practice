'''
Docstring for 45. Jump Game II

You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.
'''

'''
Intuition = check max_jump for each element till curr_max_jump
and increment jump only if we reach curr_max_jump

nums=[1,2,0,4]
i = 0
max_jump = max(max_jump, nums[i] + i) = max(0, 1+0) = 1 
if i == curr_end
then increment result and update curr_end as max_jump
jumps = 1, curr_end = 1

i = 1
max_jump = max(max_jump, nums[i] + i) = max(1, 2+1) = 3 
if i == curr_end => 1 == 1 => true
then increment result and update curr_end as max_jump
jumps = 2, curr_end = 3

i = 2
max_jump = max(3, 0+2) = 3
i != curr_end => 2 != 3

end of loop-1 => because we are calculating jumps when we jump and not when we arrive
return jumps = 2

Time: O(n)
Space: O(1)
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curr_end = 0
        max_jump = 0
        for i in range(len(nums)-1):
            max_jump = max(max_jump, nums[i]+i)
            if i == curr_end:
                jumps += 1
                curr_end = max_jump
        return jumps