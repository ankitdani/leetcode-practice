'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
'''

'''
for a day, we have 4 choices -
buy,sell,hold,skip

if buy -> -price
if sell -> +price
if hold -> already bought before, waiting for better selling price, do nothing today, move to next day
if skip -> can buy but waiting for better buying price, do nothing today, move to next day

optimization - 
to minimize repeated work, use a memo array and store results

prices=1,2,3,5
result=buy,hold,hold,sell=4

i=0
can_buy=true
result=-1

i=1
can_buy=true
skip
result=-1

i=2
can_buy=true
skip
result=-1

i=3
result=-1+5=4
can_buy=false

return result

Time: O(n)
Space: O(n)
'''

class Solution:
    def helper (self, prices, i, can_buy, memo):
        if i >= len(prices):
            return 0
        if memo[i][can_buy] != -1:
            return memo[i][can_buy]
        if can_buy:
            buy = self.helper (prices, i+1, False) - prices[i]
            skip = self.helper (prices, i+1, True)
            memo[i][can_buy] = max(buy, skip)
            return memo[i][can_buy]
        else:
            sell = prices[i] + self.helper (prices, i+2, True)
            hold = self.helper (prices, i+1, False)
            memo[i][can_buy] = max(sell, hold)
            return memo[i][can_buy]

    def maxProfit(self, prices: List[int]) -> int:
        memo = [[-1] * 2 for _ in range(len(prices))]
        return self.helper (prices, 0, True, memo)