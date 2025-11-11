'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.
'''

'''
coins=1,5
amount=5
result=>2->(1,1,1,1,1),(5)

take a coin and keep adding until amount is reached
if amount is exceeded then take next coin

Time: O(n)
Space: O(n)
'''

class Solution:
    def helper (self, amount, coins, i, memo):
        if amount == 0:
            return 1
        if i >= len(coins) or amount < 0:
            return 0
        if memo[i][amount] != -1:
            return memo[i][amount]
        take = self.helper (amount-coins[i], coins, i, memo)
        skip = self.helper (amount, coins, i+1, memo)
        memo[i][amount] = take + skip
        return memo[i][amount]

    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[-1] * (amount + 1) for _ in range(len(coins))]
        return self.helper (amount, coins, 0, memo)