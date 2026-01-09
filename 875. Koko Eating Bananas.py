'''
Docstring for 875. Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
'''

'''
piles = [3,6,7,11], h = 8
l = 1, r = 11
m = 6
hrs = ceil (3/6) + (6/6) + (7/6) + (11/6) = 6
is hrs <= h ? => yes, r = m-1 = 5

l = 1, r = 5
m = 3
hrs = ceil (3/3) + (6/3) + (7/3) + (11/3) = 10
is hrs <= h ? => no
then l = m+1 = 4

l = 4, r = 4
m = 4
hrs = ceil (3/4) + (6/4) + (7/4) + (11/4) = 8
is hrs <= h ? => yes
r = m-1 = 3

l <=r ? => no => exit loop

Time: O(nlogn)
Space: O(1)
'''
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0
        while (l <= r):
            m = l + (r-l)//2
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / m)
            if hrs <= h:
                res = m
                r = m-1
            else:
                l = m+1
        return res
