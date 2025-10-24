'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

'''
each call has 2 choices - take 1 step or 2 steps
total n steps
if we reach end of the staircase, we return 1 which denotes 1 way to reach the end of the staircase
out of bounds condition
recursively call until last step is reached 

to optimize: cache repeated steps in an array

n = 2
2-1=1
2-2=0 -> add to result

1-1=0 -> add to result
1-2=-1 -> out of bounds

2 ways

Time: O(n)
Space: O(n)
'''

class Solution:
    def helper (self, n, memo):
        if n == 0:
            return 1
        if n < 0:
            return 0
        if memo[n] != -1:
            return memo[n]
        one_step = self.helper(n-1, memo)
        two_step = self.helper(n-2, memo)
        memo[n] = one_step + two_step
        return memo[n]
    
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        memo = [-1] * (n+1)
        return self.helper(n, memo)