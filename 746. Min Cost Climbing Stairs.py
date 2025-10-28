'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''

'''
Does the top floor mean ith floor or i-1 floor ? -> i

input cost = 1,2,3,4
-> 1+3=4
-> 1+2+4=7
-> 2+4=6

result => 4

recursion
every step has 2 choice = 1 step or 2

Time: O(n)
Space: O(n)
'''

class Solution:
    def helper (self, cost, i, memo):
        if i >= len(cost):
            return 0
        if memo[i] != -1:
            return memo[i]
        one_step = self.helper (cost, i+1, memo)
        two_step = self.helper (cost, i+2, memo)
        memo[i] = cost[i] + min(one_step, two_step)
        return memo[i]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)
        return min(self.helper (cost, 0, memo), self.helper (cost, 1, memo))