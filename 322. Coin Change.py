'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''

'''
2,5
amount=10
possibilities=(2*5) or (5*2)
min = 2 coins of 5
result=>2

amount-coin -> repeat until amount == 0 (return 0) or amount < 0(return inf)

10-2=8
coin = 2
8-2=6
6-2=4
4-2=2
2-2=0
res=5

coin = 5
10-5=5
5-5=0
res=2

Time: O(n)
Space: O(n)
'''

class Solution:
    def helper (self, coins, amount, memo):
        if amount < 0:
            return float('inf')
        if amount == 0:
            return 0
        if memo[amount] != -1:
            return memo[amount]
        res = float('inf')
        for coin in coins:
            res = min(res, 1 + self.helper(coins, amount-coin, memo))
        memo[amount] = res
        return res

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1] * (amount+1)
        result = self.helper(coins, amount, memo)
        return -1 if result == float('inf') else result